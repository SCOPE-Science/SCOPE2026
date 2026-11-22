#!/usr/bin/env python3
"""Exact finite tests of mixed three-/four-edge multitheta independence collapses.

Usage: python check_theta.py.  Requires only Python 3 standard library.
The proof of the all-size result is mathematical; these are finite regression checks.
"""
from itertools import combinations
from math import comb

def data(m,q):
    assert m>=1 and q>=1
    u,v=0,1; edges=[]; four=[]; three=[]; k=2
    for _ in range(m):
        a,b,c=k,k+1,k+2; k+=3
        four.append((a,b,c)); edges += [(u,a),(a,b),(b,c),(c,v)]
    for _ in range(q):
        a,b=k,k+1; k+=2
        three.append((a,b));edges += [(u,a),(a,b),(b,v)]
    e=[(1<<a)|(1<<b) for a,b in edges]
    faces={mask for mask in range(1<<k) if all((mask&pair)!=pair for pair in e)}
    return k,faces,four,three

def collapse(F,low,high,n):
    assert low in F and high in F and (high&low)==low and (high.bit_count()==low.bit_count()+1)
    cnt=sum((low|1<<j) in F for j in range(n) if not(low>>j)&1)
    assert cnt==1,("not free",low,high,cnt)
    F.remove(low);F.remove(high)

def verify_collapse(m,q):
    n,F,fo,tr=data(m,q)
    original=len(F)
    u,v=0,1; both=3; mid=(1<<fo[0][1]); bp=1<<tr[0][1];ap=1<<tr[0][0]
    groups=[]
    # First remove every face containing both poles (using the middle of first long arm).
    lows=[x for x in F if x&both==both and not x&mid]
    for x in sorted(lows,key=lambda x:(-x.bit_count(),x)):
        collapse(F,x,x|mid,n)
    groups.append(len(lows))
    # Each selected pole is a cone along a short-arm vertex.
    for pole,piv in ((1,bp),(2,ap)):
        lows=[x for x in F if x&pole and not x&piv]
        for x in sorted(lows,key=lambda x:(-x.bit_count(),x)):
            collapse(F,x,x|piv,n)
        groups.append(len(lows))
    assert all(not (x&3) for x in F)
    # Delete a leaf from each long-arm P3 independence complex.
    for a,b,c in fo:
        bit_a=1<<a; bit_c=1<<c
        lows=[x for x in F if (x&bit_a) and not (x&bit_c)]
        for x in sorted(lows,key=lambda x:(-x.bit_count(),x)):
            collapse(F,x,x|bit_c,n)
        groups.append(len(lows))
    assert len(F)==3**(m+q)
    survivors=[(b,c) for a,b,c in fo]+tr
    expected={0}
    for x,y in survivors:
        expected={s|a for s in expected for a in (0,1<<x,1<<y)}
    assert F==expected
    assert groups==[2**(m-1),3**m*2**(q-1),3**m*2**(q-1)]+[3**q*3**i*5**(m-1-i) for i in range(m)],groups
    assert original==3**(m+q)+2*sum(groups)
    return n,original,groups

def levi(m,q,act):
    n,F,fo,tr=data(m,q)
    p=list(range(n))
    if act=='pole':
        p[0],p[1]=1,0
        for a,b,c in fo: p[a],p[c]=c,a
        for a,b in tr: p[a],p[b]=b,a
        expected=(-1)**q
    elif act=='long':
        assert m>=2
        for x,y in zip(fo[0],fo[1]):p[x],p[y]=y,x
        expected=-1
    elif act=='short':
        assert q>=2
        for x,y in zip(tr[0],tr[1]):p[x],p[y]=y,x
        expected=-1
    else: raise ValueError(act)
    assert sorted(p)==list(range(n))
    L=-1  # reduced empty-face contribution
    for face in F:
        if not face: continue
        idx=[i for i in range(n) if face>>i&1]
        mapped=[p[i] for i in idx]
        if set(mapped)!=set(idx):continue
        inv=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
        L+=(-1)**(len(idx)-1+inv)
    degree=(-1)**(m+q-1)*L
    assert degree==expected,(m,q,act,degree,expected)
    return degree

def main():
    tested=0; pairs=0; acts=0
    for m in range(1,4):
        for q in range(1,4):
            n,faces,groups=verify_collapse(m,q)
            tested+=1;pairs+=sum(groups)
            sym=['pole']+( ['long'] if m>=2 else [])+(['short'] if q>=2 else [])
            for action in sym:levi(m,q,action);acts+=1
            print('m=%d q=%d vertices=%d faces=%d collapses=%d symmetry_generators=%s OK'%(m,q,n,faces,sum(groups),','.join(sym)))
    print('PASS: %d complete simplicial collapses, %d elementary pairs, %d exact reduced Lefschetz checks'%(tested,pairs,acts))
if __name__=='__main__':main()
