"""Finite-field incidence and matrix-product tests for the theorem.
Requires Python 3 and NumPy. Run: python checker.py
"""
import itertools
import numpy as np

def bracket(q,j):
    return (q**j-1)//(q-1)

def mul(a,b,q):
    if q != 4:
        return (a*b)%q
    result=0
    while b:
        if b&1: result ^= a
        b >>= 1
        a <<= 1
        if a&4: a ^= 7  # x^2+x+1
    return result

def inv(a,q):
    return next(b for b in range(1,q) if mul(a,b,q)==1)

def add(a,b,q):
    return (a^b) if q==4 else ((a+b)%q)

def dot(u,v,q):
    out=0
    for a,b in zip(u,v):out=add(out,mul(a,b,q),q)
    return out

def points(n,q):
    seen=set();out=[]
    for u in itertools.product(range(q),repeat=n):
        if not any(u):continue
        lead=next(x for x in u if x)
        v=tuple(mul(x,inv(lead,q),q) for x in u)
        if v not in seen:seen.add(v);out.append(v)
    return out

def expected(q,n):
    v=bracket(q,n);t=bracket(q,n-1);s=bracket(q,n-2)
    F=v*t;Q=q**(n-3);k=t+(t-1)*s
    aa=q*q*bracket(q,n-3)*v//(q+1)
    bb=q**3*bracket(q,n-2)*t//(q+1)
    assert (q*q*bracket(q,n-3)*v)%(q+1)==0
    assert (q**3*bracket(q,n-2)*t)%(q+1)==0
    assert 1+2*(v-1)+aa+bb==F
    return k,[k,q**(n-2)+s*q**((n-2)/2),q**(n-2)-s*q**((n-2)/2),q**(n-2),-Q],[1,v-1,v-1,aa,bb]

def run(q,n):
    P=points(n,q);v=len(P)
    incidence=np.array([[dot(p,h,q)==0 for h in P] for p in P],dtype=np.int32)
    e=np.argwhere(incidence)
    a=e[:,0];b=e[:,1]
    cross=incidence[a[:,None],b[None,:]]
    B=(cross*cross.T).astype(np.int64)
    F=len(e);Q=q**(n-3);s=bracket(q,n-2);t=bracket(q,n-1);h3=bracket(q,n-3)
    k,values,mults=expected(q,n)
    assert B.shape==(v*t,v*t)
    assert np.all(B.sum(axis=1)==k)
    L=B@B-(q-1)*Q*B-q*Q**2*np.eye(F,dtype=np.int64)
    R=s*h3*np.ones((F,F),dtype=np.int64)+Q*(cross+cross.T) + (s-1)*Q*(a[:,None]==a[None,:]) +(t-s)*h3*(b[:,None]==b[None,:])
    assert np.array_equal(L,R),('operator-identity',q,n)
    eig=np.linalg.eigvalsh(B.astype(float))
    predicted=np.sort(np.concatenate([np.full(cnt,val) for val,cnt in zip(values,mults)]))
    err=np.max(np.abs(eig-predicted))
    assert err<1e-7,(q,n,err)
    # For smaller cases, evaluate the rank-one matrix products directly.
    if q<=3 and n==3:
        vectors=P
        for i,(pidx,hidx) in enumerate(e):
            p=vectors[pidx];h=vectors[hidx]
            assert dot(p,h,q)==0
            for j,(p2idx,h2idx) in enumerate(e):
                u=vectors[p2idx];w=vectors[h2idx]
                A=np.array([[mul(x,y,q) for y in h] for x in p],dtype=int)
                C=np.array([[mul(x,y,q) for y in w] for x in u],dtype=int)
                if q==4:raise AssertionError('direct matrix only prime fields')
                commutes=np.array_equal((A@C)%q,(C@A)%q)
                assert commutes==bool(B[i,j]),(q,n,i,j)
    print(f'q={q},n={n},flags={F},degree_plus_loop={k},max_eigen_error={err:.2g},identity=PASS,direct_products={"PASS" if q<=3 and n==3 else "not_run"}')

if __name__=='__main__':
    for q,n in [(2,3),(3,3),(4,3),(2,4),(3,4),(2,5)]:run(q,n)
    print('ALL CHECKS PASS')
