class Recognize_P:
    def __init__(self):
        # Definisi transisi state untuk mesin keadaan terbatas (finite state machine)
        self.transitions = {
            0: {"m": 1},  # State 0: Jika karakter 'm' ditemukan, pindah ke state 1
            1: {"e": 2},  # State 1: Jika karakter 'e' ditemukan, pindah ke state 2
            2: {
                "m": 3,
                "n": 18,
            },  # State 2: Jika karakter 'm' ditemukan, pindah ke state 3, jika 'n', pindah ke state 18
            3: {
                "i": 4,
                "p": 8,
                "b": 13,
            },  # State 3: Jika 'i' ditemukan, pindah ke state 4, 'p' ke state 8, 'b' ke state 13
            4: {"l": 5},  # State 4: Jika karakter 'l' ditemukan, pindah ke state 5
            5: {"i": 6},  # State 5: Jika karakter 'i' ditemukan, pindah ke state 6
            6: {"k": 7},  # State 6: Jika karakter 'k' ditemukan, pindah ke state 7
            7: {
                "i": 100
            },  # State 7: Jika karakter 'i' ditemukan, pindah ke state 100 (state akhir)
            8: {"u": 9},  # State 8: Jika karakter 'u' ditemukan, pindah ke state 9
            9: {"n": 10},  # State 9: Jika karakter 'n' ditemukan, pindah ke state 10
            10: {"y": 11},  # State 10: Jika karakter 'y' ditemukan, pindah ke state 11
            11: {"a": 12},  # State 11: Jika karakter 'a' ditemukan, pindah ke state 12
            12: {
                "i": 100
            },  # State 12: Jika karakter 'i' ditemukan, pindah ke state 100 (state akhir)
            13: {"a": 14},  # State 13: Jika karakter 'a' ditemukan, pindah ke state 14
            14: {"n": 15},  # State 14: Jika karakter 'n' ditemukan, pindah ke state 15
            15: {"g": 16},  # State 15: Jika karakter 'g' ditemukan, pindah ke state 16
            16: {"u": 17},  # State 16: Jika karakter 'u' ditemukan, pindah ke state 17
            17: {
                "n": 100
            },  # State 17: Jika karakter 'n' ditemukan, pindah ke state 100 (state akhir)
            18: {
                "j": 19,
                "g": 22,
            },  # State 18: Jika 'j' ditemukan, pindah ke state 19, jika 'g', pindah ke state 22
            19: {"a": 20},  # State 19: Jika karakter 'a' ditemukan, pindah ke state 20
            20: {"d": 21},  # State 20: Jika karakter 'd' ditemukan, pindah ke state 21
            21: {
                "i": 100
            },  # State 21: Jika karakter 'i' ditemukan, pindah ke state 100 (state akhir)
            22: {"e": 23},  # State 22: Jika karakter 'e' ditemukan, pindah ke state 23
            23: {"r": 24},  # State 23: Jika karakter 'r' ditemukan, pindah ke state 24
            24: {"j": 25},  # State 24: Jika karakter 'j' ditemukan, pindah ke state 25
            25: {"a": 26},  # State 25: Jika karakter 'a' ditemukan, pindah ke state 26
            26: {"k": 27},  # State 26: Jika karakter 'k' ditemukan, pindah ke state 27
            27: {"a": 28},  # State 27: Jika karakter 'a' ditemukan, pindah ke state 28
            28: {
                "n": 100
            },  # State 28: Jika karakter 'n' ditemukan, pindah ke state 100 (state akhir)
        }
        # State akhir yang menandakan kata dikenali sebagai predikat
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

        return (
            curr_state == self.final_state
        )  # Mengembalikan True jika state terakhir adalah state final (kata dikenali)
