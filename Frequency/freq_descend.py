# 형태의미분석 파일을 읽고 고빈도순으로 형태소를 정렬하기
with open("D:/GitHub/Tools4_Korean_Research/Frequency/소나기_tag.txt", "r", encoding = "utf-8-sig") as inp:
    product = dict()
    for line in inp.read().split():
        for p in line.split("+"):
            if (p in product):
                product[p] += 1
            else:
                product[p] = 1
    with open("D:/GitHub/Tools4_Korean_Research/Frequency/소나기_frq.txt", "w", encoding = "utf-8") as outp:
        for p, v in sorted(product.items(), key = lambda x: x[1], reverse = True):
            print("{}({})".format(p, v))
            outp.write("{}({})\n".format(p, v))