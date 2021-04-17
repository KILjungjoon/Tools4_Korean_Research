import json
import re

class GramTools:
    def __init__(self, text, remove_symbles=''):
        self.text = text
        if remove_symbles=='all':
            self.text = re.sub(r'[^\w]', ' ', text)
        elif remove_symbles:
            for symble in remove_symbles:
                self.text = self.text.replace(symble, '')
        self.lines = self.text.split('\n')

    def get_gram_by_line(self, line, n=1):
        gram_list = line.split()
        return [' '.join(gram_list[i:i+n]) for i in range(len(gram_list)-n+1)]

    def get_gram_by_lines(self, n=1, lines=[]):
        lines = lines if lines else self.lines
        n_gram = []
        for line in lines:
            n_gram.extend(self.get_gram_by_line(line, n))
        return n_gram

    def get_freq(self, n_gram):
        freq = {}
        for item in n_gram:
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
        return freq

    def get_n_gram_freq(self, n):
        n_gram      = self.get_gram_by_lines(n=n)
        n_gram_freq = self.get_freq(n_gram)
        return dict(sorted(n_gram_freq.items(), key=lambda item: item[1], reverse=True))

    def save(self, path, content, format='custom', indent=4):
        with open(path, 'w', encoding='utf-8') as f:
            if format=='custom':
                for k,v in content.items():
                    f.write(f'{k}|{v}\n')
            elif format=='json':
                json.dump(content, f, indent=indent, ensure_ascii=False)

if __name__=='__main__':
    with open('D:/경사대 선생님들/장미/전주_total.txt', 'r', encoding='utf-8') as f:
    # with open(source file path', 'r', encoding='utf-8') as f:
        text = f.read()
    g = GramTools(text, 'all')     # You can designate any seperator. 'all' removes all symbols in the n-gram text.
    # g = GramTools(text, '?')
    uni_gram = g.get_n_gram_freq(1)
    bi_gram  = g.get_n_gram_freq(2)
    tri_gram = g.get_n_gram_freq(3)
    four_gram = g.get_n_gram_freq(4)
    five_gram = g.get_n_gram_freq(5)
    six_gram = g.get_n_gram_freq(6)
    
    g.save('D:/경사대 선생님들/장미/전주_1gram.txt', uni_gram)
    g.save('D:/경사대 선생님들/장미/전주_2gram.txt', bi_gram)
    g.save('D:/경사대 선생님들/장미/전주_3gram.txt', tri_gram)
    g.save('D:/경사대 선생님들/장미/전주_4gram.txt', four_gram)
    g.save('D:/경사대 선생님들/장미/전주_5gram.txt', five_gram)
    g.save('D:/경사대 선생님들/장미/전주_6gram.txt', six_gram)