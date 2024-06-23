class Recognize_K:
    def __init__(self):
        # Definisi transisi state untuk mesin keadaan terbatas (finite state machine)
        self.transitions = {
            0: {"d": 1},  # State 0: Jika karakter 'd' ditemukan, pindah ke state 1
            1: {"i": 2},  # State 1: Jika karakter 'i' ditemukan, pindah ke state 2
            2: {" ": 3},  # State 2: Jika spasi ditemukan, pindah ke state 3
            3: {  # State 3: Jika karakter 'm', 'p', 'j', atau 't' ditemukan, pindah ke state berikutnya
                "m": 4,
                "p": 12,
                "j": 16,
                "t": 19,
            },
            4: {"a": 5},  # State 4: Jika karakter 'a' ditemukan, pindah ke state 5
            5: {  # State 5: Jika karakter 'l' ditemukan, pindah ke state 6, jika 'd' ditemukan, pindah ke state 9
                "l": 6,
                "d": 9,
            },
            6: {"u": 7},  # State 6: Jika karakter 'u' ditemukan, pindah ke state 7
            7: {"k": 8},  # State 7: Jika karakter 'k' ditemukan, pindah ke state 8
            8: {
                "u": 100
            },  # State 8: Jika karakter 'u' ditemukan, pindah ke state 100 (state akhir)
            9: {"u": 10},  # State 9: Jika karakter 'u' ditemukan, pindah ke state 10
            10: {"r": 11},  # State 10: Jika karakter 'r' ditemukan, pindah ke state 11
            11: {
                "a": 100
            },  # State 11: Jika karakter 'a' ditemukan, pindah ke state 100 (state akhir)
            12: {"a": 13},  # State 12: Jika karakter 'a' ditemukan, pindah ke state 13
            13: {"p": 14},  # State 13: Jika karakter 'p' ditemukan, pindah ke state 14
            14: {"u": 15},  # State 14: Jika karakter 'u' ditemukan, pindah ke state 15
            15: {
                "a": 100
            },  # State 15: Jika karakter 'a' ditemukan, pindah ke state 100 (state akhir)
            16: {"a": 17},  # State 16: Jika karakter 'a' ditemukan, pindah ke state 17
            17: {"w": 18},  # State 17: Jika karakter 'w' ditemukan, pindah ke state 18
            18: {
                "a": 100
            },  # State 18: Jika karakter 'a' ditemukan, pindah ke state 100 (state akhir)
            19: {"o": 20},  # State 19: Jika karakter 'o' ditemukan, pindah ke state 20
            20: {"g": 21},  # State 20: Jika karakter 'g' ditemukan, pindah ke state 21
            21: {
                "o": 100
            },  # State 21: Jika karakter 'o' ditemukan, pindah ke state 100 (state akhir)
        }
        # State akhir yang menandakan kata dikenali sebagai keterangan
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
