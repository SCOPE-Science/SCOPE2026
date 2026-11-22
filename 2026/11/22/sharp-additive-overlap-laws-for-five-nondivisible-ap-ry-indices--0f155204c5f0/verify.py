from fractions import Fraction

def digits(n):
 a=[]
 while n: a.append(n%5); n//=5
 return a

def good(n):
 return all(d%2==0 for d in digits(n))

WEIGHTS=((3,1),(1,2),(2,2),(2,1),(1,3))
def val(h):
 if h==0: return Fraction(1)
 D=digits(h);c=0;z=1
 for d in D:
  z*=WEIGHTS[d][c]
  c^=d%2
 return Fraction(z,3**len(D)) if c==0 else Fraction(0)

def family(h):
 D=digits(h)
 nz=[i for i,d in enumerate(D) if d]
 if len(nz)==1 and D[nz[0]]==2: return 'first'
 if len(nz)==2 and all(D[i]==2 for i in nz): return 'second_A'
 i=nz[0];j=nz[-1]
 if D[i]==3 and D[j]==1 and i<j and all(D[t]==4 for t in range(i+1,j)):
  return 'second_B'
 return ''

# The carry table is also checked from the raw digit-addition rule.
for d in range(5):
 for c in (0,1):
  options=[]
  for x in (0,2,4):
   q,t=divmod(x+d+c,5)
   if t in (0,2,4): options.append((q,t))
  assert len(options)==WEIGHTS[d][c],(d,c,options)
  assert all(q==((d+c)%2) for q,t in options)
print('all ten carry weights checked by digit enumeration')

for r in range(1,6):
 b=5**r
 good_arr=[good(n) for n in range(b+b//2+2)]
 for h in range(0,min(b//2,200)):
  direct=sum(good_arr[n] and good_arr[n+h] for n in range(b))
  want=val(h)*3**r
  assert direct==want,(r,h,direct,want)
print('all exact sparse-shift counts checked for depths 1..5')
for h in range(1,5**7):
 x=val(h)
 assert x<=Fraction(2,3),h
 assert (x==Fraction(2,3))==(family(h)=='first'),('first',h,x)
 assert (x==Fraction(4,9))==(family(h).startswith('second')),('second',h,x)
 assert x<=Fraction(4,9) or family(h)=='first',('gap',h,x)
print('sharp maximum/runner-up classifications verified h<78125')

A0=1;A1=5
A=[A0,A1]
for n in range(1,300):
 numerator=(2*n+1)*(17*n*(n+1)+5)*A[n] - n**3*A[n-1]
 assert numerator%(n+1)**3==0
 A.append(numerator//(n+1)**3)
for n in range(301):
 assert (A[n]%5!=0)==good(n),(n,A[n]%5)
print('direct Apéry three-term recurrence 301 values matches digit condition')
print('selected exact relative overlaps:', [(h,str(val(h))) for h in [0,1,2,3,4,5,6,8,10,12,16,18,48,50,52]])
