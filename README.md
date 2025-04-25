# 🧼 CSV Cleaner Pro+

A simple yet powerful Python utility to clean messy CSV datasets.

This tool was built to handle real-world spreadsheet problems:  
- Blank names  
- Messy $-formatted amounts  
- Inconsistent casing  
- Totally malformed rows  
- And it exports clean, structured data.

---

## 📥 Input Sample (sample_raw.csv)

```csv
Name,Email,Amount
John Doe,johndoe@email.com,$1,200.50
,missingname@email.com,$500.00
Jane Smith,janesmith@email.com,$2,300.00
INVALID ROW
Mike,MIKE@email.com,$1,000
Rachel Green,rachel@email.com,$
Tom,,1000

🧠 Cleaning Rules

    Names are required and title-cased

    Amounts are parsed into float format ($, , removed)

    Skips malformed rows

    Email is optional, but cleaned

    Output is written to cleaned_data.csv

🧰 Tech Used

    Python 3.x

    csv module

    Basic string handling & logic

    BOM handling via utf-8-sig

📤 Output Sample

Name,Email,Amount
John Doe,johndoe@email.com,1200.50
Jane Smith,janesmith@email.com,2300.00
Mike,Mike@email.com,1000.00

✅ To Run:

python clean_csv.py