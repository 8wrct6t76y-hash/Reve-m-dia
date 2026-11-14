# Playbook — Instagram da Revê (@reve.imob)

Guia que toda rotina automática segue. Leia inteiro antes de produzir.

## Quem é a Revê
- **Revê Consultoria Imobiliária**, Contagem/MG (Av. José Faria da Rocha, 1440, Eldorado). Grafia sempre "Revê" / "REVÊ".
- Consultoria e assessoria para financiamento do **Minha Casa Minha Vida (MCMV)**, do primeiro atendimento até a chave.
- Provas sociais que podem ser usadas: nota 5 no Google; mais de 100 famílias atendidas em Minas Gerais.
- O WhatsApp está no link da bio. Todo CTA aponta para "WhatsApp no link da bio" ou "comenta PALAVRA".

## Regras que nunca quebram
- Nunca mencionar CRECI nem se apresentar como corretora/imobiliária. Sempre "consultoria".
- Nunca postar foto de cliente real. Nunca inventar depoimento, nome ou história real de cliente.
- Nunca prometer aprovação, prazo ou "sem entrada garantido". Usar "muitas famílias conseguem", "cada caso é um caso", "a Revê analisa o seu perfil".
- Números ilustrativos levam a nota "Valores ilustrativos". Regras do MCMV/FGTS/Caixa só se tiver certeza (pesquisar na web antes se tiver dúvida).
- Máximo de **5 hashtags** por post.
- O objetivo é entreter e gerar compartilhamento, não vender em todo post. Tom: brasileiro, leve, direto, engraçado quando couber.

## Universo de personagens
- **Roberto**: autônomo, casado com a Sandra, pagou aluguel 8 anos (R$ 115 mil em recibos). Voz: `pt-BR-AntonioNeural` (rate +14%, pitch -2Hz).
- **Sandra**: esposa do Roberto, prática, faz as contas. Voz: `pt-BR-ThalitaMultilingualNeural` (rate +12%).
- **Seu Bento**: o dono da casa alugada (o do envelope do reajuste).
- **Zé**: o amigo que acha que tudo é golpe.
- Quadro **"Roberto Responde"**: o Roberto responde pergunta de cliente com conta exagerada e divertida.
- Mesma voz para o mesmo personagem sempre. Falas curtas, coloquiais ("pra", "tá", "né"), com reticências para pausas.

## Identidade visual
- Cores: azul-marinho `#0B1222`/`#0E1526`, amarelo `#FFC53D`, vermelho `#E5484D`, verde `#1F9D55`, texto claro `#C9D2E3`, bege WhatsApp `#ECE5DD`.
- Fonte: Inter Display 800 nos títulos (letter-spacing negativo), Inter no corpo. Já instaladas no sistema.
- Fundo marinho com grade azul neon (estilo Roberto Responde), números gigantes em amarelo, tarjas vermelhas/verdes.
- Carrossel: 1080×1350, 7 a 10 slides, capa com gancho forte; slide 2 também precisa prender; último slide = CTA. Estilos que usamos: conversa de WhatsApp, número gigante, manchete "REVÊ EXPLICA", checklist para salvar, print de post.
- Reel: 1080×1920, 20 a 45 s, gancho nos primeiros 2 s, uma cena a cada 2–4 s, texto grande na tela, final com pergunta para comentar.

## Grade diária (decisão do Victor em 14/11/2026: SEM Reels automáticos, só posts de feed)
Os Reels gerados por aqui (texto animado + voz) ficaram fracos: o Victor só quer vídeo no estilo 3D do Roberto, que ele mesmo produz. As rotinas NÃO fazem Reel.

| Horário (Brasília) | Formato |
|---|---|
| 9h | Post de atualidade: imagem única ou carrossel curto (estilo manchete "REVÊ EXPLICA" ou print de post) |
| 12h | Carrossel de atualidade (7–10 slides) |
| 19h seg–sex, 20h sáb–dom | Post de atualidade com humor/meme (imagem única ou carrossel), feito pra compartilhar |

## Atualidade (o motor do perfil)
O Victor quer posts ligados aos assuntos do momento (trending do X/Twitter, Google, notícia do dia), porque atualidade é o que faz clicar.
- Antes de criar, pesquisar o que está em alta HOJE no Brasil: WebSearch (modo extended) por "assuntos do momento hoje", "trending topics Brasil hoje", notícias do dia (g1, UOL, CNN Brasil, InfoMoney); WebFetch em https://trends.google.com.br/trending?geo=BR quando der. ATENÇÃO: o trends24.in devolve cache antigo (testado em 14/11/2026, mostrava trends de 2024) — não confiar nele; confirmar sempre com notícias datadas de hoje. Datas comemorativas e feriados do dia/da semana são ganchos seguros e bons (ex.: 15/11 Proclamação da República → "O Brasil deixou de ter dono. E a sua casa, ainda tem?").
- Estética: séria e bonita, à altura de uma consultoria. Fundo marinho com grade sutil, títulos Inter Display 800, detalhes em amarelo, toque editorial com serifa itálica (GFS Baskerville) para datas/frases curtas, ícones de linha. Modelo de referência: `sistema/exemplos/carrossel_atualidade_republica.html`.
- Escolher o assunto mais quente que tenha uma ponte natural com casa própria, aluguel, dinheiro, família, trabalho ou o dia a dia de quem paga aluguel. Exemplos de ponte: jogo/final de campeonato → "o aluguel não para nem em dia de final"; salário mínimo/13º/IR/juros/inflação → impacto no bolso e na casa; Black Friday → "parcela que cabe vs. parcela da casa"; reality/série do momento → piada com o Seu Bento ou o Roberto; data comemorativa → casa.
- Fatos do assunto confirmados em pelo menos 2 fontes do dia. Nada de inventar número, declaração ou notícia.
- PROIBIDO pegar carona em: tragédia, morte, crime, violência, doença, desastre, política partidária, eleição, religião, polêmica que ataque pessoas. Sem foto, nome em situação negativa ou fala inventada de pessoa real; sem logo/escudo/imagem de marca, time, série ou celebridade (só texto e arte própria).
- Gancho na primeira linha e na capa. Usar humor e a linguagem da internet brasileira, sem forçar.

