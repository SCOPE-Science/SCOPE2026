from fractions import Fraction as F
import random

def gcm(x,y):
 n=len(x); hull=[]
 for i in range(n):
  while len(hull)>1:
   a,b=hull[-2:]
   if (y[b]-y[a])*(x[i]-x[b]) <= (y[i]-y[b])*(x[b]-x[a]): break
   hull.pop()
  hull.append(i)
 out=[None]*n
 for a,b in zip(hull,hull[1:]):
  for j in range(a,b+1):out[j]=y[a]+(y[b]-y[a])*(x[j]-x[a])/(x[b]-x[a])
 return out,hull

def tv(y,w):return sum(w[i]*abs(y[i+1]-y[i]) for i in range(len(w)))

def formula(x,w):
 N=len(x);R=F(1); arg=(0,1)
 for a in range(N-1):
  for b in range(a+1,N):
   av=sum(w[i]*(x[i+1]-x[i]) for i in range(a,b))/(x[b]-x[a]);k=av/min(w[a:b])
   if k>R:R,arg=k,(a,b)
 return R,arg

def witness(x,w,a,b):
 n=len(x)
 q=[v*v for v in x];Y=q[:]
 M=1+max([q[a]+(q[b]-q[a])*(x[i]-x[a])/(x[b]-x[a])-q[i] for i in range(a+1,b)] or [F(0)])
 for i in range(a+1,b):Y[i]=q[a]+(q[b]-q[a])*(x[i]-x[a])/(x[b]-x[a])+M
 h=[F(0)]*n
 j=min(range(a,b),key=lambda j:w[j]);h=[F(i>j) for i in range(n)]
 eps=F(1,10000);Yp=[u+eps*t for u,t in zip(Y,h)]
 out0,H0=gcm(x,Y);out1,H1=gcm(x,Yp)
 return tv([a-b for a,b in zip(out1,out0)],w)/tv([a-b for a,b in zip(Yp,Y)],w),H0,H1,j

def test():
 # Exact rational testing avoids numerical tolerance in sharpness comparisons.
 random.seed(109)
 cases=0; exact=0
 for n in range(2,11):
  for _ in range(100):
   increments=[F(random.randint(1,8)) for __ in range(n-1)];x=[F(0)];
   for h in increments:x.append(x[-1]+h)
   w=[F(random.randint(1,12)) for __ in range(n-1)]
   K,(a,b)=formula(x,w)
   ratio,H0,H1,j=witness(x,w,a,b)
   assert K==ratio,(n,x,w,K,ratio,a,b,H0,H1)
   exact+=1
   y=[F(random.randint(-25,25)) for __ in range(n)];z=[F(random.randint(-25,25)) for __ in range(n)]
   gy,_=gcm(x,y);gz,_=gcm(x,z)
   if tv([u-v for u,v in zip(y,z)],w)>0:
    assert tv([u-v for u,v in zip(gy,gz)],w)<=K*tv([u-v for u,v in zip(y,z)],w),(x,w,y,z)
   cases+=1
 print('EXACT_RATIONAL_SHARPNESS_WITNESSES_PASS',exact)
 print('RANDOM_TWO_INPUT_WEIGHTED_VARIATION_BOUND_PASS',cases)
 # Explicit nonuniform-mesh example with exact optimal amplification five.
 x=list(map(F,[0,1,3,4]));w=list(map(F,[1,7,1]));k,(a,b)=formula(x,w)
 assert k==5 and (a,b)==(0,2)
 ratio,H0,H1,j=witness(x,w,a,b)
 assert ratio==5 and H0==H1==[0,2,3] and j==0
 print('NONUNIFORM_MESH_EXACT_GAIN_FIVE_PASS')
 print('ALL_GCM_WEIGHTED_VARIATION_CHECKS_PASS')
if __name__=='__main__':test()
