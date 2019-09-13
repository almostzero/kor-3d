import numpy as np
from time import time

class Kor3D():
    def __init__(self):
        self.syllable = 0xac00
        self.consonant = ord('ㄱ')
        self.vowel = ord('ㅏ')
    
    def phoneme_decomposition(self, letter):
        #     음절코드: 0xac00, 초성코드: 0x1100, 중성코드: 0x1161, 종성코드: 0x11a8    
        return [chr((ord(letter) - self.syllable) // (28 * 21) + 0x1100),
               chr(((ord(letter) - self.syllable) % (28 * 21)) // 28 + 0x1161),
               chr((ord(letter) - self.syllable) % 28 + 0x11a8 - 1).strip()]
    
    def trans_3d(self, letter):
        if self.syllable - 1 < ord(letter) < self.syllable + 11172:
            letter_3d = self.phoneme_decomposition(letter)
        elif self.consonant - 1 < ord(letter) < self.consonant + 30:
            letter_3d = [letter, '', '']
        elif self.vowel - 1 < ord(letter) < self.vowel + 21:
            letter_3d = ['', letter, '']
        else:
            letter_3d = [letter] * 3
        
        return letter_3d
    
    def kor_trans(self, sentence):
        start = time()
        trans_sent = np.array([self.trans_3d(letter) for letter in sentence])
        print(f'{time() - start} sec')

        return trans_sent
    
