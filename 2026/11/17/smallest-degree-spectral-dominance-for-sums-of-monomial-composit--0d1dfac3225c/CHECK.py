"""Finite diagnostics for logarithmic coefficient-space composition operators.

Run with: python CHECK.py. The output is not a proof of the asymptotic theorem.
"""
import math
import numpy as np

def r(d, n, c, g):
    return math.exp(-0.5*c*(math.log(d*n+1)**g - math.log(n+1)**g))

def test(c, g, coeff, N=80):
    degrees=sorted(coeff)
    M=max(degrees)*N
    matrix=np.zeros((M,N),dtype=complex)
    for j in range(1,N+1):
        for d in degrees:
            matrix[d*j-1,j-1]+=coeff[d]*r(d,j,c,g)
    column_energy=sum(abs(coeff[d])**2*sum(r(d,j,c,g)**2 for j in range(1,N+1)) for d in degrees)
    assert abs(np.linalg.norm(matrix,'fro')**2-column_energy)<1e-10*max(column_energy,1)
    sv=np.linalg.svd(matrix,compute_uv=False)
    assert np.all(sv[:-1]+1e-12 >= sv[1:])
    assert np.all(sv > 0)
    print('finite matrix',g,'columns',N,'frobenius and ordering PASS', 'ratio at index 40',float(sv[39]/(abs(coeff[min(degrees)])*r(min(degrees),40,c,g))))

for g in (1.4,2,2.8):
    test(1,g,{2:1+0j,3:0.7-0.3j},80)

c=0.8; d=2; p=1/(c*math.log(d))
for n in (1000,10000,1000000):
    v=n*r(d,n,c,2)**p
    assert abs(v-d**(-0.5)) < 0.01
    print('critical tail',n,'rescaled',v)
print('Supplementary diagnostics passed; infinite claims require the analytic proof.')
