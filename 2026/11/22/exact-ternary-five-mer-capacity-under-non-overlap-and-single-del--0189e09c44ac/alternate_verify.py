#!/usr/bin/env python3
"""Independent exact normal-form enumeration, using LCS rather than deletion sets."""
from itertools import combinations, product


def longest_common_subsequence(a,b):
    M = [0] * (len(b)+1)
    for x in a:
        N = [0]
        for j,y in enumerate(b):
            N.append(M[j]+1 if x==y else max(M[j+1],N[-1]))
        M = N
    return M[-1]


def eligible(x):
    return x[0] in '02' and x[-1]=='1' and all(x[:r]!=x[-r:] for r in range(1,5))


def okay(x,y):
    return (all(x[:r]!=y[-r:] and y[:r]!=x[-r:] for r in range(1,5))
            and longest_common_subsequence(x,y) <= 3)


def main():
    W=[''.join(x) for x in product('012',repeat=5)]
    W=[w for w in W if eligible(w)]
    assert len(W)==48
    N=len(W)
    links=[0]*N
    for i in range(N):
        for j in range(i+1,N):
            if okay(W[i],W[j]):
                links[i]|=1<<j
                links[j]|=1<<i
    codes=[]
    def visit(t,positions):
        if len(t)==6:
            codes.append(tuple(W[k] for k in t))
            return
        if len(t)+positions.bit_count()<6:
            return
        while positions:
            bit=positions&-positions
            i=bit.bit_length()-1
            positions^=bit
            visit(t+(i,), positions&links[i])
    visit((),(1<<N)-1)
    assert len(codes)==12, len(codes)
    # By the size-seven test, no feasible sextuple can be enlarged.
    for C in codes:
        assert not any(all(okay(w,x) for x in C) for w in W if w not in C)
    print('ALTERNATE_OK')
    print('normal_form_words',N,'normal_form_optima',len(codes))

if __name__=='__main__':main()
