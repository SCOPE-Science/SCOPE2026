"""Direct token construction and separation by internal 01 pairs.
Run: python3 verify_token_model.py
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb


def token_word(tokens):
    return ''.join({'F':'01','A':'1','B':'0','E':''}[x] for x in tokens)


def parse_tokens(w):
    out=[];i=0
    while i<len(w):
        if w[i:i+2]=='01':out.append('F');i+=2
        else:out.append('A' if w[i]=='1' else 'B');i+=1
    return ''.join(out)


def model(n,a,b):
    k=a+b;fib=defaultdict(int)
    if k>n+1:return fib
    # No empty block. Choose a A blocks followed by b B blocks.
    for modified in combinations(range(n), k):
        tokens=['F']*n
        for j,t in enumerate(modified): tokens[t]='A' if j<a else 'B'
        output=token_word(tokens)
        assert parse_tokens(output)==''.join(tokens)
        assert output.count('01')==n-k
        fib[output]+=1
    # One fully deleted block. The remaining blocks have a-1 A, b-1 B.
    for modified in combinations(range(n-1), k-2):
        base=['F']*(n-1)
        for j,t in enumerate(modified):base[t]='A' if j<a-1 else 'B'
        output=token_word(base)
        assert parse_tokens(output)==''.join(base)
        assert output.count('01')==n-k+1
        if a==1: L=0
        else:L=modified[a-2]+1
        if b==1:R=n-1
        else:R=modified[a-1]
        fiber=R-L+1
        assert fiber>=1
        fib[output]+=fiber
    return fib


def direct(n,a,b):
    w='01'*n;u='0'*a+'1'*b;fib=defaultdict(int)
    for ix in combinations(range(2*n),len(u)):
        if ''.join(w[j] for j in ix)!=u:continue
        rem=set(ix)
        fib[''.join(x for j,x in enumerate(w) if j not in rem)]+=1
    return fib


def main():
    cases=0
    for n in range(1,12):
        for a in range(1,n+2):
            for b in range(1,n+2):
                if a+b>n+1:continue
                d=direct(n,a,b)
                t=model(n,a,b)
                assert dict(d)==dict(t),(n,a,b,len(d),len(t))
                cases+=1
    print('COMPLEMENT_TOKEN_MODEL_OK',cases,'exact fiber dictionary comparisons')

if __name__=='__main__':main()
