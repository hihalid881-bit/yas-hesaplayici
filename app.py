from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def ana_sayfa():
    sonuc = None
    hata = None
    
    if request.method == 'POST':
        try:
            d_tarih_str = request.form.get('dogum_tarihi')
            h_tarih_str = request.form.get('hedef_tarih')
            
            dogum_tarihi = datetime.strptime(d_tarih_str, '%Y-%m-%d')
            hedef_tarih = datetime.strptime(h_tarih_str, '%Y-%m-%d')
            
            if hedef_tarih < dogum_tarihi:
                hata = "Hesaplanacak tarih, doğum tarihinden önce olamaz!"
            else:
                yil = hedef_tarih.year - dogum_tarihi.year
                ay = hedef_tarih.month - dogum_tarihi.month
                gun = hedef_tarih.day - dogum_tarihi.day
                
                if gun < 0:
                    ay -= 1
                    gun += 30
                if ay < 0:
                    yil -= 1
                    ay += 12
                    
                sonuc = f"O tarihte tam olarak: {yil} yaş, {ay} ay, {gun} günlük olacaksınız!"
        except Exception as e:
            hata = "Tarih işlenirken bir hata oluştu."
            
    return render_template('index.html', sonuc=sonuc, hata=hata)

app.run(debug=True)