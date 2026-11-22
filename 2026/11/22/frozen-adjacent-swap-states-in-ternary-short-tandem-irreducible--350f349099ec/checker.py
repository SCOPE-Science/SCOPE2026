"""Independent bounded checks of a ternary restricted adjacent-swap census.
All-length statements are proved separately; this script checks finite cases.
"""
from itertools import product
from collections import Counter


def fib(k):
    a,b=0,1
    for _ in range(k):a,b=b,a+b
    return a


def valid_word(w):
    return all(w[i]!=w[i+1] for i in range(len(w)-1)) and all(w[i:i+2]!=w[i+2:i+4] for i in range(len(w)-3))


def signs_to_word(s,first=0):
    w=[first]
    for d in s:w.append((w[-1]+d)%3)
    return tuple(w)


def sign_admissible(s):
    return all(not (s[i]!=s[i+1] and s[i+1]!=s[i+2]) for i in range(len(s)-2))


def runs(s):
    lens=[]
    for d in s:
        if lens and d==last:lens[-1]+=1
        else:lens.append(1)
        last=d
    return lens


def prescribed_frozen(s):
    r=runs(s)
    return len(r)>=2 and r[0]==r[-1]==1 and all(x in (2,4) for x in r[1:-1])


def degree(w):
    count=0
    for j in range(len(w)-1):
        v=list(w)
        v[j],v[j+1]=v[j+1],v[j]
        count+=valid_word(v)
    return count


def run():
    ncases=0
    for m in range(2,19):
        A=[s for s in product((-1,1),repeat=m) if sign_admissible(s)]
        frozen=0
        for s in A:
            w=signs_to_word(s)
            assert valid_word(w)
            actual=degree(w)==0
            assert actual==prescribed_frozen(s), (s,actual,runs(s))
            frozen+=actual
        n=m+1
        expected=2*fib((n-1)//2) if n%2 else 0
        assert frozen==expected,(n,frozen,expected)
        ncases+=len(A)
        print(f'n={n:2} sign_cases={len(A):5} frozen_labeled={3*frozen:5} predicted={3*expected:5}')
    # Independent direct enumeration over the original ternary alphabet.
    for n in range(3,12):
        actual=0
        for w in product(range(3),repeat=n):
            if valid_word(w):actual+=degree(w)==0
        pred=6*fib((n-1)//2) if n%2 else 0
        assert actual==pred,(n,actual,pred)
    print('PASS: sign-case checks:',ncases,'direct ternary words through length 11')

if __name__=='__main__':run()
