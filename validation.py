class Validation:
    def __init__(self, stack):
        self.stack = stack  # Menginisialisasi stack yang digunakan untuk validasi
        self.current_state = "q0"  # State awal dari Push Down Automata (PDA)

    def transition(self, token):
        # Menerapkan transisi berdasarkan token dan current_state saat ini
        if self.current_state == "q1":
            if token == "S":
                self.stack.push("S")  # Push "S" ke dalam stack
                self.current_state = "q2"  # Pindah ke state q2 setelah menemukan "S"

        elif self.current_state == "q2":
            if token == "P":
                self.stack.pop()  # Pop elemen dari stack
                self.current_state = "q3"  # Pindah ke state q3 setelah menemukan "P"

        elif self.current_state == "q3":
            if token == "O":
                self.current_state = "q4"  # Pindah ke state q4 setelah menemukan "O"
            elif token == "K":
                self.current_state = "q5"  # Pindah ke state q5 setelah menemukan "K"
            else:
                self.current_state = (
                    "qerr"  # Pindah ke state error (qerr) jika tidak sesuai
                )

        elif self.current_state == "q4":
            if token == "K":
                self.current_state = "q5"  # Pindah ke state q5 setelah menemukan "K"
            else:
                self.current_state = (
                    "qerr"  # Pindah ke state error (qerr) jika tidak sesuai
                )

        elif self.current_state == "q5":
            self.current_state = (
                "qerr"  # Pindah ke state error (qerr) jika mencapai state q5
            )

    def parse(self, tokens):
        self.stack.push("#")  # Push "#" sebagai penanda akhir dalam stack
        self.current_state = "q1"  # Set state awal ke q1
        for token in tokens:
            self.transition(
                token
            )  # Menerapkan transisi untuk setiap token dalam tokens
            if self.current_state == "qerr":
                break  # Berhenti jika mencapai state error (qerr)
        self.stack.pop()  # Pop "#" dari stack setelah selesai melakukan transisi

        if self.current_state in ["q3", "q4", "q5"]:
            self.current_state = (
                "q6"  # Jika mencapai state q3, q4, atau q5, pindah ke state q6
            )

    def validate(self, tokens):
        self.parse(tokens)  # Parsing tokens untuk validasi
        return len(self.stack.stack) == 0 and self.current_state == "q6"
        # Mengembalikan True jika stack kosong dan current_state adalah q6 (valid)
