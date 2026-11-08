"""Finite reconstruction checks for binary two-one single-grain codes."""
from itertools import combinations

def ball(n, pair):
    x = sum(1 << j for j in pair)
    out = {x}
    for j in range(1, n):
        if ((x >> (j-1)) ^ (x >> j)) & 1:
            out.add(x ^ (1 << j))
    return out

def code(n, r, j=None):
    result = {(i,i+1) for i in range(n-1)} | {(0,r)}
    if j is not None:
        result.remove((j-1,j))
        result.add((1,j))
    return result

def is_valid(n, codewords):
    seen = {}
    for pair in codewords:
        for y in ball(n,pair):
            if y in seen and seen[y]!=pair:
                return False
            seen[y]=pair
    return True

def maxcliques_binary(n):
    v=list(combinations(range(n),2)); sets=[ball(n,p) for p in v]
    k=len(v)
    good=[0]*k
    for i in range(k):
        for j in range(k):
            if i!=j and not (sets[i]&sets[j]):
                good[i] |= (1 << j)
    found=[]
    def bk(R,P,X):
        if not P and not X:
            found.append(tuple(v[i] for i in R))
            return
        if n>=4 and len(R)+(P.bit_count())<n:
            return
        z=P|X
        if z:
            pivot=max((i for i in range(k) if z>>i&1),key=lambda i:(P&good[i]).bit_count())
            choices=P & ~good[pivot]
        else:choices=P
        while choices:
            t=choices&-choices; i=t.bit_length()-1
            bk(R+(i,),P&good[i],X&good[i]); P &=~t; X |=t; choices &=~t
    bk((),(1<<k)-1,0)
    return found

def main():
    for n in range(2,11):
        actual=maxcliques_binary(n)
        M=max(map(len,actual))
        top={frozenset(s) for s in actual if len(s)==M}
        if n>=4:
            specified={frozenset(code(n,r,j)) for r in range(3,n) for j in [None]+list(range(4,n))}
            assert top==specified,(n,M,len(top),len(specified),top^specified)
            assert M==n and len(top)==(n-3)**2
        else:
            assert M==(n-1)
        print('EXHAUSTIVE',n,'max',M,'maximizers',len(top),'maximal independent sets',len(actual),flush=True)
    for n in list(range(11,40))+[40,64,100,200,512]:
        tests=[(r,j) for r in range(3,n) for j in [None]+list(range(4,n))] if n<=30 else [(3,None),(n-1,None),(n//2,min(n-1,max(4,n//2+1)))]
        for r,j in tests:
            C=code(n,r,j)
            assert len(C)==n
            assert is_valid(n,C),(n,r,j)
        print('CONSTRUCTION',n,'cases',len(tests),flush=True)
    print('VERIFY_OK')
if __name__=='__main__':main()
