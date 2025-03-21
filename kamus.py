meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "FYP": "For Your Page",
            "FOMO": "perasaan cemas takut ketinggalan",
            "CUPU": "penampilan yang terlihat lemah",
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print(meme_dict[word])
    
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan
    print("maaf kata yang anda cari tidak ada T-T")
