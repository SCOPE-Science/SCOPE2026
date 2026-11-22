#!/usr/bin/env python3
"""Exact pointwise image verification in small finite fields; no external packages."""
from itertools import product

def run(q):
    assert q in (2,3,4)
    def add(a,b): return (a^b) if q==4 else (a+b)%q
    def sub(a,b): return (a^b) if q==4 else (a-b)%q
    def mul(a,b):
        if q!=4:return (a*b)%q
        aa=(a&1)*(b&1); ab=(a&1)*((b>>1)&1)^((a>>1)&1)*(b&1)
        bb=((a>>1)&1)*((b>>1)&1)
        return (aa^bb)|((ab^bb)<<1)
    def det(M): return sub(mul(M[0],M[3]),mul(M[1],M[2]))
    matrices=list(product(range(q),repeat=4))
    # compact encodings, and bitwise/field addition need decoded tuples
    enc={m:i for i,m in enumerate(matrices)}
    def madd(A,B):return tuple(add(a,b) for a,b in zip(A,B))
    rank1=[a for a in matrices if det(a)==0]
    image=set()
    for C in rank1:
        trans=[enc[madd(C,A)] for A in rank1]
        image.update((x,y) for x in trans for y in trans)
    missing={(i,j) for i in range(len(matrices)) for j in range(len(matrices))}-image
    expected=set()
    for i,X in enumerate(matrices):
        if det(X)==0:continue
        for lam in range(2,q): # q4 labels 2,3 = nontrivial GF4
            if lam in (0,1):continue
            expected.add((i,enc[tuple(mul(lam,x) for x in X)]))
    gl=(q*q-1)*(q*q-q)
    assert len(missing)==(q-2)*gl,(q,len(missing),gl)
    assert missing==expected,(q,len(missing^expected))
    print(f'GF({q}): |image|={len(image)}, |missing|={len(missing)}, (q-2)|GL2|={(q-2)*gl}, exact subset equality PASS')

if __name__=='__main__':
    for q in (2,3,4):run(q)
