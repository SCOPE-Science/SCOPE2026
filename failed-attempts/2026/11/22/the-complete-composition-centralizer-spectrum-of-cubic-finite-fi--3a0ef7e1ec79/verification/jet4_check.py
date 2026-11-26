#!/usr/bin/env python3
"""Reproducible finite-field check of three-jet composition centralizers.
Only ordinary algebra and finite-field arithmetic are used.
"""
from collections import Counter
from itertools import product

FIELDS = [(2,1,None),(3,1,None),(5,1,None),(7,1,None),
          (2,2,(1,1,1)),(2,3,(1,1,0,1)),(3,2,(1,0,1))]

def field_tables(p, d, modulus):
    q = p**d
    digs = [tuple((i // (p**j)) % p for j in range(d)) for i in range(q)]
    to_int = {v:i for i,v in enumerate(digs)}
    add = [[to_int[tuple((u[j]+v[j])%p for j in range(d))]
            for v in digs] for u in digs]
    mul = [[0]*q for _ in range(q)]
    for i,a in enumerate(digs):
        for j,b in enumerate(digs):
            z = [0]*(2*d-1)
            for k,x in enumerate(a):
                for l,y in enumerate(b): z[k+l] = (z[k+l]+x*y)%p
            if d>1:
                for k in range(2*d-2,d-1,-1):
                    c=z[k]
                    for l in range(d): z[k-d+l]=(z[k-d+l]-c*modulus[l])%p
            mul[i][j]=to_int[tuple(z[:d])]
    return add,mul

def predicted(q,p):
    ans=Counter()
    if p==2:
        for sz,n in ((q,(q-2)*q*q),(2*q*q,2*(q*q-1)),(q**3,2)):
            ans[sz]+=n
    else:
        for sz,n in ((q,(q-3)*q*q),(3*q,q*q-q),(q*q,q),
                     (q*q+q,2*q*(q-1)),(3*q*q,2*(q-1)),(q**3,2)):
            ans[sz]+=n
    return ans

def check_one(p,d,mod):
    q=p**d
    add,mul=field_tables(p,d,mod)
    ts=list(product(range(q),repeat=3))
    sums=[]
    for a,b,c in ts:
        total=0
        aa2=mul[a][a]; aa3=mul[aa2][a]
        for u,v,w in ts:
            u2=mul[u][u]; u3=mul[u2][u]
            left2=add[mul[a][v]][mul[b][u2]]
            right2=add[mul[u][b]][mul[v][aa2]]
            if left2!=right2: continue
            left3=add[add[mul[a][w]][mul[2%p][mul[b][mul[u][v]]]]][mul[c][u3]]
            right3=add[add[mul[u][c]][mul[2%p][mul[v][mul[a][b]]]]][mul[w][aa3]]
            if left3==right3: total+=1
        sums.append(total)
    actual=Counter(sums)
    expect=predicted(q,p)
    expect=Counter({s:n for s,n in expect.items() if n})
    assert actual==expect, (q,actual,expect)
    pair_total=sum(sums)
    expected_pairs=5*q**4-4*q*q if p==2 else 3*q**4+9*q**3-11*q*q
    assert pair_total==expected_pairs,(q,pair_total,expected_pairs)
    assert sum(actual.values())==q**3
    print('FIELD',q,'CHAR',p,'CENTRALIZER_SPECTRUM',sorted(actual.items()),'COMMUTING_PAIRS',pair_total,'OK')

if __name__=='__main__':
    for p,d,mod in FIELDS: check_one(p,d,mod)
    print('JET4_FULL_CENTRALIZER_CENSUS_VERIFIED')
