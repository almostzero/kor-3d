# kor-3d
A Python library for preprocessing Korean


# Usage
 Korean syllables(음절) are composed with 1 vowel(모음) and 1 or 2 consonants(자음). It's structure is different from any other languages.

 Recently, many libraries and deep learning architectures are arisen but korean letter structure makes it harder to work with them. So here's a think about how to reflect the syllable structure information into the machine learning.
 
 This module decompose korean letters to consonants and vowels. And the result data will be change in to 3 dimentional data, Which is like RGB image data.
 
<pre><code>
from KOR_3D.korto3d import Korto3D
k3d = Korto3D()
result = k3d.kor_trans('ㄱㅎㅏㅣ가힣az!)')
print(result)

>>  3.5762786865234375e-05 sec
>>  array([['ㄱ', '', ''],
         ['ㅎ', '', ''],
         ['', 'ㅏ', ''],
         ['', 'ㅣ', ''],
         ['ᄀ', 'ᅡ', 'ᆧ'],
         ['ᄒ', 'ᅵ', 'ᇂ'],
         ['a', 'a', 'a'],
         ['z', 'z', 'z'],
         ['!', '!', '!'],
         [')', ')', ')']], dtype='\<U1')
</code></pre>