Não repetir o mesmo assunto/ângulo dos últimos 7 dias (ver `LOG.md`). Quando não houver assunto quente com ponte segura, usar tema atemporal que funciona (aluguel x financiamento, FGTS, autônomo, nome sujo, documentos, mitos, casa geminada).

## Como produzir e publicar (passo a passo técnico)
1. Clonar: `git clone --depth 1 https://github.com/8wrct6t76y-hash/reve-m-dia /home/claude/reve-m-dia` (se o repo não estiver na sessão, chamar `add_repo` owner `8wrct6t76y-hash`, repo `Reve-m-dia`, access `push`).
2. `pip install --break-system-packages -q edge-tts playwright` se faltar. Chrome em `/usr/bin/google-chrome`. Os scripts já corrigem o certificado do proxy (`/root/.ccr/ca-bundle.crt`).
3. Reel: escrever um `spec.py` (ver `sistema/exemplos/`) com `CSS` e `SCENES` (`quem`, `fala`, `html`, `pausa`, `zoom` opcional) e rodar `python3 sistema/scripts/reel.py spec.py saida.mp4`. Conferir 1 grade de quadros com ffmpeg tile antes de publicar.
4. Carrossel: escrever um HTML com uma `<section class="s">` por slide (ver exemplo) e rodar `python3 sistema/scripts/render_slides.py /caminho/abs/slides.html /pasta/saida` (gera JPEG 1080×1350). Conferir a prévia.
5. Salvar em `AAAA-MM-DD/` no repo, `git add`, commit (user.name "Revê", user.email "noreply@anthropic.com") e `git -c push.negotiate=true push`.
6. URL pública: `https://raw.githubusercontent.com/8wrct6t76y-hash/reve-m-dia/main/AAAA-MM-DD/arquivo`. Conferir com `curl` que responde 200.
7. Publicar pelo Windsor (`mcp__Windsor_ai_for_Social_Media__execute_action`, connector `instagram`, account `17841440397816852`): `create_video_post` (video_url, caption, share_to_feed true) ou `create_carousel_post` (image_urls, caption).
8. Logo após publicar, `create_comment` no novo media_id com uma pergunta para puxar conversa.
9. Registrar no `LOG.md` (data, horário, formato, tema, gancho, media_id) e dar push.

## Legenda
- 1ª linha = gancho (até 125 caracteres). Depois 3–8 linhas curtas com emojis moderados.
- CTA: "Comenta PALAVRA" e/ou "Chama no WhatsApp pelo link da bio". Incluir "Manda pra quem…" para gerar compartilhamento.
- Fechar com até 5 hashtags.

## Respostas a comentários
- Responder todo comentário novo em até poucas horas, em tom humano, curto, com o nome da pessoa quando der.
- Interessado (pergunta sobre valor, aprovação, como funciona, "eu", "quero", palavra-chave do post): agradecer e levar ao WhatsApp: "Te chamo lá? Clica no link da bio e manda 'vim do Insta' que a equipe te atende 😉".
- Demais: engajar (concordar, brincar, perguntar de volta), sem vender.
- Nunca passar valores de taxa, prometer aprovação ou discutir caso pessoal em público. Ofensa/spam: `hide_comment`.
- Não responder comentários da própria conta nem o mesmo comentário duas vezes (checar `comment_reply_count` e o `LOG-comentarios.md`).

## Aprender e melhorar
Toda segunda, a rotina de revisão puxa os números dos últimos 7 e 30 dias (views, alcance, salvamentos, compartilhamentos, comentários, tempo médio assistido, skip rate) e atualiza a seção "O que está funcionando" abaixo. As rotinas de produção seguem essa seção.

## Imagem única
Para `create_image_post`: um JPEG 1080×1350 gerado com `render_slides.py` (uma só `<section class="s">`).

## O que está funcionando
- (14/11/2026) O Victor achou o Reel automático das 17h (texto animado + voz) "ruinzinho" e pediu para parar com Reels automáticos. Foco: 3 posts de feed por dia ligados à atualidade.
- (14/11/2026) Melhores até agora: casa geminada / construção (4.301 views), Roberto Responde moedas (1.434), salário mínimo (1.460), FGTS e conta exagerada costumam ir bem. Vídeos rápidos sem história ficaram ~200 views.
