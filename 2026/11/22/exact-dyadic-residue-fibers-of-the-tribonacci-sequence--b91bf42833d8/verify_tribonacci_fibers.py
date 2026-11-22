from collections import Counter
import math
# modular matrix powers using 3x3 M: T_n from row (1,0,0) M^n (0,1,1) ; M rows [[0,1,0],[0,0,1],[1,1,1]]
M=((0,1,0),(0,0,1),(1,1,1)); ID=((1,0,0),(0,1,0),(0,0,1))
def mm(A,B,q):return tuple(tuple(sum(A[i][t]*B[t][j] for t in range(3))%q for j in range(3)) for i in range(3))
def Tfast(n,q):
 A=M; B=ID
 while n:
  if n&1:B=mm(B,A,q)
  A=mm(A,A,q);n//=2
 return (B[0][1]+B[0][2])%q

def Hd2(r,t,N):
 L=N+6
 z=1<<(L+4+N)
 x=(Tfast(8*(t+(1<<L))+r,z)-Tfast(8*t+r,z))%z
 assert x%(1<<(L+4))==0
 return (x>>(L+4))%(1<<N)
def crit(r,N):
 x=0
 for j in range(N):
  if (Hd2(r,x,j+1)>>(j))&1:x+=1<<j
 assert Hd2(r,x,N)==0
 return x
def kappa(r,N):
 a=crit(r,N+3)
 return ((Tfast(8*a+r,1<<(N+3))+(1 if r==5 else 0))//8)%(1<<N)
def sqroot_count(y,m):
 q=1<<m; y%=q
 if y==0:return 1<<(m//2)
 v=(y&-y).bit_length()-1
 if v%2:return 0
 h=v//2;s=m-2*h;u=y>>v
 if s==1:return 1<<h
 if s==2:return (1<<(h+1)) if u%4==1 else 0
 return (1<<(h+2)) if u%8==1 else 0

def formula(y,k,c5,c7):
 q=1<<k
 y%=q
 c=2*int(y%4 in (0,1)) + 4*int(y%16 in (1,2))
 m=k-3
 for r,b in ((5,(8*c5-1)%q),(7,(8*c7)%q)):
  if (y-b)%8==0: c+=2*sqroot_count(((y-b)%q)//8,m)
 return c

def go():
 for k in range(4,15):
  N=k-3;c5=kappa(5,N);c7=kappa(7,N)
  q=1<<k; T=[0,1,1]
  for i in range(3,2*q):T.append(sum(T[-3:])%q)
  C=Counter(T)
  errors=[(y,C[y],formula(y,k,c5,c7)) for y in range(q) if C[y]!=formula(y,k,c5,c7)]
  print('k=',k,'k5=',c5,'k7=',c7,'errors',len(errors),'hist',dict(sorted(Counter(C.values()).items())))
  if errors:print('ERROR',errors[:10]);raise SystemExit(1)
 print('kappa5= ',kappa(5,11),'should 1264 yes')
if __name__=='__main__':go()

# Independent exact integer-matrix coefficient audit (supplements fiber enumeration).
def check_matrix_coefficients():
    m = ((0,1,0),(0,0,1),(1,1,1))
    ident = ((1,0,0),(0,1,0),(0,0,1))
    def mul(a,b):
        return tuple(tuple(sum(a[i][l]*b[l][j] for l in range(3)) for j in range(3)) for i in range(3))
    def power(n):
        a,b=m,ident
        while n:
            if n & 1: b=mul(b,a)
            a=mul(a,a);n>>=1
        return b
    matrix8=power(8)
    assert matrix8==((13,20,24),(24,37,44),(44,68,81))
    diff=tuple(tuple(matrix8[i][j]-ident[i][j] for j in range(3)) for i in range(3))
    expected={5:(1,115,14946,4,7),7:(3,389,50562,7,7)}
    for residue, (zero,first,second,v3,v4) in expected.items():
        a=power(residue); vals=[]
        for j in range(5):
            z=sum(a[0][i] for i in (1,2)) + (1 if j==0 and residue==5 else 0)
            assert z%8==0
            vals.append(z//8)
            a=mul(a,diff)
        assert vals[:3]==[zero,first,second]
        for j,v in [(3,v3),(4,v4)]:
            assert vals[j] % (1<<(v+1)) == 1<<v
    for s in [4,5,6]:
        a=power(1<<s)
        d=tuple(tuple((a[i][j]-ident[i][j])//(1<<(s-1)) for j in range(3)) for i in range(3))
        assert all((d[i][j]-((1,1,0),(0,1,1),(1,1,2))[i][j])%4==0 for i in range(3) for j in range(3))
    return True

if __name__=='__main__':
    check_matrix_coefficients()
    print('Matrix and coefficient checks passed.')
