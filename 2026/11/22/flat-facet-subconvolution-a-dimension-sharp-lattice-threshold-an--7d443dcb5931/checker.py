"""Supplementary numerical checks for cube-norm lattice Fourier weights.
No finite test is used as a proof of the asymptotic or boundedness theorem.
"""
import math
import itertools

def ridge(d,N,p):
    return (N+1.)**p * sum((2*min(j,N-j)+1)**(d-1) /((j+1.)**p*(N-j+1.)**p) for j in range(N+1))

def approx(d,N,p,a,extra=14):
    B=N+extra
    s=0.
    for k in itertools.product(range(-B,B+1),repeat=d):
        r=max(abs(x) for x in k)
        t=max(abs((N if i==0 else 0)-x) for i,x in enumerate(k))
        s+=math.exp(-a*(r+t-N))*((N+1.)/((r+1.)*(t+1.)))**p
    return s

def test():
    cases=[(2,20,2.,1.),(2,50,2.,1.),(2,100,2.,1.),(2,100,2.,.6), (2,40,1.,1.),(3,12,3.,1.),(3,20,3.,1.)]
    for d,N,p,a in cases:
        full=approx(d,N,p,a)
        main=ridge(d,N,p)
        assert full+1e-9>=main
        assert math.isfinite(full)
        if p==d:
            print(f'd={d},N={N},a={a}, full/logN={full/math.log(N):.5f}, ridge/logN={main/math.log(N):.5f}, off={full-main:.5f}, target={2**d}')
        else: print(f'd={d},N={N},p={p}, full={full:.5f}, ridge={main:.5f}')
    # Independently count norm equality (zero exponential excess) on sample boxes.
    for d in (2,3):
        for N in (2,3,6):
            count=0
            for k in itertools.product(range(-N,N+1),repeat=d):
                r=max(abs(x) for x in k)
                s=max(abs((N if i==0 else 0)-x) for i,x in enumerate(k))
                if r+s==N:count+=1
            formula=sum((2*min(j,N-j)+1)**(d-1) for j in range(N+1))
            assert count==formula,(d,N,count,formula)
    print('all finite geometry checks passed')
if __name__=='__main__':test()
