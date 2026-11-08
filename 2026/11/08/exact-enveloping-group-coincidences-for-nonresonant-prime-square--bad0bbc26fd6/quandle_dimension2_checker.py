"""Direct F_p matrix census; checks connected non-resonant Alexander quandles."""
from itertools import product

def inverse_matrix(T,p):
 a,b,c,d=T; det=(a*d-b*c)%p; z=pow(det,-1,p)
 return ((d*z)%p,(-b*z)%p,(-c*z)%p,(a*z)%p)

def key(T,p):
 a,b,c,d=T
 tr=(a+d)%p;det=(a*d-b*c)%p
 return tr,det,int(a==d and b==0 and c==0)

def rank(matrix,p):
 A=[row[:] for row in matrix];n=len(A);m=len(A[0]);q=0
 for col in range(m):
  s=next((k for k in range(q,n) if A[k][col]%p),None)
  if s is None:continue
  A[q],A[s]=A[s],A[q];r=pow(A[q][col]%p,-1,p);A[q]=[(v*r)%p for v in A[q]]
  for j in range(n):
   if j!=q:
    mul=A[j][col]
    A[j]=[(x-mul*y)%p for x,y in zip(A[j],A[q])]
  q+=1
  if q==n:break
 return q

def S_dimension(T,p):
 a,b,c,d=T; A=[[0]*4 for i in range(4)]
 # tau(e_i tensor e_j) = T(e_j) tensor e_i.
 for i in range(2):
  for j in range(2):
   col=2*i+j
   for k in range(2):
    A[2*k+i][col]=T[2*k+j]
 M=[[(int(i==j)-A[i][j])%p for j in range(4)] for i in range(4)]
 return 4-rank(M,p)

def check(p):
 classes={}; total=0; resonant=0
 for a,b,c,d in product(range(p),repeat=4):
  T=a,b,c,d;det=(a*d-b*c)%p
  if det==0:continue
  # above condition equality exact integer zero is WRONG mod p: do below
  tr=(a+d)%p
  if (1-tr+det)%p==0: continue
  total+=1
  if det==1:
   resonant+=1
   if p<=7:assert S_dimension(T,p)==1
   continue
  if p<=7:assert S_dimension(T,p)==0
  k=key(T,p);classes[k]=T
 keys=set(classes)
 inv=lambda T: key(inverse_matrix(T,p),p)
 assert all(inv(T) in keys and inv(T)!=k for k,T in classes.items())
 Gclasses={frozenset((k,inv(T))) for k,T in classes.items()}
 expected=p*p-2*p-1
 assert len(keys)==expected,(p,len(keys),expected)
 assert len(Gclasses)==expected//2
 return p,total,resonant,len(keys),len(Gclasses)

if __name__=='__main__':
 for p in (3,5,7,11): print('CENSUS',*check(p))
 print('VERIFY_OK primes=3,5,7,11; nonresonant_class_formula=yes; inversion_fixed_classes=0')

# Independent brute-conjugacy test for the full finite groups GL_2(F_3), GL_2(F_5).
def mm(A,B,p):
 a,b,c,d=A;e,f,g,h=B
 return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)
def powm(T,k,p):
 R=(1,0,0,1)
 for _ in range(k):R=mm(R,T,p)
 return R

def full_conjugacy_check(p):
 G=[T for T in product(range(p),repeat=4) if (T[0]*T[3]-T[1]*T[2])%p]
 eligible=[T for T in G if (T[0]*T[3]-T[1]*T[2])%p!=1 and (1-T[0]-T[3]+T[0]*T[3]-T[1]*T[2])%p]
 by_key={}
 for T in eligible:by_key.setdefault(key(T,p),set()).add(T)
 assert len(by_key)==p*p-2*p-1
 for k,loc in by_key.items():
  T=next(iter(loc));orbit={mm(mm(A,T,p),inverse_matrix(A,p),p) for A in G}
  assert orbit==loc,(p,k,len(orbit),len(loc))
 return len(G),len(by_key),len(eligible)

def example():
 p=5;T=(0,1,2,2);U=powm(T,7,p)
 assert U==(0,3,1,1)
 assert powm(T,24,p)==(1,0,0,1)
 assert all(powm(T,d,p)!=(1,0,0,1) for d in (1,2,3,4,6,8,12))
 assert key(T,p)!=key(U,p) and key(inverse_matrix(T,p),p)!=key(U,p)
 assert {powm(T,j,p) for j in range(24)}=={powm(U,j,p) for j in range(24)}
 assert S_dimension(T,p)==S_dimension(U,p)==0
 return T,U

if __name__=='__main__':
 for p in (3,5):print('CONJUGACY',p,*full_conjugacy_check(p))
 print('EXAMPLE_P5',*example())
 print('VERIFY_STRONG_OK checked_independent_conjugacy_3_5=yes collision=yes')
