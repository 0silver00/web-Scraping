from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ''

with open("kakao.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ','').replace('이모티콘\n','')\
                .replace('사진\n','').replace('삭제된 메시지입니다','').replace('ㅎㅎ','').replace('나도','')\
                .replace('근데','').replace('진짜','').replace('우리','').replace('그럼','').replace('ㄷㄷ','')\
                .replace('그거','').replace('이거','').replace('너무','').replace('아니','').replace('저거','')\
                .replace('내가','').replace('약간','').replace('다들','').replace('뭐야','').replace('맞아','')\
                .replace('ㅇㅇ','').replace('ㄱㄱ','').replace('그냥','').replace('나는','').replace('오늘','')\
                .replace('저는','').replace('거기','').replace('샵검색','').replace('내일','').replace('갑자기','')\
                .replace('ㅠㅠ','').replace('사진','')

print(text)

# wc = WordCloud(font_path='C:/Windows/Fonts/H2GTRE.TTF', background_color="white", width=600, height=400)
# wc.generate(text)
# wc.to_file("result.png")

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/Windows/Fonts/H2GTRE.TTF', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")
