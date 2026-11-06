(function(){
var S=window.SQS||{base:""},d=document;
function $(s,r){return(r||d).querySelector(s)}
var m=$("#menu"),bg=$(".burger");if(bg&&m)bg.onclick=function(){m.classList.toggle("open")};
var ck=$("#ck");try{if(ck&&!localStorage.getItem("ck"))ck.style.display="block"}catch(e){}
d.querySelectorAll("[data-ck]").forEach(function(x){x.onclick=function(){try{localStorage.setItem("ck",x.getAttribute("data-ck"))}catch(e){}ck.style.display="none"}});
var p=new URLSearchParams(location.search),t={};
try{t=JSON.parse(sessionStorage.getItem("trk")||"{}")}catch(e){}
["utm_source","utm_medium","utm_campaign","utm_term","utm_content","click_id","clickid","sub1","gclid","fbclid","msclkid"].forEach(function(k){if(p.get(k))t[k]=p.get(k)});
if(!t.landing)t.landing=location.href;
try{sessionStorage.setItem("trk",JSON.stringify(t))}catch(e){}
var qz=$("#qz");if(qz)qz.onsubmit=function(e){e.preventDefault();location.href=S.base+"/"+$("#qs").value+"/?zip="+encodeURIComponent($("#qzip").value)};
var f=$("#qf");if(!f)return;
var panes=[].slice.call(f.querySelectorAll(".pane")),bars=[].slice.call(f.querySelectorAll(".bar i")),cur=0;
function show(n){cur=n;panes.forEach(function(x,i){x.classList.toggle("on",i===n)});bars.forEach(function(b,i){b.classList.toggle("on",i<=n)})}
function go(){var ok=[].slice.call(panes[cur].querySelectorAll("input,select")).every(function(e){return e.reportValidity()});if(ok)show(cur+1);return ok}
f.querySelectorAll("[data-n]").forEach(function(b){b.onclick=go});
f.querySelectorAll("[data-p]").forEach(function(b){b.onclick=function(){show(cur-1)}});
function set(n,v){if(f.elements[n]&&v)f.elements[n].value=v}
set("page_url",location.href);set("landing_url",t.landing);set("user_agent",navigator.userAgent);
["utm_source","utm_medium","utm_campaign","utm_term","utm_content","gclid","fbclid"].forEach(function(n){set(n,t[n])});
set("click_id",t.click_id||t.clickid||t.sub1);
var z=p.get("zip");if(z&&/^\d{5}$/.test(z))f.elements.zip.value=z;
f.onsubmit=function(e){e.preventDefault();
 if(cur<panes.length-1){go();return}
 if(!f.checkValidity()){f.reportValidity();return}
 var b=f.querySelector("[type=submit]");b.disabled=true;b.textContent="Submitting...";
 set("timestamp",new Date().toISOString());
 var o={};new FormData(f).forEach(function(v,k){o[k]=v});
 o.consent_text=$("#consent-text").innerText;o.site=location.hostname;
 function done(){location.href=S.base+"/thank-you/"}
 function fail(){b.disabled=false;b.textContent="Get My Free Quotes";alert("Something went wrong. Please try again.")}
 if(!S.endpoint){done();return}
 fetch(S.endpoint,{method:"POST",mode:"no-cors",headers:{"Content-Type":"text/plain;charset=utf-8"},body:JSON.stringify(o)}).then(done).catch(fail)};
})();
