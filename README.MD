# 🔗 مبدل لینک گوگل درایو به فرمت خاص

این یک ابزار دسکتاپ ساده با رابط کاربری گرافیکی (GUI) است که برای تبدیل لینک‌های اشتراک‌گذاری گوگل درایو به یک فرمت لینک خاص `googleusercontent.com` (احتمالاً مرتبط با تصاویر پروفایل یا محتوای کاربری خاص) طراحی شده است. برنامه به زبان فارسی می‌باشد.

## 📝 توضیحات

این برنامه با استفاده از پایتون و کتابخانه‌های `tkinter` (برای رابط کاربری) و `pyperclip` (برای کار با کلیپ‌بورد) ساخته شده است. کاربر یک لینک گوگل درایو را در برنامه وارد می‌کند، برنامه شناسه فایل (File ID) را از لینک ورودی استخراج کرده و سپس یک لینک جدید با فرمت زیر تولید می‌کند:
`https://lh3.googleusercontent.com/d/{FILE_ID}`

لینک تبدیل‌شده به صورت خودکار در کلیپ‌بورد کاربر کپی شده و همچنین در فیلد خروجی نمایش داده می‌شود.

---
**⚠️ نکته بسیار مهم**
---
فرمت لینک تولید شده (`https://lh3.googleusercontent.com/d/{FILE_ID}`) به نظر می‌رسد برای دسترسی به **تصاویر پروفایل گوگل** یا نوع خاصی از محتوای کاربری گوگل در نظر گرفته شده باشد. این فرمت، فرمت استاندارد برای ایجاد **لینک دانلود مستقیم** برای فایل‌های عمومی ذخیره شده در گوگل درایو (مانند اسناد، PDF، ویدئوها و غیره) **نیست**.

* اگر هدف شما ایجاد لینک دانلود مستقیم برای فایل‌های معمولی گوگل درایو است، معمولاً از فرمتی مانند `https://drive.google.com/uc?export=download&id=FILE_ID` استفاده می‌شود.
* کارایی لینک تولید شده توسط این ابزار برای فایل‌های معمولی گوگل درایو تضمین شده نیست و ممکن است به نتیجه مورد انتظار منجر نشود.
---

## ✨ ویژگی‌ها

* رابط کاربری گرافیکی ساده و روان به زبان فارسی 🇮🇷
* استخراج هوشمند شناسه فایل (File ID) از انواع لینک‌های گوگل درایو 🔍
* تبدیل لینک به فرمت `https://lh3.googleusercontent.com/d/{FILE_ID}` ⚙️
* کپی خودکار لینک نهایی در کلیپ‌بورد برای استفاده آسان 📋
* نمایش پیام‌های راهنما و وضعیت (موفقیت یا خطا) به کاربر 📢
* امکان چسباندن (Paste) محتوای کلیپ‌بورد در فیلد ورودی با `Ctrl+V` (یا `Cmd+V` در مک) و همچنین از طریق منوی راست کلیک 🖱️
* طراحی با ابعاد ثابت و غیرقابل تغییر اندازه برای جلوگیری از به‌هم‌ریختگی ظاهری

## 🎯 کاربردهای این ابزار

با در نظر گرفتن عملکرد واقعی و فرمت لینک خروجی:

1.  **استخراج شناسه فایل گوگل درایو:** این ابزار به سرعت و با دقت شناسه فایل را از لینک‌های گوگل درایو استخراج می‌کند.
2.  **تولید لینک خاص `googleusercontent.com`:** اگر نیاز به تولید لینکی با فرمت دقیق `https://lh3.googleusercontent.com/d/{FILE_ID}` دارید (مثلاً برای تست یا کاربردهای بسیار خاص مرتبط با این نوع URL)، این ابزار این کار را انجام می‌دهد.
3.  **ابزار آموزشی:** می‌تواند به عنوان یک مثال ساده از ساخت برنامه دسکتاپ با `tkinter` در پایتون، کار با عبارات منظم (Regex) برای استخراج اطلاعات از رشته‌ها، و همچنین ادغام با کلیپ‌بورد سیستم‌عامل مورد بررسی قرار گیرد.

## 🚀 نحوه اجرا

1.  مطمئن شوید که پایتون (ترجیحاً نسخه ۳) بر روی سیستم شما نصب شده است.
2.  کتابخانه `pyperclip` را نصب کنید. `tkinter` معمولاً به صورت پیش‌فرض همراه با پایتون نصب می‌شود. دستور نصب `pyperclip`:
    ```bash
    pip install pyperclip
    ```
