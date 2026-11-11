harga_laptop = 12000000
stok_laptop = 100

print("=== SISTEM KASIR MINI ===")
try:
    jumlah_beli = int(input(f"Masukkan jumlah Laptop yang ingin dibeli (Stok: {stok_laptop}): "))
    
    if jumlah_beli <= 0:
        print("Jumlah pembelian tidak valid.")
    elif jumlah_beli > stok_laptop:
        print("Transaksi Gagal: Stok tidak mencukupi!")
    else:
        total_harga = jumlah_beli * harga_laptop
        print(f"Harga Awal: Rp {total_harga:,}")
        
        if total_harga >= 30000000:
            diskon = int(total_harga * 0.10)
            print(f"Selamat! Anda dapat diskon 10%: Rp {diskon:,}")
        else:
            diskon = 0
            
        total_akhir = total_harga - diskon
        print(f"Total yang harus dibayar: Rp {total_akhir:,}")
        
        uang_pembeli = int(input("Masukkan nominal uang pembayaran: Rp "))
        
        if uang_pembeli >= total_akhir:
            kembalian = uang_pembeli - total_akhir
            stok_laptop -= jumlah_beli 
            print("\n=== NOTA TRANSAKSI ===")
            print("Status: LUNAS / BERHASIL")
            print(f"Kembalian: Rp {kembalian:,}")
            print(f"Sisa Stok Laptop Sekarang: {stok_laptop}")
        else:
            print(f"\nStatus: TRANSAKSI GAGAL. Uang kurang Rp {total_akhir - uang_pembeli:,}")
            
except ValueError:
    print("Error: Harap masukkan angka yang valid!")
