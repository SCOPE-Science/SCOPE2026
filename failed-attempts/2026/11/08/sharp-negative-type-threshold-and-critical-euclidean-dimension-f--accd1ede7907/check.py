#!/usr/bin/env python3
"""Exact independent Grassmann distance-scheme checks (standard library)."""
from math import comb, log

def qbracket(r,q):
    assert r >=0
    return (q**r-1)//(q-1)

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    top=bottom=1
    for i in range(k):
        top*=q**(n-i)-1
        bottom*=q**(i+1)-1
    assert top%bottom==0
    return top//bottom

def recurrence(n,q):
    h=qbracket(3,q)
    val=q*h*qbracket(n-3,q)
    bs=[q**(2*i+1)*qbracket(3-i,q)*qbracket(n-3-i,q) if i<3 else 0 for i in range(4)]
    cs=[qbracket(i,q)**2 for i in range(4)]
    aa=[val-bs[i]-cs[i] for i in range(4)]
    vals=[]
    for j in range(4):
        p1=q**(j+1)*qbracket(3-j,q)*qbracket(n-3-j,q)-qbracket(j,q)
        eig=[1,p1]
        for i in (1,2):
            numerator=p1*eig[i]-bs[i-1]*eig[i-1]-aa[i]*eig[i]
            assert numerator%cs[i+1]==0
            eig.append(numerator//cs[i+1])
        vals.append(eig)
    return vals,bs,cs

def closed(n,q):
    h=q*q+q+1
    u=qbracket(n-5,q)
    t1=q*q*(q+1)*(1+q*u)-1
    p21=q*q*(q*u+1)*(q**4*u-q*q-2*q-1)//(q+1)
    assert q*q*(q*u+1)*(q**4*u-q*q-2*q-1)%(q+1)==0
    t2=q**3*u-q-1
    c=q**4*u
    return [
      [1,q*h*qbracket(n-3,q),None,None],
      [1,t1,p21,-q**6*u*(q*u+1)//(q+1)],
      [1,t2,-(t2+c+1),c],
      [1,-h,q*h,-q**3],
    ]

def exact_tests():
    for q in (2,3,4,5,7,8,9,11):
        for n in (6,7,8,9,10,13):
            es,bs,cs=recurrence(n,q)
            cl=closed(n,q)
            for j in (1,2,3):
                assert es[j]==cl[j],(q,n,j,es[j],cl[j])
                assert sum(es[j])==0,(q,n,j)
            assert es[1][1]>0 and es[1][2]>0 and es[1][3]<0
            assert es[2][1]>0 and es[2][2]<0 and es[2][3]>0
            assert es[3]==[1,-qbracket(3,q),q*qbracket(3,q),-q**3]
            N=gaussian(n,3,q)
            m=[gaussian(n,j,q)-gaussian(n,j-1,q) for j in range(4)]
            assert sum(m)==N
            for i in range(4):
                assert sum(es[j][i]*m[j] for j in range(4))==(N if i==0 else 0)
    print('exact all-field recurrence, sign, multiplicity checks PASS')

def geometry_q2_n6():
    # Each rank-three F_2-subspace represented by its seven nonzero vectors.
    planes=set()
    for a in range(1,64):
        for b in range(a+1,64):
            for c in range(b+1,64):
                if c == a^b:continue
                span=(0,a,b,c,a^b,a^c,b^c,a^b^c)
                planes.add(sum(1<<v for v in span))
    planes=list(planes)
    assert len(planes)==1395
    base=next(s for s in planes if all((s>>i)&1 for i in (0,1,2,3,4,5,6,7)))
    def dd(x,y):
        sz=(x&y).bit_count()
        assert sz in (1,2,4,8)
        return 3-(sz.bit_length()-1)
    profile=[dd(base,p) for p in planes]
    eig,bs,cs=recurrence(6,2)
    for i in range(4):
        j=profile.index(i);b=planes[j]
        neighbor=[p for p in planes if dd(b,p)==1]
        assert len(neighbor)==bs[0]
        hist={x:sum(dd(base,p)==x for p in neighbor) for x in range(4)}
        assert hist.get(i-1,0)==cs[i] if i>0 else True
        assert hist.get(i+1,0)==bs[i] if i<3 else True
    counts=[profile.count(i) for i in range(4)]
    assert counts==[1,98,784,512],counts
    assert eig[1]==[1,35,28,-64]
    assert eig[2]==[1,5,-22,16]
    assert eig[3]==[1,-7,14,-8]
    print('independent 1395-vertex F_2 Grassmann geometry and intersection array PASS')

def root_eval(n,q):
    # Root of the unique-sector continuous multiplier: bisection in [0,2].
    u=qbracket(n-5,q);A=q**3*u-(q+1); C=q**4*u
    def f(t):return A-(A+C+1)*2**t+C*3**t
    lo,hi=0.,2.
    assert f(lo)==-1 and f(hi)>0
    for _ in range(90):
        t=(lo+hi)/2
        if f(t)>0:hi=t
        else:lo=t
    return (lo+hi)/2

if __name__=='__main__':
    exact_tests()
    geometry_q2_n6()
    for q in (2,3,4,5,7):
        n=6; b=root_eval(n,q)
        m2=gaussian(n,2,q)-gaussian(n,1,q)
        N=gaussian(n,3,q)
        assert b>0 and m2>0 and N-1-m2>0
        print(f'q={q} n=6 beta={b:.14g} embedding_dim={N-1-m2} out_of={N}')
    print('GRASSMANN_THREE_NEGATIVE_TYPE_PASS')
