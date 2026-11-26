#!/usr/bin/env python3
"""Independent bit-linear rank checks for reversible incidence waves on finite affine planes."""
import itertools
from collections import Counter

def field(s):
    if s in (2,3,5,7):
        return lambda x,y:(x+y)%s,lambda x,y:(x*y)%s
    if s==4:
        return lambda x,y:x^y,lambda a,b:gf4_mul(a,b)
    raise ValueError(s)

def gf4_mul(a,b):
    v=0
    for i in range(2):
        if (b>>i)&1:v^=a<<i
    if v&8:v^=0b1100
    if v&4:v^=0b111
    return v

def incidence(s):
    add,mul=field(s)
    pts=list(itertools.product(range(s),repeat=2));lines=[]
    for slope in range(s):
      for b in range(s):
        lines.append([int(y==add(mul(slope,x),b)) for x,y in pts])
    for a in range(s):
      lines.append([int(x==a) for x,y in pts])
    B=[[col[i] for col in lines] for i in range(s*s)]
    assert len(B)==s*s and len(B[0])==s*s+s
    assert all(sum(row)==s+1 for row in B)
    assert all(sum(B[i][j] for i in range(s*s))==s for j in range(s*s+s))
    return B

def rank_int_rows(rows):
    piv={}
    for row in rows:
        while row:
            p=row.bit_length()-1
            if p in piv:row^=piv[p]
            else:piv[p]=row;break
    return len(piv)

def matrix_product_rows(R,S):
   out=[]
   for row in R:
       v=0
       while row:
          p=(row&-row).bit_length()-1
          v^=S[p];row&=row-1
       out.append(v)
   return out

def rank_of_T_power(s,k):
   B=incidence(s);P=s*s;L=s*s+s;N=P+L;D=2*N
   Ar=[]
   for i in range(P):Ar.append(sum(B[i][j]<< (P+j) for j in range(L)))
   for j in range(L):Ar.append(sum(B[i][j]<<i for i in range(P)))
   Tr=[0]*D
   for i in range(N):Tr[i]=Ar[i]|(1<<(N+i))
   for i in range(N):Tr[N+i]=1<<i
   mat=[1<<i for i in range(D)];power=Tr[:]
   while k:
       if k&1:mat=matrix_product_rows(mat,power)
       k>>=1
       if k:power=matrix_product_rows(power,power)
   rk=rank_int_rows([mat[i]^(1<<i) for i in range(D)])
   return D-rk

def formula(s,k,rho=None):
   r=k&-k
   if s%2:
      return min(r,6)+(s-1)*min(r,2)+(2*(s*s-1)*min(r,2) if k%3==0 else 0)
   assert rho is not None
   N=2*s*s+s;n3=s+1;n2=2*rho-2*(s+1);n1=N-4*rho+(s+1)
   return n1*min(r,2)+n2*min(r,4)+n3*min(r,6)

def main():
    for s in (2,3,4,5):
       B=incidence(s);P=s*s;L=s*s+s;rho=rank_int_rows([sum(B[i][j]<<j for j in range(L)) for i in range(P)])
       K=(1,2,4,8) if s%2==0 else (1,2,3,4,6,8,12,24)
       obs={k:rank_of_T_power(s,k) for k in K}
       exp={k:formula(s,k,rho) for k in K}
       assert obs==exp,(s,obs,exp)
       assert obs[max(K)]==2*(P+L)
       print(f'order={s} point_line_rank={rho} global_period={max(K)} fixed_space_dimensions={obs}')
    print('PASS')
if __name__=='__main__':main()
