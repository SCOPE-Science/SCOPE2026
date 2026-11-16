"""Independent finite checks for orthogonal DCT-I two-erasure theorem.
Run: python3 check_dct1.py
This code reports consistency tests; the proof for all orders is analytical.
"""
import itertools
import math
import numpy as np


def orthogonal_dct_i(n):
    w = np.ones(n+1)
    w[0] = w[n] = 0.5
    theta = np.pi*np.arange(n+1)/n
    frequencies = np.arange(n+1)
    return np.sqrt(2/n)*np.sqrt(w[:,None]*w[None,:])*np.cos(theta[:,None]*frequencies[None,:])


def predicted(n, j, k):
    xj = math.cos(math.pi*j/n)
    xk = math.cos(math.pi*k/n)
    wj = 0.5 if j in (0,n) else 1.
    wk = 0.5 if k in (0,n) else 1.
    t = wj*(xj*xj+0.5)+wk*(xk*xk+0.5)
    a = wj*xj*xj+wk*xk*xk
    c = 0.5*(wj+wk)
    b = (wj*xj+wk*xk)/math.sqrt(2)
    # Compute discriminant as sum of squares to avoid cancellation at repeated eigenvalues.
    sqrt_disc = math.hypot(a-c,2*b)
    small = (2*wj*wk*(xj-xk)**2)/(n*(t+sqrt_disc))
    large = (t+sqrt_disc)/n
    return small, large


def endpoint_small(n):
    c = math.cos(math.pi/n)
    t = 1.25 + c*c
    delta = 2*math.sin(math.pi/(2*n))**2
    return (delta*delta)/(n*(t+math.sqrt(t*t-delta*delta)))


def main():
    assertions = 0
    smallest_error = 0.0
    for n in range(4, 53):
        q = orthogonal_dct_i(n)
        assert np.linalg.norm(q.T@q-np.eye(n+1),ord=np.inf)<4e-12
        assertions += 1
        minima=[]
        for j,k in itertools.combinations(range(n+1),2):
            small, large = predicted(n,j,k)
            b = q[np.ix_([j,k],[n-1,n])]
            sb = np.linalg.svd(b,compute_uv=False)**2
            tolerance = 4e-12
            assert abs(min(sb)-small)<tolerance,(n,j,k,'complement mismatch')
            assert abs(max(sb)-large)<tolerance,(n,j,k,'complement mismatch')
            assertions += 2
            if n<=20:
                a = q[np.ix_([i for i in range(n+1) if i not in (j,k)],range(n-1))]
                sa = np.linalg.svd(a,compute_uv=False)**2
                assert abs(min(sa)-small)<tolerance,(n,j,k,'direct mismatch')
                assert abs(max(sa)-1.)<tolerance,(n,j,k,'max mismatch')
                assertions +=2
            minima.append((small,j,k))
        minima.sort()
        exact=endpoint_small(n)
        actual_small=min(s for s,_,_ in minima)
        assert abs(actual_small-exact)<2e-15
        assertions +=1
        # Only the reflection-related endpoint pairs attain the least value.
        extremal=[(j,k) for small,j,k in minima if abs(small-actual_small)<1e-16]
        assert set(extremal)=={(0,1),(n-1,n)},(n,extremal)
        assertions +=1
        smallest_error=max(smallest_error,abs(actual_small-exact))
    for n in (101,251,501,1001,3001):
        qmin = endpoint_small(n)
        predicted_constant=n**5*qmin
        assert abs(predicted_constant-math.pi**4/18)<2e-3, (n,predicted_constant)
        assertions+=1
    print('PASS: %d assertions; max endpoint discrepancy %.3e' % (assertions,smallest_error))
    print('n=1001: n^5 * lambda_min = %.12f; limit pi^4/18 = %.12f'% (1001**5*endpoint_small(1001),math.pi**4/18))

if __name__=='__main__':
    main()
