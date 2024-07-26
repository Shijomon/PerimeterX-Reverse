import subprocess
import json
import requests
import uuid
import time
import re
import random
from user_agent import generate_user_agent
useragent=generate_user_agent(os=['win','linux'],navigator='chrome')
session = requests.Session()
uuid_val = str(uuid.uuid1())
version="v8.9.6"
proxy_list=["9rxfdi:nt321h@mn.targetedproxies.com:50010","9hf298:fhy0mt@mn.targetedproxies.com:50008","xk77jd:jbkcpe@tmobile.targetedproxies.com:30046","z16rzg:hif8oo@mn.targetedproxies.com:50029","Cloudsupport.sw3:southw$123@154.198.32.83:8083",
"Cloudsupport.rcars1:Cars$123@154.198.32.83:8083",
"Cloudsupport.rcars2:Cars$123@154.198.32.83:8083",
"Cloudsupport.rcars3:Cars$123@154.198.32.83:8083",
"Cloudsupport.rcars4:Cars$123@154.198.32.83:8083",
"Cloudsupport.rcars5:Cars$123@154.198.32.83:8083",
"Cloudsupport.rcars6:Cars$123@154.198.32.83:8083",
"Cloudsupport.rcars7:Cars$123@154.198.32.83:8083",
"Cloudsupport.rcars8:Cars$123@154.198.32.83:8083",
"Cloudsupport.rcars9:Cars$123@154.198.32.83:8083",
"Cloudsupport.rcars10:Cars$123@154.198.32.83:8083"]
proxy=random.choice(proxy_list)
session.proxies={"https":f"http://{proxy}"}


PX11560 = int(random.uniform(6000,6999))
PX12248 = 3600
refer = "https://www.skyscanner.co.in/transport/flights/cok/goi/240820/?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false"
PX11902 = 0
PX12564 = None
PX12565 = -1
PX11379 = None
appid = "rf8vapwA"
PX12458 = "Linux x86_64" if "Linux" in useragent else "Win32"
os_type='"Linux"' if "Linux" in useragent else '"Windows"'
os_version=useragent.split('/')[3].split('.')[0]

def encrypt_payload(jsonstr, uuid_val):
    node_encode = f"""
    var Ev = function (t, e, n) {{
        for (var r = ie(encode(n), 10), o = [], a = -1, i = 0; i < t.length; i++) {{
            var l = Math.floor(i / r.length + 1), c = i >= r.length ? i % r.length : i, u = r.charCodeAt(c) * r.charCodeAt(l);
            u > a && (a = u);
        }}
        for (var f = 0; t.length > f; f++) {{
            var s = Math.floor(f / r.length) + 1, d = f % r.length, p = r.charCodeAt(d) * r.charCodeAt(s);
            for (p >= e && (p = wv(p, 0, a, 0, e - 1)); -1 !== o.indexOf(p);)
                p += 1;
            o.push(p);
        }}
        return o.sort(function (t, e) {{
            return t - e;
        }});
    }};
    var encode = function (t) {{
        return Buffer.from(t, "binary").toString("base64");
    }};
    var ie = function (t, e) {{
        for (var n = "", r = 0; r < t.length; r++)
            n += String.fromCharCode(e ^ t.charCodeAt(r));
        return n;
    }};
    var wv = function (t, e, n, r, o) {{
        return Math.floor(((t - e) / (n - e)) * (o - r) + r);
    }};
    var Fa = function (t, e, n) {{
        for (var r = "", o = 0, a = t.split(""), i = 0; i < t.length; i++)
            (r += e.substring(o, n[i] - i - 1) + a[i]), (o = n[i] - i - 1);
        return (r += e.substring(o));
    }};
    function obfuscatePayload(payload, uuid, sts) {{
        var sts = sts.length === 0 ? "1604064986000" : sts;
        var BasePayload = encode(ie(payload, 50));
        var fv = ie(encode(sts), 10);
        return Fa(fv, BasePayload, Ev(fv, BasePayload.length, uuid));
    }}
    var payload=`{jsonstr}`
    var uid ="{uuid_val}"
    console.log(obfuscatePayload(payload,uid,''))
    """

    cmd = ["node", "-e", node_encode]
    result = subprocess.run(cmd, capture_output=True, text=True)
    _payload = result.stdout.strip()
    return _payload


