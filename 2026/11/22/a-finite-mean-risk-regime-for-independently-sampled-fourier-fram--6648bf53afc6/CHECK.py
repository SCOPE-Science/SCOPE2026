"""Supplementary finite checks for uniform circle Fourier frame bounds.

These checks do not prove the infinite probability assertions; see RESULT.md.
"""
import math
import numpy as np

def check():
    rng = np.random.default_rng(20261116)
    count = 0
    for n in range(3, 9):
        B2 = math.comb(2*n-2, n-1)
        assert sum(math.comb(n-1,j)**2 for j in range(n)) == B2
        count += 1
        for trial in range(200):
            z = np.exp(2j*math.pi*rng.uniform(size=3*n))
            matrices = [np.vander(z[q*n:(q+1)*n], n, increasing=True) for q in range(3)]
            G = sum((V.conj().T@V for V in matrices))
            lows = [np.linalg.eigvalsh(V.conj().T@V)[0] for V in matrices]
            eig = np.linalg.eigvalsh(G)[0]
            assert eig >= sum(lows)-1e-9
            count += 1
            V = matrices[0]
            inv = np.linalg.inv(V)
            coef = []
            for i in range(n):
                other = np.delete(z[:n], i)
                poly = np.array([1+0j])
                for a in other:
                    poly = np.convolve(poly, np.array([-a,1]))
                poly = poly/np.prod(z[i]-other)
                coef.append(poly)
            assert np.max(abs(inv-np.array(coef).T)) < 2e-5
            # The coefficient bound is derived from elementary symmetric sums.
            den = [np.prod(abs(z[i]-np.delete(z[:n], i))) for i in range(n)]
            assert np.linalg.norm(inv,'fro') <= math.sqrt(B2)*math.sqrt(sum(1/x**2 for x in den))*(1+1e-7)
            count += 2
            a = np.array([math.comb(n-1,j)*(-z[0])**(n-1-j) for j in range(n)])
            assert abs(np.vdot(a,a)-B2)<1e-6
            count+=1
    for u in np.linspace(0,1,101):
        assert 2/math.pi*math.asin(u) <= u+1e-12
        count+=1
    for integer_shape in range(1,9):
        for t in np.linspace(0,20,101):
            v = math.exp(-t)*sum(t**j/math.factorial(j) for j in range(integer_shape))
            assert 0<=v<=1+1e-12
            count+=1
    print('CHECK_OK assertions=',count,'dimensions=3..8')

if __name__=='__main__':
    check()
