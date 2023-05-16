import numpy as np, pandas as pd,os,time
from tabulate import tabulate

penyakit = [["P01","Abortus/Keguguran/B.O"],
           ["P02","Adenomiosis"],
           ["P03","Bartholinitis"],
           ["P04","Gangguan Haid"],
           ["P05","Hyperemesis Gravidarum"],
           ["P06","Infeksi Vagina/NVL"],
           ["P07","Kehamilan Ektopik/CB"],
           ["P08","Kista Cokelat"],
           ["P09","Kista Ovarium"],
           ["P010","Mioma Uteri"]]

gejala = {
    "G001":"Keluar flek",
    "G002":"Keluar darah",
    "G003":"Keluar darah yang berkepanjangan",
    "G004":"Mual dan muntah berlebihan",
    "G005":"Nyeri pada ari-ari",
    "G006":"Pusing yang berkepanjangan",
    "G007":"Nyeri saat buang air kecil",
    "G008":"Pendarahan pervaginam",
    "G009":"Perubahan gejala kehamilan secara drastis",
    "G010":"Rasa nyeri dan sakit pada panggul dan perut",
    "G011":"Disminore(rasa nyeri selama haid)",
    "G012":"Haid tidak teratur",
    "G013":"Keputihan dan bau",
    "G014":"Nyeri perut",
    "G015":"Bengkak di pangkal paha",
    "G016":"Benjolan atau pembengkakan di vagina",
    "G017":"Rasa nyeri dan sakit pada panggul",
    "G018":"Sakit dan nyeri di bagian intens saat aktivitas",
    "G019":"Kram perut sebelum atau selama haid",
    "G020":"Mengalami susah tidur",
    "G021":"Nyeri pada punggung",
    "G022":"Perut terasa penuh dan kembung",
    "G023":"Pusing dan sakit kepala",
    "G024":"Tubuh mudah kelelahan",
    "G025":"Pendarahan dalam jumlah banyak",
    "G026":"Hilang selera makan",
    "G027":"Menggigil",
    "G028":"Nyeri ulu hati",
    "G029":"Tidak haid kurang lebih 2 bulan",
    "G030":"Dehidrasi",
    "G031":"Hipotensi atau tekanan darah rendah",
    "G032":"Jantung berdebar",
    "G033":"Mengeluarkan air liur secara berlebihan",
    "G034":"Merasa stres, bingung, cemas",
    "G035":"Sangat sensitif terhadap aroma",
    "G036":"Keluar cairan",
    "G037":"Nyeri pada perut bagian bawah",
    "G038":"Gatal-gatal di bagian alat kelamin luar",
    "G039":"Keputihan,peradangan,dan kemerahan pada genitalia eksterna",
    "G040":"Nyeri pada bagian intens",
    "G041":"Nyeri saat berhubungan intim",
    "G042":"Keluar air di bekas operasi",
    "G043":"Nyeri sebelah kiri",
    "G044":"Sakit pinggang berkepanjangan",
    "G045":"Tidak haid dan tes kehamilan positif",
    "G046":"Haid tidak berhenti",
    "G047":"Nyeri pada pinggul",
    "G048":"Nyeri setelah berhubungan intim",
    "G049":"Demam",
    "G050":"Gatal-gatal di bagian perut dan kaki",
    "G051":"Mual dan muntah biasa",
    "G052":"Nyeri perut secara tiba-tiba",
    "G053":"Dada terasa teregang",
    "G054":"Masalah buang air besar dan kecil",
    "G055":"Nyeri pada pinggung,punggung dan paha",
    "G056":"Haid banyak",
    "G057":"Keluar darah dibagian intens",
    "G058":"Nyeri haid",
    "G059":"Nyeri saat terjadi penekanan pada pinggul",
    "G060":"Nyeri panggul setelah berhubungan intim",
    "G061":"Terasa tertekan pada bagian bawah usus besar",
    }
            