def timestamp1():
    return int(time.time() * 1000)


dec_payload = [
    {
        "t": "PX12095",
        "d": {
            "PX11645": refer,
            "PX12207": 0,
            "PX12458": PX12458,
            "PX11902": PX11902,
            "PX11560": PX11560,
            "PX12248": PX12248,
            "PX11385": timestamp1(),
            "PX12280": timestamp1(),
            "PX11496": uuid_val,
            "PX12564": PX12564,
            "PX12565": PX12565,
            "PX11379": PX11379,
        },
    }
]
print(dec_payload)

dec_payload = json.dumps(dec_payload, separators=(",", ":"), indent=None)
# print(dec_payload)
enc_payload = encrypt_payload(dec_payload, uuid_val)
def pc_gen(dec_payload,uid):
    pc_node=f"""
    const {{ v1: uuidv1, v4: uuidv4 }} = require('uuid');
    function It(t, n) {{
        var e = Ut(t, n);
        try {{
            for (var r = function (t) {{
                for (var n = "", e = "", r = 0; r < t.length; r++) {{
                    var a = t.charCodeAt(r);
                    a >= 48 && a <= 57 ? n += t[r] : e += a % 10
                }}
                return n + e
            }}(e), a = "", o = 0; o < r.length; o += 2)
                a += r[o];
            return a
        }} catch (t) {{ }}
    }}



    function Pt(t) {{
        var n, e = [];
        for (e[(t.length >> 2) - 1] = void 0,
            n = 0; n < e.length; n += 1)
            e[n] = 0;
        for (n = 0; n < 8 * t.length; n += 8)
            e[n >> 5] |= (255 & t.charCodeAt(n / 8)) << n % 32;
        return e
    }}
    function Ut(t, n, e) {{
        var r = function (t, n, e) {{
            if (!e)
                return Ht(Et(n, t));
            return Et(n, t)
        }}(t, n, e);
        return r
    }}
    function pt(t, n, e, r, a, o, i) {{
        return zt(e ^ (n | ~r), t, n, a, o, i)
    }}
    function bt(t, n) {{
        var e = (65535 & t) + (65535 & n);
        return (t >> 16) + (n >> 16) + (e >> 16) << 16 | 65535 & e
    }}
    function jt(t, n, e, r, a, o, i) {{
        return zt(n & e | ~n & r, t, n, a, o, i)
    }}
    function yt(t, n, e, r, a, o, i) {{
        return zt(n & r | e & ~r, t, n, a, o, i)
    }}
    function At(t, n, e, r, a, o, i) {{
        return zt(n ^ e ^ r, t, n, a, o, i)
    }}
    function zt(t, n, e, r, a, o) {{
        return bt((i = bt(bt(n, t), bt(r, o))) << (c = a) | i >>> 32 - c, e);
        var i, c
    }}
    function bt(t, n) {{
        var e = (65535 & t) + (65535 & n);
        return (t >> 16) + (n >> 16) + (e >> 16) << 16 | 65535 & e
    }}
    function dt(t, n) {{
        t[n >> 5] |= 128 << n % 32,
            t[14 + (n + 64 >>> 9 << 4)] = n;
        var e, r, a, o, i, c = 1732584193,
            u = -271733879,
            s = -1732584194,
            f = 271733878;
        for (e = 0; e < t.length; e += 16)
            r = c,
                a = u,
                o = s,
                i = f,
                c = jt(c, u, s, f, t[e], 7, -680876936),
                f = jt(f, c, u, s, t[e + 1], 12, -389564586),
                s = jt(s, f, c, u, t[e + 2], 17, 606105819),
                u = jt(u, s, f, c, t[e + 3], 22, -1044525330),
                c = jt(c, u, s, f, t[e + 4], 7, -176418897),
                f = jt(f, c, u, s, t[e + 5], 12, 1200080426),
                s = jt(s, f, c, u, t[e + 6], 17, -1473231341),
                u = jt(u, s, f, c, t[e + 7], 22, -45705983),
                c = jt(c, u, s, f, t[e + 8], 7, 1770035416),
                f = jt(f, c, u, s, t[e + 9], 12, -1958414417),
                s = jt(s, f, c, u, t[e + 10], 17, -42063),
                u = jt(u, s, f, c, t[e + 11], 22, -1990404162),
                c = jt(c, u, s, f, t[e + 12], 7, 1804603682),
                f = jt(f, c, u, s, t[e + 13], 12, -40341101),
                s = jt(s, f, c, u, t[e + 14], 17, -1502002290),
                c = yt(c, u = jt(u, s, f, c, t[e + 15], 22, 1236535329), s, f, t[e + 1], 5, -165796510),
                f = yt(f, c, u, s, t[e + 6], 9, -1069501632),
                s = yt(s, f, c, u, t[e + 11], 14, 643717713),
                u = yt(u, s, f, c, t[e], 20, -373897302),
                c = yt(c, u, s, f, t[e + 5], 5, -701558691),
                f = yt(f, c, u, s, t[e + 10], 9, 38016083),
                s = yt(s, f, c, u, t[e + 15], 14, -660478335),
                u = yt(u, s, f, c, t[e + 4], 20, -405537848),
                c = yt(c, u, s, f, t[e + 9], 5, 568446438),
                f = yt(f, c, u, s, t[e + 14], 9, -1019803690),
                s = yt(s, f, c, u, t[e + 3], 14, -187363961),
                u = yt(u, s, f, c, t[e + 8], 20, 1163531501),
                c = yt(c, u, s, f, t[e + 13], 5, -1444681467),
                f = yt(f, c, u, s, t[e + 2], 9, -51403784),
                s = yt(s, f, c, u, t[e + 7], 14, 1735328473),
                c = At(c, u = yt(u, s, f, c, t[e + 12], 20, -1926607734), s, f, t[e + 5], 4, -378558),
                f = At(f, c, u, s, t[e + 8], 11, -2022574463),
                s = At(s, f, c, u, t[e + 11], 16, 1839030562),
                u = At(u, s, f, c, t[e + 14], 23, -35309556),
                c = At(c, u, s, f, t[e + 1], 4, -1530992060),
                f = At(f, c, u, s, t[e + 4], 11, 1272893353),
                s = At(s, f, c, u, t[e + 7], 16, -155497632),
                u = At(u, s, f, c, t[e + 10], 23, -1094730640),
                c = At(c, u, s, f, t[e + 13], 4, 681279174),
                f = At(f, c, u, s, t[e], 11, -358537222),
                s = At(s, f, c, u, t[e + 3], 16, -722521979),
                u = At(u, s, f, c, t[e + 6], 23, 76029189),
                c = At(c, u, s, f, t[e + 9], 4, -640364487),
                f = At(f, c, u, s, t[e + 12], 11, -421815835),
                s = At(s, f, c, u, t[e + 15], 16, 530742520),
                c = pt(c, u = At(u, s, f, c, t[e + 2], 23, -995338651), s, f, t[e], 6, -198630844),
                f = pt(f, c, u, s, t[e + 7], 10, 1126891415),
                s = pt(s, f, c, u, t[e + 14], 15, -1416354905),
                u = pt(u, s, f, c, t[e + 5], 21, -57434055),
                c = pt(c, u, s, f, t[e + 12], 6, 1700485571),
                f = pt(f, c, u, s, t[e + 3], 10, -1894986606),
                s = pt(s, f, c, u, t[e + 10], 15, -1051523),
                u = pt(u, s, f, c, t[e + 1], 21, -2054922799),
                c = pt(c, u, s, f, t[e + 8], 6, 1873313359),
                f = pt(f, c, u, s, t[e + 15], 10, -30611744),
                s = pt(s, f, c, u, t[e + 6], 15, -1560198380),
                u = pt(u, s, f, c, t[e + 13], 21, 1309151649),
                c = pt(c, u, s, f, t[e + 4], 6, -145523070),
                f = pt(f, c, u, s, t[e + 11], 10, -1120210379),
                s = pt(s, f, c, u, t[e + 2], 15, 718787259),
                u = pt(u, s, f, c, t[e + 9], 21, -343485551),
                c = bt(c, r),
                u = bt(u, a),
                s = bt(s, o),
                f = bt(f, i);
        return [c, u, s, f]
    }}
    function mt(t) {{
        var n, e = "";
        for (n = 0; n < 32 * t.length; n += 8)
            e += String.fromCharCode(t[n >> 5] >>> n % 32 & 255);
        return e
    }}
    function gt(t) {{
        return unescape(encodeURIComponent(t))
    }}
    var ir = new Uint8Array(16);
    var or = function () {{
        return crypto.getRandomValues(ir), ir;
    }};
    var vr = or(), hr = [1 | vr[0], vr[1], vr[2], vr[3], vr[4], vr[5]], dr = 16383 & (vr[6] << 8 | vr[7]), pr = 0, mr = 0;
    function Et(t, n) {{
        return function (t, n) {{
            var e, r = Pt(t),
                a = [],
                o = [];
            for (a[15] = o[15] = void 0,
                r.length > 16 && (r = dt(r, 8 * t.length)),
                e = 0; e < 16; e += 1)
                a[e] = 909522486 ^ r[e],
                    o[e] = 1549556828 ^ r[e];
            var i = dt(a.concat(Pt(n)), 512 + 8 * n.length);
            return mt(dt(o.concat(i), 640))
        }}(gt(t), gt(n))
    }}
    function wt() {{
        return +new Date;
    }}
    function Wr(t, e, n, r) {{
        var o = "";
        var dr=16383;
        var mr=0,pr = 0;
        if (r) try {{
            for (var a = ((new Date).getTime() * Math.random() + "").replace(".", ".".charCodeAt()).split("").slice(-16), i = 0; i < a.length; i++) a[i] = parseInt(10 * Math.random()) * +a[i] || parseInt(Math.random() * ar);
            o = fr(a, 0);
        }} catch (t) {{ }}
        
        var c = e && n || 0, u = e || [], l = void 0 !== (t = t || {{}}).clockseq ? t.clockseq : dr, s = void 0 !== t.msecs ? t.msecs : wt(), f = void 0 !== t.nsecs ? t.nsecs : mr + 1, v = s - pr + (f - mr) / 1e4;
        if (v < 0 && void 0 === t.clockseq && (l = l + 1 & 16383), (v < 0 || s > pr) && void 0 === t.nsecs && (f = 0), f >= 1e4) throw new Error("uuid.v1(): Can't create more than 10M uuids/sec");
        pr = s, mr = f, dr = l;
        var h = (1e4 * (268435455 & (s += 122192928e5)) + f) % 4294967296;
        u[c++] = h >>> 24 & 255, u[c++] = h >>> 16 & 255, u[c++] = h >>> 8 & 255, u[c++] = 255 & h;
        var d = s / 4294967296 * 1e4 & 268435455;
        u[c++] = d >>> 8 & 255, u[c++] = 255 & d, u[c++] = d >>> 24 & 15 | 16, u[c++] = d >>> 16 & 255, u[c++] = l >>> 8 | 128, u[c++] = 255 & l;
        for (var p = t.node || hr, m = 0; m < 6; m++) u[c + m] = p[m];
        var W = e || fr(u);
        return o === W ? o : W;
    }}

    for (var ur = [], lr = {{}}, sr = 0; sr < 256; sr++) ur[sr] = (sr + 256).toString(16).substr(1), lr[ur[sr]] = sr;
    function fr(t, e) {{
        var n = e || 0, r = ur;
        return r[t[n++]] + r[t[n++]] + r[t[n++]] + r[t[n++]] + "-" + r[t[n++]] + r[t[n++]] + "-" + r[t[n++]] + r[t[n++]] + "-" + r[t[n++]] + r[t[n++]] + "-" + r[t[n++]] + r[t[n++]] + r[t[n++]] + r[t[n++]] + r[t[n++]] + r[t[n++]];
    }}
    function Ht(t) {{
        var n, e, r = "0123456789abcdef",
            a = "";
        for (e = 0; e < t.length; e += 1)
            n = t.charCodeAt(e),
                a += r.charAt(n >>> 4 & 15) + r.charAt(15 & n);
        return a
    }}

    //uid_val = uuidv1()
    uid_val='{uid}';
    var myval = `${{uid_val}}:{version}:330`;
    var dtval = '{dec_payload}';
    l = It(dtval, myval);
    console.log(l);
    """
    cmd = ["node", "-e", pc_node]
    result = subprocess.run(cmd, capture_output=True, text=True)
    _payload = result.stdout.strip()
    return _payload

