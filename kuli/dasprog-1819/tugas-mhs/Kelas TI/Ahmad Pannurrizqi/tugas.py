saya = input('berat badan saya (kg):')
teman =input('berat badan teman (kg):')
saya=int(saya)
teman=int(teman)
hasil1 =(saya- teman)
hasil2 =(teman- saya)
if saya > teman:
	kategori = 'saya lebih berat' ,abs(hasil1), 'kg dari teman'
elif teman > saya:
	kategori = 'saya lebih ringan' ,abs(hasil2), 'kg dari teman'
else:
	kategori = 'berat saya sama dengan teman '
print('{}'.format(kategori)) 
