from konlpy.tag import Kkma
from konlpy.tag import Okt

def basic_example():
    # 샘플 텍스트
    text = "안녕하세요. 자연어처리 공부를 시작했어요!"
    
    # Okt(Open Korean Text) 형태소 분석기 사용
    okt = Okt()
    
    # 형태소 분석 예제
    print("형태소 분석 결과:")
    print(okt.morphs(text))
    
    # 품사 태깅 예제
    print("\n품사 태깅 결과:")
    print(okt.pos(text))
    
    # 명사 추출 예제
    print("\n명사 추출 결과:")
    print(okt.nouns(text))

if __name__ == "__main__":
    basic_example()
