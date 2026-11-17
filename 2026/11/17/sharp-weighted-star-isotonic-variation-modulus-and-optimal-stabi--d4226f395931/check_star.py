from fractions import Fraction as Q
from itertools import combinations,product
from random import Random

def iso(x,mu):
    m=len(x)-1
    order=sorted(range(m),key=lambda i:x[i+1]); s=mu[0]*x[0]; M=mu[0]
    for k in range(m+1):
        c=s/M
        if (k==0 or x[1+order[k-1]]<=c) and (k==m or c<=x[1+order[k]]):
            return [c]+[max(x[i+1],c) for i in range(m)]
        if k<m:
            s+=mu[1+order[k]]*x[1+order[k]];M+=mu[1+order[k]]
    raise RuntimeError('no threshold')

def tv(d,v):return sum(v[i]*abs(d[i+1]-d[0]) for i in range(len(v)))
def formula(mu,v):
    return max([Q(1)]+[mu[i+1]*sum(v[j] for j in range(len(v)) if i!=j)/(v[i]*(mu[0]+mu[i+1])) for i in range(len(v))])

def face_norms(mu,v):
    m=len(v);out=[]
    for mask in range(2**m):
        S={i for i in range(m) if mask>>i&1}
        den=mu[0]+sum(mu[i+1] for i in S)
        vals=[Q(1) for j in range(m) if j not in S]
        vals.extend(mu[i+1]*sum(v[j] for j in range(m) if j not in S)/(den*v[i]) for i in S)
        out.append(max(vals+[Q(0)]))
    return max(out)

rng=Random(2440); count=0
for m in range(2,9):
 for trial in range(40):
  mu=[Q(rng.randint(1,15)) for _ in range(m+1)];v=[Q(rng.randint(1,15)) for _ in range(m)]
  L=formula(mu,v); assert face_norms(mu,v)==L
  for i in range(m):
   x=[Q(0)]+[Q(2) for _ in range(m)];x[i+1]=Q(-2)
   eps=Q(1,1000)
   y=x.copy();y[i+1]+=eps
   a=iso(x,mu);b=iso(y,mu)
   r=tv([a[j]-b[j] for j in range(m+1)],v)/tv([x[j]-y[j] for j in range(m+1)],v)
   target=mu[i+1]*sum(v[j] for j in range(m) if j!=i)/(v[i]*(mu[0]+mu[i+1]))
   assert r==target,(m,mu,v,i,r,target)
   count+=1
  for j in range(35):
   x=[Q(rng.randrange(-20,21),5) for _ in range(m+1)]
   y=[Q(rng.randrange(-20,21),5) for _ in range(m+1)]
   dx=[a-b for a,b in zip(x,y)]; V=tv(dx,v)
   if V:
    Fx,Fy=iso(x,mu),iso(y,mu)
    assert tv([a-b for a,b in zip(Fx,Fy)],v)<=L*V,(m,mu,v,x,y)
   count+=1
 for m0 in [1,2,4,7,16]:
  mu=[Q(m0)]+[Q(1)]*m; v=[Q(1)]*m
  target=max(Q(1),Q(m-1,m0+1))
  assert formula(mu,v)==target
print('EXACT_RATIONAL_FACE_AND_PAIR_TESTS_PASS',count)
for m in range(2,13):
 mu=[Q(1)]*(m+1);v=[Q(1)]*m
 assert formula(mu,v)==max(Q(1),Q(m-1,2))
print('UNIFORM_BRANCHING_THRESHOLD_2_TO_12_PASS')