3.  فایل اسکریپت `google-drive-direct-link.py` را دانلود کنید.
4.  اسکریپت را اجرا کنید:
    ```bash
    python google-drive-direct-link.py
    ```
5.  پس از باز شدن پنجره برنامه، لینک گوگل درایو مورد نظر خود را در کادر ورودی ("لینک را وارد کنید") قرار دهید.
6.  روی دکمه "تبدیل کن" کلیک کنید.
7.  لینک تبدیل‌شده در کادر خروجی ("لینک تبدیل شده") نمایش داده شده و همزمان در کلیپ‌بورد شما کپی می‌شود.

## 🧑‍💻 توسعه و اطلاعات بیشتر

این اسکریپت به عنوان یک ابزار کمکی برای تبدیل فرمت لینک‌های گوگل درایو به یک ساختار خاص ارائه شده است.

برای مشاهده سایر پروژه‌ها و اطلاعات بیشتر، می‌توانید از وب‌سایت زیر که توسط **Nambebnar** مدیریت می‌شود، دیدن فرمایید:

[https://intellsoft.ir](https://intellsoft.ir)

---
---
---

# 🔗 Google Drive Link Converter (to a Specific Format)

This is a simple desktop tool with a Graphical User Interface (GUI) designed to convert Google Drive sharing links into a specific `googleusercontent.com` link format (possibly related to profile pictures or specific user content). The application's UI is in Persian.

## 📝 Description

This program is built using Python with the `tkinter` library (for the UI) and `pyperclip` (for clipboard operations). The user inputs a Google Drive link, the program extracts the File ID from it, and then generates a new link in the following format:
`https://lh3.googleusercontent.com/d/{FILE_ID}`

The converted link is automatically copied to the user's clipboard and also displayed in the output field.

---
**⚠️ Very Important Note**
---
The generated link format (`https://lh3.googleusercontent.com/d/{FILE_ID}`) appears to be intended for accessing **Google profile pictures** or a specific type of Google user content. This format is **not** the standard way to create **direct download links** for general files stored in Google Drive (such as documents, PDFs, videos, etc.).

* If your goal is to create direct download links for regular Google Drive files, a format like `https://drive.google.com/uc?export=download&id=FILE_ID` is typically used.
* The functionality of the link generated by this tool for regular Google Drive files is not guaranteed and may not lead to the expected outcome.
---

## ✨ Features

* Simple and smooth GUI in Persian 🇮🇷
* Smart extraction of File ID from various Google Drive link formats 🔍
* Converts link to the `https://lh3.googleusercontent.com/d/{FILE_ID}` format ⚙️
* Automatic copying of the final link to the clipboard for easy use 📋
* Displays guidance and status messages (success or error) to the user 📢
* Ability to paste clipboard content into the input field using `Ctrl+V` (or `Cmd+V` on Mac) and also via a right-click context menu 🖱️
* Fixed size design to prevent layout issues

## 🎯 Use Cases for This Tool

Considering the actual functionality and the output link format:

1.  **Extracting Google Drive File ID:** The tool quickly and accurately extracts the file ID from Google Drive links.
2.  **Generating specific `googleusercontent.com` links:** If you need to generate a link with the exact format `https://lh3.googleusercontent.com/d/{FILE_ID}` (e.g., for testing or very specific use cases related to this URL type), this tool will do that.
3.  **Educational Tool:** Can be studied as a simple example of building a desktop application with `tkinter` in Python, working with regular expressions (Regex) for extracting information from strings, and integrating with the OS clipboard.

## 🚀 How to Run

1.  Ensure Python (preferably version 3) is installed on your system.
2.  Install the `pyperclip` library. `tkinter` is usually installed by default with Python. Command to install `pyperclip`:
    ```bash
    pip install pyperclip
    ```
3.  Download the `google-drive-direct-link.py` script file.
4.  Run the script:
    ```bash
    python google-drive-direct-link.py
    ```
5.  After the program window opens, paste your desired Google Drive link into the input box ("لینک را وارد کنید" - "Enter the link").
6.  Click the "تبدیل کن" (Convert) button.
7.  The converted link will be displayed in the output box ("لینک تبدیل شده" - "Converted link") and simultaneously copied to your clipboard.

## 🧑‍💻 Development and More Info

This script is provided as a helper tool to convert Google Drive link formats to a specific structure.

For other projects and more information, you can visit the following website managed by **Nambebnar**:

[نرم افزار های تخصصی دوربین مداربسته](https://intellsoft.ir)