gejala_pasien = []
            
def pertanyaan():
    panjang = -1
    kode =[x for x in gejala.keys()]
    for key,value in gejala.items():
        clear()
        tanya = "Apakah "+value
        print(f""" {'='*78}
|{'Jawablah pertanyaan berikut ini':>51} [{key}] {'|':>20}
|{'='*78}|
|{'|':>79}
|{'|':>79}
|{tanya:^78}|
|{'|':>79}
|{'1.Iya':>30}{'2.Tidak':>25}{'|':>24}
|{'|':>79}
|{'3.Hentikan Diagnosa':^78}|
|{'|':>79}
|{'|':>79}
 {'='*78}""")
        panjang +=1
        pilih = input(" Pilih[1/2/3]: ")
        match pilih:
            case"1":
                gejala_pasien.append(kode[panjang])
            case"3":
                break

    menu()
   

def clear():
    sistem_operasi = os.name
    match sistem_operasi:
        case"posix":
            os.system("clear")
        case"nt":
            os.system("cls")


def menu():
    clear()
    print(f""" {'='*78}
| {'Menu':^77}|
|{'='*78}|
|{'|':>79}
|{'|':>79}
| Silahkan pilih menu di bawah:{'|':>49} 
| 1. Diagnosa ulang{'|':>61}
| 2. Gejala yang dialami{'|':>56}
| 3. Hasil diagnosa{'|':>61}
| 4. Keluar{'|':>69}
|{'|':>79}
|{'|':>79}
 {'='*78}""")
    try:
        choice = int(input(" Masukkan pilihan: "))
        if choice == 1:
            gejala_pasien.clear()
            pertanyaan()
        elif choice == 2:
            gejala_yang_dialami()
        elif choice == 3:
            vonis = diagnosa(gejala_pasien)
            hasil_diagnose = "".join(vonis)
            if hasil_diagnose == " Anda tidak memasukkan gejala apapun":
                print(" Anda tidak memasukkan gejala apapun")
            else:
                print(f" Anda Divonis: {hasil_diagnose}")
            exit()
        elif choice == 4:
            exit()
    except ValueError:
        print(" Tidak boleh menggunakan angka!")
        time.sleep(1.5)
        menu()


def gejala_yang_dialami():
    clear()
    gejala_pasien_copy = gejala_pasien.copy()
    if not gejala_pasien:
        print(" Silahkan masukkan gejala terlebih dahulu !")
        input(" Tekan enter untuk kembali ke menu")
        menu()
    else:
        gejala_pasien_copy.sort()
        gejala_yang_dialami= list(filter(lambda item: item[0] in gejala_pasien, gejala.items()))
        dataframes = pd.DataFrame(gejala_yang_dialami)
        diseases_table = tabulate(dataframes,headers=["Kode Gejala","Nama Gejala"],
                                 tablefmt="fancy_grid",numalign="left")
        print(diseases_table)

        input(" Tekan enter untuk kembali ke menu")
        menu()
    

