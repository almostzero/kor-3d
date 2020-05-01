from KOR_3D.kor3d import *

# phoneme decomposition
text = 'ㄱㅎㅏㅣ가힣az!)'
result = sent2vects(text)
print(result)

sart_point = 0xac00
''.join([chr(i) for i in range(sart_point, sart_point + 200)])

