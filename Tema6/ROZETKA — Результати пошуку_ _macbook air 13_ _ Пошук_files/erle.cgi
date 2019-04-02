
(function (ph){
try{
var A = self['' || 'AdriverCounter'], 
	a = A(ph);
a.reply = {
ph:ph,
rnd:'790729',
bt:62,
sid:195467,
pz:0,
sz:'%2fua%2fsearch%2f%3ftext%3dmacbook%2bair%2b13',
bn:0,
sliceid:0,
netid:0,
ntype:0,
tns:0,
pass:'',
adid:0,
bid:2864425,
geoid:122,
cgihref:'//ad.adriver.ru/cgi-bin/click.cgi?sid=195467&ad=0&bid=2864425&bt=62&bn=0&pz=0&xpid=DUxN4nd0YXVWM89Ca69dnJXbzFB2JjIUs92AoMVwY6K0jllkWhmDGFhtJ_-9bc-Nqr35XMEE&ref=https:%2f%2frozetka.com.ua%2fua%2fsearch%2f%3ftext%3dmacbook%2bair%2b13&custom=153%3Dnull',
target:'_blank',
width:'0',
height:'0',
alt:'AdRiver',
mirror:A.httplize('//colo2.adriver.ru'), 
comp0:'0/script.js',
custom:{"153":"null"},
cid:'',
uid:0,
xpid:'DUxN4nd0YXVWM89Ca69dnJXbzFB2JjIUs92AoMVwY6K0jllkWhmDGFhtJ_-9bc-Nqr35XMEE'
}
var r = a.reply;

r.comppath = r.mirror + '/images/0002864/0002864425/' + (/^0\//.test(r.comp0) ? '0/' : '');
r.comp0 = r.comp0.replace(/^0\//,'');
if (r.comp0 == "script.js" && r.adid){
	A.defaultMirror = r.mirror; 
	A.loadScript(r.comppath + r.comp0 + '?v' + ph) 
} else if ("function" === typeof (A.loadComplete)) {
   A.loadComplete(a.reply);
}
(function (o) {
	var i, w = o.c || window, d = document, y = 10;
	function oL(){
		if (!w.postMessage || !w.addEventListener) {return;}
		if (w.document.readyState == 'complete') {return sL();}
		w.addEventListener('load', sL, false);
	}
	function sL(){try{i.contentWindow.postMessage('pgLd', '*');}catch(e){}}
	function mI(u, oL){
		var i = d.createElement('iframe'); i.setAttribute('src', o.hl(u)); i.onload = oL; with(i.style){width = height = '10px'; position = 'absolute'; top = left = '-10000px'} d.body.appendChild(i);
		return i;
	}
	function st(u, oL){
		if (d.body){return i = mI(u, oL)}
		if(y--){setTimeout(function(){st(u, oL)}, 100)}
	}
	st(o.hl('//content.adriver.ru/banners/0002186/0002186173/0/l6.html?0&4&6&0&790729&0&0&122&93.75.203.6&counter&' + (o.all || 0)), oL);
}({
	hl: A.httplize,
	
}));
}catch(e){} 
}('1'));
