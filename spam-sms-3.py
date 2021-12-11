import json,os,sys
import requsts as rek

banner="""
[×] pembuat : risky. 
[×] spam sms-3.    
[×] awali : 08xxxxx. 
[×] kalau error hbgi wa 089681551536
"""
os.system("clear")
target = input(" Nomor :  ")
jl = input(" Jumlah :  ")
print(banner)


headers = {
"Host":"registrasi.tri.co.id",
"Connection":"keep-alive",
"Content-Length":"26",
"Accept":"application/json, text/javascript, */*; q=0.01",
"Origin":"https://registrasi.tri.co.id",
"X-Requested-With":"XMLHttpRequest",
"Save-Data":"on"
"User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Prime Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"Referer":"https://registrasi.tri.co.id/",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
}

api_url = "https://registrasi.tri.co.id/daftar/regenerateOTP/token&msisdn=0"+target

respon = rek.post(api_url,headers).text

status = json.loads(respon)
for i in str(jl):
        print ("SMS BERHASIL")
else:
        print ("SMS GAGAL")


