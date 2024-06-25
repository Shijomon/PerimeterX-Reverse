import json,requests,re,base64,time
ses=requests.Session()
proxy='aiproxies:IPr0yalPr0xy_country-fr@geo.iproyal.com:12321'
proxies={'https':f"http://{proxy}"}
ses.proxies=proxies
time1=round(time.time()*1000)
unique={0: 85, 1: 19, 2: 48, 3: 77, 4: 11, 5: 40, 6: 69, 7: 3, 8: 32, 9: 61, 10: 90, 11: 24, 12: 53, 13: 82, 14: 16, 15: 45, 16: 74, 17: 8, 18: 37, 19: 66, 20: 0, 21: 29, 22: 58, 23: 87, 24: 21, 25: 50, 26: 79, 27: 13, 28: 42, 29: 71, 30: 5, 31: 34, 32: 63, 33: 92, 34: 26, 35: 55, 36: 84, 37: 18, 38: 47, 39: 76, 40: 10, 41: 39, 42: 68, 43: 2, 44: 31, 45: 60, 46: 89, 47: 23, 48: 52, 49: 81, 50: 15, 51: 44, 52: 73, 53: 7, 54: 36, 55: 65, 56: 94, 57: 28, 58: 57, 59: 86, 60: 20, 61: 49, 62: 78, 63: 12, 64: 41, 65: 70, 66: 4, 67: 33, 68: 62, 69: 91, 70: 25, 71: 54, 72: 83, 73: 17, 74: 46, 75: 75, 76: 9, 77: 38, 78: 67, 79: 1, 80: 30, 81: 59, 82: 88, 83: 22, 84: 51, 85: 80, 86: 14, 87: 43, 88: 72, 89: 6, 90: 35, 91: 64, 92: 93, 93: 27, 94: 56}
def char_conv(t, e):
    return ord(t[e])
def wed(t, e):
    a = "2GAM"
    t = a + t
    s = ""
    c = []
    u = unique
    f = len(t)
    h = len(e)
    p = i = 94

    for i in range(i, 0, -1):
        p = (p + u[(i)] + char_conv(t, i % f)) % 95
        n = u[(i)]
        u[(i)] = u[(p)]
        u[(p)] = n

    i = p = o = 0
    while o < h:
        if len(c) > 0:
            r = c.pop()
            o -= 1
        else:
            r = char_conv(e, o)
            if r < 32 or r > 125:
                if r > 2047:
                    c.append(126)
                    c.append(80 + (r >> 11))
                else:
                    c.append(126)
                c.append(48 + (r >> 6 & 31))
                c.append(48 + (63 & r))
                continue

        p = (p + u[((i + 1) % 95)]) % 95
        n = u[(i)]
        u[(i)] = u[(p)]
        u[(p)] = n
        r += u[(u[(i)] + u[(p)]) % 95]
        if r > 126:
            r -= 95
        s += chr(r)
        o += 1

    return a + s


