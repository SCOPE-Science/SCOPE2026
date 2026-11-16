#!/usr/bin/env python3
"""Independent discrete Fourier and analytic-form checks for half-radius Lee disks."""
import cmath, math
import numpy as np


def asserted(n):
    assert n%2==1 and n>=3
    r=(n-1)//2
    z=np.zeros((n,n),dtype=float)
    for x in range(n):
        for y in range(n):
            if min(x,n-x)+min(y,n-y)<=r:
                z[x,y]=1
    fft=np.fft.fft2(z)
    threshold=1/(2*math.cos(math.pi/n))
    assert int(z.sum())==(n*n+1)//2
    expected=[]
    for k in range(n):
        for l in range(n):
            if k==l==0:
                a=(n*n+1)/2
            elif (k+l)%2==0:
                a=(-1)**k/(math.cos(math.pi*k/n)+math.cos(math.pi*l/n))
            else:
                a=(-1)**(k+1)/(math.cos(math.pi*l/n)-math.cos(math.pi*k/n))
            assert abs(fft[k,l]-a)<3e-7, ('formula',n,k,l,fft[k,l],a)
            expected.append(a)
    assert abs(min(abs(x) for x in expected)-threshold)<2e-10, ('minimum',n)
    minimum_indices={(k,l) for k in range(n) for l in range(n) if abs(abs(fft[k,l])-threshold)<1e-8}
    target={(1,1),(1,n-1),(n-1,1),(n-1,n-1)}
    assert minimum_indices==target, ('extremizers',n,minimum_indices,target)
    return n*n, float(np.max(np.abs(fft))/np.min(np.abs(fft)))

def main():
    trials=0
    for n in range(3,102,2):
        n2,condition=asserted(n)
        assert abs(condition-(n*n+1)*math.cos(math.pi/n))<5e-7
        trials+=n2
    print('PASS: 50 odd moduli from 3 to 101,',trials,'individual spectral formula comparisons; exact four minimizer characters and condition numbers.')

if __name__=='__main__': main()
