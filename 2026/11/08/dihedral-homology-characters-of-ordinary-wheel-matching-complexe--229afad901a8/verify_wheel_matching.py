#!/usr/bin/env python3
"""Exact finite tests for dihedral characters of ordinary wheel matching complexes.
Only Python standard library is needed; full mathematical proof is given separately.
"""
from functools import lru_cache
from math import gcd

def P(m):
    assert m>=0
    x,y=1,0
    if m==0:return 1
    if m==1:return 0
    for i in range(2,m+1):x,y=y,y-x
    return y

def C(m):
    # I(C_m;-1)=2*cos(pi*m/3), extended to m=1,2 for quotient orbits.
    return (2,1,-1,-2,-1,1)[m%6]

def graph(n):
    return [tuple(sorted((i,(i+1)%n))) for i in range(n)]+[(i,n) for i in range(n)]

def edge_perm(n,a,flip):
    edges=graph(n);lookup={e:j for j,e in enumerate(edges)}
    def f(v):return n if v==n else ((a-v)%n if flip else (a+v)%n)
    return [lookup[tuple(sorted((f(u),f(v))))] for u,v in edges]

def face_list(n):
    edges=graph(n)
    masks=[]
    def walk(j, used, mask):
        if j==len(edges):masks.append(mask);return
        walk(j+1,used,mask)
        u,v=edges[j]
        if not ((used>>u)&1 or (used>>v)&1):walk(j+1, used|(1<<u)|(1<<v),mask|(1<<j))
    walk(0,0,0)
    return masks

def signed_fixed_faces(faces,p):
    s=0
    for mask in faces:
        sel=[i for i in range(len(p)) if (mask>>i)&1]
        act=[p[i] for i in sel]
        if sum(1<<i for i in act)!=mask:continue
        # parity of induced permutation on ordered vertices of the simplex
        inversions=sum(act[i]>act[j] for i in range(len(act)) for j in range(i+1,len(act)))
        s+=(-1)**(len(sel)+inversions)
    return s

def orbit_eval(n,a,flip):
    edges=graph(n);p=edge_perm(n,a,flip); seen=set();orbits=[]
    for i in range(2*n):
        if i in seen:continue
        orb=[];j=i
        while j not in seen:
            seen.add(j);orb.append(j);j=p[j]
        orbits.append(orb)
    masks=[]
    for orb in orbits:
        v=[z for j in orb for z in edges[j]]
        if len(v)==len(set(v)):masks.append(sum(1<<z for z in v))
    N=len(masks);conf=[]
    for i in range(N):conf.append(sum((1<<j) for j in range(N) if masks[i]&masks[j]))
    @lru_cache(None)
    def ind(S):
        if not S:return 1
        v=(S&-S).bit_length()-1
        return ind(S&~(1<<v))-ind(S&~conf[v])
    return ind((1<<N)-1)

def beta(n):return 2 if n%3==0 else n-1 if n%3==1 else n+1

def degree(n):return (n-1)//3

def predict_F(n,a,flip):
    if flip:
        return 0 if n%2 else -P(n//2-2)
    if a==0:return C(n)-n*P(n-2)
    return C(gcd(n,a))

def char_pred(n,a,flip):
    return (-1)**(degree(n)+1)*predict_F(n,a,flip)

def invariant_rank(n):
    return sum(char_pred(n,a,fl) for fl in (False,True) for a in range(n))//(2*n)

def run():
    count=0;faces_count=0
    for n in range(3,15):
        faces=face_list(n); faces_count+=len(faces)
        assert sum((-1)**(m.bit_count()) for m in faces)==predict_F(n,0,False)
        assert char_pred(n,0,False)==beta(n)
        for fl in (False,True):
            for a in range(n):
                perm=edge_perm(n,a,fl)
                assert sorted(perm)==list(range(2*n))
                x=signed_fixed_faces(faces,perm)
                y=orbit_eval(n,a,fl)
                z=predict_F(n,a,fl)
                assert x==y==z,(n,a,fl,x,y,z)
                count+=1
        if n<14:
            print(f'rim={n:02d} faces={len(faces):05d} beta={beta(n):02d} degree={degree(n)} invariants={invariant_rank(n)}')
    print(f'INDEPENDENT_SIGNED_LEFSCHETZ_AND_ORBIT_COUNT_PASS actions={count} total_face_lists={faces_count}')
    for n in range(3,205):
        assert char_pred(n,0,False)==beta(n)
        # odd/even reflection closed form
        for a in (0,1):
            r=char_pred(n,a,True)
            formula= 0 if n%2 or n%3==0 else (-1)**(n//2+1)
            assert r==formula,(n,r,formula)
        s=sum(char_pred(n,a,fl) for fl in (False,True) for a in range(n))
        assert s%(2*n)==0 and 0<=s//(2*n)<=beta(n)
        # formula by congruence class; check independent finite examples
        assert invariant_rank(n)==int(n%12 in (2,5,10,11)),(n,invariant_rank(n))
    print('PERIODIC_CHARACTER_AND_BURNSIDE_CHECK_PASS n=3..204')

if __name__=='__main__':run()
