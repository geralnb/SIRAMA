import requests


semester_dipilih = 2

url = "https://service-v2.telkomuniversity.ac.id/read/api/read/d6c09f330d8af5c7d63f64d2c251498fbdfed81d/13/4" #UBAH /13/x MENJADI TINGKAT

headers = {
    "Host": "service-v2.telkomuniversity.ac.id",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Authorization": "Bearer eyJXXXXXXXXX",
    "Origin": "https://sirama.telkomuniversity.ac.id",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Referer": "https://sirama.telkomuniversity.ac.id/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    # Pastikan data berbentuk list sebelum difilter
    if isinstance(data, list):
        # Filter data berdasarkan semester yang dipilih
        semester_data = [item for item in data if item.get("semester") == semester_dipilih]

        if semester_data:
            print(f"Data untuk semester {semester_dipilih}:")
            for item in semester_data:
                print(f"{item['subject_name']}, SKS: {item['credit']}, Kelas: {item['class']}")
        else:
            print(f"Tidak ada data untuk semester {semester_dipilih}.")
    else:
        print("Format data tidak sesuai, bukan list.")
else:
    print(f"Error: {response.status_code}")