message =[
    {
        "intgr": {
            "othr": {
                "wael": "function(t,o,r){var i=\"object\"===(void 0===r?\"undefined\":n(r))&&null!==r,p=i?r.capture:r;r=i?c(r):{},r.passive=s(r.passive,t),r.capture=void 0===p?u.capture:p,e.call(this,t,o,r)}",
                "dael": "function(t,o,r){var i=\"object\"===(void 0===r?\"undefined\":n(r))&&null!==r,p=i?r.capture:r;r=i?c(r):{},r.passive=s(r.passive,t),r.capture=void 0===p?u.capture:p,e.call(this,t,o,r)}",
                "bael": "function(t,o,r){var i=\"object\"===(void 0===r?\"undefined\":n(r))&&null!==r,p=i?r.capture:r;r=i?c(r):{},r.passive=s(r.passive,t),r.capture=void 0===p?u.capture:p,e.call(this,t,o,r)}"
            },
            "n": {},
            "n_pg": {},
            "nc": {},
            "w": {},
            "n_v": {},
            "nc_v": {}
        }
    },
    {
        "initdata": {
            "document_referrer": "",
            "status": "",
            "performance_memory": {
                "totalJSHeapSize": 84027705,
                "usedJSHeapSize": 80740825,
                "jsHeapSizeLimit": 2172649472
            },
            "screen": {
                "availWidth": 1368,
                "availHeight": 741,
                "width": 1368,
                "height": 768,
                "colorDepth": 24,
                "pixelDepth": 24,
                "availLeft": 0,
                "availTop": 27,
                "orientation": "object",
                "onchange": "object",
                "isExtended": False,
                "addEventListener": "function",
                "dispatchEvent": "function",
                "removeEventListener": "function"
            },
            "devicePixelRatio": 1,
            "styleMedia_type": "screen",
            "history_length": 3,
            "opener": "null",
            "navigator_userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "location_href": "https://www.autoeurope.fr/",
            "RemotePlayback": "function RemotePlayback() { [native code] }",
            "Permissions": "function Permissions() { [native code] }",
            "Notification": "function Notification() { [native code] }",
            "MediaSession": "function MediaSession() { [native code] }",
            "name": "",
            "defaultView": True,
            "console": {
                "debug": "function debug() { [native code] }",
                "error": "function error() { [native code] }",
                "info": "function info() { [native code] }",
                "log": "function log() { [native code] }",
                "warn": "function warn() { [native code] }",
                "dir": "function dir() { [native code] }",
                "dirxml": "function dirxml() { [native code] }",
                "table": "function table() { [native code] }",
                "trace": "function trace() { [native code] }",
                "group": "function group() { [native code] }",
                "groupCollapsed": "function groupCollapsed() { [native code] }",
                "groupEnd": "function groupEnd() { [native code] }",
                "clear": "function clear() { [native code] }",
                "count": "function count() { [native code] }",
                "countReset": "function countReset() { [native code] }",
                "assert": "function assert() { [native code] }",
                "profile": "function profile() { [native code] }",
                "profileEnd": "function profileEnd() { [native code] }",
                "time": "function time() { [native code] }",
                "timeLog": "function timeLog() { [native code] }",
                "timeEnd": "function timeEnd() { [native code] }",
                "timeStamp": "function timeStamp() { [native code] }",
                "context": "function context() { [native code] }",
                "createTask": "function createTask() { [native code] }",
                "memory": {
                    "totalJSHeapSize": 84027705,
                    "usedJSHeapSize": 80740825,
                    "jsHeapSizeLimit": 2172649472
                }
            },
            "localStorage": "object",
            "webkitNotifications": "undefined",
            "webkitAudioContext": "undefined",
            "chrome": [
                "loadTimes",
                "csi",
                "app"
            ],
            "navtype": 2,
            "navredirs": 0,
            "loadTimes": "function () { [native code] }",
            "vendor": "Google Inc.",
            "codename": "Mozilla",
            "navLanguages": [
                "en-GB"
            ],
            "navOnline": True,
            "navVibrate": "function vibrate() { [native code] }",
            "navWebdriver": False,
            "ServiceWorker": "function ServiceWorker() { [native code] }",
            "Cache": "function Cache() { [native code] }",
            "PaymentAddress": "function PaymentAddress() { [native code] }",
            "mediaDevices": {},
            "navHardwareConc": 4,
            "navDevMem": 8,
            "navLocks": "obj",
            "navLocksR": "function request() { [native code] }",
            "origin": "https://www.autoeurope.fr",
            "protocol": "https:",
            "hidden": False,
            "compatMode": "CSS1Compat",
            "visibilityState": "visible",
            "ddl_origin": "https://www.autoeurope.fr",
            "top_ref": "",
            "toingApply": "{}.toing.apply(",
            "fto": False,
            "fptsName": "toing",
            "rod": {
                "lw": 0,
                "hg": 4503599627370496
            },
            "end": "l",
            "plugins": [
                "internal-pdf-viewer"
            ],
            "plugext": {
                "0": {
                    "f": "internal-pdf-viewer",
                    "n": "PDF Viewer"
                },
                "1": {
                    "f": "internal-pdf-viewer",
                    "n": "Chrome PDF Viewer"
                },
                "2": {
                    "f": "internal-pdf-viewer",
                    "n": "Chromium PDF Viewer"
                },
                "3": {
                    "f": "internal-pdf-viewer",
                    "n": "Microsoft Edge PDF Viewer"
                },
                "4": {
                    "f": "internal-pdf-viewer",
                    "n": "WebKit built-in PDF"
                }
            },
            "plugins_len": 5,
            "iframe_depth": -1,
            "viewport": {
                "width": 1368,
                "height": 230
            },
            "screenXY": {
                "x": 0,
                "y": 27,
                "left": 0,
                "top": 27
            },
            "pageSize": {
                "scrollBarPosX": 0,
                "scrollBarPosY": 0,
                "pageHeight": 230,
                "pageWidth": 1368
            },
            "notifications": "w3c",
            "cryptoSubtle": "object",
            "platform": "Linux x86_64",
            "mobile_browser": False,
            "mtp": "undef",
            "bars": 63,
            "windowSize": {
                "outerHeight": 741,
                "innerHeight": 230,
                "outerWidth": 1368,
                "innerWidth": 1368
            },
            "connection": {
                "effectiveType": "4g",
                "rtt": 50,
                "downlink": 10,
                "saveData": False
            },
            "orientation": {
                "angle": 0,
                "type": "landscape-primary"
            },
            "smd": {
                "ok": True,
                "ex": False
            },
            "hat": {
                "wv": False
            },
            "first_run": True,
            "jsVersion": 1.5,
            "engine": "webkit",
            "ts": time1-2,
            "tz": 5.5,
            "tz2": "Asia/Calcutta"
        }
    },
    {
        "postct": {
            "mo": "2",
            "ci": "421275",
            "spa": "1",
            "dt": "4212751652380115911000",
            "pd": "acc",
            "si": "FRA",
            "time": time1
        }
    },
    {
        "initdata": {
            "location_href": "https://www.autoeurope.fr/",
            "document_referrer": "",
            "t": time1-73295
        }
    },
    {
        "oz": {
            "oz_st": time1-73549
        }
    },
    {
        "orion": {
            "run_ts": time1-6629
        }
    },
    {
        "SPA": {
            "attempt": "0",
            "firstSession": "AgGRqvELDPaI9weF",
            "eventType": "12"
        }
    }
]
message_decode = json.dumps(message)
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Pragma': 'no-cache',
    'Referer': 'https://www.autoeurope.fr/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

