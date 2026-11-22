#!/usr/bin/env python3
"""Exact checks for rank-two algebra retractions of square-zero-variable rings.
All arithmetic uses prime fields; no external modules or files needed.
"""
from itertools import product
from math import comb


def ring(d,q):
    L=1<<d
    Z=(0,)*L
    def mul(a,b):
        c=[0]*L
        for i,ai in enumerate(a):
            if not ai: continue
            for j,bj in enumerate(b):
                if bj and not i&j:
                    c[i|j]=(c[i|j]+ai*bj)%q
        return tuple(c)
    def ev(poly, imgs):
        out=[0]*L
        for m,a in enumerate(poly):
            if not a: continue
            v=[0]*L; v[0]=a; v=tuple(v)
            for i in range(d):
                if m&(1<<i): v=mul(v,imgs[i])
            out=[(x+y)%q for x,y in zip(out,v)]
        return tuple(out)
    def x(i):
        v=[0]*L;v[1<<i]=1;return tuple(v)
    return L,Z,mul,ev,x


def rank(vecs,q):
    if not vecs: return 0
    a=[list(v) for v in vecs];rows=len(a); cols=len(a[0]); r=0
    for c in range(cols):
        i=next((i for i in range(r,rows) if a[i][c]),None)
        if i is None: continue
        a[r],a[i]=a[i],a[r]
        inv=pow(a[r][c],-1,q)
        a[r]=[(t*inv)%q for t in a[r]]
        for j in range(rows):
            if j!=r and a[j][c]:
                t=a[j][c]; a[j]=[(b-t*v)%q for b,v in zip(a[j],a[r])]
        r+=1
        if r==rows:break
    return r


def image_rank(imgs,d,q,ev):
    L=1<<d; monos=[]
    for m in range(L):
        p=[0]*L;p[m]=1;monos.append(ev(tuple(p),imgs))
    return rank(monos,q)


def param_family(d,q):
    L,Z,mul,ev,x=ring(d,q)
    ans=[]
    for i in range(d):
        excluded=[j for j in range(d) if j!=i]
        upper=[m for m in range(1,L) if not (m&(1<<i))]
        for a in product(range(q),repeat=len(upper)):
            z=list(x(i))
            for m,c in zip(upper,a):
                if c:
                    p=[0]*L;p[m|(1<<i)]=c
                    z=[(h+k)%q for h,k in zip(z,p)]
            z=tuple(z)
            assert mul(z,z)==Z
            for vfree in product(range(q),repeat=d-1):
                v=[0]*d;v[i]=1
                for j,c in zip(excluded,vfree):v[j]=c
                imgs=tuple(tuple((c*a)%q for a in z) for c in v)
                ans.append((i,z,tuple(v),imgs))
    return ans


def test_param(d,q):
    L,Z,mul,ev,x=ring(d,q)
    es=param_family(d,q)
    B=(1<<(d-1))+d-2
    C=(1<<(d-1))-1
    assert len(es)==d*q**B
    assert len({e[3] for e in es})==len(es)
    assert len({(i,z) for i,z,v,imgs in es})==d*q**C
    degree_hist={}
    orbit_hist={}
    for i,z,v,imgs in es:
        assert all(ev(img,imgs)==img for img in imgs)
        assert image_rank(imgs,d,q,ev)==2
        # Nonlinear linearization: theta maps x_i to z, others to themselves.
        theta=tuple(z if j==i else x(j) for j in range(d))
        normal=tuple(tuple(c*a%q for a in x(i)) for c in v)
        assert all(ev(theta[j],imgs)==ev(normal[j],theta) for j in range(d))
        support=sum(v[j]!=0 for j in range(d) if j!=i)
        deg=(d-1-support)*q**(B-1)
        degree_hist[deg]=degree_hist.get(deg,0)+1
        orbit_hist[support]=orbit_hist.get(support,0)+1
    for s in range(d):
        assert orbit_hist[s]==d*comb(d-1,s)*(q-1)**s*q**C
        assert degree_hist[(d-1-s)*q**(B-1)]==orbit_hist[s]
    # Check the commutation criterion against actual full algebra compositions.
    if d==2:
        pairs=product(es,repeat=2)
    else:
        # Exhaust all ordered pairs at q=3,d=3 (531,441 pairs).
        pairs=product(es,repeat=2)
    count=0
    for (i,z,v,imgs),(j,t,w,jmgs) in pairs:
        # Apply each map to the other image generator using exact coefficients.
        # e(f(x_k)) = w_k e(t), f(e(x_k)) = v_k f(z).
        ez=ev(t,imgs); ft=ev(z,jmgs)
        ok=all(tuple(c*a%q for a in ez)==tuple(b*a%q for a in ft)
               for c,b in zip(w,v))
        expected=(i==j and z==t and v==w) or (i!=j and v[j]==0 and w[i]==0)
        assert ok==expected, (d,q,i,j,v,w,z,t)
        count+=ok
    expected_total=d*q**B+d*(d-1)*q**(2*B-2)
    assert count==expected_total
    print('PARAM',d,q,'count',len(es),'orbit_sizes',[orbit_hist[s] for s in range(d)],
          'degrees',sorted(degree_hist.items()),'ordered_commuting',count)


def test_full_2(q):
    d=2;L,Z,mul,ev,x=ring(d,q)
    sq=[]
    for a in product(range(q),repeat=L-1):
        w=(0,)+a
        if mul(w,w)==Z:sq.append(w)
    candidates=[]
    for A in product(sq,repeat=d):
        if all(ev(A[j],A)==A[j] for j in range(d)):
            candidates.append((A,image_rank(A,d,q,ev)))
    rank2={a for a,r in candidates if r==2}
    predicted={e[3] for e in param_family(d,q)}
    assert rank2==predicted
    print('FULL2',q,'squarezero_elements',len(sq),'all_idempotent_maps',len(candidates),
          'rank2',len(rank2),'other_ranks',sorted(set(r for a,r in candidates)))

if __name__=='__main__':
    test_full_2(3)
    test_full_2(5)
    test_param(2,3)
    test_param(2,5)
    test_param(3,3)
    print('ODD_SQUAREZERO_RANK_TWO_RETRACTION_CHECKS_PASSED')
