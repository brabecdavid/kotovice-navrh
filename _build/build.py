#!/usr/bin/env python3
"""Sestaví statické stránky webu JablKOTOVICE do kořene složky.
Spouštět:  python3 _build/build.py   (nic dalšího není potřeba)
Hlavička a patička se píšou jen tady, stránky se z nich poskládají.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORIG = "https://www.kotovice.cz"
DL = ORIG + "/e_download.php?file="

# ---------------------------------------------------------------- ikony
def ico(name, cls=""):
    P = {
        "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
        "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
        "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
        "board": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>',
        "home": '<path d="m3 11 9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
        "people": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14c3 0 5 2.2 5 5"/>',
        "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
        "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
        "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
        "doc": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/>',
        "fire": '<path d="M12 3c1 3 5 5 5 10a5 5 0 0 1-10 0c0-2 1-3 2-4 0 2 1 3 2 3 0-3-1-6 1-9z"/>',
        "ball": '<circle cx="12" cy="12" r="9"/><path d="M12 3v18M3 12h18M5.5 5.5c3 3 3 10 0 13M18.5 5.5c-3 3-3 10 0 13"/>',
        "tree": '<path d="M12 21v-6M7 15h10l-5-12z"/><path d="M8.5 10h7"/>',
        "fish": '<path d="M3 12c3-4 8-5 12-2l4-3v10l-4-3c-4 3-9 2-12-2z"/><circle cx="8" cy="11" r=".8" fill="currentColor"/>',
        "book": '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 21V5M8 7h7"/>',
        "cart": '<path d="M3 4h2l2.4 11h10.2L20 8H6.2"/><circle cx="9" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/>',
        "swing": '<path d="M4 21 8 3h8l4 18M8 3l2 11h4l2-11M10 14v3M14 14v3"/>',
        "glass": '<path d="M7 3h10l-1 8a4 4 0 0 1-8 0zM12 15v6M8 21h8"/>',
        "camera": '<path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
        "leaf": '<path d="M5 19c0-9 6-14 15-14 0 9-5 15-14 15"/><path d="M5 19 13 11"/>',
    }
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[name]}</svg>'

APPLE_BODY = "M100 58C82 44 44 44 33 82c-10 38 14 92 44 97 12 2 15-4 23-4s11 6 23 4c30-5 54-59 44-97-11-38-49-38-67-24Z"

COLORS = {
    "red": ("#FF6A5C", "#D7262E", "#9E141B"),
    "green": ("#C8EB72", "#7DB52F", "#3F7A1C"),
}

def apple(cls="", uid="a", color="red"):
    """Značka jablka – znak, ne ilustrace. Gradient generovaný na místě (unikátní id)."""
    c0, c1, c2 = COLORS[color]
    return f'''<svg class="{cls}" viewBox="0 0 200 200" aria-hidden="true"><defs>
<radialGradient id="g{uid}" cx="38%" cy="34%" r="75%"><stop offset="0" stop-color="{c0}"/><stop offset=".55" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></radialGradient>
<linearGradient id="l{uid}" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#4E8A22"/><stop offset="1" stop-color="#8FC544"/></linearGradient></defs>
<path d="M101 60c0-16 3-30 12-41" stroke="#5B3A1E" stroke-width="8" stroke-linecap="round" fill="none"/>
<path fill="url(#g{uid})" d="{APPLE_BODY}"/>
<path fill="url(#l{uid})" d="M106 46c10-22 38-26 52-18-10 22-36 28-52 18Z"/>
<path d="M110 43c14-6 26-10 40-13" stroke="#3F7420" stroke-width="2.4" stroke-linecap="round" fill="none" opacity=".7"/>
<ellipse cx="64" cy="92" rx="10" ry="24" fill="#fff" opacity=".32" transform="rotate(22 64 92)"/>
</svg>'''

# malé ploché jablko místo písmene O v názvu
APPLE_O = ('<svg class="o" viewBox="28 14 144 170" aria-hidden="true">'
           '<path d="M101 60c0-16 3-30 12-41" stroke="currentColor" stroke-width="11" stroke-linecap="round" fill="none"/>'
           f'<path fill="var(--o-fill,#E8302F)" d="{APPLE_BODY}"/>'
           '<path fill="var(--o-leaf,#7DB52F)" d="M106 46c10-22 38-26 52-18-10 22-36 28-52 18Z"/>'
           '<ellipse cx="64" cy="94" rx="11" ry="25" fill="#fff" opacity=".35" transform="rotate(22 64 94)"/></svg>')

WM = ('<span class="wm" role="img" aria-label="JablKOTOVICE"><span class="j">Jabl</span>'
      f'<span class="k">K{APPLE_O}T{APPLE_O}VICE</span></span>')

NAV = [
    ("index.html", "Úvod", ""),
    ("jablko.html", "Jablko", "apple-link"),
    ("obec.html", "Obec", ""),
    ("uredni-deska.html", "Úřední deska", ""),
    ("urad.html", "Úřad", ""),
    ("zivot.html", "Život v obci", ""),
    ("kontakt.html", "Kontakt", ""),
]

FOTO = {  # soubor: (popisek, autor/licence)
    "kotovice-rybnik": ("Kotovice – rybník na návsi", "Foto: Pavel Hrdlička, Wikimedia Commons, CC BY-SA 4.0"),
    "kotovice-urad": ("Kotovice – obecní úřad", "Foto: Pavel Hrdlička, Wikimedia Commons, CC BY-SA 4.0"),
    "kotovice-kaple": ("Kotovice – kaple se zvoničkou z roku 1895", "Foto: Pavel Hrdlička, Wikimedia Commons, CC BY-SA 4.0"),
    "kotovice-ulice": ("Kotovice – boční ulice", "Foto: Pavel Hrdlička, Wikimedia Commons, CC BY-SA 4.0"),
    "kotovice-cesta": ("Kotovice – cesta na Chotěšov", "Foto: Pavel Hrdlička, Wikimedia Commons, CC BY-SA 4.0"),
    "kotovice-dum": ("Kotovice – usedlost", "Foto: Pavel Hrdlička, Wikimedia Commons, CC BY-SA 4.0"),
    "novy-naves": ("Nový – náves", "Foto: Pavel Hrdlička, Wikimedia Commons, CC BY-SA 4.0"),
    "novy-naves-2": ("Nový – náves s posezením", "Foto: Pavel Hrdlička, Wikimedia Commons, CC BY-SA 4.0"),
    "novy-kaple": ("Nový – kaple z roku 1937", "Foto: Pavel Hrdlička, Wikimedia Commons, CC BY-SA 4.0"),
    "novy-cesta": ("Nový – cesta do Záluží", "Foto: Pavel Hrdlička, Wikimedia Commons, CC BY-SA 4.0"),
    "zaluzi-gigant": ("Záluží – barokní dvůr Gigant", "Foto: Pavel Hrdlička, Wikimedia Commons, CC BY-SA 4.0"),
    "zaluzi-kaple": ("Záluží – kaplička", "Foto: Pavel Hrdlička, Wikimedia Commons, CC BY-SA 4.0"),
    "zaluzi-hasicarna": ("Záluží – hasičská zbrojnice", "Foto: Pavel Hrdlička, Wikimedia Commons, CC BY-SA 4.0"),
    "zaluzi-sever": ("Záluží – severní část vsi", "Foto: Pavel Hrdlička, Wikimedia Commons, CC BY-SA 4.0"),
    "zaluzi-immaculata": ("Záluží – socha Panny Marie (Immaculata) z roku 1737", "Foto: Wikimedia Commons, CC0"),
    "zaluzi-socha-gigant": ("Záluží – socha u statku Gigant", "Foto: Wikimedia Commons, CC0"),
}

def img(name, alt=None, cls="", big=False, eager=False):
    a = alt or FOTO[name][0]
    src = f"img/foto/{name}{'' if big else '-m'}.jpg"
    return f'<img class="{cls}" src="{src}" alt="{a}" {"" if eager else "loading=lazy"} decoding="async">'

def fig(name, wide=True):
    t, c = FOTO[name]
    return f'<figure class="figure">{img(name, big=wide)}<figcaption>{t}. {c}</figcaption></figure>'

BASE = '<script>document.write(\'<base href="\' + (location.pathname.indexOf("/kotovice-navrh/") === 0 ? "/kotovice-navrh/" : "/") + \'">\')</script>'

# ---------------------------------------------------------------- kostra stránky
def page(fname, title, desc, body, extra_js=""):
    nav = "".join(
        f'<li><a href="{h}" class="{c}"{" aria-current=page" if h == fname else ""}>{t}</a></li>' for h, t, c in NAV)
    html = f'''<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
{BASE if fname == "404.html" else ""}
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#15361F">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="img/foto/kotovice-rybnik.jpg">
<link rel="icon" href="img/jablko.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Figtree:wght@400;500;600;700;800&display=swap&subset=latin-ext" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#obsah">Přeskočit na obsah</a>
<div class="top"><div class="wrap">
  <a class="ico" href="tel:+420377880004">{ico("phone")}377 880 004</a>
  <a class="ico" href="mailto:obec.kotovice@volny.cz">{ico("mail")}obec.kotovice@volny.cz</a>
  <a class="ico hide-s" href="urad.html#hodiny">{ico("clock")}Po a St 8–17</a>
</div></div>
<header class="site"><div class="wrap">
  <a class="brand" href="index.html" aria-label="JablKOTOVICE – úvodní stránka">{apple(uid="logo")}<span>{WM}<small>obec s největším jablkem v&nbsp;republice</small></span></a>
  <button class="burger" aria-expanded="false" aria-controls="menu">{ico("menu")}Menu</button>
  <nav class="main" id="menu" aria-label="Hlavní menu"><ul>{nav}</ul></nav>
</div></header>
<main id="obsah">
{body}
</main>
<footer class="site">
  <div class="wrap">
    <div>
      {WM}
      <p class="claim">obec s největším jablkem v&nbsp;republice</p>
      <p>Obec Kotovice · Kotovice 22, 333 01 Stod<br>Kotovice · Nový · Záluží</p>
    </div>
    <div><h4>Úřad</h4><ul>
      <li><a href="uredni-deska.html">Úřední deska</a></li>
      <li><a href="urad.html#hodiny">Úřední hodiny</a></li>
      <li><a href="urad.html#povinne">Povinné informace</a></li>
      <li><a href="urad.html#podatelna">E-podatelna</a></li>
      <li><a href="urad.html#gdpr">GDPR</a></li>
    </ul></div>
    <div><h4>Obec</h4><ul>
      <li><a href="jablko.html">Největší jablko</a></li>
      <li><a href="obec.html">Historie a památky</a></li>
      <li><a href="zivot.html">Spolky a akce</a></li>
      <li><a href="zivot.html#galerie">Fotogalerie</a></li>
    </ul></div>
    <div><h4>Kontakt</h4><ul>
      <li><a href="tel:+420377880004">377 880 004</a></li>
      <li><a href="tel:+420724187805">724 187 805 (starosta)</a></li>
      <li><a href="mailto:obec.kotovice@volny.cz">obec.kotovice@volny.cz</a></li>
      <li>Datová schránka: f4pb6r7</li>
    </ul></div>
  </div>
  <div class="bottom"><div class="wrap">
    <span>© 2026 Obec Kotovice · IČ 00574023 · Vypěstováno v Kotovicích</span>
    <span>Fotografie: Pavel Hrdlička a další autoři, Wikimedia Commons (CC BY-SA 4.0 / CC0) · Mapa © přispěvatelé OpenStreetMap</span>
  </div></div>
</footer>
{extra_js}<script src="assets/app.js"></script>
</body>
</html>
'''
    (ROOT / fname).write_text(html, encoding="utf-8")
    print("✓", fname)

def page_hero(crumb, h1, p, bg=None, red=False, art=""):
    bgs = f'<div class="bg" style="background-image:url(img/foto/{bg}.jpg)"></div>' if bg else ""
    return f'''<section class="page-hero{" red" if red else ""}">{bgs}{art}<div class="wrap">
<div class="crumbs"><a href="index.html">Úvod</a> / {crumb}</div>
<h1>{h1}</h1><p>{p}</p></div></section>'''

HOURS = '''<ul class="hours">
<li><b>Pondělí</b><span>8:00 – 17:00<small>starosta 9:00 – 12:00</small></span></li>
<li><b>Středa</b><span>8:00 – 17:00<small>starosta 10:00 – 12:00</small></span></li>
</ul><p style="font-size:.93rem;color:var(--muted)">Po předchozí telefonické domluvě lze sjednat schůzku se starostou i mimo úřední hodiny.</p>'''

MAP = '<iframe title="Mapa obce Kotovice" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=13.105%2C49.652%2C13.185%2C49.695&amp;layer=mapnik&amp;marker=49.6720%2C13.1545"></iframe>'

# ================================================================ ÚVOD
index = f'''
<section class="hero">
  <div class="hero-bg" style="background-image:url(img/foto/kotovice-rybnik.jpg)"></div>
  <div class="wrap">
    <div>
      <span class="eyebrow">Kotovice · Nový · Záluží</span>
      <h1>{WM}</h1>
      <p class="sub">obec s <mark>největším jablkem</mark> v&nbsp;republice</p>
      <p class="lead">Tři vesnice na západním okraji Plzeňské kotliny, 17 km od Plzně. Historie od roku 1272, barokní dvůr Gigant, lípa stará přes 350 let – a v Záluží dozrálo rekordní jablko o váze 697 gramů.</p>
      <div class="ctas">
        <a class="btn btn-red" href="jablko.html">Kousněte do rekordu {ico("arrow")}</a>
        <a class="btn btn-ghost-light" href="uredni-deska.html">Úřední deska</a>
      </div>
    </div>
    <button class="hero-apple" type="button" aria-label="Zatřást jabloní" title="Zatřeste jabloní">
      <svg class="stamp" viewBox="0 0 300 300" aria-hidden="true"><defs><path id="kruh" d="M150 150m-128 0a128 128 0 1 1 256 0a128 128 0 1 1-256 0"/></defs>
        <text><textPath href="#kruh">největší jablko v republice • jablkotovice • </textPath></text></svg>
      {apple("apple", "hero")}
      <span class="badge-rec">Rekord<b>697 g</b>v ČR</span>
    </button>
  </div>
  <span class="credit">Kotovice, rybník na návsi · foto Pavel Hrdlička, CC BY-SA 4.0</span>
</section>

<div class="quick wrap"><ul class="bite-wrap">
  <li><a class="bite" href="uredni-deska.html"><span class="qi">{ico("board")}</span><span><b>Úřední deska</b><span>Vyhlášky, usnesení, rozpočty</span></span></a></li>
  <li><a class="bite" href="jablko.html"><span class="qi">{ico("leaf")}</span><span><b>Rekordní jablko</b><span>697 gramů a zápis v knize rekordů</span></span></a></li>
  <li><a class="bite" href="urad.html"><span class="qi">{ico("clock")}</span><span><b>Úřad a hodiny</b><span>Po a St 8:00 – 17:00</span></span></a></li>
  <li><a class="bite" href="kontakt.html"><span class="qi">{ico("phone")}</span><span><b>Kontakt a platby</b><span>Telefon, e-mail, číslo účtu</span></span></a></li>
</ul></div>

<section class="s"><div class="wrap grid-2">
  <div>
    <div class="s-head"><div><div class="kicker green">{ico("board")} Z úřední desky</div><h2>Čerstvě utržené</h2></div>
      <a class="btn btn-ghost" href="uredni-deska.html">Celá deska {ico("arrow")}</a></div>
    <div class="board"><ol class="dl" data-deska-latest="6"><li class="empty"><a href="uredni-deska.html">Otevřít úřední desku</a></li></ol></div>
  </div>
  <aside class="card">
    <h3>{ico("clock")} Úřední hodiny</h3>
    <span class="open-now" data-open-now><i></i>Úřední hodiny</span>
    {HOURS}
    <a class="btn btn-green" href="kontakt.html" style="width:100%;justify-content:center">Kontakty na úřad</a>
  </aside>
</div></section>

<section class="apple-band"><div class="wrap">
  {apple("apple-big", "band")}
  <div>
    <div class="kicker">Rekord ze Záluží</div>
    <h2>697 gramů. Největší jablko v&nbsp;republice vyrostlo u&nbsp;nás.</h2>
    <p>Na zhruba sedmdesátileté jabloni na zahradě v Záluží dozrálo jablko s obvodem 39 centimetrů. Zapsalo se do České databanky rekordů a loňský rekord překonalo o 83 gramů.</p>
    <div class="ctas" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:24px">
      <a class="btn btn-light" href="jablko.html">Celý příběh jablka {ico("arrow")}</a>
      <a class="btn btn-ghost-light" href="jablko.html#velikost">Jak je velké?</a>
    </div>
  </div>
</div></section>

<section class="s"><div class="wrap">
  <div class="s-head"><div><div class="kicker">{ico("home")} Tři jablka z jednoho stromu</div><h2>Kotovice, Nový a Záluží</h2></div>
    <p>Od roku 1991 je spravuje společný obecní úřad v Kotovicích. Dohromady 977 hektarů a tři návsi, každá s vlastní kaplí.</p></div>
  <div class="villages bite-wrap">
    <a class="village bite" href="obec.html#kotovice">{img("kotovice-kaple")}<span class="pill">od roku 1272</span><div class="in"><h3>Kotovice</h3><p>Typická náves, kaple se zvoničkou z roku 1895 a obecní úřad.</p></div></a>
    <a class="village bite" href="obec.html#novy">{img("novy-kaple")}<span class="pill">od roku 1828</span><div class="in"><h3>Nový</h3><p>Unikátně dochovaná náves, kulturní dům a rybník Kravský.</p></div></a>
    <a class="village bite" href="obec.html#zaluzi">{img("zaluzi-gigant")}<span class="pill">dvůr Gigant</span><div class="in"><h3>Záluží</h3><p>Barokní dvůr Gigant, památná lípa – a zahrada s rekordní jabloní.</p></div></a>
  </div>
</div></section>

<section class="s" style="padding-top:0"><div class="wrap">
  <div class="stats bite-wrap">
    <div class="stat bite"><b>1272</b><span>první písemná zmínka o obci</span></div>
    <div class="stat bite"><b>977 ha</b><span>rozloha katastru tří vesnic</span></div>
    <div class="stat bite"><b>270</b><span>obyvatel podle obecních stránek</span></div>
    <div class="stat bite"><b>360 let</b><span>stáří památné lípy u dvora Gigant</span></div>
    <div class="stat bite"><b>697 g</b><span>váha rekordního jablka ze Záluží</span></div>
  </div>
</div></section>

<section class="s" style="padding-top:0"><div class="wrap map-wrap">
  <div class="card">
    <div class="kicker">{ico("pin")} Kde nás najdete</div>
    <h2 style="font-size:2rem">17 km od Plzně</h2>
    <p>Kotovice leží na západním okraji Plzeňské kotliny, 4 km severozápadně od Stoda, v nadmořské výšce 365–385 m.</p>
    <table class="info"><tr><th>Adresa úřadu</th><td>Kotovice 22, 333 01 Stod</td></tr>
    <tr><th>Okres</th><td>Plzeň-jih</td></tr><tr><th>Mikroregion</th><td>Radbuza</td></tr></table>
    <p style="margin-top:18px"><a class="btn btn-ghost" href="https://www.openstreetmap.org/?mlat=49.6720&amp;mlon=13.1545#map=14/49.6720/13.1545" target="_blank" rel="noopener">Otevřít velkou mapu</a></p>
  </div>
  <div class="map">{MAP}</div>
</div></section>
'''
page("index.html", "JablKOTOVICE – obec s největším jablkem v republice",
     "Návrh webu obce Kotovice (Kotovice, Nový, Záluží) – úřední deska, úřad, život v obci a rekordní jablko o váze 697 gramů.", index,
     '<script src="assets/deska.js"></script>\n')

# ================================================================ JABLKO
small_apple = lambda c, u: apple("", u, c)
jablko = page_hero("Jablko", "Největší jablko v republice",
    "697 gramů, obvod 39 centimetrů. Rekordní jablko vyrostlo na zahradě v Záluží a má svůj zápis v České databance rekordů.", red=True, art=apple("art", "ph1")) + f'''
<div class="wrap layout">
  <nav class="subnav" aria-label="Na této stránce"><ul>
    <li><a href="#rekord">Rekord</a></li><li><a href="#cisla">V číslech</a></li>
    <li><a href="#velikost">Skutečná velikost</a></li><li><a href="#pribeh">Příběh</a></li><li><a href="#psali">Psali o nás</a></li></ul></nav>
  <div class="prose">
    <section id="rekord"><div class="split">
      <div>
        <div class="kicker">Rekord ze Záluží</div>
        <h2>Jablko, které vytáhlo váhu</h2>
        <p>Na přibližně 70 let staré jabloni na zahradě v Kotovicích-Záluží vypěstoval Jiří Bárta ze Vsi Touškov jablko o hmotnosti <b>697 gramů</b> a obvodu <b>39 centimetrů</b>.</p>
        <p>Plod se dostal do České databanky rekordů Agentury Dobrý den, která provozuje Muzeum rekordů v Pelhřimově. Od té doby jsou Kotovice obcí s největším jablkem v&nbsp;republice.</p>
      </div>
      <div class="ph"><div>{apple(uid="ph")}Sem patří fotka rekordního jablka<br><small style="font-weight:500">ideálně s pěstitelem nebo u jabloně</small></div></div>
    </div>
    <div class="todo">Fotku vyžádat od pěstitele nebo od Agentury Dobrý den. Fotka z novinového článku patří agentuře a bez svolení ji použít nejde.</div>
    </section>

    <section id="cisla">
      <h2>Jablko v číslech</h2>
      <div class="facts">
        <div><b>697 g</b><span>hmotnost jablka</span></div>
        <div><b>39 cm</b><span>obvod jablka</span></div>
        <div><b>~70 let</b><span>stáří jabloně</span></div>
        <div><b>+83 g</b><span>oproti loňskému rekordu</span></div>
      </div>
      <p>Na váze by ho vyvážila zhruba čtyři běžná jablka z obchodu.</p>
      <div class="compare" aria-hidden="true">{small_apple("red","c0")}<span class="eq">=</span>{small_apple("green","c1")}{small_apple("green","c2")}{small_apple("green","c3")}{small_apple("green","c4")}</div>
    </section>

    <section id="velikost">
      <h2>Ve skutečné velikosti</h2>
      <div class="real">
        <div>
          <p>Kdyby bylo jablko dokonale kulaté, mělo by při obvodu 39 cm průměr asi <b>12,4 centimetru</b>. Přesně tak široké je jablko níže – přiložte k obrazovce jablko z kuchyně a porovnejte.</p>
          <p style="color:var(--muted);font-size:.92rem">Na většině obrazovek odpovídá velikost přibližně, na mobilu se jablko zmenší, aby se vešlo.</p>
        </div>
        {apple(uid="real").replace('viewBox="0 0 200 200"', 'viewBox="0 0 200 222"').replace("</svg>", '<g stroke="#A9161E" stroke-width="1.4" fill="none"><path d="M33 200h134" stroke-dasharray="3 3"/><path d="M33 194v12M167 194v12"/></g><text x="100" y="217" text-anchor="middle" font-family="Figtree,sans-serif" font-weight="700" font-size="9" fill="#A9161E">průměr ≈ 12,4 cm</text></svg>')}
      </div>
    </section>

    <section id="pribeh">
      <h2>Jak se rodí rekord</h2>
      <p>Rekord převzalo jablko ze Záluží od Pavla Šustra ze Všejan na Mladoboleslavsku, jehož loňské jablko bylo o 83 gramů lehčí.</p>
      <div class="todo">Doplnit od pěstitele: odrůdu, kdy jablko utrhl a jak se o jabloň stará. A zeptat se, jestli souhlasí se zveřejněním jména a fotky na webu obce.</div>
    </section>

    <section id="psali">
      <h2>Psali o nás</h2>
      <a class="press" href="https://plzenska.drbna.cz/zpravy/904876-sedmdesatileta-jablon-vyplodila-obri-jablko-je-z-toho-zapis-v-knize-rekordu.html" target="_blank" rel="noopener">
        <span class="src">{ico("doc")}</span>
        <span><b>Sedmdesátiletá jabloň vyplodila obří jablko. Je z toho zápis v knize rekordů</b><small>Plzeňská Drbna · Zuzana Pešková · 6. 11. 2026</small></span></a>
      <p style="margin-top:16px"><a href="https://www.dobryden.cz/" target="_blank" rel="noopener">Agentura Dobrý den – Česká databanka rekordů</a></p>
    </section>
  </div>
</div>'''
page("jablko.html", "Největší jablko v republice – JablKOTOVICE",
     "Rekordní jablko ze Záluží: 697 gramů, obvod 39 cm, zápis v České databance rekordů.", jablko)

# ================================================================ OBEC
obec = page_hero("Obec", "Obec a její historie",
    "Kotovice, Nový a Záluží – tři vesnice, které spojuje společná historie od roku 1272 i společný obecní úřad.", bg="novy-naves") + f'''
<div class="wrap layout">
  <nav class="subnav" aria-label="Na této stránce"><ul>
    <li><a href="#o-obci">O obci</a></li><li><a href="#kotovice">Kotovice</a></li><li><a href="#novy">Nový</a></li>
    <li><a href="#zaluzi">Záluží</a></li><li><a href="#gigant">Dvůr Gigant</a></li><li><a href="#soucasnost">Současnost</a></li></ul></nav>
  <div class="prose">
    <section id="o-obci">
      <h2>O obci</h2>
      <p>Obec Kotovice leží na západním okraji Plzeňské kotliny, 17 km jihozápadně od Plzně a 4 km severozápadně od Stoda, v nadmořské výšce zhruba 365–385 m n. m. Do správního území o rozloze 977 ha patří ještě vesnice Nový a Záluží. Žije zde celkem 270 obyvatel.</p>
      <div class="facts">
        <div><b>1272</b><span>první zmínka</span></div><div><b>977 ha</b><span>rozloha</span></div>
        <div><b>270</b><span>obyvatel</span></div><div><b>3</b><span>vesnice</span></div><div><b>7</b><span>zastupitelů</span></div>
      </div>
      <p>Do roku 1990 patřily všechny tři obce pod správu MNV ve Stodě, od roku 1991 se osamostatnily a spravuje je Obecní úřad Kotovice. O správě rozhoduje sedmičlenné zastupitelstvo včetně starosty a místostarosty.</p>
    </section>

    <section id="kotovice">
      <h2>Kotovice</h2>
      <p>První zmínka o obci pochází již z roku 1272, a to v souvislosti s chotěšovským klášterem, k němuž tehdy patřila. Jako obec raně feudální má typickou náves, v historickém jádru se dochovalo několik památkově významných budov, většinou hospodářských usedlostí z let 1850–1930.</p>
      {fig("kotovice-rybnik")}
      <h3>Co v Kotovicích najdete</h3>
      <ul class="ticks">
        <li><b>Čtyřbokou kapli se střešní zvoničkou</b> z roku 1895.</li>
        <li><b>Usedlost č. p. 10</b> s dochovanou fasádou svědčící o výstavnosti zdejších dvorů – stále chráněná památkovou péčí.</li>
        <li><b>Původní německou školu</b> v areálu dnešního dětského hřiště, dnes pro volnočasové aktivity místní mládeže.</li>
        <li><b>Bývalou českou menšinovou školu</b> postavenou po roce 1918 pro děti českých obyvatel zdejších vsí; roku 2000 upravenou na 4 byty.</li>
      </ul>
      <div class="split">{fig("kotovice-kaple", False)}{fig("kotovice-urad", False)}</div>
    </section>

    <section id="novy">
      <h2>Nový</h2>
      <p>Obec je novověkého založení, vznikla po zrušení někdejšího klášterního dvora v roce 1828. Na malé, pravidelné návsi je po obvodu unikátně dochovaná historizující zástavba – hospodářské usedlosti ji lemují ze tří stran. Plánovitě zde byly vystavěny nevelké usedlosti lidové architektury, takže v roce 1938 zde stálo již 20 domů.</p>
      {fig("novy-naves-2")}
      <ul class="ticks">
        <li><b>Zděná čtyřboká kaple</b> z roku 1937 v centru návsi, s pětibokým závěrem a věží nad předsíní; fasádu člení lesénový řád.</li>
        <li><b>Usedlosti č. p. 6 a 7</b> s takzvaným polopatrem a branami s vodorovným překladem.</li>
        <li><b>Litinový křížek</b> na žulovém podstavci z 19. století proti domům č. p. 3 a 4, v jeho nice drobná plastika Piety.</li>
        <li><b>Kulturní dům</b> s pohostinstvím – v sálku se konají maškarní bály, mikulášské besídky, taneční zábavy i poslední leče.</li>
        <li><b>Hřiště pro míčové sporty</b> na návsi a obecní <b>rybník Kravský</b> za vsí směrem na Chotěšov.</li>
      </ul>
    </section>

    <section id="zaluzi">
      <h2>Záluží</h2>
      <p>I tato obec je raně feudálního původu, v roce 1272 patřila také k chotěšovskému klášteru. Žije zde přibližně stejný počet obyvatel jako v Novém – okolo padesáti.</p>
      <div class="split">{fig("zaluzi-kaple", False)}{fig("zaluzi-immaculata", False)}</div>
      <ul class="ticks">
        <li><b>Památná lípa velkolistá</b> před domem č. p. 35 u dvora Gigant – stará přibližně 360 let, téměř 34 m vysoká, s obvodem kmene kolem 7 metrů. Mnohokrát ji zasáhl blesk, naposledy v srpnu 2001.</li>
        <li><b>Malá zděná kaplička</b> a vedle ní <b>socha Panny Marie – Immaculata</b> z roku 1737 na hranolovém soklu.</li>
        <li><b>Hasičská zbrojnice</b> se čtyřbokou věží.</li>
        <li><b>Vodní plocha</b> vzniklá zatopením pískového lomu na jižní straně vsi – chov ryb a rekreace.</li>
        <li><b>Zahrada s rekordní jabloní</b> – na zhruba sedmdesátileté jabloni tu dozrálo jablko o váze 697 gramů, zapsané v České databance rekordů. <a href="jablko.html">Více o jablku</a></li>
      </ul>
    </section>

    <section id="gigant">
      <h2>Barokní dvůr Gigant</h2>
      {fig("zaluzi-gigant")}
      <p>Dominantou Kotovicka je klášterní barokní dvůr Gigant v Záluží. Se stavbou dvora do dnešní podoby se začalo asi v polovině 17. století a dokončen byl roku 1711. U dvora stojí památná lípa stará více než 350 let s obvodem kmene 691 cm.</p>
      <p>Asi 500 m za dvorem jihozápadním směrem leží <b>Dvorský rybník</b> o rozloze 4 ha, revitalizovaný v letech 2000–2002. Dvůr Gigant prochází rekonstrukcí a připravuje se pro rekreaci a další komerční využití.</p>
    </section>

    <section id="soucasnost">
      <h2>Současnost</h2>
      <p>Na návsi v Kotovicích sídlí obecní úřad, kde je jednou týdně otevřena místní knihovna s bezplatným internetem. Je zde i prodejna sloužící obyvatelům všech okolních vesnic. Děti i dospělí mohou využívat dětské víceúčelové hřiště postavené s podporou Programu obnovy venkova Plzeňského kraje. Ve všech třech vesnicích byly opraveny kapličky a obnovena veřejná zeleň.</p>
      <a class="btn btn-red" href="zivot.html">Život v obci {ico("arrow")}</a>
    </section>
  </div>
</div>'''
page("obec.html", "Obec a historie – JablKOTOVICE",
     "Historie a památky obce Kotovice a vesnic Nový a Záluží – barokní dvůr Gigant, památná lípa, kaple.", obec)

# ================================================================ ÚŘEDNÍ DESKA
deska = page_hero("Úřední deska", "Úřední deska",
    "Všechny vyhlášky, usnesení zastupitelstva, rozpočty a oznámení na jednom místě. Hledejte slovem nebo filtrujte podle kategorie.", bg="kotovice-urad", art=apple("art", "ud", "green")) + f'''
<div class="wrap" style="padding-top:50px;padding-bottom:90px" data-deska>
  <div class="filters">
    <label class="search" for="q">{ico("search")}<span class="sr">Hledat na úřední desce</span>
      <input id="q" type="search" placeholder="Hledat – např. rozpočet, odpad, usnesení…" autocomplete="off"></label>
    <div class="chips" data-chips aria-label="Kategorie"></div>
    <div class="f-row"><span data-count></span>
      <span class="seg" role="group" aria-label="Zobrazit"><button data-mode="aktualni" aria-pressed="true">Aktuální</button><button data-mode="archiv" aria-pressed="false">Archiv</button><button data-mode="vse" aria-pressed="false">Vše</button></span></div>
  </div>
  <div class="board"><ol class="dl"></ol><div class="more"><button class="btn btn-ghost" data-more hidden>Utrhnout další</button></div></div>
  <noscript><p>Pro filtrování zapněte JavaScript. Úplný seznam je na <a href="{ORIG}/urad-obce/uredni-deska/">původní úřední desce</a>.</p></noscript>
  <p style="color:var(--muted);font-size:.9rem;margin-top:18px">Dokumenty se otevírají v plném znění na serveru obce. Fyzická úřední deska je u obecního úřadu, Kotovice 22.</p>
</div>'''
page("uredni-deska.html", "Úřední deska – Obec Kotovice",
     "Elektronická úřední deska obce Kotovice – vyhlášky, usnesení, rozpočty, oznámení.", deska,
     '<script src="assets/deska.js"></script>\n')

# ================================================================ ÚŘAD
def doc(href, title, note=""):
    return f'<li><a href="{href}" target="_blank" rel="noopener"><span class="pdf">PDF</span><span>{title}{f"<small>{note}</small>" if note else ""}</span></a></li>'

urad = page_hero("Úřad", "Obecní úřad",
    "Úřední hodiny, povinné informace, e-podatelna, územní plán a dokumenty ke stažení.", bg="kotovice-urad", art=apple("art", "ur", "green")) + f'''
<div class="wrap layout">
  <nav class="subnav" aria-label="Na této stránce"><ul>
    <li><a href="#hodiny">Úřední hodiny</a></li><li><a href="#vedeni">Vedení obce</a></li><li><a href="#dokumenty">Dokumenty</a></li>
    <li><a href="#uzemni-plan">Územní plán</a></li><li><a href="#dcov">Dotace DČOV</a></li><li><a href="#podatelna">E-podatelna</a></li>
    <li><a href="#povinne">Povinné informace</a></li><li><a href="#gdpr">GDPR</a></li></ul></nav>
  <div class="prose">
    <section id="hodiny"><div class="split" style="align-items:start">
      <div><h2>Úřední hodiny</h2><span class="open-now" data-open-now><i></i>Úřední hodiny</span>{HOURS}</div>
      <div>{fig("kotovice-urad", False)}</div></div>
    </section>

    <section id="vedeni">
      <h2>Vedení obce</h2>
      <div class="split">
        <div class="person"><span class="avatar">JR</span><div><div class="label">Starosta</div><b style="font-family:var(--f-head);font-size:1.25rem">Jakub Rada</b><br><a href="tel:+420724187805">724 187 805</a></div></div>
        <div class="person"><span class="avatar">JP</span><div><div class="label">Místostarosta</div><b style="font-family:var(--f-head);font-size:1.25rem">Josef Poukar</b><br><a href="tel:+420377880004">377 880 004</a></div></div>
      </div>
      <p style="margin-top:20px">Zastupitelstvo má sedm členů. Při zastupitelstvu pracuje finanční a kontrolní výbor. Usnesení z veřejných zasedání najdete na <a href="uredni-deska.html?kat=Usnesení">úřední desce</a>.</p>
      <div class="todo">Doplnit jmenný seznam zastupitelů po ustavujícím zasedání 4. 11. 2026.</div>
    </section>

    <section id="dokumenty">
      <h2>Dokumenty ke stažení</h2>
      <ul class="docs">
        {doc("dokumenty/zadost-o-pujceni-vybaveni.pdf", "Žádost o půjčení vybavení", "stoly, lavice a další obecní vybavení")}
      </ul>
      <p style="margin-top:16px">Rozpočty, závěrečné účty a vyhlášky jsou na <a href="uredni-deska.html">úřední desce</a>.</p>
    </section>

    <section id="uzemni-plan">
      <h2>Územní plán obce Kotovice</h2>
      <p>Územní plán – jednotný standard + úplné znění po změně č. 1. Změna č. 1 (převod do JS) byla spolufinancována z prostředků státního rozpočtu ČR z programu Ministerstva pro místní rozvoj ČR.</p>
      <ul class="docs">
        {doc("dokumenty/up-informace-o-vydani-zmeny-1.pdf", "Informace o vydání Změny č. 1 ÚP Kotovice", "132 kB")}
        {doc("dokumenty/up-textova-cast.pdf", "Textová část", "654 kB")}
        {doc("dokumenty/up-vykres-zakladniho-cleneni.pdf", "Výkres základního členění území", "1,6 MB")}
        {doc("dokumenty/up-hlavni-vykres.pdf", "Hlavní výkres", "3,8 MB")}
        {doc("dokumenty/up-verejne-prospesne-stavby.pdf", "Výkres veřejně prospěšných staveb", "856 kB")}
        {doc("dokumenty/up-koncepce-infrastruktury.pdf", "Koncepce dopravní a technické infrastruktury", "1,8 MB")}
        {doc("dokumenty/up-koordinacni-vykres.pdf", "Koordinační výkres", "4,0 MB")}
      </ul>
    </section>

    <section id="dcov">
      <h2>Dotace na domácí čistírnu odpadních vod</h2>
      <p>Obec podporuje z rozpočtu výstavbu domácích čistíren odpadních vod (DČOV). Podmínky a žádost:</p>
      <ul class="docs">
        {doc("dokumenty/dcov-dotacni-program.pdf", "Dotační program – DČOV", "280 kB")}
        {doc("dokumenty/dcov-pravidla.pdf", "Pravidla poskytování dotace", "785 kB")}
        {doc("dokumenty/dcov-zadost.pdf", "Příloha č. 1 – žádost", "229 kB")}
      </ul>
    </section>

    <section id="podatelna">
      <h2>E-podatelna</h2>
      <table class="info">
        <tr><th>Adresa pro doručování</th><td>Obec Kotovice, Kotovice 22, 333 01 Kotovice</td></tr>
        <tr><th>ID datové schránky</th><td><b>f4pb6r7</b> <button class="copy" data-copy="f4pb6r7">Kopírovat</button></td></tr>
        <tr><th>Elektronická adresa podatelny</th><td><a href="mailto:obec.kotovice@volny.cz">obec.kotovice@volny.cz</a></td></tr>
        <tr><th>Hodiny podatelny</th><td>Po 8:00–15:30 · Út 8:00–14:00 · St 8:00–17:00 · Pá 8:00–12:00</td></tr>
        <tr><th>Přijímané formáty</th><td>PDF, DOC, DOCX, TXT, JPG/JPEG, PNG, XLS, XLSX (i zabalené v ZIP), max. 15 MB</td></tr>
        <tr><th>Fyzické nosiče</th><td>flash disk, CD-ROM, DVD-ROM</td></tr>
      </table>
      <div class="todo">Hodiny podatelny se na původním webu liší od úředních hodin (Út a Pá). Ověřit, které platí.</div>
      <p style="margin-top:14px">Datovou zprávu v chybném formátu nebo se škodlivým programem úřad nezpracuje, pokud se vadu nepodaří odstranit ve spolupráci s odesílatelem. Totéž platí pro neúplný nebo poškozený dokument. Podání podle § 37 správního řádu musí obsahovat, kdo je činí, které věci se týká a co se navrhuje.</p>
    </section>

    <section id="povinne">
      <h2>Povinné informace</h2>
      <p style="color:var(--muted)">Informace zveřejňované podle zákona č. 106/1999 Sb., o svobodném přístupu k informacím.</p>
      <table class="info">
        <tr><th>1. Název</th><td>Obec Kotovice</td></tr>
        <tr><th>2. Důvod a způsob založení</th><td>Obec vznikla podle zákona č. 367/1990 Sb., o obcích, dnem voleb do obecního zastupitelstva v roce 1990. Funkce vykonává podle zákona č. 128/2000 Sb.</td></tr>
        <tr><th>3. Organizační struktura</th><td>Zastupitelstvo, finanční výbor, kontrolní výbor</td></tr>
        <tr><th>4. Kontaktní spojení</th><td>Kotovice 22, 333 01 Kotovice · tel. 377 880 004, 724 187 805 · obec.kotovice@volny.cz</td></tr>
        <tr><th>4.3 Úřední hodiny</th><td>Pondělí a středa 8:00–17:00</td></tr>
        <tr><th>4.8 Datová schránka</th><td>f4pb6r7</td></tr>
        <tr><th>5. Bankovní spojení</th><td>19423361/0100, Komerční banka, a.s.</td></tr>
        <tr><th>6. IČO</th><td>00574023</td></tr>
        <tr><th>7. Plátce DPH</th><td>Nejsme plátci DPH</td></tr>
        <tr><th>8. Rozpočet</th><td><a href="uredni-deska.html?kat=Rozpočet">Úřední deska – rozpočet</a></td></tr>
        <tr><th>9. Žádosti o informace</th><td>Ústně v kanceláři úřadu, písemně osobně nebo poštou na adresu úřadu, e-mailem, datovou schránkou f4pb6r7 nebo telefonicky na 724 187 805.</td></tr>
      </table>
      <h3>Lhůty podle zákona 106/1999 Sb.</h3>
      <ul class="ticks">
        <li>Odkaz na zveřejněnou informaci – 7 dnů</li>
        <li>Výzva k upřesnění nesrozumitelné nebo příliš obecné žádosti – 7 dnů</li>
        <li>Odložení žádosti mimo působnost úřadu – 7 dnů</li>
        <li>Poskytnutí informace žadateli – 15 dnů</li>
      </ul>
      <p><a href="{ORIG}/urad-obce/povinne-informace/" target="_blank" rel="noopener">Úplné znění povinných informací</a> · <a href="uredni-deska.html?kat=Informace dle zák. 106/1999 Sb.">Výroční zprávy a odpovědi na žádosti</a></p>
    </section>

    <section id="gdpr">
      <h2>Ochrana osobních údajů (GDPR)</h2>
      <p>Službu pověřence pro obec Kotovice vykonává <b>Mikroregion Radbuza</b> prostřednictvím MAS Radbuza, z.s., konkrétně Mgr. et Mgr. Miroslav Šuma, nám. ČSA 24, 333 01 Stod.</p>
      <table class="info">
        <tr><th>Telefon</th><td><a href="tel:+420720021963">720 021 963</a>, <a href="tel:+420725830833">725 830 833</a></td></tr>
        <tr><th>E-mail</th><td><a href="mailto:gdpr@mas-radbuza.cz">gdpr@mas-radbuza.cz</a></td></tr>
        <tr><th>Správce údajů</th><td>Obec Kotovice, Kotovice č. 22, 333 01 Stod, IČ 00574023</td></tr>
      </table>
      <p style="margin-top:14px"><a href="{ORIG}/urad-obce/gdpr/" target="_blank" rel="noopener">Úplné prohlášení o zpracování osobních údajů</a></p>
    </section>
  </div>
</div>'''
page("urad.html", "Obecní úřad – Obec Kotovice",
     "Úřední hodiny, vedení obce, povinné informace, e-podatelna, územní plán a dokumenty obce Kotovice.", urad)

# ================================================================ ŽIVOT V OBCI
gal = ["kotovice-rybnik", "kotovice-kaple", "kotovice-urad", "kotovice-ulice", "kotovice-cesta", "kotovice-dum",
       "novy-naves", "novy-naves-2", "novy-kaple", "novy-cesta", "zaluzi-gigant", "zaluzi-kaple",
       "zaluzi-hasicarna", "zaluzi-sever", "zaluzi-immaculata", "zaluzi-socha-gigant"]
gallery = "".join(
    f'<button data-full="img/foto/{g}.jpg" data-title="{FOTO[g][0]}" data-credit="{FOTO[g][1]}">{img(g)}<span>{FOTO[g][0].split(" – ")[0]}</span></button>'
    for g in gal)

def club(icon, name, text):
    return f'<div class="club"><span class="ic">{ico(icon)}</span><h3>{name}</h3><p>{text}</p></div>'

zivot = page_hero("Život v obci", "Život v obci",
    "Kde to v Kotovicích, Novém a Záluží žije: spolky, akce, služby a fotky ze všech tří vesnic.", bg="novy-naves-2") + f'''
<div class="wrap layout">
  <nav class="subnav" aria-label="Na této stránce"><ul>
    <li><a href="#akce">Akce v roce</a></li><li><a href="#spolky">Spolky</a></li><li><a href="#sluzby">Služby</a></li>
    <li><a href="#odpady">Odpady</a></li><li><a href="#galerie">Fotogalerie</a></li></ul></nav>
  <div class="prose">
    <section id="akce">
      <h2>Akce po celý rok – od bálu po nadílku</h2>
      <p>Obec, hasiči a spolky pořádají akce pro děti i dospělé. Pozvánky vyvěšujeme na <a href="uredni-deska.html?kat=Oznámení">úřední desce</a>.</p>
      <div class="year">
        <div><small>zima</small><b>Hasičský bál</b>SDH v kulturním domě Nový</div>
        <div><small>zima</small><b>Dětský maškarní bál</b>v kulturním domě Nový</div>
        <div><small>jaro / léto</small><b>Den dětí</b>pro děti z obce</div>
        <div><small>konec léta</small><b>Rybářské závody</b>na Střelnici v Novém</div>
        <div><small>léto</small><b>Kino</b>v Novém</div>
        <div><small>sezóna</small><b>Autobusové zájezdy</b>na zajímavá místa republiky</div>
        <div><small>advent</small><b>Adventní setkání</b>na návsi v Novém</div>
        <div><small>prosinec</small><b>Mikulášská nadílka</b>pro nejmenší</div>
      </div>
      <div class="todo">Doplnit termíny akcí na rok 2027 – ideálně s datem, místem a pořadatelem.</div>
    </section>

    <section id="spolky">
      <h2>Spolky</h2>
      <div class="clubs">
        {club("fire", "SDH – hasiči", "Pořádají hasičský bál a adventní setkání. Hledají nové členy – chceš se stát hasičem?")}
        {club("ball", "TJ Sokol Záluží", "Taneční zábavy a sportovní život v obci.")}
        {club("tree", "Myslivecké sdružení", "Péče o zvěř v okolí, tradiční poslední leč.")}
      </div>
      <div class="todo">Doplnit kontakty na předsedy spolků (jméno, telefon nebo e-mail).</div>
    </section>

    <section id="sluzby">
      <h2>Kde si co zařídit</h2>
      <div class="clubs">
        {club("book", "Knihovna", "Na obecním úřadě v Kotovicích, otevřeno jednou týdně, s bezplatným internetem.")}
        {club("cart", "Prodejna", "Prodejna v Kotovicích č. 59 slouží obyvatelům všech okolních vesnic.")}
        {club("glass", "Kulturní dům Nový", "Pohostinství a sál pro bály, besídky a zábavy.")}
        {club("swing", "Dětské hřiště", "Víceúčelové hřiště v Kotovicích, hřiště pro míčové sporty na návsi v Novém.")}
      </div>
      <div class="todo">Doplnit otevírací dobu knihovny, prodejny a pohostinství.</div>
    </section>

    <section id="odpady">
      <h2>Odpady</h2>
      <p>V Kotovicích je sběrné místo, větší odpad můžete odvézt do sběrného dvora ve Stodě. Poplatek za odpad a pravidla stanoví obecně závazná vyhláška.</p>
      <p><a class="btn btn-ghost" href="uredni-deska.html?q=odpad">Vše o odpadech na úřední desce {ico("arrow")}</a></p>
    </section>

    <section id="galerie">
      <h2>Fotogalerie</h2>
      <div class="gallery">{gallery}</div>
      <p style="margin-top:16px;font-size:.9rem;color:var(--muted)">Starší alba z akcí (dětský den, výlov Zálužského rybníka, adventní zpívání) najdete v <a href="{ORIG}/fotografie/" target="_blank" rel="noopener">archivu fotografií</a>.</p>
    </section>
  </div>
</div>'''
page("zivot.html", "Život v obci – JablKOTOVICE",
     "Spolky, akce, služby a fotogalerie obce Kotovice, Nový a Záluží.", zivot)

# ================================================================ KONTAKT
kontakt = page_hero("Kontakt", "Kontakt",
    "Zavolejte, napište, nebo se zastavte v úředních hodinách. Na úřadě nekoušeme – to necháváme jablkům.", bg="kotovice-ulice") + f'''
<div class="wrap" style="padding-top:50px;padding-bottom:30px">
  <div class="contact-grid">
    <div class="card"><div class="label">Telefon na úřad</div><a class="big-link" href="tel:+420377880004">377 880 004</a>
      <div class="label" style="margin-top:16px">Starosta – mobil</div><a class="big-link" href="tel:+420724187805">724 187 805</a></div>
    <div class="card"><div class="label">E-mail</div><a class="big-link" href="mailto:obec.kotovice@volny.cz">obec.kotovice@volny.cz</a>
      <div class="label" style="margin-top:16px">Datová schránka</div><span class="big-link">f4pb6r7</span><button class="copy" data-copy="f4pb6r7">Kopírovat</button></div>
    <div class="card"><div class="label">Adresa</div><span class="big-link">Obecní úřad Kotovice<br>Kotovice 22<br>333 01 Stod</span></div>
  </div>
</div>
<div class="wrap grid-2" style="padding-bottom:30px">
  <div class="card">
    <h3>Fakturační a platební údaje</h3>
    <table class="info">
      <tr><th>Název</th><td>Obec Kotovice</td></tr>
      <tr><th>Sídlo</th><td>Kotovice č. 22, 333 01 Stod</td></tr>
      <tr><th>IČ</th><td>00574023</td></tr>
      <tr><th>Plátce DPH</th><td>ne</td></tr>
      <tr><th>Číslo účtu</th><td><b>19423361/0100</b> (Komerční banka)<br><button class="copy" data-copy="19423361/0100">Kopírovat číslo účtu</button></td></tr>
    </table>
    <h3 style="margin-top:28px">Vedení obce</h3>
    <div class="split">
      <div class="person"><span class="avatar">JR</span><div><div class="label">Starosta</div><b>Jakub Rada</b></div></div>
      <div class="person"><span class="avatar">JP</span><div><div class="label">Místostarosta</div><b>Josef Poukar</b></div></div>
    </div>
  </div>
  <aside class="card"><h3>{ico("clock")} Úřední hodiny</h3><span class="open-now" data-open-now><i></i>Úřední hodiny</span>{HOURS}</aside>
</div>
<div class="wrap" id="mapa" style="padding-bottom:90px;scroll-margin-top:100px"><div class="map" style="min-height:420px">{MAP}</div></div>'''
page("kontakt.html", "Kontakt – Obec Kotovice",
     "Kontakty na obecní úřad Kotovice – telefon, e-mail, datová schránka, číslo účtu, úřední hodiny a mapa.", kontakt)

# ================================================================ 404
e404 = f'''<section class="e404"><div>
  <svg viewBox="0 0 200 200" aria-hidden="true"><path d="M101 40c0-12 3-22 10-30" stroke="#5B3A1E" stroke-width="8" stroke-linecap="round" fill="none"/>
  <path fill="#D7262E" d="M100 42c-22-10-52-6-56 22 30 0 42 10 56 10s26-10 56-10c-4-28-34-32-56-22Z"/>
  <path fill="#F6E7C8" d="M62 74c8 18 8 40 0 62h76c-8-22-8-44 0-62-12 4-24 6-38 6s-26-2-38-6Z"/>
  <path fill="#D7262E" d="M44 136c4 30 34 36 56 28 22 8 52 2 56-28-30 0-42-6-56-6s-26 6-56 6Z"/>
  <g fill="#5B3A1E"><ellipse cx="92" cy="104" rx="3" ry="6"/><ellipse cx="108" cy="104" rx="3" ry="6"/></g></svg>
  <h1>Tady zbyl jen ohryzek</h1>
  <p style="color:var(--muted);font-size:1.1rem;max-width:44ch;margin:0 auto 24px">Stránka, kterou hledáte, už někdo snědl – nebo nikdy nedozrála. Zkuste to z úvodu.</p>
  <a class="btn btn-red" href="index.html">Zpět na úvod {ico("arrow")}</a>
</div></section>'''
page("404.html", "Stránka nenalezena – JablKOTOVICE", "Tato stránka neexistuje.", e404)

# favicon
(ROOT / "img" / "jablko.svg").write_text(apple(uid="fav").replace('<svg class=""', '<svg xmlns="http://www.w3.org/2000/svg"'), encoding="utf-8")
print("✓ img/jablko.svg")
