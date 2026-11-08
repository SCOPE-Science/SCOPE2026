"""Independent renewal-cycle simulation of occupation moments; no external packages."""
from math import comb
from random import Random
from check import Q, moments, forward

def main():
    rng=Random(20260706)
    b_atoms=[(1.0,0.4),(2.0,0.6)]
    a_atoms=[(0.5,0.2),(0.25,0.5),(0.125,0.3)]
    b=moments([(Q(1),Q(2,5)),(Q(2),Q(3,5))],4)
    a=moments([(Q(1,2),Q(1,5)),(Q(1,4),Q(1,2)),(Q(1,8),Q(3,10))],3)
    H,F,v=forward(b,a,3)
    U=0.0; raw=[0.0,0.0,0.0]; total=0.0
    for i in range(180000):
        B=1.0 if rng.random()<0.4 else 2.0
        A=0.5 if (t:=rng.random())<0.2 else 0.25 if t<0.7 else 0.125
        if i>200:
            total+=B
            for k in range(1,4):
                raw[k-1]+=((U+B)**(k+1)-U**(k+1))/(k+1)
        U=A*(U+B)
    for k in range(1,4):
        est=raw[k-1]/total
        ref=float(F[k])
        print('off variance-excess moment',k,'cycle-average',round(est,7),'exact',round(ref,7),'relative',round(abs(est/ref-1),5))
        assert abs(est-ref)/ref<0.025
    print('simulation corroborated')
if __name__=='__main__':main()
