import numpy as np
from .LETTERS import *

# 일본어는 나중에
# https://m.blog.naver.com/PostView.nhn?blogId=aoba8615&logNo=140012660052&proxyReferer=https:%2F%2Fwww.google.com%2F


def check_encodings(string):
    """
    문자열의 인코딩을 확인하는 함수
    문자열이 유니코드가 아니면 디코드해서 변환
    :param string: 확인하고 싶은 문자열
    :return: 유니코드로 변환된 문자열
    """
    pass


def lang(syllable):
    """
    음절의 언어를 분류해주는 함수
    현재는 한글, 영어, 특수문자를 구분
    한글, 영어 이외에는 모두 특수문자 취급
    추후 일본어, 기타 음소문자 및 음운문자 대상으로 확장할 것
    :param syllable: 입력 음절
    :return language: 분류 결과
    """
    kor = any([True if syllable in v else False for k, v in kor_phonemes.items()] +
              [0xac00 - 1 < ord(syllable) < 0xac00 + 11172])
    eng = any([True if syllable.lower() in v else False for k, v in eng_phonemes.items()])

    if kor:
        language = 'kor'
    elif eng:
        language = 'eng'
    else:
        language = 'sc'

    return language


def syll2vect_kor(syllable):
    kor_startpoint = 0xac00
    if kor_startpoint - 1 < ord(syllable) < kor_startpoint + 11172:
        vector = [kor_phonemes['onset'][(ord(syllable) - kor_startpoint) // (28 * 21)],
                  kor_phonemes['nucleua'][((ord(syllable) - kor_startpoint) % (28 * 21)) // 28],
                  kor_phonemes['coda'][(ord(syllable) - kor_startpoint) % 28]]
    elif syllable in kor_phonemes['nucleua']:
        vector = ['', syllable, '']
    else:
        vector = [syllable, '', '']

    return vector

def syll2vect_eng(syllable):
    if syllable.lower() in eng_phonemes['consonants']:
        vector = [syllable, '', '']
    else:
        vector = ['', syllable, '']

    return vector

def syll2vect_sc(syllable):
    vector = ['', '', syllable]

    return vector

def syll2vect(syllable):
    """
    음절을 벡터로 변환하는 함수

    :param syllable: 입력 음절
    :return vector: 변환된 벡터
    """
    trans_dict = {
        'kor': syll2vect_kor,
        'eng': syll2vect_eng,
        'sc': syll2vect_sc
    }
    vector = trans_dict[lang(syllable)](syllable)

    return vector


def sent2vects(sentence):
    """
    문장의 음절을 벡터로 변환하는 함수

    :param sentence: 바꿔야할 문장
    :return vectors: 벡터로 바뀐 문장
    """
    vectors = [syll2vect(syllable) for syllable in sentence]

    return vectors
