"""Reproducible exact-rational tests of the cubic tangential-gradient frame at type-D roots."""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial


def poly(d, entries):
    return {tuple(k): F(v) for k, v in entries.items() if v}


def basis(d):
    result=[]
    for i in range(d):
        z={}
        a=[0]*d; a[i]=3; z[tuple(a)]=F(1)
        c=F(3,d+2)
        for j in range(d):
            a=[0]*d; a[i]+=1;a[j]+=2;t=tuple(a)
            z[t]=z.get(t,F(0))-c
        result.append(('Z',poly(d,z)))
    for i in range(d):
        others=[j for j in range(d) if j!=i]
        anchor=others[-1]
        for j in others[:-1]:
            a=[0]*d; a[i]+=1; a[j]+=2
            b=[0]*d; b[i]+=1; b[anchor]+=2
            result.append(('T',poly(d,{tuple(a):1,tuple(b):-1})))
    for i,j,k in combinations(range(d),3):
        a=[0]*d; a[i]=a[j]=a[k]=1
        result.append(('Q',poly(d,{tuple(a):1})))
    return result


def moment(e,d):
    if any(k%2 for k in e): return F(0)
    res=F(1)
    for k in e:
        for j in range(1,k,2):res*=j
    for j in range(0,sum(e),2):res/=d+j
    return res


def sphere_product(p,q,d):
    out=F(0)
    for a,ca in p.items():
        for b,cb in q.items():
            out+=ca*cb*moment(tuple(x+y for x,y in zip(a,b)),d)
    return out


def eval_poly(p,y):
    out=F(0)
    for e,c in p.items():
        t=c
        for yi,ei in zip(y,e):
            if ei:t*=yi**ei
        out+=t
    return out


def derivative(p,d):
    return [{tuple(e[:j]+(e[j]-1,)+e[j+1:]):v*e[j] for e,v in p.items() if e[j]} for j in range(d)]


def root_vectors(d):
    for i,j in combinations(range(d),2):
        for s,t in product((-1,1),repeat=2):
            y=[0]*d;y[i]=s;y[j]=t
            yield y


def sample_gram(p,q,dp,dq,roots):
    out=F(0)
    for y in roots:
        gp=[eval_poly(c,y) for c in dp]
        gq=[eval_poly(c,y) for c in dq]
        out+=sum(a*b for a,b in zip(gp,gq))/4-F(9,8)*eval_poly(p,y)*eval_poly(q,y)
    return out/len(roots)


def expected(d):
    return dict(
        Z=F((d+4)*(d*d+4*d-8),8*(d-1)*(d+1)),
        T=F((d+2)*(d+4)*(2*d-5),24*(d-1)*(d+1)),
        Q=F((d+2)*(d+4),2*(d-1)*(d+1)))


def verify(d,all_pairs=True):
    b=basis(d)
    assert len(b)==(d+4)*d*(d-1)//6
    roots=list(root_vectors(d))
    assert len(roots)==2*d*(d-1)
    deriv=[derivative(p,d) for _,p in b]
    lam=expected(d)
    for i,(s,p) in enumerate(b):
        choices=range(i,len(b)) if all_pairs else [i]
        for j in choices:
            t,q=b[j]
            a=sample_gram(p,q,deriv[i],deriv[j],roots)
            ref=3*(d+1)*sphere_product(p,q,d)
            expected_value=ref*lam[s] if s==t else F(0)
            if a!=expected_value:
                raise AssertionError((d,i,j,s,t,a,expected_value))
    print('PASS d=%d dimension=%d roots=%d pairs=%d eigenvalues=%s'%(d,len(b),len(roots),len(b)*(len(b)+1)//2 if all_pairs else len(b),lam),flush=True)

if __name__=='__main__':
    for d in range(3,8):verify(d)
    verify(8,False);verify(9,False)
    print('PASS exact symbolic full pairwise Gram checks for d=3..7, diagonal checks d=8..9')
