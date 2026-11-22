"""Finite independent deletion-deck tests for Dyck reconstruction graphs."""
from itertools import product

def dyck(n, cap=None):
    def rec(w,h,o,c):
        if o==n and c==n:
            yield w
        if o<n and (cap is None or h<cap):
            yield from rec(w+'1',h+1,o+1,c)
        if c<n and h>0:
            yield from rec(w+'0',h-1,o,c+1)
    yield from rec('',0,0,0)

def deck(w):
    return {w[:i]+w[i+1:] for i in range(len(w))}

def encoding(b):
    return '1'+''.join('01' if c=='1' else '10' for c in b)+'0'

def runflip(a,b):
    d=[j for j,(x,y) in enumerate(zip(a,b)) if x!=y]
    return bool(d) and d==list(range(d[0],d[-1]+1)) and len(set(a[d[0]:d[-1]+1]))==1

def pos_sum(w):
    return sum(i+1 for i,c in enumerate(w) if c=='1')

for n in range(1,9):
    d=list(dyck(n,2)); all_d=list(dyck(n)); m=n-1
    assert len(d)==2**m
    assert set(d)=={encoding(''.join(p)) for p in product('01',repeat=m)}
    dk={w:deck(w) for w in all_d}; edges=0
    for i,x in enumerate(d):
        for y in d[i+1:]:
            adjacent=len(dk[x]&dk[y])>=2
            b=lambda w:''.join('1' if w[2*j+1:2*j+3]=='01' else '0' for j in range(n-1))
            assert adjacent==runflip(b(x),b(y)),(n,x,y)
            if adjacent:
                edges+=1
                assert (pos_sum(x)-pos_sum(y))%n != 0
    assert edges==(n-2)*(2**(n-1))+1
    for i,x in enumerate(all_d):
        for y in all_d[i+1:]:
            if len(dk[x]&dk[y])>=2:
                assert (pos_sum(x)-pos_sum(y))%n!=0,(n,x,y)
    print('n=%d height2=%d edges=%d all_Dyck=%d OK'%(n,len(d),edges,len(all_d)))
