#!/usr/bin/env python3
"""Restore layer lock/alphaLock from 2aa99d8 and add streamline stabilizer (prototype 0.5)."""
from pathlib import Path
import subprocess
import re
import sys

base = None
try:
    base = subprocess.check_output(["git", "show", "2aa99d8:index.html"], text=True)
except Exception:
    p = Path("index.html")
    if p.exists():
        base = p.read_text(encoding="utf-8")
if not base:
    sys.exit("no base index.html")

if "stabOut" not in base:
    base = base.replace(
        "docName:'Untitled artwork',autosaveTimer:null,db:null};",
        "docName:'Untitled artwork',autosaveTimer:null,db:null,stabBuf:[],stabOut:null};",
    )

base = base.replace(
    '<div class="field"><div class="field-head"><label for="smooth">Stabilization</label><output id="smoothOut">20%</output></div><input class="range" id="smooth" type="range" min="0" max="90" value="20"></div>',
    '<div class="field"><div class="field-head"><label for="smooth">Stabilizer</label><output id="smoothOut">20%</output></div><input class="range" id="smooth" type="range" min="0" max="95" value="20"><p class="note">Higher values lag the stroke and smooth wobble (streamline-style).</p></div>',
)

if "layer-thumb" not in base:
    base = base.replace(
        ".layer{display:flex;align-items:center;gap:8px;padding:9px;border:1px solid transparent;border-radius:9px;background:#1d1d23;min-width:0}",
        ".layer{display:flex;align-items:center;gap:8px;padding:7px;border:1px solid transparent;border-radius:9px;background:#1d1d23;min-width:0;cursor:pointer}.layer-thumb{width:36px;height:28px;border-radius:5px;background:#0e0e12;border:1px solid #2c2c36;flex-shrink:0;object-fit:cover}",
    )

NEW_DRAW = r"""function strokeWidth(p){const pressure=Math.max(.02,Math.min(1,p||.5));const shaped=Math.pow(pressure,state.pressureCurve);return state.size*(.12+.88*shaped)}
function drawSegment(a,b){const l=activeLayer();if(!l||l.locked)return;const ctx=l.ctx;ctx.save();ctx.lineCap='round';ctx.lineJoin='round';ctx.globalAlpha=state.opacity;if(state.tool==='eraser'){ctx.globalCompositeOperation='destination-out'}else{ctx.globalCompositeOperation=l.alphaLock?'source-atop':'source-over';ctx.strokeStyle=state.color}ctx.lineWidth=strokeWidth(b.p);ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();ctx.restore()}
function stabReset(p){state.stabBuf=[];state.stabOut=p?{x:p.x,y:p.y,p:p.p}:null;state.lastPoint=p||null}
function stabStep(raw){const k=Math.max(0,Math.min(.95,state.smooth));if(!state.stabOut){state.stabOut={x:raw.x,y:raw.y,p:raw.p};return state.stabOut}const alpha=1-k;const out={x:state.stabOut.x+(raw.x-state.stabOut.x)*alpha,y:state.stabOut.y+(raw.y-state.stabOut.y)*alpha,p:state.stabOut.p+(raw.p-state.stabOut.p)*Math.max(alpha,.15)};state.stabOut=out;return out}
function stabFlush(toPoint){if(!state.lastPoint||!toPoint)return;const sx=state.lastPoint.x,sy=state.lastPoint.y,sp=state.lastPoint.p;const dist=Math.hypot(toPoint.x-sx,toPoint.y-sy);if(dist<.15){state.lastPoint=toPoint;return}const steps=Math.max(1,Math.min(16,Math.ceil(dist/(Math.max(1.5,state.size*.28)))));let a=state.lastPoint;for(let i=1;i<=steps;i++){const t=i/steps;const b={x:sx+(toPoint.x-sx)*t,y:sy+(toPoint.y-sy)*t,p:sp+(toPoint.p-sp)*t};drawSegment(a,b);a=b}state.lastPoint=toPoint}
function onDown(e){if(state.spaceDown||(e.button===1)){state.panning=true;state.panPointer={x:e.clientX,y:e.clientY,id:e.pointerId};paper.setPointerCapture?.(e.pointerId);e.preventDefault();return}if(e.button!==undefined&&e.button!==0)return;const p=point(e);if(state.tool==='eyedropper'){const composite=document.createElement('canvas');composite.width=W;composite.height=H;const c=composite.getContext('2d');state.layers.forEach(l=>{if(l.visible)c.drawImage(l.canvas,0,0)});const x=Math.max(0,Math.min(W-1,Math.floor(p.x))),y=Math.max(0,Math.min(H-1,Math.floor(p.y)));const d=c.getImageData(x,y,1,1).data;state.color='#'+[d[0],d[1],d[2]].map(n=>n.toString(16).padStart(2,'0')).join('');document.getElementById('color').value=state.color;document.getElementById('hexOut').textContent=state.color.toUpperCase();return}const al=activeLayer();if(al&&al.locked&&state.tool!=='eyedropper'){toast('Layer is locked');return}snapshot();state.drawing=true;state.lineStart=p;stabReset(p);paper.setPointerCapture?.(e.pointerId);document.getElementById('pressureStatus').textContent=e.pointerType==='pen'?'Stylus input detected':e.pointerType==='touch'?'Touch input detected':'Mouse input';if(state.tool!=='line'){drawSegment(p,{...p,x:p.x+.01,y:p.y+.01})}e.preventDefault()}
function onMove(e){if(state.panning&&state.panPointer&&state.panPointer.id===e.pointerId){state.panX+=e.clientX-state.panPointer.x;state.panY+=e.clientY-state.panPointer.y;state.panPointer={x:e.clientX,y:e.clientY,id:e.pointerId};applyViewport();e.preventDefault();return}if(!state.drawing||!state.lastPoint)return;const raw=point(e);if(state.tool==='line'){state.lastPoint=raw;e.preventDefault();return}const smoothed=stabStep(raw);stabFlush(smoothed);e.preventDefault()}
function onUp(e){if(state.panning){state.panning=false;state.panPointer=null;return}if(!state.drawing)return;const p=point(e);if(state.tool==='line'&&state.lineStart){drawSegment(state.lineStart,p)}else if(state.tool!=='line'&&state.lastPoint){const drain=Math.max(1,Math.round(2+state.smooth*14));for(let i=0;i<drain;i++){const out=stabStep(p);stabFlush(out)}stabFlush(p)}state.drawing=false;state.lastPoint=null;state.lineStart=null;state.stabBuf=[];state.stabOut=null;renderLayers();scheduleAutosave()}"""

