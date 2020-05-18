from KOR_3D.kor3d import sent2vects, vects2sent

# phoneme decomposition
text = 'ㄱㄲㅎㄳㅄㅏㅣㅢ가깬댟az !)123'
result = sent2vects(text)
print(result)

recover = vects2sent(result)
print(''.join(recover))
text == recover