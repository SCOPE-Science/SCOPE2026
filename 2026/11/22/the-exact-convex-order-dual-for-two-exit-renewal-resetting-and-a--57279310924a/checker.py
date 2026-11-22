"""Exact rational checks for the convex-order dual of two-exit renewal resetting.
Only finite test cases are checked; the universal theorem has a separate proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb

def frac(a,b=1): return Q(a,b)

def diff2(a,i): return a[i-1]-2*a[i]+a[i+1]

def ratio(a,b,p):
    aa=sum((x*y for x,y in zip(a,p)),Q(0)); bb=sum((x*y for x,y in zip(b,p)),Q(0))
    if not bb: return None
    return aa/bb

def convex_leq(p,q):
    N=len(p)
    if sum(p)!=sum(q) or sum((i+1)*v for i,v in enumerate(p))!=sum((i+1)*v for i,v in enumerate(q)):return False
    return all(sum((i-k)* (q[k-1]-p[k-1]) for k in range(1,i))>=0 for i in range(2,N))

def curvature_test(a,b):
    qs=[a[i]/b[i] for i in range(len(a)) if b[i]>0]
    l,h=min(qs),max(qs)
    return all(diff2(a,i)-r*diff2(b,i) <= 0 for i in range(1,len(a)-1) for r in (l,h))

def baseline_exits(P,z,n):
    # P interior transition up-probability array, indices 1..a-1
    a=len(P)-1; dist={z:Q(1)};low=high=Q(0)
    A=[]; B=[]
    for t in range(1,n+1):
        new={}
        for k,v in dist.items():
            up=P[k]; down=1-up
            if k==1: low+=v*down
            else: new[k-1]=new.get(k-1,Q(0))+v*down
            if k==a-1: high+=v*up
            else: new[k+1]=new.get(k+1,Q(0))+v*up
        dist=new; A.append(low);B.append(low+high)
    return A,B

def check():
    assertions=0
    for a in (4,6,8,10):
      for up in (Q(1,3),Q(1,2),Q(3,4)):
       P=[Q(0)]+[up]*(a-1)+[Q(0)]
       for z in range(1,a):
        A,B=baseline_exits(P,z,a+6)
        if z==a//2:
         ratios={A[i]/B[i] for i in range(len(A)) if B[i]}
         assert len(ratios)==1
         assertions+=1
        else:
         k=(a-z) if z<a//2 else z
         assert k>=3
         # R=k-1, spread S=(k-2,k); R=k, spread S=(k-1,k+1).
         p1=[Q(0)]*(a+6);q1=p1.copy();p1[k-2]=1;q1[k-3]=q1[k-1]=Q(1,2)
         p2=[Q(0)]*(a+6);q2=p2.copy();p2[k-1]=1;q2[k-2]=q2[k]=Q(1,2)
         assert convex_leq(p1,q1) and convex_leq(p2,q2)
         r1=ratio(A,B,p1);s1=ratio(A,B,q1)
         r2=ratio(A,B,p2);s2=ratio(A,B,q2)
         assert r1 is not None and s1 is not None and r2 is not None and s2 is not None
         assert (r1-s1)*(r2-s2)<0
         assertions+=4
    # Exhaustively probe the signed cone identity on small rational simplex clocks.
    for N in (4,5):
     # Mixed completion pairs obtained from normalized arbitrary nonnegative step masses.
     for lmass in (tuple(Q(i,12) for i in (1,0,1,2,0)),tuple(Q(i,12) for i in (0,2,1,0,1))):
      for hmass in (tuple(Q(i,12) for i in (0,0,1,1,2)),tuple(Q(i,12) for i in (1,0,0,2,1))):
       A=[];B=[];la=ha=Q(0)
       for i in range(N):
        la+=lmass[i];ha+=hmass[i];A.append(la);B.append(la+ha)
       bds=[a/b for a,b in zip(A,B) if b]
       for i in range(1,N-1):
        for r in (min(bds),max(bds)):
         assert diff2(A,i)-r*diff2(B,i) == (A[i-1]-2*A[i]+A[i+1])-r*(B[i-1]-2*B[i]+B[i+1])
         assertions+=1
       # integer grid simplex probability vectors with denominator 4
       ps=[]
       for seq in product(range(5),repeat=N):
        if sum(seq)==4: ps.append([Q(k,4) for k in seq])
       for p in ps:
        for q in ps:
         if not convex_leq(p,q):continue
         qr=ratio(A,B,p);qs=ratio(A,B,q)
         if qr is None or qs is None:continue
         c=[Q(0)]*(N+1)
         for i in range(2,N):c[i]=sum((i-k)*(q[k-1]-p[k-1]) for k in range(1,i))
         assert all(x>=0 for x in c)
         lhs=sum((q[i]-p[i])*(A[i]-qr*B[i]) for i in range(N))
         rhs=sum(c[i]*(A[i-2]-2*A[i-1]+A[i]-qr*(B[i-2]-2*B[i-1]+B[i])) for i in range(2,N))
         assert lhs==rhs
         assert (qs-qr)*sum(q[i]*B[i] for i in range(N))==rhs
         assertions+=3
         if curvature_test(A,B):
          assert qs<=qr
          assertions+=1
    print('PASS exact rational assertions:',assertions)

if __name__=='__main__':check()
