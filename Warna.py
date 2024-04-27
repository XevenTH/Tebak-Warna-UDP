class Warna:
    def __init__(self, warna, jawaban):
        self.warna = warna
        self.jawaban = jawaban

    def GetWarna(self):
        return self.warna

    def GetPointAnswer(self, jawaban):
        if str(self.jawaban).lower() == str(jawaban).lower():
            return 0
        else:
            return 100