pc_val=pc_gen(dec_payload,uuid_val)
print(pc_val)

headers = {
    'authority': 'www.skyscanner.co.in',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-GB,en;q=0.6',
    'sec-ch-ua': f'"Not_A Brand";v="8", "Chromium";v="{os_version}", "Brave";v="{os_version}"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': os_type,
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': useragent,
}

params = {
    'adultsv2': '1',
    'cabinclass': 'economy',
    'childrenv2': '',
    'ref': 'home',
    'rtn': '0',
    'preferdirects': 'false',
    'outboundaltsenabled': 'false',
    'inboundaltsenabled': 'false',
}

response = session.get('https://www.skyscanner.co.in/transport/flights/cok/goi/240820/', params=params, headers=headers)
print(response)
open("resolve.html","w").write(response.text)
pxhd = response.cookies["_pxhd"]
# enc_payload='sddsfffxdd@3333333333333333333333333333333333333'
data1={
    "payload": enc_payload,
    "appId": f"PX{appid}",
    "tag": version,
    "uuid": uuid_val,
    "ft": "330",
    "seq": "0",
    "en": "NTA",
    "pc": pc_val,
    "pxhd": pxhd,
    "rsc": "1",
}


response = session.post(
    f"https://www.skyscanner.co.in/{appid}/xhr/api/v2/collector",
    headers=headers,
    data=data1,
)
print(response)
print(response.text)
headers = {
    'authority': 'www.skyscanner.co.in',
    'accept': 'application/json',
    'accept-language': 'en-GB,en;q=0.6',
    'content-type': 'application/json',
    'origin': 'https://www.skyscanner.co.in',
    'referer': refer,
    'sec-ch-ua': f'"Not_A Brand";v="8", "Chromium";v="{os_version}", "Brave";v="{os_version}"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': os_type,
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': useragent,
    'x-skyscanner-ads-sponsored-view-type': 'ADS_SPONSORED_VIEW_DAY_VIEW',
    'x-skyscanner-channelid': 'website',
    'x-skyscanner-consent-adverts': 'true',
    'x-skyscanner-currency': 'INR',
    'x-skyscanner-locale': 'en-GB',
    'x-skyscanner-market': 'IN',
    'x-skyscanner-traveller-context': 'b2e5ec27-ce68-4174-a23e-e13c0f01f098',
    'x-skyscanner-trustedfunnelid': '65a57f3b-4a03-4f4b-8667-88f6cd9d1536',
    'x-skyscanner-viewid': '65a57f3b-4a03-4f4b-8667-88f6cd9d1536',
}

json_data = {
    'cabinClass': 'ECONOMY',
    'childAges': [],
    'adults': 1,
    'legs': [
        {
            'legOrigin': {
                '@type': 'entity',
                'entityId': '95673550',
            },
            'legDestination': {
                '@type': 'entity',
                'entityId': '95790306',
            },
            'dates': {
                '@type': 'date',
                'year': '2024',
                'month': '08',
                'day': '20',
            },
        },
    ],
}

response = session.post(
    'https://www.skyscanner.co.in/g/radar/api/v2/web-unified-search/',
    headers=headers,
    json=json_data,
)

print("final",response)
open("skyscanner.html","w").write(response.text)
