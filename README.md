# nlp_3d
A Python library for preprocessing Korean

# Environment
- ubuntu 18.04 LTS
- python 3.7
- jupyter lab

# Usage
 Korean syllables(음절) are composed of 1 vowel(모음) and 1 or 2 consonants(자음). It's structure is different from any other languages. They're also called onset(초성), nucleua(중성), coda(종성).

 Recently, many libraries and deep learning architectures are arisen but korean letter structure makes it harder to work with them. So here's a thinking about how to reflect the syllable structure information into the NLP machine learning projects.
 
 This module decompose korean letters to consonants and vowels. And the result data will be changed to 3 dimentional data, Which is like RGB image data.
 
<pre><code>
from KOR_3D.kor3d import sent2vects, vects2sent

# phoneme decomposition
text = 'ㄱㄲㅎㄳㅄㅏㅣㅢ가깬댟az !)123'
result = sent2vects(text)
print(result)
 
[['ㄱ' '' '']
 ['ㄲ' '' '']
 ['ㅎ' '' '']
 ['ㄳ' '' '']
 ['ㅄ' '' '']
 ['' 'ㅏ' '']
 ['' 'ㅣ' '']
 ['' 'ㅢ' '']
 ['ㄱ' 'ㅏ' '']
 ['ㄲ' 'ㅐ' 'ㄴ']
 ['ㄷ' 'ㅑ' 'ㄳ']
 ['' 'a' '']
 ['z' '' '']
 ['' '' ' ']
 ['' '' '!']
 ['' '' ')']
 ['' '' '1']
 ['' '' '2']
 ['' '' '3']]


# phoneme composition
recover = vects2sent(result)
print(recover)

ㄱㄲㅎㄳㅄㅏㅣㅢ가깬댟az !)123

text == recover
True
</code></pre>

