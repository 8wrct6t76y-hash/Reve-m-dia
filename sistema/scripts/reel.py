# Gera Reel 1080x1920: python3 reel.py spec.py saida.mp4
# spec.py define CSS (str) e SCENES: lista de dicts {quem, fala, html, pausa}
import asyncio, ssl, sys, os, subprocess, json, runpy, tempfile, edge_tts.communicate as c
c._SSL_CTX = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
import edge_tts
from playwright.async_api import async_playwright
VOZ = {"roberto":("pt-BR-AntonioNeural","+14%","-2Hz"),"sandra":("pt-BR-ThalitaMultilingualNeural","+12%","+0Hz")}
spec = runpy.run_path(sys.argv[1]); out = sys.argv[2]
tmp = tempfile.mkdtemp(); FPS=30
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]))
def sh(*a): subprocess.run(list(a),check=True)
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width":1080,"height":1920})
        segs=[]
        for i,s in enumerate(spec["SCENES"]):
            html=f"<!doctype html><html><head><meta charset=utf-8><style>{spec['CSS']}</style></head><body>{s['html']}</body></html>"
            hp=f"{tmp}/{i}.html"; open(hp,"w").write(html)
            await pg.goto("file://"+hp); await pg.wait_for_timeout(150)
            img=f"{tmp}/{i}.png"; await pg.screenshot(path=img)
            wav=f"{tmp}/{i}.wav"
            if s.get("fala"):
                v,r,pt=VOZ[s["quem"]]; mp3=f"{tmp}/{i}.mp3"
                await edge_tts.Communicate(s["fala"],v,rate=r,pitch=pt).save(mp3)
                sh("ffmpeg","-loglevel","error","-y","-i",mp3,"-af","silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,apad=pad_dur=%s"%s.get("pausa",0.25),"-ar","44100","-ac","2",wav)
            else:
                sh("ffmpeg","-loglevel","error","-y","-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-t",str(s.get("dur",1.5)),wav)
            d=dur(wav); n=int(d*FPS)+1
            mp4=f"{tmp}/{i}.mp4"
            z = s.get("zoom",0.0006)
            # leve zoom contínuo + pop no início
            sh("ffmpeg","-loglevel","error","-y","-loop","1","-i",img,"-i",wav,
               "-vf",f"scale=1188:2112,zoompan=z='min(1+{z}*on,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps={FPS},format=yuv420p",
               "-c:v","libx264","-preset","veryfast","-crf","20","-c:a","aac","-b:a","192k","-t",str(d),"-shortest",mp4)
            segs.append(mp4)
        await b.close()
    lst=f"{tmp}/l.txt"; open(lst,"w").write("".join(f"file '{x}'\n" for x in segs))
    raw=f"{tmp}/raw.mp4"
    sh("ffmpeg","-loglevel","error","-y","-f","concat","-safe","0","-i",lst,"-c","copy",raw)
    sh("ffmpeg","-loglevel","error","-y","-i",raw,"-af","highpass=f=80,equalizer=f=3500:t=q:w=1:g=2.5,acompressor=threshold=-20dB:ratio=2.5:attack=5:release=80,loudnorm=I=-14:TP=-1.5",
       "-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart",out)
    print("ok", dur(out))
asyncio.run(main())
