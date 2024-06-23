from helper.recognize_s import Recognize_S  # Mengimpor Recognize_S untuk subjek
from helper.recognize_p import Recognize_P  # Mengimpor Recognize_P untuk predikat
from helper.recognize_o import Recognize_O  # Mengimpor Recognize_O untuk objek
from helper.recognize_k import Recognize_K  # Mengimpor Recognize_K untuk keterangan


class TokenRecognizer:
    def set_token(self, sentence):
        tokens = []  # Inisialisasi daftar token
        words = sentence.split()  # Memecah kalimat menjadi kata-kata
        i = 0

        # Iterasi melalui kata-kata dalam kalimat
        while i < len(words):
            word = words[i].lower()  # Mengambil kata dan merubahnya menjadi huruf kecil

            # Memeriksa apakah kata adalah subjek (S), predikat (P), atau objek (O)
            if Recognize_S().recognize(word):
                tokens.append("S")
                i += 1
            elif Recognize_P().recognize(word):
                tokens.append("P")
                i += 1
            elif Recognize_O().recognize(word):
                tokens.append("O")
                i += 1
            else:
                found_keterangan = False
                # Jika kata bukan subjek, predikat, atau objek, coba cari keterangan (K)
                for j in range(2, len(words) - i + 1):
                    phrase = " ".join(
                        words[i : i + j]
                    )  # Gabung kata-kata menjadi frasa
                    if Recognize_K().recognize(
                        phrase
                    ):  # Memeriksa apakah frasa adalah keterangan
                        tokens.append("K")
                        i += j
                        found_keterangan = True
                        break
                if not found_keterangan:
                    tokens.append(
                        "UNKNOWN"
                    )  # Jika tidak ditemukan yang cocok, tambahkan UNKNOWN
                    i += 1

        return tokens  # Mengembalikan daftar token yang telah dihasilkan
