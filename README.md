# nlp_3d
A Python library for preprocessing Korean


# Usage
 Korean syllables(음절) are composed with 1 vowel(모음) and 1 or 2 consonants(자음). It's structure is different from any other languages.

 Recently, many libraries and deep learning architectures are arisen but korean letter structure makes it harder to work with them. So here's a think about how to reflect the syllable structure information into the machine learning.
 
 This module decompose korean letters to consonants and vowels. And the result data will be change in to 3 dimentional data, Which is like RGB image data.
 
<pre><code>
from KOR_3D.kor3d import Kor3D
k3d = Kor3D()

# phoneme decomposition
result = k3d.kor_trans('ㄱㅎㅏㅣ가힣az!)')
print(result)

>>  3.5762786865234375e-05 sec
>>  array([['ㄱ', '', ''],
       ['', 'ㅏ', ''],
       ['!', '!', '!'],
       [' ', ' ', ' '],
       ['1', '1', '1'],
       ['5', '5', '5'],
       ['0', '0', '0'],
       ['ㅇ', 'ㅕ', 'ᆧ'],
       [' ', ' ', ' '],
       ['ㄱ', 'ㅗ', 'ㅅ']])

# phoneme composition
recover = k3d.vec_trans(result)
print(''.join(recover))

>>  6.771087646484375e-05 sec
>>  'ㄱㅎㅏㅣ가힣az!)'
</code></pre>

~~TODO: make composing module back to original korean syllables~~
Korean nlp preprocessing module finished.
