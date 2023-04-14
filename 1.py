print('NAMA : WAODE SITI NURHALISA')
print('NIM : E1E120100')
print('PROGRAM MENENTUKAN FUNGSI INTERVASI FUUZZY')

print('Pertanyaan : ')
minta = float(input('Masukkan  Jumlah Permintaan = '))
sedia = float(input('Masukkan Jumlah Persediaan = '))

print('\n1. Fuzzyfikasi')


def permintaan_turun(minta):
    if minta <= 1000:
        return 1.0
    elif minta >= 5000:
        return 0.0
    else:
        return (5000 - minta) / (5000 - 1000)


def permintaan_naik(minta):
    if minta <= 1000:
        return 0.0
    elif minta >= 5000:
        return 1.0
    else:
        return (minta - 1000) / (5000 - 1000)


def persediaan_turun(sedia):
    if sedia <= 100:
        return 1.0
    elif sedia >= 600:
        return 0.0
    else:
        return (600 - sedia) / (600 - 100)


def persediaan_naik(sedia):
    if sedia <= 100:
        return 0.0
    elif sedia >= 600:
        return 1.0
    else:
        return (sedia - 100) / (600 - 100)


def produksi_brg_turun(produksi):
    if produksi <= 2000:
        return 1.0
    elif produksi >= 7000:
        return 0.0
    else:
        return (7000 - produksi) / (7000-2000)


def produksi_brg_naik(produksi):
    if produksi <= 2000:
        return 0.0
    elif produksi >= 7000:
        return 1.0
    else:
        return (produksi - 2000) / (7000-2000)


print('Nilai derajat keanggotaan permintaan turun = ', permintaan_turun(minta))
print('Nilai derajat keanggotaan permintaan naik = ', permintaan_naik(minta))
print('Nilai derajat keanggotaan persediaan turun = ', persediaan_turun(sedia))
print('Nilai derajat keanggotaan persediaan naik = ', persediaan_naik(sedia))


print('\n2. Operasi Logika Fuzzy dan')
print('3. Implikasi Kaidah Fuzzy')
nilai_min1 = min(permintaan_turun(minta), persediaan_naik(sedia))
print("Nilai minimum adalah", nilai_min1)
nilai_min2 = min(permintaan_turun(minta), persediaan_turun(sedia))
print("Nilai minimum adalah", nilai_min2)
nilai_min3 = min(permintaan_naik(minta), persediaan_naik(sedia))
print("Nilai minimum adalah", nilai_min3)
nilai_min4 = min(permintaan_naik(minta), persediaan_turun(sedia))
print("Nilai minimum adalah", nilai_min4)

print('\n4. Agregasi')
print('(', '', nilai_min1, ',', '', nilai_min2, ')')
nilai_max1 = max(nilai_min1, nilai_min2)
print("Nilai Maximum adalah", nilai_max1)
print('(', '', nilai_min3, ',', '', nilai_min4, ')')
nilai_max2 = max(nilai_min3, nilai_min4)
print("Nilai Maximum adalah", nilai_max2)

z1 = 7000 - (5000*nilai_max1)
print("Nilai a1 adalah ", z1)
z2 = 7000 - (5000*nilai_max2)
print("Nilai a2 adalah ", z2)

print("\n ", nilai_max1, " ; z <= ", z1)
print("7000-z/5000", " ; ", z1, "<=z<=", z2)
print(" ", nilai_max2, " ; >= ", z2)






















