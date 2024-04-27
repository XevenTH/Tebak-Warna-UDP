class Warna:
    def __init__(self, warna, jawaban):
        self.warna = warna
        self.jawaban = jawaban

    def GetWarna(self):
        return self.warna

    def GetJawaban(self):
        return self.jawaban

    def GetPointAnswer(self, jawaban):
        return 100 if self.jawaban == jawaban else 0