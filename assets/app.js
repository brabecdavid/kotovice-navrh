/* JablKOTOVICE – drobné interakce webu (bez knihoven) */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* --- mobilní menu --- */
  var burger = $(".burger"), nav = $("nav.main");
  if (burger && nav) {
    burger.addEventListener("click", function () {
      var on = nav.classList.toggle("on");
      burger.setAttribute("aria-expanded", on ? "true" : "false");
    });
  }

  /* --- je teď otevřeno? (úřední hodiny: Po a St 8–17) --- */
  var HOURS = { 1: [8, 17], 3: [8, 17] };
  $$("[data-open-now]").forEach(function (el) {
    var d = new Date(), h = HOURS[d.getDay()], t = d.getHours() + d.getMinutes() / 60;
    var open = h && t >= h[0] && t < h[1];
    el.classList.toggle("is-open", !!open);
    el.innerHTML = "<i></i>" + (open ? "Úřad je teď otevřený" : "Úřad je teď zavřený");
  });

  /* --- úřední deska --- */
  var DATA = window.DESKA || [];
  var MES = ["led", "úno", "bře", "dub", "kvě", "čvn", "čvc", "srp", "zář", "říj", "lis", "pro"];
  var today = new Date().toISOString().slice(0, 10);
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function cz(iso) { if (!iso) return ""; var p = iso.split("-"); return (+p[2]) + ". " + (+p[1]) + ". " + p[0]; }
  function isNew(iso) { return iso && (new Date(today) - new Date(iso)) / 864e5 <= 14; }
  function row(r) {
    var p = r.od ? r.od.split("-") : ["", "1", "1"];
    var tags = '<span class="tag">' + esc(r.k) + "</span>";
    if (isNew(r.od)) tags = '<span class="tag red">Čerstvě utržené</span>' + tags;
    if (r.do) tags += '<span class="tag grey">sejmutí ' + cz(r.do) + "</span>";
    return '<li><a href="' + esc(r.u) + '" target="_blank" rel="noopener">' +
      '<span class="date' + (isNew(r.od) ? " nove" : "") + '" aria-label="Vyvěšeno ' + cz(r.od) + '"><b>' + (+p[2] || "–") + "</b><small>" + (MES[+p[1] - 1] || "") + " " + (p[0] || "").slice(2) + "</small></span>" +
      '<span><span class="t">' + esc(r.t) + '</span><span class="meta">' + tags + "</span></span>" +
      '<span class="arr" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M7 17 17 7M8 7h9v9"/></svg></span></a></li>';
  }

  var latest = $("[data-deska-latest]");
  if (latest) latest.innerHTML = DATA.slice(0, +latest.getAttribute("data-deska-latest") || 5).map(row).join("");

  var board = $("[data-deska]");
  if (board) {
    var list = $("ol", board), countEl = $("[data-count]"), moreBtn = $("[data-more]"), q = $("#q"), chips = $("[data-chips]");
    var state = { k: "", q: "", mode: "aktualni", limit: 25 };
    var cats = {};
    DATA.forEach(function (r) { cats[r.k] = (cats[r.k] || 0) + 1; });
    var order = Object.keys(cats).sort(function (a, b) { return cats[b] - cats[a]; });
    chips.innerHTML = '<button class="chip" aria-pressed="true" data-k="">Vše<em>' + DATA.length + "</em></button>" +
      order.map(function (k) { return '<button class="chip" aria-pressed="false" data-k="' + esc(k) + '">' + esc(k) + "<em>" + cats[k] + "</em></button>"; }).join("");
    var params = new URLSearchParams(location.search);
    if (params.get("kat")) state.k = params.get("kat");
    if (params.get("q")) { state.q = params.get("q"); q.value = state.q; }

    function norm(s) { return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); }
    function render() {
      $$(".chip", chips).forEach(function (c) { c.setAttribute("aria-pressed", c.getAttribute("data-k") === state.k ? "true" : "false"); });
      $$("[data-mode]").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-mode") === state.mode ? "true" : "false"); });
      var nq = norm(state.q.trim());
      var res = DATA.filter(function (r) {
        var archived = r.do && r.do < today;
        if (state.mode === "aktualni" && archived) return false;
        if (state.mode === "archiv" && !archived) return false;
        if (state.k && r.k !== state.k) return false;
        if (nq && norm(r.t + " " + r.k).indexOf(nq) < 0) return false;
        return true;
      });
      list.innerHTML = res.length ? res.slice(0, state.limit).map(row).join("") : '<li class="empty">Nic jsme nenašli – ani červíčka. Zkuste jiné slovo nebo kategorii.</li>';
      countEl.textContent = res.length + (res.length === 1 ? " dokument" : res.length < 5 && res.length ? " dokumenty" : " dokumentů");
      moreBtn.hidden = res.length <= state.limit;
    }
    chips.addEventListener("click", function (e) { var b = e.target.closest(".chip"); if (!b) return; state.k = b.getAttribute("data-k"); state.limit = 25; render(); });
    $$("[data-mode]").forEach(function (b) { b.addEventListener("click", function () { state.mode = b.getAttribute("data-mode"); state.limit = 25; render(); }); });
    q.addEventListener("input", function () { state.q = q.value; state.limit = 25; render(); });
    moreBtn.addEventListener("click", function () { state.limit += 25; render(); });
    render();
  }

  /* --- zatřes jabloní: po kliknutí na velké jablko se sesypou jablíčka --- */
  var shaker = $(".hero-apple");
  var APPLE = '<svg viewBox="28 14 144 170"><path d="M101 60c0-16 3-30 12-41" stroke="#5B3A1E" stroke-width="10" stroke-linecap="round" fill="none"/><path fill="COLOR" d="M100 58C82 44 44 44 33 82c-10 38 14 92 44 97 12 2 15-4 23-4s11 6 23 4c30-5 54-59 44-97-11-38-49-38-67-24Z"/><path fill="#4E8A22" d="M106 46c10-22 38-26 52-18-10 22-36 28-52 18Z"/><ellipse cx="64" cy="94" rx="11" ry="25" fill="#fff" opacity=".35" transform="rotate(22 64 94)"/></svg>';
  var calm = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (shaker) shaker.addEventListener("click", function () {
    if (calm || !document.body.animate) return;
    var H = window.innerHeight, W = window.innerWidth, n = W < 600 ? 14 : 26;
    for (var i = 0; i < n; i++) {
      (function (i) {
        var el = document.createElement("div");
        el.className = "falling";
        var size = 28 + Math.random() * 30;
        el.style.width = el.style.height = size + "px";
        el.style.left = Math.random() * (W - size) + "px";
        el.innerHTML = APPLE.replace("COLOR", Math.random() < .78 ? "#D7262E" : "#8BBF3F");
        document.body.appendChild(el);
        var rot = (Math.random() * 2 - 1) * 540, drift = (Math.random() * 2 - 1) * 60;
        var a = el.animate([
          { transform: "translate(0,0) rotate(0deg)" },
          { transform: "translate(" + drift + "px," + (H + 120) + "px) rotate(" + rot + "deg)" }
        ], { duration: 1300 + Math.random() * 900, delay: Math.random() * 600, easing: "cubic-bezier(.45,0,.9,.6)", fill: "forwards" });
        a.onfinish = function () { el.remove(); };
      })(i);
    }
  });

  /* --- červík: občas vykoukne z velkého jablka --- */
  var worm = $(".hero .worm");
  if (worm && !calm) {
    var peek = function () {
      worm.classList.remove("peek"); void worm.getBoundingClientRect(); worm.classList.add("peek");
      setTimeout(peek, 11000 + Math.random() * 9000);
    };
    setTimeout(peek, 3500 + Math.random() * 2500);
  }

  /* --- galerie / lightbox --- */
  var gal = $$(".gallery button");
  if (gal.length) {
    var lb = document.createElement("div");
    lb.className = "lb"; lb.setAttribute("role", "dialog"); lb.setAttribute("aria-modal", "true"); lb.setAttribute("aria-label", "Fotografie");
    lb.innerHTML = '<figure><img alt=""><figcaption></figcaption></figure><button class="x" aria-label="Zavřít">✕</button><button class="p" aria-label="Předchozí">‹</button><button class="n" aria-label="Další">›</button>';
    document.body.appendChild(lb);
    var idx = 0, last;
    function show(i) {
      idx = (i + gal.length) % gal.length; var b = gal[idx];
      $("img", lb).src = b.getAttribute("data-full"); $("img", lb).alt = b.getAttribute("data-title");
      $("figcaption", lb).innerHTML = esc(b.getAttribute("data-title")) + "<small>" + esc(b.getAttribute("data-credit")) + "</small>";
    }
    function close() { lb.classList.remove("on"); if (last) last.focus(); }
    gal.forEach(function (b, i) { b.addEventListener("click", function () { last = b; show(i); lb.classList.add("on"); $(".x", lb).focus(); }); });
    $(".x", lb).onclick = close; $(".p", lb).onclick = function () { show(idx - 1); }; $(".n", lb).onclick = function () { show(idx + 1); };
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    document.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("on")) return;
      if (e.key === "Escape") close(); if (e.key === "ArrowLeft") show(idx - 1); if (e.key === "ArrowRight") show(idx + 1);
    });
  }

  /* --- kopírování údajů (číslo účtu, datovka) --- */
  $$("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var v = b.getAttribute("data-copy");
      (navigator.clipboard ? navigator.clipboard.writeText(v) : Promise.reject()).then(function () {
        var o = b.textContent; b.textContent = "Zkopírováno ✓"; setTimeout(function () { b.textContent = o; }, 1600);
      }).catch(function () {});
    });
  });

  /* --- zvýraznění podnabídky při scrollu --- */
  var sub = $$(".subnav a[href^='#']");
  if (sub.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (e) {
        if (e.isIntersecting) sub.forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === "#" + e.target.id); });
      });
    }, { rootMargin: "-30% 0px -60% 0px" });
    sub.forEach(function (a) { var t = document.getElementById(a.getAttribute("href").slice(1)); if (t) io.observe(t); });
  }
})();
