def hitung_pangkat(bilangan, pangkat):
  if pangkat > 1:
    return bilangan * hitung_pangkat(bilangan, pangkat - 1)

  return bilangan

input_bilangan, input_pangkat = input("masukan angka (bilangan, pangkat): ").split()
print(hitung_pangkat(int(input_bilangan), int(input_pangkat)))