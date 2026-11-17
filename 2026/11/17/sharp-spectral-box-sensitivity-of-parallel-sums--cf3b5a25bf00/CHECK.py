"""Supplementary numerical diagnostics for the sharp parallel-sum sensitivity envelope.

Requires NumPy. This checker does not prove the infinite-dimensional bound.
"""
import math
import numpy as np


def formula(k):
    edge = 2 + math.sqrt(5)
    return (k / (k + 1))**2 if k <= edge else (k + 6 + 1/k)/16


def witness(k):
    assert k > 1
    c, r = (k+1)/2, (k-1)/2
    K = 2*c*c-r*r
    a = min(k, math.sqrt(k*K)/r)
    v1 = (a*a+k)/(2*c)
    v2 = math.sqrt(max(0, a*a-v1*v1))
    v = np.array([v1, v2])
    e = np.array([1., 0.])
    u = c*e-r*(v+c*e)/np.linalg.norm(v+c*e)
    def mat(w):
        return c*np.eye(2)+r*np.array([[w[0],w[1]], [w[1],-w[0]]])
    return mat((u-c*e)/r), mat((v-c*e)/r)


def sensitivity(A,B):
    return np.linalg.norm(B@np.linalg.inv(A+B),2)**2


def psum(A,B):
    return B-B@np.linalg.solve(A+B,B)


def random_spd(k,dim,rng):
    Q,_=np.linalg.qr(rng.normal(size=(dim,dim)))
    d=1+(k-1)*rng.random(dim)
    return (Q*d)@Q.T


def main():
    assert_count=0
    rng=np.random.default_rng(1907526)
    kappas=(1.0001, 1.01, 1.5, 2., 4., 2+math.sqrt(5), 5., 9., 5+2*math.sqrt(6), 10., 100.)
    for k in kappas:
        A,B=witness(k)
        for T in (A,B):
            assert np.allclose(np.linalg.eigvalsh(T),[1,k],atol=1e-10,rtol=1e-10)
            assert_count+=1
        assert abs(sensitivity(A,B)-formula(k))<1e-10*max(1,formula(k)); assert_count+=1
        for dim in (2,3,5):
            for trial in range(75):
                C,D=random_spd(k,dim,rng),random_spd(k,dim,rng)
                assert sensitivity(C,D) <= formula(k)*(1+5e-11)
                assert_count+=1
    for k in (3.,6.,10.):
        A,B=witness(k)
        A=.999*A+.001*((k+1)/2)*np.eye(2)
        M=B@np.linalg.inv(A+B)
        eig,U=np.linalg.eigh(M.T@M)
        v=U[:,-1]
        H=np.outer(v,v)
        for h in (1e-6,2e-7):
            actual=np.linalg.norm(psum(A+h*H,B)-psum(A,B),2)/h
            target=sensitivity(A,B)
            assert abs(actual-target)<2e-5*max(1,target)
            assert_count+=1
    print('PARALLEL_SUM_DIAGNOSTICS_OK',assert_count)

if __name__=='__main__':
    main()
