#!/usr/bin/env python3
"""Numerical and algebraic checks for the homogeneous three-state active-Potts fold.

Requires numpy and scipy; all all-parameter and equilibrium-count assertions are
proved analytically in RESULT.md, rather than inferred from these finite tests.
"""
import numpy as np
from scipy.optimize import root, brentq


def sig(z):
    return 1.0 / (1.0 + np.exp(-z))


def flow(q, k, b):
    x, y = q
    r = np.array([1 - x - y, x, y], dtype=np.result_type(x, y, k, b, float))
    w = np.array([sig(b + k * (r[(i+1) % 3] - r[i])) for i in range(3)])
    J = np.array([(r[i] + r[(i+1) % 3]) * w[i] - r[(i+1) % 3] for i in range(3)])
    return np.array([J[0] - J[1], J[1] - J[2]])


def jac(q, k, b):
    h = 1e-25
    return np.column_stack([np.imag(flow([q[0]+1j*h, q[1]], k, b))/h,
                            np.imag(flow([q[0], q[1]+1j*h], k, b))/h])


def fixed_k(b, c):
    return brentq(lambda k: k-b-np.log(k)-c, max(2.,b), b+np.log(b)+c+20, xtol=1e-13)


def fold_eq(Z, b):
    x,y,k=Z
    return [*(k*flow([x,y], k,b)),np.linalg.det(jac([x,y],k,b))]


def verify():
    cs=1+np.log(1.5)
    for b in (8.,20.,40.,80.):
        kp=b+np.log(b)+cs+(np.log(b)+cs-1)/b
        sol=root(fold_eq,[1/(3*kp),1/(3*kp),kp], args=(b,),tol=2e-12)
        assert np.linalg.norm(fold_eq(sol.x,b))<3e-12, (b,sol)
        x,y,k=sol.x
        assert 0<x<1 and 0<y<1 and x+y<1
        print('FOLD b=',b,'k=',format(k,'.12f'),'k_asymp=',format(kp,'.12f'),
              'scaled_minorities=',format(k*x,'.8f'),format(k*y,'.8f'))
    for b,c in ((20.,cs+0.5),(40.,cs+0.5),(40.,cs-0.5)):
        k=fixed_k(b,c)
        assert np.linalg.norm(flow([1/3,1/3],k,b))<1e-14
        if c>cs:
            fun=lambda u: 2*u-np.exp(-c+3*u)
            lo=brentq(fun,1e-10,1/3)
            hi=brentq(fun,1/3,max(4.,c*2))
            eigclasses=[]
            for u in (lo,hi):
                S=root(lambda p: k*flow(p,k,b),[u/k,u/k],tol=1e-11)
                assert np.linalg.norm(k*flow(S.x,k,b))<1e-10
                assert np.linalg.norm(k*S.x-u)<.35
                eig=np.linalg.eigvals(jac(S.x,k,b))
                eigclasses.append('node' if np.all(eig<0) else 'saddle' if np.prod(eig)<0 else 'undetermined')
            assert eigclasses==['node','saddle'],eigclasses
            print('ORDERED_BRANCHES b=',b,'c=',round(c,7),'root_types=',eigclasses)
        else:
            print('BELOW_THRESHOLD b=',b,'c=',round(c,7),'center_residual=',np.linalg.norm(flow([1/3,1/3],k,b)))
    print('VERIFY_OK fold_points=4 ordered_pairs=2 uniform_equilibria=3; FINITE_CHECK_ONLY')


if __name__=='__main__':
    verify()
