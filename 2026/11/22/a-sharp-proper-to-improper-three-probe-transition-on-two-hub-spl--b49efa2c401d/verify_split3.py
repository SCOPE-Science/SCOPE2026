"""Exact-rational independent checks for the three-color split-resolvent theorem."""
from fractions import Fraction as F
from itertools import product

def inverse(A):
    n=len(A)
    E=[[F(A[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for i in range(n):
        j=next(k for k in range(i,n) if E[k][i]);E[i],E[j]=E[j],E[i]
        t=E[i][i];E[i]=[a/t for a in E[i]]
        for k in range(n):
            if k!=i:
                t=E[k][i];E[k]=[x-t*y for x,y in zip(E[k],E[i])]
    return [row[n:] for row in E]

def matrix(q,mu):
    n=q+2
    A=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
      for j in range(i+1,n):
        if i<2 or j<2:
          A[i][j]-=1;A[j][i]-=1;A[i][i]+=1;A[j][j]+=1
    for i in range(n):A[i][i]+=mu
    return A

def compositions(q):
    for x in range(q+1):
      for y in range(q-x+1):
        yield x,y,q-x-y

def score(r,s,beta):
    return sum(F(r[i]*(r[i]-1),2)+r[i]*s[i]+beta*F(s[i]*(s[i]-1),2) for i in range(3))

def predicted(q,beta):
    H=(q*q)//4
    a0=((1,1,0),(0,0,q))
    if beta<F(1,H):return [a0]
    b=[]
    for x in range(q-1):
      y=(q-x)//2;z=q-x-y
      b.append((score((2,0,0),(x,y,z),beta),((2,0,0),(x,y,z))))
    low=min(v for v,_ in b)
    opt=[conf for v,conf in b if v==low]
    if beta==F(1,H):return [a0]+opt
    return opt

def norm(r,s):
    return tuple(sorted(zip(r,s)))

def check():
    exact=0;direct=0; thresholds=0
    for q in range(4,16):
      H=q*q//4
      betas=[F(1,1000),F(1,H),F(1,H+1),F(1,max(1,H-1)),F(1,3),F(1,2),F(7,8),F(99,100)]
      for beta in betas:
       if not F(0)<beta<F(1):continue
       candidates=[]
       for r in [(2,0,0),(1,1,0)]:
        for s in compositions(q):
         if any(r[i]+s[i]==0 for i in range(3)):continue
         candidates.append((score(r,s,beta),norm(r,s)))
         exact+=1
       val=min(a for a,_ in candidates)
       actual={b for a,b in candidates if a==val}
       forecast={norm(*c) for c in predicted(q,beta)}
       assert actual==forecast,(q,beta,actual,forecast)
    # Direct independent inverse-matrix and counted variance checks, not only scores
    for q in range(4,9):
      for mu in [F(1,10),F(1,1),F(2,1),F(8,1)]:
       B=inverse(matrix(q,mu))
       c=1/(mu*(mu+q+2));t=c*2/(mu+2); beta=(t/c)**2
       for i in range(q+2):
        for j in range(i+1,q+2):
         assert B[i][j]==(t if i>=2 and j>=2 else c)
       for r in [(2,0,0),(1,1,0)]:
        for s in compositions(q):
         if any(r[i]+s[i]==0 for i in range(3)):continue
         labels=[0]*r[0]+[1]*r[1]+[2]*r[2]+[0]*s[0]+[1]*s[1]+[2]*s[2]
         # Clique occupies first two positions, indie the rest
         val=4*sum(B[i][j]**2 for i in range(q+2) for j in range(i+1,q+2) if labels[i]==labels[j])
         assert val==4*c*c*score(r,s,beta)
         direct+=1
    for q in range(4,51):
      H=q*q//4; beta=F(1,H)
      # Boundary split and merged extremal profiles have same risk.
      z=(q//2,q-q//2)
      aa=score((1,1,0),(0,0,q),beta)
      bb=score((2,0,0),(0,*z),beta)
      assert aa==bb
      assert aa-bb==0
      thresholds+=1
    print(f'PASS {exact} rational score comparisons, {direct} independent inverse/variance comparisons, {thresholds} exact critical identities')
if __name__=='__main__':check()
