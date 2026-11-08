"""Exact arithmetic tests for two-level antipodal oscillations in the logistic Game of Life."""
from fractions import Fraction as F
from collections import Counter

def cells(H,W):
    return [[((i+u)%H)*W+(j+v)%W for u in (-1,0,1) for v in (-1,0,1) if u or v]
            for i in range(H) for j in range(W)]

def update(s,L,nb):
    c=1-L
    out=[]
    for i,N in enumerate(nb):
        m=sum(s[j] for j in N)
        if F(3,2)<=m<F(5,2):out.append(s[i])
        elif F(5,2)<=m<=F(7,2):out.append(c*s[i]+L)
        else:out.append(c*s[i])
    return out

def test_pattern(bits,L,nb):
    c=1-L
    x=c/(1+c)
    y=1/(1+c)
    s=[y if (bits>>i)&1 else x for i in range(len(nb))]
    sw=[x if (bits>>i)&1 else y for i in range(len(nb))]
    k=[sum(((bits>>j)&1)!=((bits>>i)&1) for j in N) for i,N in enumerate(nb)]
    good=all(F(5,2)<=8*x+q*(y-x)<=F(7,2) for q in k)
    if good:
        assert update(s,L,nb)==sw
        assert update(sw,L,nb)==s
    return good,tuple(sorted(set(k)))

def main():
    nb=cells(4,4)
    params=[F(2,9),F(1,4),F(1,3),F(1,2),F(6,11),F(2,3),F(3,4),F(6,7),F(7,8),F(1,1)]
    valid_count=Counter()
    checks=0
    for bits in range(1<<16):
        ks=[sum(((bits>>j)&1)!=((bits>>i)&1) for j in N) for i,N in enumerate(nb)]
        for L in params:
            lo=max((F(2,9-2*k) for k in ks),default=F(0)) if max(ks)<=3 else None
            hi=min((F(6,11-2*k) for k in ks),default=F(1)) if max(ks)<=3 else None
            c=1-L; x=c/(1+c); y=1/(1+c)
            good=all(F(5,2)<=8*x+k*(y-x)<=F(7,2) for k in ks)
            bnd=(max(ks)<=3 and lo<=L<=hi)
            assert good==bnd,(bits,L,ks)
            checks+=1
            if good:
                verdict, _=test_pattern(bits,L,nb)
                assert verdict
                valid_count[str(L)]+=1
    # Explicit 2-wide vertical and horizontal stripe on 4x4
    horizontal=sum((1<<(i*4+j)) for i in range(4) for j in range(4) if i%4>=2)
    vertical=sum((1<<(i*4+j)) for i in range(4) for j in range(4) if j%4>=2)
    for L in [F(2,3),F(3,4),F(7,8),F(1,1)]:
        for bits in [horizontal,vertical]:
            assert test_pattern(bits,L,nb)==(True,(3,))
    # exact strict branch margin at lambda 3/4, permitting full-dimensional perturbations.
    L=F(3,4); c=1-L; x=c/(1+c); y=1/(1+c)
    m=8*x+3*(y-x)
    assert F(5,2)<m<F(7,2)
    # first and second steps followed by small arbitrary perturbations.
    eps=F(1,10000)
    sb=[y if (vertical>>i)&1 else x for i in range(16)]
    sample=[sb[i]+(eps if i%2==0 else -eps) for i in range(16)]
    t1=update(sample,L,nb)
    t2=update(t1,L,nb)
    # Correct affine two-step return depends on phase: low x => G then D (c^2 s+c lambda), high y => D then G (c^2 s+lambda).
    for i in range(16):
        z=c*c*sample[i]+(L if (vertical>>i)&1 else c*L)
        assert t2[i]==z,(i,t2[i],z)
    print('VERIFY_OK exact_checks=',checks,' valid_4x4_counts=',dict(valid_count), 'margin=',str(m))
if __name__=='__main__':main()
