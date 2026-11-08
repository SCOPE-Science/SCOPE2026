#!/usr/bin/env python3
"""Reproducible finite-field checks for fifth exterior algebra commutator fibers.
No dependencies beyond Python's standard library.  Characteristic is odd.
"""
from itertools import product, combinations
from collections import defaultdict
from math import prod

V2=list(combinations(range(5),2))
V3=list(combinations(range(5),3))
V4=list(combinations(range(5),4))

def wedge1_1(u,v,p):
    return tuple((u[i]*v[j]-u[j]*v[i])%p for i,j in V2)

def wedge1_3(u,v,p):
    ans=[]
    for I in V4:
        s=0
        for j,idx in enumerate(I):
            sub=I[:j]+I[j+1:]
            s+=(-1)**j*u[idx]*v[V3.index(sub)]
        ans.append(s%p)
    return tuple(ans)

def wedge1_4(u,b,p):
    return sum(((-1)**j)*u[j]*b[V4.index(tuple(i for i in range(5) if i!=j))] for j in range(5))%p

def rank(rows,p):
    if not rows:return 0
    M=[list(v) for v in rows]; r=0; cols=len(M[0])
    for c in range(cols):
        k=next((i for i in range(r,len(M)) if M[i][c]%p),None)
        if k is None:continue
        M[r],M[k]=M[k],M[r]
        inv=pow(M[r][c],-1,p)
        M[r]=[x*inv%p for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]%p:
                t=M[i][c]
                M[i]=[(a-t*b)%p for a,b in zip(M[i],M[r])]
        r+=1
        if r==len(M):break
    return r

def augmented_image(u,w,p):
    """Return column-span basis as five-coordinate row vectors from the literal wedge multiplication."""
    zero=[0]*10
    out=[]
    for side in range(2):
        for j in range(10):
            v=zero.copy();v[j]=1
            out.append(wedge1_3(u if side==0 else w,v,p))
    return out

def count_for_target(p,a,b):
    """Exhaustively enumerate 5-vector pairs, independently solve 3-form linear system."""
    vectors=list(product(range(p),repeat=5));n=0; fibers=0
    # Each pair (u,w) fixes degree-two output.  Degree-four coordinates are
    # produced by 20 independent degree-three input coordinates.
    span_cache={}; rank_hist=defaultdict(int)
    for u in vectors:
        for w in vectors:
            if wedge1_1(u,w,p)!=a:continue
            n+=1
            # Dependence class is computed by canonical projective representation:
            # image depends only on span(u,w) (verified below from literal matrices).
            if not any(u) and not any(w):
                key=('zero',)
            elif any(wedge1_1(u,w,p)):
                key=('plane',)  # rank five is checked directly using literal columns
            else:
                x=u if any(u) else w
                scale=pow(next(t for t in x if t),-1,p)
                key=tuple(t*scale%p for t in x)
            if key not in span_cache:
                # The 'plane' label merges all planes only because every such
                # wedge map has full rank; verify this fact on random planes below.
                M=augmented_image(u,w,p)
                rk=rank(M,p)
                in_image=rank(M+[b],p)==rk
                span_cache[key]=(rk,in_image)
            rk,ok=span_cache[key]
            rank_hist[rk]+=1
            if ok:fibers+=p**(20-rk)
    return n,fibers,dict(rank_hist)

def associative_wedge_product(a,b,p):
    """Literal 32 by 32 multiplication table in the five-generator algebra."""
    out=[0]*32
    for I,x in enumerate(a):
        if not x:continue
        for J,y in enumerate(b):
            if not y or (I&J):continue
            inv=sum(1 for i in range(5) for j in range(5)
                    if (I>>i)&1 and (J>>j)&1 and i>j)
            out[I|J]=(out[I|J]+x*y*(-1 if inv&1 else 1))%p
    return tuple(out)

def check_direct_products():
    import random
    for p in (3,5,7):
        r=random.Random(4200+p)
        for t in range(155):
            x=tuple(r.randrange(p) for _ in range(32))
            y=tuple(r.randrange(p) for _ in range(32))
            xy=associative_wedge_product(x,y,p)
            yx=associative_wedge_product(y,x,p)
            bracket=tuple((a-b)%p for a,b in zip(xy,yx))
            u=tuple(x[1<<i] for i in range(5))
            w=tuple(y[1<<i] for i in range(5))
            v=tuple(x[sum(1<<i for i in I)] for I in V3)
            vprime=tuple(y[sum(1<<i for i in I)] for I in V3)
            a=wedge1_1(u,w,p)
            # 3-form wedge 1-form is negative of 1-form wedge 3-form.
            b=tuple((aa-bb)%p for aa,bb in zip(wedge1_3(u,vprime,p),
                                                        wedge1_3(w,v,p)))
            expected=[0]*32
            for I,coef in zip(V2,a):expected[sum(1<<i for i in I)]=(2*coef)%p
            for I,coef in zip(V4,b):expected[sum(1<<i for i in I)]=(2*coef)%p
            assert bracket==tuple(expected),(p,t)
        print(f'literal 32-dimensional associative products: p={p}: 155 pairs PASS')

def run():
    check_direct_products()
    p=3;zero2=(0,)*10;zero4=(0,)*5
    e2=list(zero2);e2[V2.index((0,1))]=1; e2=tuple(e2)
    rank4=list(e2);rank4[V2.index((2,3))]=1;rank4=tuple(rank4)
    b1=(1,0,0,0,0);b2=(0,0,0,0,1);b3=(1,1,0,1,2)
    tests=[('zero',zero2,zero4),('zero-four',zero2,b1),('simple-zero',e2,zero4),('simple-four-a',e2,b1),('simple-four-b',e2,b2),('simple-four-c',e2,b3),('nonsimple',rank4,b1)]
    for name,a,b in tests:
        m,total,hist=count_for_target(p,a,b)
        if a==zero2:
            expected=p**20+(p**5-1)*(p+1)*p**16 if b==zero4 else (p**4-1)*(p+1)*p**16
        elif a==e2:expected=p**16*(p**2-1)
        else:expected=0
        assert total==expected,(name,total,expected)
        print(f'{name}: vector_pair_count={m}, core_fiber={total}, ranks={hist}, PASS')
    # Explicit direct matrix-rank tests for independently constructed wedge maps.
    for p in (3,5,7):
        for i in range(101):
            u=tuple((i*i+2*i*j+3*j*j+2)%p for j in range(5))
            w=tuple((i**3+4*i*j+j*j+3*j+1)%p for j in range(5))
            r=rank(augmented_image(u,w,p),p)
            d=rank([u,w],p)
            assert r=={0:0,1:4,2:5}[d],(p,i,d,r)
        print(f'finite-field rank verification: p={p}: 101 instances PASS')
    for q in (3,5,7,9):
        # symbolic total-fiber mass check, valid for any q, including extension fields
        d=(q**5-1)*(q**4-1)//(q**2-1)
        A=q**20+(q**5-1)*(q+1)*q**16
        B=(q**4-1)*(q+1)*q**16
        C=q**16*(q**2-1)
        assert A+(q**5-1)*B+d*q**5*C==q**30
        print(f'fiber-mass polynomial q={q}: PASS')
    print('ALL_FIFTH_EXTERIOR_COMMUTATOR_CHECKS_PASS')
if __name__=='__main__':run()
