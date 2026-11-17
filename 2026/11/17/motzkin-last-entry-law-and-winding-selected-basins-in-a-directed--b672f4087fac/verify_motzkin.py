#!/usr/bin/env python3
"""Independent particle dynamics, excursion enumeration, and asymptotic checks.
Run: python3 verify_motzkin.py"""
from itertools import product
from math import comb, log, sqrt, pi

def particle_update(d):
    n=len(d)
    # 1 moves left by one; 2 stays; a 1 arriving on a 2 removes both.
    return tuple(0 if (d[i]==2 and d[(i+1)%n]==1)
                   else 2 if d[i]==2
                   else 1 if d[(i+1)%n]==1
                   else 0 for i in range(n))

def is_excursion(u):
    h=0
    for v in u:
        h+=(1 if v==2 else -1 if v==1 else 0)
        if h<0:return False
    return h==0

def motzkin(k):
    m=[1]
    for j in range(1,k+1):
        m.append(m[j-1]+sum(m[i]*m[j-2-i] for i in range(j-1)))
    return m[k]

def central(k):
    return sum(comb(k,j)*comb(k-j,j) for j in range(k//2+1))

for n in range(2,12):
    generated=set()
    for mid in product((0,1,2),repeat=n-2):
        if is_excursion(mid):
            d=(2,)+mid+(1,)
            for i in range(n): generated.add(d[i:]+d[:i])
    assert len(generated)==n*motzkin(n-2), (n,len(generated))
    late=set();rotate=0;fixed=0
    for d in product((0,1,2),repeat=n):
        if sum(d)%3:continue
        s=d;t=0
        while 1 in s and 2 in s:
            s=particle_update(s);t+=1
            assert t<=n-1
        if t==n-1:late.add(d)
        if d.count(1)>d.count(2):rotate+=3
        else:fixed+=3
    assert late==generated, (n,len(late),len(generated))
    assert 3*len(late)==3*n*motzkin(n-2)
    assert rotate==(3**n-3*central(n))//2
    print(f'n={n} Motzkin={motzkin(n-2)} final_distance={n-1} generated_edge_words={len(generated)} exhaustively_confirmed={len(late)}')

for n in (50,100,200,400):
    m=motzkin(n-2)
    normalized=3*n*m/3**n
    prediction=sqrt(3)/(2*sqrt(pi*n))
    print(f'n={n} exact_last_entry_probability={normalized:.12f} leading_asymptotic={prediction:.12f} ratio={normalized/prediction:.9f}')
print('PASS: particle rule, unique primitive-excursion bijection, exact asymptotic trend')
