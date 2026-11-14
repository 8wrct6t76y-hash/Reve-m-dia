CSS = """
body{margin:0;width:1080px;height:1920px;font-family:'Inter',sans-serif;overflow:hidden}
.chat{width:1080px;height:1920px;background:#ECE5DD;display:flex;flex-direction:column}
.top{background:#0E1526;padding:120px 60px 44px;display:flex;align-items:center;gap:28px}
.av{width:110px;height:110px;border-radius:55px;background:#F2A7B5;color:#0E1526;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:46px}
.msgs{flex-grow:1;padding:60px 56px;display:flex;flex-direction:column;justify-content:flex-end;gap:30px;padding-bottom:330px}
.b{max-width:820px;padding:34px 42px;font-size:54px;line-height:1.25;color:#111827}
.in{align-self:flex-start;background:#fff;border-radius:0 34px 34px 34px}
.out{align-self:flex-end;background:#D9FDD3;border-radius:34px 0 34px 34px}
.new{box-shadow:0 0 0 6px #FFC53D}
.h{font-family:'Inter Display','Inter';font-weight:800;letter-spacing:-4px;line-height:.95}
.full{width:1080px;height:1920px;box-sizing:border-box;background-color:#0B1222;background-image:linear-gradient(rgba(47,107,255,.22) 2px,transparent 2px),linear-gradient(90deg,rgba(47,107,255,.22) 2px,transparent 2px);background-size:90px 90px;background-position:0 1100px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px;text-align:center;padding:0 80px}
.tag{font-weight:800;font-size:44px;padding:18px 34px;border-radius:14px}
.brand{position:absolute;top:60px;left:0;right:0;text-align:center;font-weight:700;font-size:30px;letter-spacing:4px;color:#8A96AD}
"""
HDR = '<div class="top"><div class="av">S</div><div style="display:flex;flex-direction:column;gap:6px"><span style="color:#fff;font-weight:700;font-size:48px">Sandra ❤</span><span style="color:#8A96AD;font-size:32px">online</span></div></div>'
FALAS = [
 ("sandra","in","Roberto… você sabe quanto a gente já pagou de aluguel?"),
 ("roberto","out","Sei lá, amor… uns trinta mil?"),
 ("sandra","in","Faz a conta comigo: oito anos de aluguel."),
]
def chat(n):
    bs="".join(f'<div class="b {d}{" new" if i==n-1 else ""}">{t}</div>' for i,(q,d,t) in enumerate(FALAS[:n]))
    return f'<div class="chat">{HDR}<div class="msgs">{bs}</div></div>'
SCENES = [
 {"quem":"sandra","fala":"Roberto... você sabe quanto a gente já pagou de aluguel?","html":chat(1),"pausa":0.2},
 {"quem":"roberto","fala":"Sei lá, amor... uns trinta mil?","html":chat(2),"pausa":0.2},
 {"quem":"sandra","fala":"Faz a conta comigo. Oito anos de aluguel.","html":chat(3),"pausa":0.15},
 {"quem":"sandra","fala":"Cento e quinze mil reais.","pausa":0.5,"zoom":0.0015,"html":'<div class="full"><div class="brand">REVÊ</div><div style="color:#fff;font-size:56px;font-weight:700">8 anos de aluguel</div><div class="h" style="font-size:230px;color:#FFC53D">R$ 115<br>MIL</div></div>'},
 {"quem":"roberto","fala":"Cento e quinze mil?! E a casa?","pausa":0.15,"html":'<div class="full"><div class="brand">REVÊ</div><div class="h" style="font-size:150px;color:#fff">E a casa?</div></div>'},
 {"quem":"sandra","fala":"Continua sendo do Seu Bento.","pausa":0.45,"zoom":0.0012,"html":'<div class="full"><div class="brand">REVÊ</div><div class="h" style="font-size:150px;color:#fff">Continua sendo do <span style="color:#FFC53D">Seu Bento.</span></div><div class="tag" style="background:#E5484D;color:#fff">100% DO ALUGUEL FICA COM O DONO</div></div>'},
 {"quem":"roberto","fala":"Amor, amanhã cedo eu vou na Revê. Chega de pagar a casa dos outros.","pausa":0.4,"html":'<div class="full"><div class="brand">REVÊ</div><div class="h" style="font-size:132px;color:#fff">Chega de pagar a casa <span style="color:#FFC53D">dos outros.</span></div></div>'},
 {"quem":"roberto","fala":"E você? Quanto já pagou de aluguel? Comenta aí.","pausa":0.8,"html":'<div class="full" style="background:#FFC53D;background-image:none"><div class="brand" style="color:#0E1526">REVÊ · @reve.imob</div><div class="h" style="font-size:140px;color:#0E1526">Quanto você já pagou de aluguel?</div><div class="tag" style="background:#0E1526;color:#fff">COMENTA AQUI 👇</div><div style="font-size:40px;font-weight:600;color:#0E1526">Valores ilustrativos</div></div>'},
]
