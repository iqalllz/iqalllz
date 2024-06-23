class Recognize_S:
    def __init__(self):
        # Inisialisasi tabel transisi dengan state dan transisi yang sesuai
        self.transitions = {
            0: {"n": 1},  # Dari state 0, jika menerima 'n' maka pindah ke state 1
            1: {
                "a": 2,  # Dari state 1, jika menerima 'a' maka pindah ke state 2
                "i": 4,  # Dari state 1, jika menerima 'i' maka pindah ke state 4
                "u": 6,  # Dari state 1, jika menerima 'u' maka pindah ke state 6
                "e": 8,  # Dari state 1, jika menerima 'e' maka pindah ke state 8
                "o": 10,  # Dari state 1, jika menerima 'o' maka pindah ke state 10
            },
            2: {"n": 3},  # Dari state 2, jika menerima 'n' maka pindah ke state 3
            3: {
                "a": 100
            },  # Dari state 3, jika menerima 'a' maka pindah ke state 100 (state final)
            4: {"n": 5},  # Dari state 4, jika menerima 'n' maka pindah ke state 5
            5: {
                "i": 100
            },  # Dari state 5, jika menerima 'i' maka pindah ke state 100 (state final)
            6: {"n": 7},  # Dari state 6, jika menerima 'n' maka pindah ke state 7
            7: {
                "u": 100
            },  # Dari state 7, jika menerima 'u' maka pindah ke state 100 (state final)
            8: {"n": 9},  # Dari state 8, jika menerima 'n' maka pindah ke state 9
            9: {
                "e": 100
            },  # Dari state 9, jika menerima 'e' maka pindah ke state 100 (state final)
            10: {"n": 11},  # Dari state 10, jika menerima 'n' maka pindah ke state 11
            11: {
                "o": 100
            },  # Dari state 11, jika menerima 'o' maka pindah ke state 100 (state final)
        }
        # Tentukan state final sebagai 100
        self.final_state = 100

    def recognize(self, word):
        curr_state = 0  # Inisialisasi state awal
        for letter in word:
            if (
                curr_state in self.transitions
                and letter in self.transitions[curr_state]
            ):
                curr_state = self.transitions[curr_state][
                    letter
                ]  # Pindah ke state berikutnya
            else:
                curr_state = (
                    -1
                )  # Jika tidak ada transisi yang sesuai, set state ke -1 (state tidak valid)

        print("TEST: ", curr_state)
        return (
            curr_state == self.final_state
        )  # Mengembalikan True jika state terakhir adalah state final (kata dikenali)
