"""Reproduce finite checks of pair-deletion collisions in Stirling permutations.
Run: python3 verify.py. Uses only Python standard library.
"""
from collections import Counter
from itertools import combinations
from math import prod
from fractions import Fraction


def stirling_words(n):
    words=[(1,1)]
    for k in range(2,n+1):
        words=[word[:p]+(k,k)+word[p:] for word in words for p in range(2*k-1)]
    return words


def output(word,i):
    return tuple(v-(v>i) for v in word if v!=i)


def dd(n):
    return prod(range(1,2*n,2))


def pair_count(n,i,j):
    a=j-i
    return dd(i)*(prod(2*t+1-2*a for t in range(j,n)) +
                  2*prod(2*t-2*a for t in range(j,n)))


def geometric_type(w,i,j):
    fs=[]; ls=[]
    for k in range(i,j+1):
        fs.append(w.index(k));ls.append(len(w)-1-w[::-1].index(k))
    nest=all(fs[k+1]==fs[k]+1 and ls[k+1]==ls[k]-1 for k in range(j-i))
    sibling=(all(ls[k]==fs[k]+1 for k in range(j-i+1)) and
             (all(fs[k+1]==fs[k]+2 for k in range(j-i)) or
              all(fs[k+1]==fs[k]-2 for k in range(j-i))))
    return nest or sibling


def check(n):
    observed=Counter(); histogram=Counter(); singleton=[]
    words=stirling_words(n)
    for w in words:
        images=[output(w,i) for i in range(1,n+1)]
        hist=len(set(images));histogram[hist]+=1
        for i,j in combinations(range(1,n+1),2):
            collision=images[i-1]==images[j-1]
            assert collision==geometric_type(w,i,j),(n,w,i,j)
            if collision:
                observed[(i,j)]+=1
                assert all(images[k-1]==images[i-1] for k in range(i,j+1))
        if hist==1:
            singleton.append(w)
        assert hist == n-sum(images[i]==images[i+1] for i in range(n-1))
    assert len(words)==dd(n)
    for i,j in combinations(range(1,n+1),2):
        assert observed[(i,j)]==pair_count(n,i,j),(n,i,j,observed[(i,j)],pair_count(n,i,j))
    expect=Fraction(n,1)-Fraction(2,3)-Fraction(n-1,2*n-1) if n>=2 else Fraction(1,1)
    assert Fraction(sum(k*v for k,v in histogram.items()),len(words))==expect
    if n>=2:
        assert len(singleton)==3
    print('n',n,'sources',len(words),'distinct_deck_hist',sorted(histogram.items()),'pairwise_checks',len(words)*n*(n-1)//2,'mean',str(expect))

if __name__=='__main__':
    for n in range(2,8):
        check(n)
    print('VERIFY_OK')
