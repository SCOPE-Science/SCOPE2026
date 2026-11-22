#!/usr/bin/env python3
"""Exact cyclotomic certificate for 16-point four-sample Fourier stability.
Only Python standard library. A 16th root is represented in Z[z]/(z^8+1).
Positive definiteness is tested by Sylvester's criterion at threshold 1/1000.
"""
from itertools import combinations,permutations
from math import isqrt
import hashlib
N=16; SCALE=10**25; THRESHOLD_DENOM=1000
ZERO=(0,)*8; ONE=(1,)+(0,)*7

def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def mul(a,b):
 c=[0]*8
 for i,x in enumerate(a):
  if not x:continue
  for j,y in enumerate(b):
   if not y:continue
   s=i+j
   if s<8:c[s]+=x*y
   else:c[s-8]-=x*y
 return tuple(c)
def zm(k):
 k%=16; c=[0]*8;c[k%8]=1 if k<8 else -1
 return tuple(c)
def conj(a):return tuple(sum(a[j]*zm(-j)[i] for j in range(8)) for i in range(8))

def det(M):
 n=len(M); out=ZERO
 for p in permutations(range(n)):
  inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
  v=ONE
  for i,j in enumerate(p):v=mul(v,M[i][j])
  out=plus(out,neg(v) if inv%2 else v)
 return out

# Rigorous floor/ceiling bounds on 10^25 times cos(k*pi/8).
# Uses only integer square-root inequalities (no floating point).
S=SCALE
s2=isqrt(2*S*S)
def sqrt_enclosure_floor(a,b):
 """Enclose sqrt(x) where a <= x <= b are integer numerators divided by four."""
 lo=isqrt(a//4);hi=isqrt((b+3)//4)+1
 return lo,hi
c1=sqrt_enclosure_floor(2*S*S+S*s2,2*S*S+S*(s2+1))
c3=sqrt_enclosure_floor(2*S*S-S*(s2+1),2*S*S-S*s2)
c2=(s2//2,(s2+2)//2+1)
base={0:(S,S),1:c1,2:c2,3:c3,4:(0,0),5:(-c3[1],-c3[0]),6:(-c2[1],-c2[0]),7:(-c1[1],-c1[0])}
def real_sign(a):
 assert a==conj(a), ('not real',a,conj(a))
 lo=hi=0
 for j,v in enumerate(a):
  b,c=base[j]
  if v>=0:lo+=v*b;hi+=v*c
  else:lo+=v*c;hi+=v*b
 if lo>0:return 1,lo
 if hi<0:return -1,-hi
 if lo==hi==0:return 0,0
 raise ArithmeticError('Unresolved root enclosure: '+str((a,lo,hi)))

def matrix(R,C):
 return [[plus(tuple(THRESHOLD_DENOM*sum(zm((r*(C[j]-C[i]))%16)[t] for r in R) for t in range(8)), neg(ONE) if i==j else ZERO) for j in range(4)] for i in range(4)]

def certify_good(R):
 m=[None]*4;counts=[0]*4;checksum=hashlib.sha256()
 for C in combinations(range(16),4):
  H=matrix(R,C)
  for k in range(1,5):
   d=det([row[:k] for row in H[:k]])
   s,margin=real_sign(d)
   assert s==1,('not positive definite',R,C,k,d)
   counts[k-1]+=1
   m[k-1]=margin if m[k-1] is None else min(m[k-1],margin)
   checksum.update((','.join(map(str,C))+'/'+str(k)+':'+','.join(map(str,d))+'\n').encode())
 return counts,m,checksum.hexdigest()

def bad_witness(R,C):
 H=matrix(R,C);d=det(H);s,margin=real_sign(d)
 assert s==-1,(R,C,s)
 return d,margin

def orbit(R):return {tuple(sorted((a*x+b)%16 for x in R)) for a in range(1,16,2) for b in range(16)}

def main():
 allU={R for R in combinations(range(16),4) if len(set(r%4 for r in R))==4}
 reps=[(0,1,2,3),(0,1,2,7),(0,1,3,14)]
 ors=[orbit(R) for R in reps]
 assert [len(x) for x in ors]==[64,128,64]
 assert len(set.union(*ors))==256 and set.union(*ors)==allU
 assert not any(ors[i]&ors[j] for i in range(3) for j in range(i+1,3))
 print('UNIVERSAL_ROWS',len(allU),'AFFINE_ORBITS',[len(x) for x in ors])
 for R,C in [(reps[0],(0,1,2,3)),(reps[1],(0,1,4,5))]:
  d,margin=bad_witness(R,C)
  print('BAD_ORBIT',R,'COLUMN_WITNESS',C,'DETERMINANT_SIGN',-1,'CERTIFIED_MARGIN_NUMERATOR',margin,'SCALE',S,'DET_COEFFS',d)
 counts,margins,digest=certify_good(reps[2])
 print('GOOD_ORBIT',reps[2],'SYLVESTER_MINOR_COUNTS',counts,'MIN_CERTIFIED_MARGIN_NUMERATORS',margins,'SCALE',S,'DIGEST',digest)
 print('PASS: all optimal 64 row sets have squared min singular value > 1/1000 for EVERY 4-column set; other 192 universal sets each have a submatrix with squared min singular value < 1/1000')
if __name__=='__main__':main()
