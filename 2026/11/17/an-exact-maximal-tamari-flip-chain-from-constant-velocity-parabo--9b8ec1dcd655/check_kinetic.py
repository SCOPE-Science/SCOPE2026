import itertools
from fractions import Fraction

def del_tri(xs):
 n=len(xs); out=[]
 for a,b,c in itertools.combinations(range(n),3):
  # direct circumcircle equation: (x_i-x_a) u +(y_i-y_a) v= -(norm_i -norm_a) with circle x^2+y^2+ux+vy+w=0
  # use rational arithmetic
  xi,xj,xk=(xs[i] for i in (a,b,c)); yi,yj,yk=(x*x for x in (xi,xj,xk))
  A=xj-xi;B=yj-yi;C=-(xj*xj+yj*yj-xi*xi-yi*yi)
  D=xk-xi;E=yk-yi;F=-(xk*xk+yk*yk-xi*xi-yi*yi)
  det=A*E-B*D
  u=(C*E-B*F)/det; v=(A*F-C*D)/det
  w=-(xi*xi+yi*yi+u*xi+v*yi)
  if all(xs[t]*xs[t]+xs[t]**4+u*xs[t]+v*xs[t]**2+w > 0 for t in range(n) if t not in (a,b,c)):
   out.append((a,b,c))
 return set(out)

def edges(tris):
 from collections import Counter
 c=Counter(tuple(sorted(e)) for t in tris for e in itertools.combinations(t,2))
 return {e for e,num in c.items() if num==2}

for n in range(4,9):
 a=[3**i for i in range(n)]
 all_events={sum(a[x] for x in (i,i+1,j,j+1)):(i,j) for i in range(n-3) for j in range(i+2,n-1)}
 assert len(all_events)==(n-2)*(n-3)//2
 ss=sorted(all_events,reverse=True)
 periods=[2*ss[0]+1]+[ss[k]+ss[k+1] for k in range(len(ss)-1)]+[2*ss[-1]-1]
 tris=[]
 for j,u in enumerate(periods):
  # x_i=2a_i +u/2 corresponding h=u/2, event at h=-sum a_i/4 => u=-sum a_i/2. easier use x_i=8a_i + U, U = -(sum_i + sum_j); event U=-2*sum a. 
  U=-u
  xx=[Fraction(8*z+U,1) for z in a]
  ts=del_tri(xx)
  assert len(ts)==n-2,(n,U,len(ts))
  tris.append(ts)
 assert edges(tris[0])=={(i,n-1) for i in range(1,n-2)}
 assert edges(tris[-1])=={(0,i) for i in range(2,n-1)}
 for k,s in enumerate(ss):
  before=edges(tris[k]);after=edges(tris[k+1]);deld=before-after;add=after-before
  i,j=all_events[s]; assert deld=={(i+1,j+1)},(n,k,s,i,j,deld,add)
  assert add=={(i,j)},(n,k,s,i,j,deld,add)
 print('OK n=',n,'flips',len(ss), 'end fans',sorted(edges(tris[0])), sorted(edges(tris[-1])))

print('PARABOLIC_KINETIC_DELAUNAY_CHECKS_OK')
