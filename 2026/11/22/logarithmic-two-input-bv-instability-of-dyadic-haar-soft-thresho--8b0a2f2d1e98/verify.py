"""Exact-rational dyadic Haar soft-threshold BV modulus checks (public science only)."""
from fractions import Fraction
from itertools import product
import random


def derivative_vectors(depth, cut):
    """Rows are n*D(h_I <h_I, 1_{i>=cut}>), for ancestor scales."""
    n=1<<depth
    out=[]
    for k in range(1,depth+1):
        s=1<<k; L=(cut//s)*s; R=L+s
        m=min(cut-L,R-cut)
        if m==0:continue
        factor=(n//s)*m
        a=[0]*n
        for i in range(L,L+s//2):a[i]=-factor
        for i in range(L+s//2,R):a[i]=factor
        out.append(tuple(a[i+1]-a[i] for i in range(n-1)))
    return out


def sharp(depth):
    n=1<<depth
    best=(0,0,0)
    for cut in range(1,n):
        ds=derivative_vectors(depth,cut)
        x=[0]*(n-1); prev=0
        if len(ds)==0:continue
        for q in range(1,1<<len(ds)):
            mask=q^(q>>1)
            change=mask^prev
            b=change.bit_length()-1
            sign=1 if mask&(1<<b) else -1
            D=ds[b]
            for i in range(n-1):x[i]+=sign*D[i]
            v=sum(abs(t) for t in x)
            if v>best[0]:best=(v,cut,mask)
            prev=mask
    return Fraction(best[0],n),best[1:]


def test_selected_witness(depth):
    n=1<<depth
    assert depth%2==0 and depth>=4
    j=(n-1)//3
    levels=list(range(2,depth-1,4))
    v=[0]*(n-1)
    supports=[]
    for k in levels:
        s=1<<k;L=(j//s)*s;R=L+s;m=min(j-L,R-j)
        assert j%s==(s-1)//3 and m/s>=1/4
        assert L>0 and R<n
        a=derivative_vectors(depth,j)
        # across the unique scale k, selected detail derivative
        detail=[0]*n
        for i in range(L,L+s//2):detail[i]=-m*(n//s)
        for i in range(L+s//2,R):detail[i]=m*(n//s)
        derivative=[detail[i+1]-detail[i] for i in range(n-1)]
        supports.append({i for i,z in enumerate(derivative) if z})
        v=[v[i]+derivative[i] for i in range(n-1)]
        assert sum(abs(t) for t in derivative)==4*m*(n//s)
    for i in range(len(supports)):
        for j in range(i+1,len(supports)):
            assert not supports[i]&supports[j],('overlap',depth,levels)
    total=Fraction(sum(abs(t) for t in v),n)
    assert total==sum(Fraction(4*((1<<k)-1),3*(1<<k)) for k in levels)
    assert total>=len(levels)
    return levels,total


def haar_transform(v):
    n=len(v);ans=[sum(v)/n]
    for k in range(1,n.bit_length()):
        s=1<<k
        for l in range(0,n,s):
            x=sum(v[l:l+s//2]);y=sum(v[l+s//2:l+s]);ans.append((x-y)/(s**0.5))
    return ans

def threshold(v,t):
    n=len(v);out=[sum(v)/n]*n
    for k in range(1,n.bit_length()):
        s=1<<k
        for l in range(0,n,s):
            c=(sum(v[l:l+s//2])-sum(v[l+s//2:l+s]))/(s**0.5)
            a=max(abs(c)-t,0)
            c=(a if c>=0 else -a)/(s**0.5)
            for i in range(l,l+s//2):out[i]+=c
            for i in range(l+s//2,l+s):out[i]-=c
    return out

def tv(v):return sum(abs(v[i+1]-v[i]) for i in range(len(v)-1))

def test_random():
    rng=random.Random(314159)
    for d in range(1,6):
        K=float(sharp(d)[0]);n=1<<d
        for _ in range(120):
            a=[rng.randrange(-30,31)/8 for i in range(n)]
            b=[rng.randrange(-30,31)/8 for i in range(n)]
            t=1.25
            aa=threshold(a,t);bb=threshold(b,t)
            assert tv([u-v for u,v in zip(aa,bb)])<=K*tv([u-v for u,v in zip(a,b)])+1e-8
    print('RANDOM_TWO_INPUT_HAAR_SHRINKAGE_CHECKS_PASS 600')

if __name__=='__main__':
    expected={1:Fraction(1),2:Fraction(3,2),3:Fraction(2),4:Fraction(21,8),5:Fraction(3),6:Fraction(117,32),7:Fraction(4),8:Fraction(597,128)}
    for d,want in expected.items():
        got,arg=sharp(d)
        assert got==want,(d,got,want,arg)
        print('EXACT_ALL_CUTS_ALL_RELEVANT_MASKS_PASS',d,got,arg)
    for d in (4,8,12,16):
        levels,v=test_selected_witness(d)
        print('LOG_GROWTH_EXPLICIT_DISJOINT_WITNESS_PASS',d,levels,v)
    test_random()
    print('ALL_HAAR_BV_CERTIFICATES_PASS')
