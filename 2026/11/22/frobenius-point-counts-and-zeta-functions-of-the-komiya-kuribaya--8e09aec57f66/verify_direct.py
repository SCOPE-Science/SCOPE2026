import sys
sys.path.insert(0,'/tmp')
from kkcore import L

def count_direct(p):
 def root(a):return next((j for j in range(p) if j*j%p==a%p),None)
 ir,rr=root(-1),root(5)
 if ir is None:
  d=p-1; I=(0,1);R=(0,root(-5)) if rr is None else (rr,0)
 else:
  I=(ir,0);d=5 if rr is None else 1;R=(0,1) if rr is None else (rr,0)
 assert R[1] is not None
 def mm(a,b):return ((a[0]*b[0]+d*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
 IR=mm(I,R)
 def conv(c):return ((c[0]+c[1]*I[0]+c[2]*R[0]+c[3]*IR[0])%p,(c[1]*I[1]+c[2]*R[1]+c[3]*IR[1])%p)
 V=[tuple(conv(c) for c in l) for l in L]
 P=[(1,a,b) for a in range(p) for b in range(p)] +[(0,1,a) for a in range(p)] +[(0,0,1)]
 def point_on(l,pt):
  return (sum(l[j][0]*pt[j] for j in range(3))%p==0 and sum(l[j][1]*pt[j] for j in range(3))%p==0)
 return sum(any(point_on(l,pt) for l in V) for pt in P)
for p in [7,11,13,17,29,37,89]:
 ans=count_direct(p)
 print('p',p,'points',ans)
