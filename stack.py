class Stack:
    def __init__(self):
        self.stack = []  # Inisialisasi stack sebagai list kosong

    def top(self):
        return self.stack[-1]  # Mengembalikan elemen paling atas dari stack

    def push(self, item):
        self.stack.append(item)  # Menambahkan item ke dalam stack

    def pop(self):
        item = self.stack[
            len(self.stack) - 1
        ]  # Mengambil elemen paling atas dari stack
        self.stack = self.stack[
            : len(self.stack) - 1
        ]  # Menghapus elemen paling atas dari stack
        return item  # Mengembalikan elemen yang dihapus dari stack