def diagnosa(gejala_yang_dialami):
    if not gejala_yang_dialami:
        return" Anda tidak memasukkan gejala apapun"
    else:
        try:
            if gejala_yang_dialami [0] == "G001" and gejala_yang_dialami[1] == "G002" and gejala_yang_dialami[2] == "G003" and gejala_yang_dialami[3] == "G004" and gejala_yang_dialami[4] == "G005" and gejala_yang_dialami[5] == "G006" and gejala_yang_dialami[6] == "G007" and gejala_yang_dialami[7] == "G008"and gejala_yang_dialami[8] == "G009"and gejala_yang_dialami[9] == "G010":
                return penyakit[0][1]
            elif gejala_yang_dialami[0] == "G011" and gejala_yang_dialami [1] == "G012" and gejala_yang_dialami[2] == "G013" and gejala_yang_dialami[3] == "G014":
                return penyakit[1][1]
            elif gejala_yang_dialami[0] == "G015" and gejala_yang_dialami [1] == "G016" and gejala_yang_dialami[2] == "G017" and gejala_yang_dialami[3] == "G018":
                return penyakit[2][1]
            elif gejala_yang_dialami[0] == "G019" and gejala_yang_dialami [1] == "G020" and gejala_yang_dialami[2] == "G021" and gejala_yang_dialami[3] == "G022"and gejala_yang_dialami[4] == "G023"and gejala_yang_dialami[5] == "G024" and gejala_yang_dialami[6] == "G025":
                return penyakit[3][1]
            elif gejala_yang_dialami[0] == "G023" and gejala_yang_dialami [1] == "G026" and gejala_yang_dialami[2] == "G027" and gejala_yang_dialami[3] == "G028" and gejala_yang_dialami[4] == "G029" and gejala_yang_dialami[5] == "G030" and gejala_yang_dialami[6] == "G031"and gejala_yang_dialami[7] == "G032"and gejala_yang_dialami[8] == "G033"and gejala_yang_dialami[9] == "G034"and gejala_yang_dialami[10] == "G035":
                return penyakit[4][1]
            elif gejala_yang_dialami[0] == "G007" and gejala_yang_dialami [1] == "G036" and gejala_yang_dialami[2] == "G037" and gejala_yang_dialami[3] == "G038" and gejala_yang_dialami[4] == "G039" and gejala_yang_dialami[5] == "G040" and gejala_yang_dialami[6] == "G041":
                return penyakit[5][1]
            elif gejala_yang_dialami[0] == "G025" and gejala_yang_dialami [1] == "G042" and gejala_yang_dialami[2] == "G043" and gejala_yang_dialami[3] == "G044" and gejala_yang_dialami[4] == "G045":
                return penyakit[6][1]
            elif gejala_yang_dialami[0] == "G007" and gejala_yang_dialami [1] == "G012" and gejala_yang_dialami[2] == "G024" and gejala_yang_dialami[3] == "G034" and gejala_yang_dialami[4] == "G038" and gejala_yang_dialami[5] == "G044" and gejala_yang_dialami[6] == "G046"and gejala_yang_dialami[7] == "G047"and gejala_yang_dialami[8] == "G048":
                return penyakit[7][1]
            elif gejala_yang_dialami[0] == "G006" and gejala_yang_dialami [1] == "G022" and gejala_yang_dialami[2] == "G048" and gejala_yang_dialami[3] == "G049" and gejala_yang_dialami[4] == "G050" and gejala_yang_dialami[5] == "G051" and gejala_yang_dialami[6] == "G052"and gejala_yang_dialami[7] == "G053"and gejala_yang_dialami[8] == "G054":
                return penyakit[8][1]
            elif gejala_yang_dialami[0] == "G022" and gejala_yang_dialami [1] == "G056" and gejala_yang_dialami[2] == "G057" and gejala_yang_dialami[3] == "G058" and gejala_yang_dialami[4] == "G059" and gejala_yang_dialami[5] == "G060" and gejala_yang_dialami[6] == "G061":
                return penyakit[9][1]
            else:
                print(" Penyakit yang anda alami tidak diketahui, mungkin gejala yang di masukkan tidak lengkap. Mohon di ulangi lagi!")
                gejala_pasien.clear()
                time.sleep(1.5)
                pertanyaan()
        except:
            print(" Penyakit yang anda alami tidak diketahui, mungkin gejala yang di masukkan tidak lengkap. Mohon di ulangi lagi!")
            gejala_pasien.clear()
            time.sleep(1.5)
            pertanyaan()


while True:
    clear()
    print(f"{'Selamat datang di Program Diagnosa Kandungan':^78}\n")
    mulai = input(f"{'Mulai diagnosa?[y/n]: ':>50}").lower()
    if mulai == "y":
        pertanyaan()
        
