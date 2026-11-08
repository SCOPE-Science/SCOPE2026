from collections import defaultdict
from fractions import Fraction
from functools import lru_cache

def D(q,k):
    p=Fraction(1)
    for i in range(1,k+1):p*=Fraction(q**i-1,q**i)
    return p

def predicted(n,q):
    d={}
    for r in range(n//2+1):
      for s in range(r+1):
        c4=r;c3=n-2*r;c2=s;c1=2*(r-s)
        cols=[c1+c2+c3+c4,c2+c3+c4,c3+c4,c4]
        autom_exp=sum(i*i for i in cols)
        coefficient=Fraction(q**(5*n*n-autom_exp))*D(q,n)**2
        for c in (c1,c2,c3,c4):coefficient/=D(q,c)
        assert coefficient.denominator==1
        d[(r,s)]=int(coefficient)
    return d

def mul(a,b,q):
    z=0
    for i in range(2):
        for j in range(2):
            t=sum(((a//q**(2*i+k))%q)*((b//q**(2*k+j))%q) for k in range(2))%q
            z+=t*q**(2*i+j)
    return z


def matrix6(A,B,C,D,F):
    def entry(M,i,j):return (M>>(2*i+j))&1
    T=[[0]*6 for _ in range(6)]
    for i in range(2):
      for j in range(2):
        T[i][j]=entry(A,i,j)
        T[2+i][j]=entry(B,i,j)
        T[2+i][2+j]=entry(A,i,j)
        T[2+i][4+j]=entry(C,i,j)
        T[4+i][j]=entry(D,i,j)
        T[4+i][4+j]=entry(F,i,j)
    return [sum(T[i][j]<<j for j in range(6)) for i in range(6)]

def rankbinary(rows):
    basis={}
    for r in rows:
        while r:
            k=r.bit_length()-1
            if k not in basis:
                basis[k]=r;break
            r^=basis[k]
    return len(basis)

def matmulrows(U,V):
    return [__import__('functools').reduce(int.__xor__, (V[j] for j in range(len(V)) if (row>>j)&1),0) for row in U]

def exhaustive2():
    tab=[[mul(a,b,2) for b in range(16)] for a in range(16)]
    squarezero=[a for a in range(16) if tab[a][a]==0]
    bytype=defaultdict(int); checked=0
    for A in squarezero:
      for F in squarezero:
        for C in range(16):
          if tab[A][C]^tab[C][F]:continue
          for D in range(16):
            if tab[D][A]^tab[F][D]:continue
            for B in range(16):
              if tab[B][A]^tab[A][B]^tab[C][D]!=9:continue # identity diag bits0,3
              rows=matrix6(A,B,C,D,F)
              sq=matmulrows(rows,rows)
              assert sq==[0,0,1,2,0,0],(A,B,C,D,F,rows,sq)
              cube=matmulrows(sq,rows)
              r=rankbinary(cube)
              d=4-rankbinary(rows)
              s=r-d
              bytype[(r,s)]+=1
              checked+=1
    assert dict(bytype)==predicted(2,2),(bytype,predicted(2,2))
    print('n2 q2',dict(sorted(bytype.items())),checked)

def exhaustive1(q):
  found=defaultdict(int)
  for a in range(q):
   for b in range(q):
    for c in range(q):
     for d in range(q):
      for f in range(q):
       mat=[[a,0,0],[b,a,c],[d,0,f]]
       mul3=lambda X,Y:[[sum(X[i][k]*Y[k][j] for k in range(3))%q for j in range(3)] for i in range(3)]
       if mul3(mat,mat)==[[0,0,0],[1,0,0],[0,0,0]]:
        found[(0,0)]+=1
  assert dict(found)==predicted(1,q),(found,predicted(1,q))
  print('n1 q',q,dict(found))
if __name__=='__main__':
  for q in (2,3,5):exhaustive1(q)
  exhaustive2()
  for n in (3,4):
    for q in (2,3):
      counts=predicted(n,q)
      print('formula_nq',n,q,len(counts),sum(counts.values()))
  print('VERIFY_OK')
