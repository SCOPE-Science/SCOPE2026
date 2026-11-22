"""Independent numerical checks for conditional shape law of random cyclic triangles."""
import math,random
random.seed(20261112)
for t in [0.03,0.01,0.003]:
    n=650000
    counts=0; urange=[0]*5; wrange=[0]*5; corner=[0]*3
    for _ in range(n):
        a,b=sorted((random.random(),random.random()))
        gaps=[a,b-a,1-b]
        angles=[g*math.pi/2 for g in gaps]
        r=4*math.prod(math.sin(x) for x in angles)
        if r<t:
            counts+=1
            i=max(range(3),key=lambda j:angles[j]);corner[i]+=1
            u=math.log(angles[(i+1)%3])/math.log(t)
            w=r/t
            if 0<=u<1: urange[min(4,int(5*u))]+=1
            if 0<=w<1: wrange[min(4,int(5*w))]+=1
    expected=6/math.pi**2*t*math.log(1/t)
    print('t',t,'samples',n,'events',counts,'ratio',round(counts/n/expected,3),'corners',corner,
          'u_bins',urange,'w_bins',wrange)
