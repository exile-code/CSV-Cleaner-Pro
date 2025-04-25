#clean_csv_file

import csv

def clean_csv(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        reader.fieldnames = [h.strip() for h in reader.fieldnames] #sanitize column headers
        print("Detected CSV Columns:", reader.fieldnames)


        cleaned_rows = []

        for row in reader:
            try:
                name = row.get('Name', '').strip().title()
                email = row.get('Email', '').strip()
                raw_amount = row.get('Amount', '').replace('$','').replace(',','').strip()

                if not name or not raw_amount:
                    raise ValueError("Missing required fields")

                amount = float(raw_amount)

                cleaned_rows.append({
                    'Name': name,
                    'Email': email,
                    'Amount': amount
                })

            except Exception as e:
                print(f"⚠️ Skipping malformed row: {row} — Reason: {e}")
                
    #Sort by Amount Descending
    cleaned_rows.sort(key=lambda x: x['Amount'], reverse=True)

    #write cleaned CSV
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Email', 'Amount'])
        writer.writeheader()
        writer.writerows(cleaned_rows)

#Run the cleaner
clean_csv('sample_raw.csv', 'cleaned_data.csv')