m = re.search(
    r"function drawSegment\(a,b\)\{.*?function onUp\(e\)\{.*?scheduleAutosave\(\)\}",
    base,
    re.S,
)
if not m:
    sys.exit("draw block not found in base")
base = base[: m.start()] + NEW_DRAW + base[m.end() :]

base = base.replace("Prototype 0.3", "Prototype 0.5")
base = base.replace("Prototype 0.4", "Prototype 0.5")
base = base.replace(
    "createdWith:'Yugatn Art Prototype 0.3'",
    "createdWith:'Yugatn Art Prototype 0.5'",
)
base = base.replace(
    "createdWith:'Yugatn Art Prototype 0.4'",
    "createdWith:'Yugatn Art Prototype 0.5'",
)

if "function layerThumbData" not in base:
    base = base.replace(
        "function renderLayers()",
        'function layerThumbData(l){try{const c=document.createElement("canvas");c.width=36;c.height=28;const x=c.getContext("2d");x.fillStyle="#0e0e12";x.fillRect(0,0,36,28);x.drawImage(l.canvas,0,0,W,H,0,0,36,28);return c.toDataURL("image/png")}catch(e){return""}}\nfunction renderLayers()',
    )
    m2 = re.search(r"row\.innerHTML='<button class=\"layer-vis\".*?</span>';", base)
    if m2:
        base = base.replace(
            m2.group(0),
            m2.group(0)
            + "const thumb=document.createElement('img');thumb.className='layer-thumb';thumb.alt='';thumb.src=layerThumbData(l);row.insertBefore(thumb,row.firstChild);",
            1,
        )

Path("index.html").write_text(base, encoding="utf-8")
for need in ("stabStep", "alphaLock", "locked", "duplicateLayer", "Prototype 0.5"):
    if need not in base:
        sys.exit(f"missing {need}")
print("wrote index.html", len(base), "bytes")
