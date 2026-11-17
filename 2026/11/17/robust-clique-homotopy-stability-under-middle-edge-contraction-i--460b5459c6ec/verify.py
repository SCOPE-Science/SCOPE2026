#!/usr/bin/env python3
"""Finite independent checks for robust-clique petal contraction and sphere counts."""
from collections import Counter
from math import comb


def independence_number(mask, adj):
    cache = {0: 0}
    def rec(s):
        if s not in cache:
            t = s & -s
            v = t.bit_length() - 1
            cache[s] = max(rec(s ^ t), 1 + rec(s & ~t & ~adj[v]))
        return cache[s]
    return rec(mask)


def graph(m, kind):
    d = 4 if kind == 'pentagon' else 3
    adj = [0] * (1 + m*d)
    def edge(a,b):
        adj[a] |= 1<<b
        adj[b] |= 1<<a
    for i in range(m):
        a = 1 + i*d
        if d == 4:
            for u,v in ((0,a),(a,a+1),(a+1,a+2),(a+2,a+3),(a+3,0)):
                edge(u,v)
        else:
            for u,v in ((0,a),(a,a+1),(a+1,a+2),(a+2,0)):
                edge(u,v)
    return adj


def cliq(m,k,kind):
    adj = graph(m,kind)
    n = len(adj)
    # Test every induced vertex subset independently of any petal formulas.
    return [s for s in range(1,1<<n) if independence_number(s,adj) < k]


def contraction(s,m):
    t = s&1
    for i in range(m):
        x = (s >> (1+4*i))&15
        y = (x&1) | (2 if x&6 else 0) | (4 if x&8 else 0)
        t |= y << (1+3*i)
    return t


def face_betti(faces):
    groups = {}
    for s in faces:
        groups.setdefault(s.bit_count()-1,[]).append(s)
    ranks = {}
    for d in sorted(groups,reverse=True):
        if d == 0:continue
        rows={s:j for j,s in enumerate(groups[d-1])}
        piv={}
        for x in groups[d]:
            v=0
            bits=x
            while bits:
                b=bits&-bits
                bits ^= b
                v ^= 1<<rows[x^b]
            while v:
                j=v.bit_length()-1
                if j in piv:v ^= piv[j]
                else:
                    piv[j]=v
                    break
        ranks[d]=len(piv)
    betti={d:len(group)-ranks.get(d,0)-ranks.get(d+1,0) for d,group in groups.items()}
    betti[0]-=1
    return {d:v for d,v in betti.items() if v}


def local_states(kind):
    adj=graph(1,kind)
    d=len(adj)-1
    middle=(0b0110 if d==4 else 0b0010)
    out={}
    for p in (0,1,2):
        for q in (0,1):
            fs=set()
            for s in range(1<<d):
                actual=s<<1
                if independence_number(actual,adj)<=p and independence_number((s&middle)<<1,adj)<=q:
                    fs.add(s)
            out[(p,q)]=fs
    return out


def verify():
    L=local_states('pentagon')
    Q=local_states('square')
    for p in (0,1,2):
        for q in (0,1):
            src=L[p,q]
            dst=Q[p,q]
            images={(s&1)|(2 if s&6 else 0)|(4 if s&8 else 0) for s in src}
            assert images==dst,(p,q,images,dst)
            print('LOCAL',p,q,'five_faces',len(src),'four_faces',len(dst))
    for m in range(1,5):
        for k in range(2,6):
            f5=cliq(m,k,'pentagon')
            f4=cliq(m,k,'square')
            target=set(f4)
            assert all(contraction(s,m) in target for s in f5)
            # Every quadrilateral face is hit by the simplicial contraction.
            assert {contraction(s,m) for s in f5} == target
            predicted={} if m<k-1 else {2*k-3:comb(m,k-1)}
            beta5=face_betti(f5)
            beta4=face_betti(f4)
            assert beta5==predicted,(m,k,beta5,predicted)
            assert beta4==predicted,(m,k,beta4,predicted)
            print('GLOBAL',m,k,'pentagon_faces',len(f5),'square_faces',len(f4),'betti',beta5)
    print('ALL_PETAL_CONTRACTION_CHECKS_PASS')
if __name__=='__main__':verify()
