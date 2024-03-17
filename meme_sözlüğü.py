meme_dict = {
            "LOL": "komik bir şeye verilen cevap",
            "CRINGE": "garip ya da utandırıcı bir şey",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek",
            ":D": "yandan gülme emojisi" 
            }
print("Selamlar")
while True:
    word=input("Bilmediğin meme kelimesini yaz: ")
    word=word.upper()

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        # Kelime eşleşmiyorsa ne yapmalıyız?
        print("Sözlükte bulunmamaktadır")
