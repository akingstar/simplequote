import re
s = open("index.html", encoding="utf-8").read()

def rep(old, new):
    global s
    assert old in s, "NOT FOUND: " + old[:60]
    s = s.replace(old, new, 1)

CSS = """
:root{--gold:#C9A24B;--gl:#E5C97A}
body{background:#F4F6FA}
h1,h2{font-family:'Playfair Display',Georgia,serif;letter-spacing:-.01em}
.top{background:#050E1F;border-bottom:1px solid #C9A24B55;font-weight:500}
.top a{color:var(--gl);font-weight:600;margin-left:20px}.top a:hover{color:#fff}
.nav{background:#ffffffee;backdrop-filter:blur(10px);border-bottom:1px solid #E5C97A66}
.logo{font-size:1.4rem}.logo b{color:var(--gold)}
.nl{position:relative}.nl:after{content:"";position:absolute;left:0;bottom:2px;height:2px;width:0;background:var(--gold);transition:.25s}
.nl:hover:after{width:100%}
.cta{background:linear-gradient(135deg,var(--gold),var(--gl));color:#0A192F;font-weight:700;box-shadow:0 6px 16px #c9a24b55}
.cta:hover{background:linear-gradient(135deg,var(--gl),var(--gold));transform:translateY(-1px)}
.hero{position:relative;padding:80px 5% 96px;background:linear-gradient(135deg,rgba(5,14,31,.94),rgba(30,58,138,.86)),url(images/hero.jpg) center/cover,#0A192F}
.hero:after{content:"";position:absolute;left:0;right:0;bottom:0;height:4px;background:linear-gradient(90deg,transparent,var(--gold),transparent)}
.hero h1{font-size:3rem}.hero h1 span{color:var(--gl)}
.eyebrow{display:inline-block;background:#C9A24B22;border:1px solid #C9A24B88;color:var(--gl);padding:6px 16px;border-radius:50px;font-size:.8rem;font-weight:600;margin-bottom:18px;letter-spacing:.03em}
.card{border-top:4px solid var(--gold);border-radius:20px;box-shadow:0 30px 60px #0000004d}
.btn{background:linear-gradient(135deg,#16A34A,#15803D);box-shadow:0 8px 18px #16a34a44;border-radius:10px}
.btn:hover{transform:translateY(-1px);box-shadow:0 12px 24px #16a34a66}
.trust{background:#fff;border-bottom:1px solid var(--b)}
.trust .wrap{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;padding:22px 5%}
.ti{display:flex;gap:12px;align-items:center;font-weight:600;font-size:.9rem;color:var(--p)}.ti b{font-size:1.6rem}
.sh h2{font-size:2.2rem}.sh h2:after{content:"";display:block;width:60px;height:3px;background:var(--gold);margin:12px auto 0;border-radius:3px}
.vc{border-radius:16px;border:1px solid var(--b)}.vc:hover{border-color:var(--gold);box-shadow:0 22px 40px #0A192F26}
.vi{height:190px}.vc:hover .vl{background:var(--p)}
.sc{border-radius:14px}.sc i{background:linear-gradient(135deg,var(--gold),var(--gl));color:#0A192F}
.vh{padding:64px 5%}.vh h1{font-size:2.6rem}
.page{border-top:4px solid var(--gold);box-shadow:0 14px 34px #0A192F14}.page h1{color:var(--p)}
.foot{background:linear-gradient(180deg,#0A192F,#050E1F);border-top:3px solid var(--gold)}.foot h4{color:var(--gl)}
.cband{background:linear-gradient(135deg,#0A192F,#1E3A8A);color:#fff}.cband h2{color:#fff;font-size:1.8rem;margin-bottom:8px}
.cgrid{display:grid;grid-template-columns:1.2fr 1fr auto;gap:30px;align-items:center}
.cband p{color:#CBD5E1}.cband a:not(.cta){color:var(--gl);text-decoration:underline}
@media(max-width:992px){.trust .wrap{grid-template-columns:1fr 1fr}.cgrid{grid-template-columns:1fr}.hero h1{font-size:2.1rem}.top a{margin-left:12px}}
"""
rep("</style>", CSS + "</style>")
s = re.sub(r"family=Poppins:wght@[0-9;]+&display=swap", "family=Poppins:wght@600;700;800&family=Playfair+Display:wght@600;700&display=swap", s, count=1)

# Top bar
s, n = re.subn(r'<div class="top">.*?</span></div>',
 '<div class="top"><span>🇺🇸 Serving consumers across the United States · Free quote-request service</span>'
 '<span><a href="#/about">About Us</a><a href="#/contact">Contact</a><a href="#/privacy">Privacy</a><a href="#/disclosure">Advertising Disclosure</a></span></div>',
 s, count=1, flags=re.S)
assert n == 1, "top bar not found"

# Main menu
rep('<nav class="menu" id="menu">', '<nav class="menu" id="menu"><a class="nl" href="#/">Home</a>')
rep('<a class="cta" id="navcall" style="display:none"></a>',
    '<a class="nl" href="#/about">About</a><a class="nl" href="#/contact">Contact</a>'
    '<a class="cta" id="navcall" style="display:none"></a><a class="cta" href="#/">Get Free Quote</a>')

# Hero eyebrow
rep('<section class="hero"><div class="hc"><div><h1>',
    '<section class="hero"><div class="hc"><div><span class="eyebrow">🇺🇸 FREE QUOTES · UNITED STATES</span><h1>')

# Trust strip
rep('<section class="sec"><div class="wrap"><div class="sh"><h2>Choose a Service</h2>',
    '<div class="trust"><div class="wrap"><div class="ti"><b>🆓</b>Free to use</div><div class="ti"><b>🤝</b>No obligation</div>'
    '<div class="ti"><b>🏢</b>Independent providers</div><div class="ti"><b>🔒</b>Encrypted connection</div></div></div>'
    '<section class="sec"><div class="wrap"><div class="sh"><h2>Choose a Service</h2>')

# Contact band at end of home
rep('handled.</p></div></div></div></section>`}',
    'handled.</p></div></div></div></section>'
    '<section class="sec cband"><div class="wrap cgrid"><div><h2>Questions? We are here to help.</h2>'
    '<p>Learn <a href="#/about">more about us</a> or reach our team directly.</p></div>'
    '<div>${CONFIG.email?`<p>✉ ${CONFIG.email}</p>`:""}${CONFIG.phoneText?`<p>📞 ${CONFIG.phoneText}</p>`:""}'
    '${CONFIG.address?`<p>📍 ${CONFIG.address}</p>`:""}</div><a class="cta" href="#/contact">Contact Us</a></div></section>`}')

open("index.html", "w", encoding="utf-8").write(s)
print("Upgrade done")
