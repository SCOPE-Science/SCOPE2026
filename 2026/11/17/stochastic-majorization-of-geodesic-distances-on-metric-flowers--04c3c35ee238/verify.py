"""Independent numerical checks for stochastic ordering of metric-flower distances.
Uses direct integration of conditional distance kernels, not the derivative proof.
"""
from fractions import Fraction as F
from random import Random

def plus(x): return max(x,F(0))

def within(a,t):
    # ordered pairs on a single loop, arclength squared
    return a*plus(a-2*t)

def cross(a,b,t):
    # ordered endpoints on distinct loops, quadrant triangle complement
    c=2*t
    return a*b-(c*c-plus(c-a)**2-plus(c-b)**2-plus(c-a-b)**2)/2

def tail(vec,t):
    L=sum(vec)
    numerator=sum(within(a,t) for a in vec)
    numerator+=sum(2*cross(vec[i],vec[j],t) for i in range(len(vec)) for j in range(i+1,len(vec)))
    return numerator/(L*L)

def numeric(a,b,t,step=400):
    # direct grid for the distance for two independently chosen points on 2 petals
    N=step
    L=a+b
    N2=0
    lengths=[float(a),float(b)]
    for i,li in enumerate(lengths):
      for j,lj in enumerate(lengths):
        for u in range(N):
          x=(u+.5)*li/N
          for v in range(N):
            y=(v+.5)*lj/N
            d=min(abs(x-y),li-abs(x-y)) if i==j else min(x,li-x)+min(y,lj-y)
            if d>float(t): N2+=li*lj/(N*N)
    return N2/float(L*L)

def main():
    r=Random(20261108)
    cases=0
    for m in range(2,9):
        for _ in range(60):
            v=[F(r.randint(1,40),13) for _ in range(m)]
            i,j=r.sample(range(m),2)
            if v[i] < v[j]:i,j=j,i
            eps=F(r.randint(1,30),1000)
            w=list(v);w[i]+=eps;w[j]-=eps
            if w[j]<=0: continue
            for k in range(51):
                t=sum(v)*F(k,100)
                assert tail(w,t)>=tail(v,t),(m,v,w,t,tail(w,t),tail(v,t))
                cases+=1
    # Direct Riemann integrals on a separate exact grid compare sufficiently far from kinks
    for a,b,t in [(F(3),F(2),F(1,4)),(F(3),F(2),F(3,4)),(F(3),F(2),F(7,4))]:
        exact=float(tail([a,b],t))
        sim=numeric(a,b,t,400)
        assert abs(exact-sim)<.005,(a,b,t,exact,sim)
    # strict inequality at one threshold for a nontrivial length transfer
    a,b=F(3),F(1);t=F(3,4)
    assert tail([a+F(1,8),b-F(1,8)],t)>tail([a,b],t)
    print('METRIC_FLOWER_STOCHASTIC_SCHUR_OK',cases)

if __name__=='__main__': main()
