CSS = """
body{margin:0;width:1080px;height:1920px;font-family:'Inter',sans-serif;overflow:hidden}
.h{font-family:'Inter Display','Inter';font-weight:800;letter-spacing:-4px;line-height:.95}
.full{position:relative;width:1080px;height:1920px;box-sizing:border-box;background-color:#0B1222;background-image:linear-gradient(rgba(47,107,255,.25) 2px,transparent 2px),linear-gradient(90deg,rgba(47,107,255,.25) 2px,transparent 2px);background-size:90px 90px;background-position:0 1100px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:44px;text-align:center;padding:0 80px}
.tag{font-weight:800;font-size:42px;padding:18px 34px;border-radius:14px}
.ep{position:absolute;top:110px;left:0;right:0;display:flex;justify-content:center}
.ep span{background:#FFC53D;color:#0B1222;font-weight:800;font-size:32px;letter-spacing:3px;padding:12px 26px;border-radius:10px}
.sub{position:absolute;bottom:300px;left:80px;right:80px;color:#fff;font-weight:700;font-size:50px;line-height:1.2;text-shadow:0 4px 16px rgba(0,0,0,.6)}
.n{font-family:'Inter Display';font-weight:800;font-size:300px;line-height:.8;color:#FFC53D;letter-spacing:-10px}
.x{font-size:52px;color:#C9D2E3;line-height:1.3}
"""
EP='<div class="ep"><span>ROBERTO RESPONDE · FGTS</span></div>'
def S(inner, sub, bg=""): return f'<div class="full" {bg}>{EP}{inner}<div class="sub">{sub}</div></div>'
SCENES=[
 {"quem":"roberto","fala":"O dinheiro do seu FGTS pode virar a entrada da sua casa. Sabia disso?","pausa":0.2,"zoom":0.0012,
  "html":S('<div class="h" style="font-size:150px;color:#fff">Seu <span style="color:#FFC53D">FGTS</span> pode virar a entrada da sua casa</div>','Sabia disso?')},
 {"quem":"roberto","fala":"Tem muita gente com esse dinheiro parado, e nem lembra que ele existe.","pausa":0.2,
  "html":S('<div class="h" style="font-size:130px;color:#fff">Dinheiro <span style="color:#FFC53D">parado</span></div><div class="tag" style="background:#E5484D;color:#fff">E MUITA GENTE NEM LEMBRA</div>','nem lembra que ele existe.')},
 {"quem":"roberto","fala":"Mas pra usar, tem três regras. Bora?","pausa":0.25,
  "html":S('<div class="n">3</div><div class="h" style="font-size:120px;color:#fff">regras</div>','Bora?')},
 {"quem":"roberto","fala":"Um: somar pelo menos três anos de carteira assinada. Não precisa ser na mesma empresa.","pausa":0.3,
  "html":S('<div class="n">1</div><div class="h" style="font-size:96px;color:#fff">3 anos de carteira assinada</div><div class="x">somando tudo, mesmo em empresas diferentes</div>','Não precisa ser na mesma empresa.')},
 {"quem":"roberto","fala":"Dois: não ter outro imóvel na cidade onde você mora ou trabalha.","pausa":0.3,
  "html":S('<div class="n">2</div><div class="h" style="font-size:96px;color:#fff">Sem outro imóvel na sua cidade</div><div class="x">onde você mora ou trabalha</div>','não ter outro imóvel na cidade.')},
 {"quem":"roberto","fala":"Três: não ter outro financiamento habitacional ativo.","pausa":0.3,
  "html":S('<div class="n">3</div><div class="h" style="font-size:96px;color:#fff">Sem financiamento habitacional ativo</div>','não ter outro financiamento ativo.')},
 {"quem":"roberto","fala":"Passou nas três? Esse dinheiro entra na compra, você financia menos, e a parcela fica menor.","pausa":0.35,"zoom":0.0012,
  "html":S('<div class="tag" style="background:#1F9D55;color:#fff">PASSOU NAS 3?</div><div class="h" style="font-size:130px;color:#fff">Financia menos.<br><span style="color:#FFC53D">Parcela menor.</span></div>','e a parcela fica menor.')},
 {"quem":"roberto","fala":"Comenta FGTS, que a gente te explica o passo a passo. E manda pra quem tem carteira assinada!","pausa":0.8,
  "html":'<div class="full" style="background:#FFC53D;background-image:none"><div class="ep"><span style="background:#0B1222;color:#FFC53D">REVÊ · @reve.imob</span></div><div class="h" style="font-size:150px;color:#0B1222">Comenta FGTS 👇</div><div style="font-size:52px;font-weight:600;color:#0B1222;line-height:1.3">e manda pra quem tem carteira assinada</div><div style="font-size:34px;color:#0B1222">Regras do FGTS para moradia. Cada caso é um caso.</div></div>'},
]
