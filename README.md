# nlp_3d
A Python library for preprocessing Korean

# Environment
- ubuntu 18.04 LTS
- python 3.7
- jupyter lab

# Usage
 Korean syllables(음절) are composed of 1 vowel(모음) and 1 or 2 consonants(자음). It's structure is different from any other languages.

 Recently, many libraries and deep learning architectures are arisen but korean letter structure makes it harder to work with them. So here's a thinking about how to reflect the syllable structure information into the NLP machine learning projects.
 
 This module decompose korean letters to consonants and vowels. And the result data will be changed to 3 dimentional data, Which is like RGB image data.
 
<pre><code>
from KOR_3D.kor3d import Kor3D
k3d = Kor3D()

# phoneme decomposition
result = k3d.kor_trans('ㄱㅎㅏㅣ가힣az!)')
print(result)

>>  3.5762786865234375e-05 sec
>>  array([['ㄱ', '', ''],
       ['ㅎ', '', ''],
       ['', 'ㅏ', ''],
       ['', 'ㅣ', ''],
       ['ㄱ', 'ㅏ', 'ᆧ'],
       ['ㅎ', 'ㅣ', 'ㅎ'],
       ['a', 'a', 'a'],
       ['z', 'z', 'z'],
       ['!', '!', '!'],
       [')', ')', ')']])

# phoneme composition
recover = k3d.vec_trans(result)
print(''.join(recover))

>>  6.771087646484375e-05 sec
>>  'ㄱㅎㅏㅣ가힣az!)'
</code></pre>

~~Korean nlp 3D preprocessing module finished.~~  
Adding Timer...
