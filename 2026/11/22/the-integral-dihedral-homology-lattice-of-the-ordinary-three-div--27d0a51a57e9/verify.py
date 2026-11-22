#!/usr/bin/env python3
"""Finite chain checks for the integral cycle-symmetry theorem.
Run with Python 3, standard library only. Mathematical proof covers all parameters.
"""
from itertools import combinations, product
from math import gcd

def independent(vertices,n):
    v=set(vertices)
    return all(((a+1)%n) not in v for a in v)

def cross_cycle(k,j):
    n=3*k
    pairs=[((3*t+j)%n,(3*t+j+1)%n) for t in range(k)]
    chain={}
    for bits in product((0,1),repeat=k):
        v=[pairs[t][bits[t]] for t in range(k)]
        assert independent(v,n)
        sign=(-1)**sum(bits)
        sign*=(-1)**sum(v[i]>v[h] for i in range(k) for h in range(i+1,k))
        v=tuple(sorted(v))
        chain[v]=chain.get(v,0)+sign
    return {v:c for v,c in chain.items() if c}

def act(z,p):
    out={}
    for v,c in z.items():
        w=[p[a] for a in v]
        s=(-1)**sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))
        w=tuple(sorted(w))
        out[w]=out.get(w,0)+c*s
    return {v:c for v,c in out.items() if c}

def boundary(z):
    out={}
    for v,c in z.items():
        for i in range(len(v)):
            w=v[:i]+v[i+1:]
            out[w]=out.get(w,0)+(-1)**i*c
    return {w:c for w,c in out.items() if c}

def scale(z,s):
    return {v:s*c for v,c in z.items() if c*s}

def faces(n,m):
    return [v for v in combinations(range(n),m) if independent(v,n)]

def rank_mod_p(cols,p):
    piv={}
    for col in cols:
        a={i:v%p for i,v in col.items() if v%p}
        while a:
            i=min(a);c=a[i]
            if i not in piv:
                inv=pow(c,-1,p)
                piv[i]={j:(v*inv)%p for j,v in a.items()}
                break
            for j,v in piv[i].items():
                w=(a.get(j,0)-c*v)%p
                if w:a[j]=w
                else:a.pop(j,None)
    return len(piv)

def rank_boundary(n,m,p):
    # Differential from (m-1)-simplices (m-element subsets)
    low={v:i for i,v in enumerate(faces(n,m-1))} if m>1 else {():0}
    cols=[]
    for face in faces(n,m):
        col={}
        for i in range(m):
            v=face[:i]+face[i+1:]
            col[low[v]]=col.get(low[v],0)+(-1)**i
        cols.append(col)
    return rank_mod_p(cols,p)

def main():
    for k in range(1,8):
        n=3*k;s=(-1)**(k-1);h=(-1)**(k*(k+1)//2)
        a,b,c=[cross_cycle(k,j) for j in range(3)]
        assert not boundary(a) and not boundary(b) and not boundary(c)
        r=[(i+1)%n for i in range(n)]
        t=[(-i)%n for i in range(n)]
        assert act(a,r)==b and act(b,r)==c and act(c,r)==scale(a,s)
        assert act(a,t)==scale(c,h) and act(b,t)==scale(b,h) and act(c,t)==scale(a,h)
        f0=tuple(range(0,n,3));f1=tuple(range(1,n,3))
        for f in (f0,f1):
            assert independent(f,n)
            assert all(not independent(f+(i,),n) for i in range(n) if i not in f)
        assert [z.get(f0,0) for z in (a,b,c)]==[1,0,-1]
        assert [z.get(f1,0) for z in (a,b,c)]==[(-1)**k,1,0]
        rot=((0,-1),(1,(-1)**k))
        ref=((-h,0),(h*(-1)**k,h))
        def mul(A,B):return tuple(tuple(sum(A[i][t]*B[t][j] for t in (0,1)) for j in (0,1)) for i in (0,1))
        def power(A,e):
            v=((1,0),(0,1))
            for _ in range(e):v=mul(v,A)
            return v
        assert power(rot,3)==((s,0),(0,s))
        assert power(rot,n)==((1,0),(0,1))
        assert power(ref,2)==((1,0),(0,1))
        assert mul(mul(ref,rot),ref)==power(rot,n-1)
        det_coin=(rot[0][0]-1)*(rot[1][1]-1)-rot[0][1]*rot[1][0]
        assert det_coin==(3 if k%2 else 1)
        # In rank two, the gcd of all 2x2 minors of [R-I | S-I]
        # is the order of the full-dihedral coinvariant quotient.
        full_cols=[(rot[0][j]-(j==0),rot[1][j]-(j==1)) for j in range(2)]
        full_cols += [(ref[0][j]-(j==0),ref[1][j]-(j==1)) for j in range(2)]
        coin_order=0
        for i in range(4):
            for j in range(i+1,4):
                coin_order=gcd(coin_order,abs(full_cols[i][0]*full_cols[j][1]-full_cols[i][1]*full_cols[j][0]))
        assert coin_order==(3 if k%4==3 else 1)
        print('cycle',n,'sparse terms',len(a),'rotation coinvariant order',det_coin,'full-dihedral coinvariant order',coin_order,'PASS')
    for k in range(1,6):
        n=3*k
        for p in (2,3,5):
            # For n=3, use augmented reduced chain in degree zero
            d=rank_boundary(n,k,p)
            u=rank_boundary(n,k+1,p)
            beta=len(faces(n,k))-d-u
            assert beta==2,(n,p,beta)
            print('modular reduced homology',n,'prime',p,'degree',k-1,'betti',beta)
    print('CYCLE_DIHEDRAL_INTEGRAL_LATTICE_VERIFIED')

if __name__=='__main__': main()
