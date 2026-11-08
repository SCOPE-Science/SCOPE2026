#!/usr/bin/env python3
"""Recompute distinct-square counts by independent string scanning and finite coefficient sums."""
from math import comb
from random import Random


def positive_count(left, right):
    return max(0, right-left+1)


def interval_count(pre, post, middle):
    return positive_count(max(0, middle-post), min(pre, middle))


def formula(a, b, c, d):
    return (max(a,b,c,d)//2
            + interval_count(a,c,b)
            + interval_count(b,d,c)
            - (interval_count(a,d,b) if b==c else 0))


def direct(a,b,c,d):
    word='0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d
    squares=set()
    for start in range(len(word)):
        for root_length in range(1, (len(word)-start)//2 + 1):
            left=word[start:start+root_length]
            if left==word[start+root_length:start+2*root_length]:
                squares.add(left+left)
    return len(squares)


def binom3(t):
    return comb(t+3,3) if t>=0 else 0


def coeff(m):
    z=0
    for k in range(1,m//2+1):
        for j in range(1,5):
            z+=(-1)**(j+1)*comb(4,j)*binom3(m-2*k*j)
    n1=sum((r+1)*comb(m-2*r+2,2) for r in range(m//2+1))
    diagonal=sum((r+1)*(m-3*r+1) for r in range(m//3+1))
    return z+2*n1-diagonal


def main():
    count=0
    for n in range(3,31):
        m=n-3
        for a in range(m+1):
            for b in range(m-a+1):
                for c in range(m-a-b+1):
                    d=m-a-b-c
                    actual=direct(a,b,c,d)
                    expected=formula(a,b,c,d)
                    assert actual==expected, (n,a,b,c,d,actual,expected)
                    count+=1
    print('DIRECT_SQUARES_OK',count)
    rng=Random(1197223)
    for _ in range(240):
        m=rng.randrange(28,100)
        cuts=sorted([rng.randrange(m+1) for _ in range(3)])
        a,b,c,d=cuts[0],cuts[1]-cuts[0],cuts[2]-cuts[1],m-cuts[2]
        assert direct(a,b,c,d)==formula(a,b,c,d)
    print('LONG_RANDOM_OK 240')
    for m in range(51):
        total=sum(formula(a,b,c,m-a-b-c)
                  for a in range(m+1) for b in range(m-a+1)
                  for c in range(m-a-b+1))
        assert total==coeff(m), (m,total,coeff(m))
    print('GENERATING_FUNCTION_OK 0..50')
    print('INITIAL_TOTALS', [coeff(m) for m in range(12)])

if __name__=='__main__': main()
