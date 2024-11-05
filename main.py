import requests

# API URL ve kimlik doğrulama bilgileriniz
url = "https://apitest.isyerimpos.com/v1/payRequest3d"
headers = {
    "Content-Type": "application/json",
    "MerchantId": "11039",
    "UserId": "445",
    "ApiKey": "AQAAAAEAACcQAAAAEBfEWS9XGrZta1wfYC1qeTCA2gJIbDH1+rQEdrY8k4qE8EFtWf3i0Axyb4jY2uReyw==",
}

# Model verileri
model = {
    "ReturnUrl": "https://isyeriasdresi.com/payresult",
    "OrderId": "ORDER_ID",
    "ClientIp": "123.123.123.123",
    "Installment": 1,
    "Amount": 10.00,
    "Is3D": True,
    "IsAutoCommit": True,  # 3DPAY için False gönderilmeli
    "ReflectCost": False,  # null, true, veya false olabilir
    "CardInfo": {
        "CardOwner": "KART SAHIBI",
        "CardNo": "1234123412341234",
        "Month": "01",
        "Year": "26",
        "Cvv": "123",
    },
    "CustomerInfo": {
        "Name": "MUSTERI ADI",
        "Phone": "5301230011",
        "Email": "test@test.com",
        "Address": "Adres Bilgisi",
        "Description": "İşlem Açıklaması",
    },
    "Products": [
        {
            "Name": "URUN ADI",
            "Count": 5,
            "UnitPrice": 2.00,
        }
    ],
    "Payments": [
        {
            "AccountOwner": "HESAP SAHIBI",
            "IBAN": "TR720006701000000078840200",
            "Description": "Islem Aciklamasi",
            "Amount": 9.00,
        }
    ],
}

response = requests.post(url, json=model, headers=headers)

if response.status_code == 200:
    try:
        data = response.json()
        content = data.get("Content")
        print("Message:", data.get("Message"))
        print("UID:", content.get("Uid"))
        print("Payment Link:", content.get("PaymentLink"))
        print("Response as HTML:", content.get("ResponseAsHtml"))
    except ValueError:
        print("Sunucudan geçersiz bir JSON yanıtı döndü:", response.text)
else:
    print("Hata oluştu:", response.status_code)
    print("Sunucunun döndürdüğü hata mesajı:", response.text)
