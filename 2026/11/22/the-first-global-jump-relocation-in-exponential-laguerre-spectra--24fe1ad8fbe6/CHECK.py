#!/usr/bin/env python3
"""Standard-library exact rational certificate for finite Laguerre jump geometry."""
from fractions import Fraction as F
from math import comb,factorial

D=10**11
CRIT={
0:[],
1:[(99999999999,100000000001),(199999999999,200000000001)],
2:[(58578643762,58578643763),(126794919243,126794919244),(341421356237,341421356238),(473205080756,473205080757)],
3:[(41577455678,41577455679),(93582222752,93582222753),(229428036027,229428036028),(330540728933,330540728934),(628994508293,628994508294),(775877048314,775877048315)],
4:[(32254768961,32254768962),(74329192798,74329192799),(174576110115,174576110116),(257163500764,257163500765),(453662029692,453662029693),(573117875168,573117875169),(939507091230,939507091231),(1095389431268,1095389431269)],
5:[(26356031971,26356031972),(61703085327,61703085328),(141340305910,141340305911),(211296595857,211296595858),(359642577104,359642577105),(461083315101,461083315102),(708581000585,708581000586),(839906697120,839906697121),(1264080084427,1264080084428),(1426010306592,1426010306593)]}
ROOTS={
0:[(69314718055,69314718056)],
1:[(41504274311,41504274312)],
2:[(30168017467,30168017468)],
3:[(23879308268,23879308269),(85809287527,85809287528),(101588948083,101588948084)],
4:[(19842366797,19842366798),(55792331387,55792331388),(94875888205,94875888206)],
5:[(17016314242,17016314243),(42299589373,42299589374),(84075143713,84075143714)]}

def clean(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a

def add(a,b):
 return clean([ (a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))])

def sub(a,b):return add(a,[-v for v in b])

def mul(a,b):
 v=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):v[i+j]+=x*y
 return clean(v)

def der(a):return clean([a[i]*i for i in range(1,len(a))] or [F(0)])

def lag(k):return [F((-1)**j*comb(k,j),factorial(j)) for j in range(k+1)]

def polys(n):
 L=[lag(k) for k in range(n+1)]
 Q=[F(1)];B=[F(1)]
 for k in range(1,n+1):
  d=sub(L[k],L[k-1]);Q=add(Q,mul(d,L[k]));B=add(B,mul(d,d))
 assert clean(sub(Q,sub(B,[a/F(2) for a in der(B)])))==[F(0)]
 return Q,B,sub(der(Q),Q)

def evalp(p,t):
 v=F(0)
 for a in reversed(p):v=v*t+a
 return v

def Iadd(a,b):return(a[0]+b[0],a[1]+b[1])
def Imul(a,b):
 vals=[x*y for x in a for y in b]
 return(min(vals),max(vals))
def Ieval(p, t):
 v=(F(0),F(0))
 for a in reversed(p):v=Iadd(Imul(v,t),(a,a))
 return v

def exp_bounds(t):
 assert t>=0 and t< F(20)
 M=120
 term=F(1);s=term
 for k in range(1,M+1):
  term=term*t/k;s+=term
 next_term=term*t/F(M+1)
 ratio=t/F(M+2)
 return (s, s+next_term/(1-ratio))

def expI(t):return(exp_bounds(t[0])[0],exp_bounds(t[1])[1])
def negexpI(t):
 e=expI(t)
 return F(1)/e[1],F(1)/e[0]
def hI(Q,t):return Imul(Ieval(Q,t),negexpI(t))
def rI(B,t):
 u=negexpI(t);u2=Imul(u,u)
 b=Ieval(B,t);v=Imul(u2,b)
 return (u[0]-v[1],u[1]-v[0])

def bracket(v):return (F(v[0],D),F(v[1],D))

def certify():
 count=0
 for n in range(6):
  Q,B,A=polys(n)
  assert len(A)-1==2*n
  crit=[bracket(v) for v in CRIT[n]]
  root=[bracket(v) for v in ROOTS[n]]
  assert len(crit)==2*n
  assert all(crit[i][1]<crit[i+1][0] for i in range(len(crit)-1))
  for a,b in crit:
   assert evalp(A,a)*evalp(A,b)<0,(n,float(a),float(b))
   count+=1
  # The polynomial A of degree 2n has exactly these distinct positive roots.
  statuses=[]
  for t in crit:
   h=hI(Q,t)
   assert h[0]>F(1,2) or h[1]<F(1,2),('critical undecided',n,tuple(map(float,h)))
   statuses.append('+' if h[0]>F(1,2) else '-')
   count+=1
  print('n',n,'critical h-1/2:', ''.join(statuses))
  # H=exp(-t)Q(t) starts above 1/2 and ends below;
  # between critical points it is strictly monotone.
  allstatus=['+']+statuses+['-']
  crossings=[i for i in range(len(allstatus)-1) if allstatus[i]!=allstatus[i+1]]
  assert len(crossings)==len(root),(n,crossings,len(root))
  for i,t in enumerate(root):
   a,b=t
   left=hI(Q,(a,a));right=hI(Q,(b,b))
   assert (left[0]>F(1,2) and right[1]<F(1,2)) or (left[1]<F(1,2) and right[0]>F(1,2)),('root fail',n,i,tuple(map(float,left)),tuple(map(float,right)))
   assert (i==0 or root[i-1][1]<a)
   count+=1
  values=[rI(B,t) for t in root]
  best_index=max(range(len(values)),key=lambda i:(values[i][0]+values[i][1])/2)
  assert all(values[best_index][0]>v[1] for j,v in enumerate(values) if j!=best_index),(n,[(float(a),float(b)) for a,b in values])
  assert best_index== (2 if n==5 else 0),(n,best_index)
  print('  critical t range', [(round(float(t[0]),11),round(float(t[1]),11)) for t in root])
  print('  maxima squared', [(round(float(lo),12),round(float(hi),12)) for lo,hi in values], 'winner',best_index)
  count+=len(values)
 print('LAGUERRE_EXACT_CERTIFICATE_PASSED',count)

if __name__=='__main__':certify()
