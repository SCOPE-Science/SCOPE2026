"""Independent finite-spectral checks for two-range ring absorption.
Run: python check_resonances.py. Only numpy required.
"""
import math
import numpy as np


def fourier_result(n, r, tol=1e-8):
    E=np.array([2*r*math.cos(2*math.pi*k/n)+2*math.cos(4*math.pi*k/n) for k in range(n)])
    groups=[]
    for k in range(n):
        for group in groups:
            if abs(E[k]-E[group[0]])<tol:
                group.append(k)
                break
        else:
            groups.append([k])
    s=0.
    for ks in groups:
        e=sum(k%2==0 for k in ks)
        o=len(ks)-e
        s+=4*e*o/(n*len(ks))
    return s, groups


def matrix_result(n,r,tol=1e-7):
    H=np.zeros((n,n))
    for j in range(n):
        for hop,value in [(1,r),(-1,r),(2,1.),(-2,1.)]:
            H[j,(j+hop)%n]+=value
    E,U=np.linalg.eigh(H)
    # Within each distinct energy, remove the detector-bright component.
    total=0.
    i=0
    while i<n:
        j=i+1
        while j<n and abs(E[j]-E[i])<tol:
            j+=1
        B=U[:,i:j]
        trap=B[0,:]
        src=B[n//2,:]
        total += src@src - (src@trap)**2/(trap@trap)
        i=j
    return total


count=0
for n in range(6,51,2):
    r=4*math.cos(math.pi/n)**2
    p,groups=fourier_result(n,r,1e-7)
    target=8/(3*n)
    assert abs(p-target)<1e-10, (n,p,target,groups)
    count+=1
    for rr,target_p in [(4.2,0), (r+0.003,0), (r-0.003,None), (r, target)]:
        pF,_=fourier_result(n,rr,1e-8)
        if target_p is not None:
            assert abs(pF-target_p)<1e-10, (n,rr,pF,target_p)
        pM=matrix_result(n,rr,1e-7)
        assert abs(pF-pM)<3e-8,(n,rr,pF,pM)
        count+=1
print('PASS:',count,'independent spectral/grouping checks, including first resonance all even n=6..50')
for n in [6,8,10,12,14,20,30]:
    r=4*math.cos(math.pi/n)**2
    print('n=',n,' J2/J1=',round(1/r,8),' tuned antipodal survival=',round(fourier_result(n,r)[0],12))
