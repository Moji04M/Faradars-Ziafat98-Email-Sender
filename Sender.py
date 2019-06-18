'''
Faradars Ziafat98 Email Sender;
Github repository link: https://github.com/Moji04M/Faradars-Ziafat98-Email-Sender
'''

import requests
import re

email = "PUT_YOUR_EMAIL_ADDRESS_HERE"

links = [ # To remove a course, just comment it!
'https://faradars.org/courses/fvst9701/fvst9701-split-clustering-using-r', # آموزش خوشه بندی تفکیکی با نرم افزار R
'https://faradars.org/courses/fvadb96051/fvadb96051-adobe-lightroom', # آموزش Adobe Lightroom (ادوبی لایت روم) برای ویرایش و روتوش تصاویر
'https://faradars.org/courses/fvmec94052/fvmec94052-basic-finite-element-analysis-abaqus', # آموزش نرم افزار آنالیز اجزای محدود ABAQUS – مقدماتی
'https://faradars.org/courses/fvmng95101/fvmng95101-business-model-canvas', # آموزش بوم مدل کسب و کار
'https://faradars.org/courses/fvarch9511/fvarch9511-modeling-and-energy-analysis-using-revit', # آموزش مدل سازی و تحلیل انرژی با رویت (Revit)
'https://faradars.org/courses/fvst9501/fvst9501-quality-control-using-spss', # آموزش کنترل کیفیت آماری با SPSS
'https://faradars.org/courses/fvtyp9403/fvtyp9403-typing-with-10-fingers', # آموزش تایپ ده انگشتی
'https://faradars.org/courses/fvps94071/fvps94071-photoshop-for-printing-and-advertising', # آموزش فتوشاپ برای استفاده در صنعت چاپ و تبلیغات
'https://faradars.org/courses/fvacw96042/fvacw96042-principles-of-writing-scientific-article', # آموزش نگارش مقاله علمی – مبانی و اصول اولیه
'https://faradars.org/courses/fvcvl94121/fvcvl94121-structural-loading-using-excel', # آموزش بارگذاری سازه ها با اکسل
'https://faradars.org/courses/fvor95041/fvor95041-making-decision-in-economics-project', # آموزش تصمیم گیری در انتخاب پروژه های اقتصادی
'https://faradars.org/courses/fvst94082/fvst94082-statistical-quality-control', # آموزش کنترل کیفیت آماری
'https://faradars.org/courses/fvxl95051/fvxl95051-microsoft-office-excel', # آموزش اکسل (Microsoft Office Excel 2016)
'https://faradars.org/courses/fvae9507/fvae9507-basic-after-effects', # آموزش افترافکت (After Effects) – مقدماتی
'https://faradars.org/courses/fvill9408/fvill9408-adobe-illustrator', # آموزش نرم افزار طراحی گرافیکی Adobe Illustrator
'https://faradars.org/courses/fvcvl94062/fvcvl94062-etabs', # آموزش نرم افزار ETABS
'https://faradars.org/courses/fvlnx9510/fvlnx9510-basic-linux-operating-system', # آموزش سیستم عامل لینوکس (Linux) – مقدماتی
'https://faradars.org/courses/fvor101/fvor101-planning-and-production-control-and-inventories', # آموزش برنامه ریزی و کنترل تولید و موجودی ها
'https://faradars.org/courses/fvpht9407/fvpht9407-basic-python-programming/', # آموزش برنامه نویسی پایتون – مقدماتی
'https://faradars.org/courses/fvps9402/fvps9402-basic-photoshop', # آموزش فتوشاپ (Photoshop) – مقدماتی
'https://faradars.org/courses/fvh4c94062/fvh4c94062-basic-of-web-design-using-html', # آموزش طراحی وب با HTML – مقدماتی
'https://faradars.org/courses/fvand9406/fvand9406-basic-android-programming', # آموزش برنامه نویسی اندروید (Android) – مقدماتی
'https://faradars.org/courses/fvwp9705/fvwp9705-basic-of-wordpress', # آموزش وردپرس (WordPress) – مقدماتی
'https://faradars.org/courses/fvacw96031/fvacw96031-principles-of-study-and-speed-reading-skills', # آموزش اصول مطالعه – مهارت‌ های تند خوانی و دقیق خوانی
'https://faradars.org/courses/fvjs94062/fvjs94062-javascript-programming', # آموزش جاوا اسکریپت (JavaScript)
'https://faradars.org/courses/fvmec93031/fvmec93031-solidworks', # مجموعه آموزش های نرم افزار سالیدورکز (SOLIDWORKS)
'https://faradars.org/courses/fvst9405/fvst9405-introduction-probability-and-statistics', # آموزش آمار و احتمال مهندسی
'https://faradars.org/courses/fvcrl9310/fvcrl9310-coreldraw', # مجموعه آموزش های کاربردی طراحی و گرافیک با نرم افزار کورل (CorelDRAW)
'https://faradars.org/courses/fvmec94053/fvmec94053-engineering-mechanics-statics', # آموزش استاتیک
'https://faradars.org/courses/fvml9505/fvml9505-machine-learning', # آموزش یادگیری ماشین
'https://faradars.org/courses/fvor9408/fvor9408-planning-and-project-management-using-primavera', # آموزش نرم افزار برنامه ریزی و کنترل پروژه Primavera
'https://faradars.org/courses/fvee103/fvee103-electronics-i', # آموزش الکترونیک ۱
'https://faradars.org/courses/fvor94092/fvor94092-business-intelligence-bi-using-excel', # آموزش پیاده سازی هوش تجاری در اکسل
'https://faradars.org/courses/fvcvl103/fvcvl103-mechanics-materials', # آموزش مقاومت مصالح
'https://faradars.org/courses/fvee9511/fvee9511-photovoltaic-power-plant-design-using-pvsyst', # آموزش طراحی نیروگاه فتوولتائیک با نرم افزار PVsyst (پی وی سیست)
'https://faradars.org/courses/fvacw9403/fvacw9403-scientific-presentation', # آموزش شیوه ارائه علمی
'https://faradars.org/courses/fvor102/fvor102-fundamentals-of-project-management-using-pmbok', # آموزش مبانی مدیریت پروژه با رویکرد PMBOK
'https://faradars.org/courses/mvrmo9012/mvrmo9012-multiobjective-optimization-video-tutorials-pack', # مجموعه آموزش های بهینه سازی چند هدفه در متلب
'https://faradars.org/courses/fvev9403/fvev9403-principals-and-techniques-of-econometrics-by-eviews', # آموزش مبانی و روش های اقتصاد سنجی با  Eviews
'https://faradars.org/courses/fvlv9403/fvlv9403-introduction-to-labview', # آموزش نرم افزار صنعتی کنترل و مانیتورینگ LabVIEW
'https://faradars.org/courses/fvtimng9701/fvtimng9701-time-management-to-personal-and-professional-productivity', # آموزش مدیریت زمان جهت بهره وری شخصی و حرفه ای
'https://faradars.org/courses/fvtel9504/fvtel9504-computer-network-security', # آموزش امنیت شبکه های کامپیوتری
'https://faradars.org/courses/fvee9512/fvee9512-basic-internet-of-things-iot', # آموزش اینترنت اشیا (Internet of things) – مقدماتی
'https://faradars.org/courses/fvch102/fvch102-general-chemistry', # آموزش شیمی عمومی
'https://faradars.org/courses/fvcvl9405/fvcvl9405-application-matlab-dynamics-structures', # آموزش کاربرد متلب در دینامیک سازه ها
'https://faradars.org/courses/fvlaw9607/fvlaw9607-basic-drafting-international-trade-contracts', # آموزش نگارش قراردادهای تجاری بین المللی – مقدماتی
'https://faradars.org/courses/fvmng9410/fvmng9410-positive-leadership', # آموزش رهبری مثبت گرا
'https://faradars.org/courses/fvacw95101/fvacw95101-scientific-journals-indexed-in-scopus' # آموزش نمایه سازی نشریه های علمی در Scopus
]

url = 'https://faradars.org/ev/ziafat98/email/'

s = requests.Session()
all_ = len(links)
counter = 0

for link in links:
    counter += 1
    print(f'Proccesing {link}... {counter} of {all_}.')
    code = re.findall('https://faradars.org/courses/(.+)/.+', link)[0].upper()
    payload = {'nazri-course-sku': code, 'email': email}
    r = s.post(url, payload, allow_redirects=False)
    if r.status_code == 302 and r.headers['Location'] == 'https://faradars.org/ev/ziafat98/index.php/?sent=1':
        print('OK, sended! :)')
    else:
        print(f'''Failed! :(\nStatus code: {r.status_code}''')
        break
    s.cookies.clear()
    print('====================')

print('\n=== Completed!')
sleep(4)
