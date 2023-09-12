def not_defteri():
    notlar = []

    while True:
        print("****************************")
        print("1. Not Ekle")
        print("2. Notları Göster")
        print("3. Çıkış")

        secim = input("Seçiminizi yapın (1/2/3): ")
        print("********************************")

        if secim == '1':
            not_ekle = input("Notu girin: ")
            notlar.append(not_ekle)
            print("Not başarıyla eklendi!")
        elif secim == '2':
            print("Notlar:")
            for i, notu in enumerate(notlar):
                print(f"{i+1}. {notu}")
        elif secim == '3':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz giriş!")

not_defteri()
