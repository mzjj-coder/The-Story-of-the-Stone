import csv
import requests
requests.packages.urllib3.disable_warnings()
f=open('C:\\Users\\mzjj\\Desktop\\红楼梦弹幕\\8.csv','wt',newline='',encoding='utf-8-sig')
writer=csv.writer(f)
writer.writerow(["弹幕ID","用户名","弹幕内容","发布时间","点赞数"])
url="https://mfm.video.qq.com/danmu?otype=json&target_id=2195446109%26vid%3Dj00249qgend&timestamp=15&_=1638519233021"
#https://mfm.video.qq.com/danmu?otype=json&callback=jQuery19107157188185924201_1638441714392&target_id=2195446109%26vid%3Dj00249qgend&session_key=0%2C0%2C0&timestamp=15&_=1638441714393
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
for i in range(15,10000,30):
 data={"timestamp":i}
 response=requests.get(url,headers=headers,params=data)
 res=eval(response.text)
 con=res["comments"]
 if res["count"]!=0:
  for var in con:
   danmu=var["content"]#弹幕内容
   name=var["opername"]#用户名
   commentid=var["commentid"]#弹幕ID
   time=var["timepoint"]#发布时间
   upcount=var["upcount"]#点赞数
   nm=[name]
   dm=[danmu]
   id=[commentid]
   ti=[time]
   up=[upcount]
   writer.writerows(zip(id,nm,dm,ti,up))
#https://mfm.video.qq.com/danmu?otype=json&target_id=2195444531%26vid%3Ds0024dm0l1p&timestamp=15&_=1638518309608
f.close()