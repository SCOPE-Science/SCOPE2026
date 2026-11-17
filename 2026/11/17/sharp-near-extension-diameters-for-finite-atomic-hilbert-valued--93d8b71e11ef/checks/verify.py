from math import sqrt
import random
rng=random.Random(20261110)
assertions=0
for q in (1.1,1.5,1.9,2,2.1,3,4,6,15):
 for n in (2,3,5,11):
  w=[0.1+rng.random() for _ in range(n)]
  w=[v/sum(w) for v in w]
  a=[rng.random() if rng.random()>.15 else 0.0 for _ in range(n)]
  scale=(sum(w[i]*a[i]**q for i in range(n)))**(-1/q)
  a=[v*scale for v in a]
  u=[w[i]*a[i]**q for i in range(n)]
  for R in (1.001,1.05,1.8,4):
   delta=R**q-1
   if q<=2: maximum=sqrt(R**2-1)
   else: maximum=sqrt((min(u)+delta)**(2/q)-min(u)**(2/q))
   for _ in range(250):
    b=[(0.001+rng.random()) for _ in range(n)]
    # scale so norm constraint exactly binding via bisection
    low,hi=0,1
    def cost(t):return sum(w[i]*(a[i]*a[i]+(t*b[i])**2)**(q/2) for i in range(n))
    while cost(hi)<R**q:hi*=2
    for i in range(65):
     mid=(low+hi)/2
     if cost(mid)>R**q:hi=mid
     else:low=mid
    t=(low+hi)/2
    B=(sum(w[i]*(t*b[i])**q for i in range(n)))**(1/q)
    assert B<=maximum+1e-9,(q,n,R,maximum,B)
    assertions+=1
   if q<2:
    b=[sqrt(R*R-1)*v for v in a]
   elif q==2:
    b=[0]*n;b[0]=sqrt((R*R-1)/w[0])
   else:
    j=min(range(n),key=lambda i:u[i]);b=[0]*n
    b[j]=sqrt(((u[j]+delta)**(2/q)-u[j]**(2/q))/w[j]**(2/q))
   cost_b= sum(w[i]*(a[i]*a[i]+b[i]*b[i])**(q/2) for i in range(n))
   norm_b=(sum(w[i]*b[i]**q for i in range(n)))**(1/q)
   assert abs(cost_b-R**q)<1e-10*max(1,R**q),(q,n,R,cost_b)
   assert abs(norm_b-maximum)<1e-8,(q,n,R,norm_b,maximum)
   assertions+=2
print('BOCHNER_HB_SHARP_STRESS_OK',assertions)
