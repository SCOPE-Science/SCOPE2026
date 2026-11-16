"""Independent finite-dimensional numerical checks for one-frequency band-replacement Fourier frames.
Run: python CHECK.py. Requires numpy; finite checks do not prove universal statements.
"""
import math
import numpy as np

def matrix(q, m, b, theta):
    freq = [k for k in range(2*q) if k != q+b] + [m*q+b]
    pts = [j/q for j in range(q)] + [(j+theta)/q for j in range(q)]
    return np.exp(2j*np.pi*np.outer(freq, pts))/math.sqrt(2*q)

def prediction(q, m, theta):
    a = abs(math.cos(math.pi*theta))
    b = abs(math.cos(math.pi*m*theta))
    return np.array(sorted([1-a,1+a]*(q-1) + [1-b,1+b]), dtype=float)

def optimum(m):
    if m % 2: return 0.0, (0.5,)
    c=math.sin(math.pi/(2*(m+1)))
    return c,(m/(2*(m+1)),(m+2)/(2*(m+1)))

def run():
    tests=0
    for q in range(2,11):
        for m in range(2,12):
            for b in sorted(set([0,q//2,q-1])):
                for theta in [0.13,0.31,0.5,0.79,0.916]:
                    A=matrix(q,m,b,theta)
                    vals=np.linalg.eigvalsh(A.conj().T@A)
                    pred=prediction(q,m,theta)
                    assert np.allclose(vals,pred,atol=3e-12,rtol=2e-12), (q,m,b,theta,vals,pred)
                    tests+=1
    for m in range(2,40):
        c,thetas=optimum(m)
        for theta in thetas:
            observed=max(abs(math.cos(math.pi*theta)),abs(math.cos(math.pi*m*theta)))
            assert abs(observed-c)<1e-12,(m,theta,c,observed)
            tests+=1
        # finite grid consistency only; exact optimality uses analytical proof
        grid=np.linspace(0,1,4001)
        gridmax=np.maximum(np.abs(np.cos(np.pi*grid)),np.abs(np.cos(np.pi*m*grid)))
        assert min(gridmax)>=c-1e-11
        tests+=1
    for q in range(2,9):
        for m in range(2,20):
            A=matrix(q,m,q-1,0.5)
            rank=np.linalg.matrix_rank(A,tol=1e-8)
            assert rank==2*q-(m%2==0),(q,m,rank)
            tests+=1
    for m in [2,3,4,5,8,10,13]:
        for r in range(1,m):
            theta0=r/m
            for epsilon in [1e-3,2e-4]:
                theta=theta0+epsilon
                c=max(abs(math.cos(math.pi*theta)),abs(math.cos(math.pi*m*theta)))
                condition=math.sqrt((1+c)/(1-c))
                coefficient=condition*math.pi*m*abs(epsilon)/2
                assert abs(coefficient-1)<3e-3,(m,r,epsilon,coefficient)
                tests+=1
    print(f'CHECKS_PASSED {tests}')

if __name__ == '__main__':
    run()