params = {
    'dt': '4212751652380115911000',
    'pd': 'acc',
    'mo': '2',
    'ci': '421275',
    'spa': '1',
}

response = ses.get('https://s.s.autoeurope.com/2/421275/clear.js', params=params, headers=headers)
print(response)
open("tabulate.html","w").write(response.text)
oz_tc=re.search('ozoki_tc = "(.*?)"',response.text).group(1)
oz_dt=re.search('ozoki_dt = "(.*?)"',response.text).group(1)
oz_sg = wed(oz_tc, message_decode)
oz_sg=base64.b64encode(oz_sg.encode()).decode()
print(oz_tc)
print(oz_dt)
print(oz_sg)

headers = {
    'authority': 'www.autoeurope.fr',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://www.autoeurope.fr',
    'pragma': 'no-cache',
    'referer': 'https://www.autoeurope.fr/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

data = {
    'viewSize': 'desk-wide',
    'display_label': 'Lisbon Airport',
    'display_labelr': 'null',
    'city': 'LISBON',
    'cityr': 'null',
    'puloclist': '1995,2015,14568,62009,683300,1416250,1636275,2011525,2245225,2246700,2250525,2252825,2259925,2492725,2506575,2769475,2830575,3608900,3882225,3887450,3994925,4288636,4404224,4416329,4423486,4426659,4426687,4429241,4434926,4483742,4487465,4488846,4497062,4497851,4499538,4501031,4501084,4501090,4510091,4510139,4514010,4514016,4515143,4515534',
    'doloclist': 'null',
    'pucode': 'PT',
    'docode': 'null',
    'puloctype': 'AIRPORT',
    'doloctype': 'null',
    'puCal': '2023-05-21',
    'doCal': '2023-05-24',
    'putime': '10:00',
    'dotime': '10:00',
    'puchaos_hub_id': '3862',
    'dochaos_hub_id': 'null',
    'searchAge': '40',
    'searchAgeCheckbox': 'true',
    'showFillAgeCheckout': 'true',
    'bookingstep': 'searchwait',
    'bookingUUID': '',
    'excl_ltr': 'false',
    'excl_cats': '',
    'pu': '[object Object]',
    'drop': 'false',
    'tgt': 'undefined',
    'oz_tc': oz_tc,
    'oz_sg': oz_sg,
    'oz_dt': oz_dt,
}

response = ses.post('https://www.autoeurope.fr/search/',  headers=headers, data=data)
print(response)
open("response1.html","w").write(response.text)
jsonpost=re.search('name="jsonPost" value="(.*?)"',response.text).group(1)

headers = {
    'authority': 'www.autoeurope.fr',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://www.autoeurope.fr',
    'pragma': 'no-cache',
    'referer': 'https://www.autoeurope.fr/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

data = {
    'bookingstep': 'getrates',
    'aff': 'AUTOEUROPE',
    'jsonPost': jsonpost,
    'lookupFromInterstitial': 'true',
    'success': 'true',
    'searchTypeFlag': 'm',
    'oz_tc': oz_tc,
    'oz_sg': oz_sg,
    'oz_dt': oz_dt,
    'tc_len': '16',
    'sg_len': '16788',
    'dt_len': '7500',
}

response = ses.post('https://www.autoeurope.fr/results/', headers=headers, data=data)
print(response)
open("final.html","w").write(response.text)



