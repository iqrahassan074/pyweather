import streamlit as st
import requests
from datetime import datetime

API_KEY = "fcc8de7015bbb202209bbf0261babf4c"
API_URL = "https://api.openweathermap.org/data/2.5/weather"

translations = {
    "en": {
        "Weather App": "🌤️ pyWeather",
        "placeholder": "Enter city name",
        "language": "Language",
        "search": "Search",
        "temp": "Temperature",
        "condition": "Condition",
        "minmax": "Min / Max",
        "date": "Date",
        "notfound": "City not found. Please enter the name in English.",
        "weather": {
            "Clear": "Clear",
            "Clouds": "Clouds",
            "Rain": "Rain",
            "Snow": "Snow",
            "Sunny": "Sunny",
            "Haze": "Haze",
            "Smog": "Smog"
        },
        "days": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        "months": ["January", "February", "March", "April", "May", "June", "July", "August",
                   "September", "October", "November", "December"]
    },
    "ur": {
        "Weather App": "🌤️ موسم ایپ",
        "placeholder": "شہر کا نام درج کریں",
        "language": "زبان",
        "search": "تلاش کریں",
        "temp": "درجہ حرارت",
        "condition": "موسم",
        "minmax": "کم از کم / زیادہ سے زیادہ",
        "date": "تاریخ",
        "notfound": "شہر نہیں ملا۔ براہ کرم انگریزی میں نام درج کریں۔",
        "weather": {
            "Clear": "صاف",
            "Clouds": "بادل",
            "Rain": "بارش",
            "Snow": "برف",
            "Sunny": "دھوپ",
            "Haze": "دھند",
            "Smog": "دھواں"
        },
        "days": ["اتوار", "پیر", "منگل", "بدھ", "جمعرات", "جمعہ", "ہفتہ"],
        "months": ["جنوری", "فروری", "مارچ", "اپریل", "مئی", "جون", "جولائی", "اگست",
                   "ستمبر", "اکتوبر", "نومبر", "دسمبر"]
    },
    "hi": {
        "Weather App": "🌤️ मौसम ऐप",
        "placeholder": "शहर का नाम दर्ज करें",
        "language": "भाषा",
        "search": "खोजें",
        "temp": "तापमान",
        "condition": "मौसम",
        "minmax": "न्यूनतम / अधिकतम",
        "date": "तारीख",
        "notfound": "शहर नहीं मिला। कृपया अंग्रेज़ी में नाम दर्ज करें।",
        "weather": {
            "Clear": "साफ़",
            "Clouds": "बादल",
            "Rain": "बारिश",
            "Snow": "बर्फ़",
            "Sunny": "धूप",
            "Haze": "धुंध",
            "Smog": "धुआँ"
        },
        "days": ["रविवार", "सोमवार", "मंगलवार", "बुधवार", "गुरुवार", "शुक्रवार", "शनिवार"],
        "months": ["जनवरी", "फरवरी", "मार्च", "अप्रैल", "मई", "जून", "जुलाई", "अगस्त",
                   "सितंबर", "अक्टूबर", "नवंबर", "दिसंबर"]
    },
    "bn": {
        "Weather App": "🌤️ আবহাওয়া অ্যাপ",
        "placeholder": "শহরের নাম লিখুন",
        "language": "ভাষা",
        "search": "খুঁজুন",
        "temp": "তাপমাত্রা",
        "condition": "আবহাওয়া",
        "minmax": "নূন্যতম / সর্বোচ্চ",
        "date": "তারিখ",
        "notfound": "শহর পাওয়া যায়নি। ইংরেজিতে নাম লিখুন।",
        "weather": {
            "Clear": "স্বচ্ছ",
            "Clouds": "মেঘলা",
            "Rain": "বৃষ্টি",
            "Snow": "তুষার",
            "Sunny": "রৌদ্রোজ্জ্বল",
            "Haze": "কুয়াশা",
            "Smog": "ধোঁয়া"
        },
        "days": ["রবিবার", "সোমবার", "মঙ্গলবার", "বুধবার", "বৃহস্পতিবার", "শুক্রবার", "শনিবার"],
        "months": ["জানুয়ারি", "ফেব্রুয়ারি", "মার্চ", "এপ্রিল", "মে", "জুন", "জুলাই", "আগস্ট",
                   "সেপ্টেম্বর", "অক্টোবর", "নভেম্বর", "ডিসেম্বর"]
    },
    "ar": {
        "Weather App": "🌤️ تطبيق الطقس",
        "placeholder": "أدخل اسم المدينة",
        "language": "اللغة",
        "search": "بحث",
        "temp": "درجة الحرارة",
        "condition": "الطقس",
        "minmax": "الأدنى / الأعلى",
        "date": "التاريخ",
        "notfound": "المدينة غير موجودة. الرجاء إدخال الاسم باللغة الإنجليزية.",
        "weather": {
            "Clear": "صافي",
            "Clouds": "غائم",
            "Rain": "مطر",
            "Snow": "ثلج",
            "Sunny": "مشمس",
            "Haze": "ضباب",
            "Smog": "دخان"
        },
        "days": ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت"],
        "months": ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس",
                   "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"]
    },
    "tr": {
        "Weather App": "🌤️ Hava Durumu Uygulaması",
        "placeholder": "Şehir adı girin",
        "language": "Dil",
        "search": "Ara",
        "temp": "Sıcaklık",
        "condition": "Durum",
        "minmax": "Min / Maks",
        "date": "Tarih",
        "notfound": "Şehir bulunamadı. Lütfen ismi İngilizce girin.",
        "weather": {
            "Clear": "Açık",
            "Clouds": "Bulutlu",
            "Rain": "Yağmur",
            "Snow": "Kar",
            "Sunny": "Güneşli",
            "Haze": "Pus",
            "Smog": "Duman"
        },
        "days": ["Pazar", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi"],
        "months": ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos",
                   "Eylül", "Ekim", "Kasım", "Aralık"]
    }
}

st.set_page_config(page_title="Multilingual Weather App", layout="centered")

lang = st.selectbox("🌐 Language / زبان / भाषा", ["en", "ur", "hi", "bn", "ar", "tr"])
t = translations[lang]

st.title(t["Weather App"])
city = st.text_input(t["placeholder"])

if st.button(t["search"]):
    if city.strip() == "":
        st.warning("Please enter a city name.")
    else:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        res = requests.get(API_URL, params=params)
        data = res.json()

        if data.get("cod") != 200:
            st.error(t["notfound"])
        else:
            name = data["name"]
            country = data["sys"]["country"]
            temp = round(data["main"]["temp"])
            temp_min = round(data["main"]["temp_min"])
            temp_max = round(data["main"]["temp_max"])
            weather_condition = data["weather"][0]["main"]
            translated_condition = t["weather"].get(weather_condition, weather_condition)

            now = datetime.now()
            day = t["days"][now.weekday()]
            month = t["months"][now.month - 1]
            date_str = f"{day}, {now.day} {month} {now.year}"

            st.subheader(f"{name}, {country}")
            st.write(f"📅 **{t['date']}**: {date_str}")
            st.write(f"🌡️ **{t['temp']}**: {temp}°C")
            st.write(f"🌥 **{t['condition']}**: {translated_condition}")
            st.write(f"🔻 **{t['minmax']}**: {temp_min}°C / {temp_max}°C")

