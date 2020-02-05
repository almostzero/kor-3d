import numpy as np

from Utils.show_progress import Timer

class Kor3D:
    def __init__(self):
        self.syllable = 0xac00
        self.consonant = ord('ㄱ')
        self.vowel = ord('ㅏ')
        self.upper_consonants = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
        self.vowels = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
        self.lower_consonants = ['ᆧ','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
    
    def phoneme_decomposition(self, letter):
        #     음절코드: 0xac00, 초성코드: 0x1100, 중성코드: 0x1161, 종성코드: 0x11a8    
        # return [chr((ord(letter) - self.syllable) // (28 * 21) + 0x1100),
        #        chr(((ord(letter) - self.syllable) % (28 * 21)) // 28 + 0x1161),
        #        chr((ord(letter) - self.syllable) % 28 - 1 + 0x11a8).strip()]
        return [self.upper_consonants[(ord(letter) - self.syllable) // (28 * 21)],
               self.vowels[((ord(letter) - self.syllable) % (28 * 21)) // 28],
               self.lower_consonants[(ord(letter) - self.syllable) % 28]]
    
    def trans_syllable_3d(self, letter):
        if self.syllable - 1 < ord(letter) < self.syllable + 11172:
            letter_3d = self.phoneme_decomposition(letter)
        elif self.consonant - 1 < ord(letter) < self.consonant + 30:
            letter_3d = [letter, '', '']
        elif self.vowel - 1 < ord(letter) < self.vowel + 21:
            letter_3d = ['', letter, '']
        else:
            letter_3d = [letter] * 3
        
        return letter_3d
    
    @Timer(message='transform to array')
    def trans_sent_3n(self, sentence):
        trans_sent = np.array([self.trans_syllable_3d(letter) for letter in sentence])
        print(f'tranfrom string to 3*n dimension array')

        return trans_sent
    
    def phoneme_composition(self, vector):
        upper_consonant = self.upper_consonants.index(vector[0])
        vowel = self.vowels.index(vector[1])
        lower_consonant = self.lower_consonants.index(vector[2])
        
        return chr(((upper_consonant * 21) + vowel) * 28 + lower_consonant + 0xac00)
    
    def trans_syllable_1d(self, vector):
        if vector[0] == vector[1] == vector[2]:
            letter = vector[0]
        elif not vector[2]:
            letter = [x for x in vector if x][0]
        else:
            letter = self.phoneme_composition(vector)
            
        return letter
    
    @Timer(message='transform 3D array to sentence')
    def trans_sent_1n(self, vectors):
        trans_vec = [self.trans_syllable_1d(vector) for vector in vectors]
        print(f'tranfrom 3*n dimension array to string')
        
        return ''.join(trans_vec)
