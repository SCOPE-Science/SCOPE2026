"""Independent labeled-alphabet verification for short-block Abelian-cube avoidance.
Run with Python 3: python check_direct.py
"""
from collections import Counter
from itertools import product


def good(word):
    for k in range(len(word)-2):
        if word[k] == word[k+1] == word[k+2]:
            return False
    for k in range(len(word)-5):
        a,b,c = word[k:k+2],word[k+2:k+4],word[k+4:k+6]
        if Counter(a) == Counter(b) == Counter(c):
            return False
    return True


def brute(n):
    return sum(good(word) for word in product(range(3), repeat=n))


def dp(N):
    # Uses actual ternary letter-labeled suffixes, no relabeling quotient.
    counts = {():1}
    out = [1]
    for n in range(1,N+1):
        nxt=Counter()
        for tail, count in counts.items():
            for c in range(3):
                word = tail + (c,)
                if len(word)>=3 and word[-3:] == (c,c,c):
                    continue
                if len(word)>=6:
                    a,b,d=word[-6:-4],word[-4:-2],word[-2:]
                    if Counter(a)==Counter(b)==Counter(d):
                        continue
                nxt[word[-5:]]+=count
        counts=nxt
        out.append(sum(counts.values()))
    return out

def main():
    seq=dp(130)
    for n in range(0,12):
        assert brute(n)==seq[n], (n,brute(n),seq[n])
    assert seq[:13] == [1,3,9,24,66,180,468,1206,3150,8232,21462,55950,145920]
    d=[1,-1,-2,-4,-4,-2,1,2,1]
    assert all(sum(d[j]*seq[n-j] for j in range(9))==0 for n in range(11,131))
    print('PASS: direct 3^n enumeration n<=11; labeled 3^5 suffix DP through n=130')
    print('PASS: initial values and recurrence independently reproduced')

if __name__ == '__main__':
    main()
