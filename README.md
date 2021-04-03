# Tools4_Korean_Research
 Basic analysis tools for Korean research and education.(한국어 연구와 교육을 위한 기본적인 텍스트 분석 도구)
 
## n-gram_extractor.py 사용 방법(Tutorial for n-gram_extractor.py)

1. 48행 'D:/GitHub/Tools4_Korean_Research/president_moon.txt' 부분을 분석하려는 파일의 경로로 변경하세요.
 
2. 51행 가장 중요한 부분입니다. g = GramTools(text, '|') 에서 ' ' 안은 임의의 구분자를 넣을 수 있습니다. '씄'과 같은 이상한 음절을 넣어도 됩니다.
   텍스트에서 출현할 확률이 거의 없는 구분자를 넣어 주면 n-gram 출력할 때 original text 안의 모든 기호가 보존되어 나타납니다.
   g = GramTools(text, 'all') 'all'을 입력하면 original text 안의 모든 기호가 사라집니다.
   따라서, 분석 텍스트 안에 다양한 기호들이 있고 그 기호들도 분석할 필요가 있다면 '|'이나 '씄' 등을 넣어 주시면 됩니다.
   
3. 52~55행 uni_gram부터 four_gram까지만 기본으로 넣어두었습니다. 5-gram을 원한다면 five_gram = g.get_n_gram_freq(5) 처럼 코드를 추가하시면 됩니다.
   텍스트의 특징에 따라 다르지만 n이 커지면 큰 의미가 없습니다.

4. 57~60행 출력할 경로와 파일명을 소스코드처럼 지정해 주시면 됩니다.
5. 빈도순으로 정렬된 결과를 보실 수 있습니다. 

### president_moon.txt(문재인 대통령 취임사)의 n-gram 결과를 보겠습니다.

1. 한 개 어절의 빈도인 1gram에서는 고빈도순으로 '대통령이'(17회), '되겠습니다'(13회) 
   두 개 어절쌍의 빈도인 2gram에서는 '대통령이 되겠습니다'(12회), '국민 여러분'(5회)순입니다.
   어떤 대통령이 되겠다는 각오와 약속을 국민들에게 선포하는 내용입니다. 대통령 취임사의 특성을 잘 볼 수 있습니다.

2. 이처럼 n-gram은 어절 단위로 텍스트를 보면서 텍스트의 주제를 분석하는 데 유익한 도구입니다.

   ![image](https://user-images.githubusercontent.com/62131328/113483000-c770c980-94d3-11eb-9b3f-ec94cb697223.png)
   ![image](https://user-images.githubusercontent.com/62131328/113483022-f2f3b400-94d3-11eb-9676-98455241b607.png)
   ![image](https://user-images.githubusercontent.com/62131328/113483046-1159af80-94d4-11eb-8ad4-9a09a595edb6.png)
   ![image](https://user-images.githubusercontent.com/62131328/113483059-21718f00-94d4-11eb-8210-c0dd32d9e947.png)
