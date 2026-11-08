#!/usr/bin/env python3
"""Independent finite checks for a four-run word's maximal closed occurrences."""
from itertools import product


def is_closed(w):
    if len(w) == 1:
        return True
    # find() counts overlapping substring occurrences on later offsets.
    return any(w[:k] == w[-k:] and w.find(w[:k], 1) == len(w)-k
               for k in range(1, len(w)))


def exhaustive_mcs(w):
    out = set()
    for i in range(len(w)):
        for j in range(i+1, len(w)+1):
            if not is_closed(w[i:j]):
                continue
            if i > 0 and is_closed(w[i-1:j]):
                continue
            if j < len(w) and is_closed(w[i:j+1]):
                continue
            out.add((i,j))
    return out


def formula(a,b,c,d):
    n = a+b+c+d
    intervals = {(0,a), (a,a+b), (a+b,a+b+c), (a+b+c,n)}
    for x in range(1,min(a,c)+1):
        if x != c or c > a:
            intervals.add((a-x,a+b+x))
    for y in range(1,min(b,d)+1):
        if y != b or b > d:
            intervals.add((a+b-y,a+b+c+y))
    intervals.add((a-min(a,c),a+b+c+min(b,d)))
    return intervals


def count_formula(a,b,c,d):
    return 5+min(a,c)+min(b,d)-int(c<=a)-int(b<=d)


def four_compositions(n):
    for a in range(1,n-2):
        for b in range(1,n-a-1):
            for c in range(1,n-a-b):
                d=n-a-b-c
                yield a,b,c,d


def main():
    exact=0
    for a,b,c,d in product(range(1,9),repeat=4):
        w='0'*a+'1'*b+'0'*c+'1'*d
        actual=exhaustive_mcs(w)
        predicted=formula(a,b,c,d)
        assert actual==predicted, (a,b,c,d,actual-predicted,predicted-actual)
        assert len(predicted)==count_formula(a,b,c,d), (a,b,c,d)
        exact += 1
    print('PASS exact endpoint and count comparisons:',exact)
    for n in range(4,33):
        actual={count_formula(*quad) for quad in four_compositions(n)}
        maximum=5 if n==4 else n//2+4
        expected=set(range(5,maximum+1))
        assert actual==expected,(n,actual,expected)
    print('PASS lengthwise attainable spectra: n=4,...,32')

if __name__=='__main__':
    main()
