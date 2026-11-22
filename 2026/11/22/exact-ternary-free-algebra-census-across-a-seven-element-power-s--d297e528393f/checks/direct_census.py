#!/usr/bin/env python3
"""Independent direct finite-algebra evaluation of three-generator free ai-semirings."""
from itertools import product

def terms(n):
    return [(h, 1<<h,False) for h in range(n)]+[(h,C,True) for h in range(n) for C in range(1,1<<n) if C>>h&1]

def word_bits(n,kind):
    t=terms(n); a={'U':list(range(8)),'A':list(range(1,8)),'N':list(range(4)),'L':list(range(4)),'D':[0,1]}[kind]
    size={'U':3,'A':3,'N':2,'L':2,'D':1}[kind]
    result=[0]*len(t)
    for idx,values in enumerate(product(a,repeat=n)):
        for j,(h,C,lg) in enumerate(t):
            if not lg:
                out=values[h]
            elif not all(values[v] for v in range(n) if C>>v&1):
                out=0
            elif kind in ('U','A'):
                x=values[h];out=((x&1)|((x&4)>>2))| (x&2)
            elif kind=='N':out=1
            elif kind=='L':out=values[h]
            else:out=1
            for s in range(size):
                if out>>s&1:result[j]|=1<<(size*idx+s)
    return result

def dsu_count(pairs):
    # pairs entries (betaSig, etaSig)
    d=list(range(len(pairs)))
    def root(x):
        while d[x]!=x:d[x]=d[d[x]];x=d[x]
        return x
    def union(x,y):
        x=root(x);y=root(y)
        if x!=y:d[x]=y
    for k in (0,1):
        first={}
        for idx,p in enumerate(pairs):
            s=p[k]
            if s in first:union(idx,first[s])
            else:first[s]=idx
    return len(set(root(i) for i in range(len(pairs))))

def calculate(n):
    w={k:word_bits(n,k) for k in ('U','A','N','L','D')}
    classes={'U':set(),'A':set(),'beta':set(),'eta':set(),'gamma':set(),'alpha':set()}
    representatives={}; u_pairs=[]
    T=len(terms(n))
    for p in range(1,1<<T):
        w_sig={k:0 for k in w}
        for i in range(T):
            if p>>i&1:
                for k in w:w_sig[k]|=w[k][i]
        sig=tuple(w_sig[k] for k in ('U','A','N','L','D'))
        keys={'U':sig[0], 'A':sig[1], 'beta':(sig[1],sig[2]), 'eta':(sig[1],sig[3]),'gamma':(sig[1],sig[4]),'alpha':(sig[1],sig[2],sig[3])}
        for k,v in keys.items():classes[k].add(v)
        if sig not in representatives:
            representatives[sig]=len(u_pairs);u_pairs.append((keys['beta'],keys['eta']))
    ret={k:len(v) for k,v in classes.items()}
    ret['delta']=dsu_count(u_pairs)
    return ret

if __name__=='__main__':
    for n in (1,2,3):print(n,calculate(n))
    assert calculate(3)=={'U':1727,'A':63,'beta':583,'eta':511,'gamma':188,'alpha':1065,'delta':239}
    print('VERIFY_OK')
