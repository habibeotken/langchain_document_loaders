# LangChain Document Loaders (Gradio + Gemini)

Bu proje, bir TXT belgesini yükleyip doğal dilde soru sorabileceğiniz basit bir arayüz sunar. Belgeler LangChain ile parçalanır, FAISS üzerinde vektörleştirilir ve cevaplar Gemini 2.5 Flash modeli tarafından üretilir.

## Özellikler
- TXT belge yükleme
- Belge içeriğine göre soru-cevap
- Gradio arayüzü

## Gereksinimler
- Python 3.10+
- Google Gemini API anahtarı

## Kurulum

1) Depoyu klonlayın ve klasöre girin.

2) Sanal ortam oluşturup etkinleştirin (önerilir):
- Windows (PowerShell):
  - `python -m venv .venv`
  - `.venv\Scripts\Activate.ps1`

3) Bağımlılıkları kurun:
- `pip install gradio python-dotenv langchain langchain-community langchain-google-genai faiss-cpu`

4) Ortam değişkenlerini ayarlayın:
- [env.example](env.example) dosyasını `.env` olarak kopyalayın ve `GEMINI_API_KEY` değerini girin.

## Çalıştırma
- `python app.py`

Uygulama çalışınca tarayıcınızda Gradio arayüzü açılır.

## Kullanım
1) TXT dosyanızı yükleyin.
2) Sorunuzu yazın.
3) Cevabı görüntüleyin.

## Notlar
- Yalnızca `.txt` dosyaları desteklenir.
- Daha büyük belgeler için bellek kullanımı artabilir.

## Lisans
Bu proje için lisans belirtilmemiştir.
