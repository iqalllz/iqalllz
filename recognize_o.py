class Recognize_O:
    def __init__(self):
        # Definisi transisi state untuk mesin keadaan terbatas (finite state machine)
        self.transitions = {
            0: {
                "s": 1,
                "r": 7,
                "g": 11,
                "t": 14,
                "m": 18,
            },  # State 0: Karakter awal dapat 's', 'r', 'g', 't', atau 'm'
            1: {"e": 2},  # State 1: Jika karakter 'e' ditemukan, pindah ke state 2
            2: {"k": 3},  # State 2: Jika karakter 'k' ditemukan, pindah ke state 3
            3: {"o": 4},  # State 3: Jika karakter 'o' ditemukan, pindah ke state 4
            4: {"l": 5},  # State 4: Jika karakter 'l' ditemukan, pindah ke state 5
            5: {"a": 6},  # State 5: Jika karakter 'a' ditemukan, pindah ke state 6
            6: {
                "h": 100
            },  # State 6: Jika karakter 'h' ditemukan, pindah ke state 100 (state akhir)
            7: {"u": 8},  # State 7: Jika karakter 'u' ditemukan, pindah ke state 8
            8: {"m": 9},  # State 8: Jika karakter 'm' ditemukan, pindah ke state 9
            9: {"a": 10},  # State 9: Jika karakter 'a' ditemukan, pindah ke state 10
            10: {
                "h": 100
            },  # State 10: Jika karakter 'h' ditemukan, pindah ke state 100 (state akhir)
            11: {"u": 12},  # State 11: Jika karakter 'u' ditemukan, pindah ke state 12
            12: {"r": 13},  # State 12: Jika karakter 'r' ditemukan, pindah ke state 13
            13: {
                "u": 100
            },  # State 13: Jika karakter 'u' ditemukan, pindah ke state 100 (state akhir)
            14: {"u": 15},  # State 14: Jika karakter 'u' ditemukan, pindah ke state 15
            15: {"g": 16},  # State 15: Jika karakter 'g' ditemukan, pindah ke state 16
            16: {"a": 17},  # State 16: Jika karakter 'a' ditemukan, pindah ke state 17
            17: {
                "s": 100
            },  # State 17: Jika karakter 's' ditemukan, pindah ke state 100 (state akhir)
            18: {"a": 19},  # State 18: Jika karakter 'a' ditemukan, pindah ke state 19
            19: {"s": 20},  # State 19: Jika karakter 's' ditemukan, pindah ke state 20
            20: {"j": 21},  # State 20: Jika karakter 'j' ditemukan, pindah ke state 21
            21: {"i": 22},  # State 21: Jika karakter 'i' ditemukan, pindah ke state 22
            22: {
                "d": 100
            },  # State 22: Jika karakter 'd' ditemukan, pindah ke state 100 (state akhir)
        }
        # State akhir yang menandakan kata dikenali sebagai objek
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
