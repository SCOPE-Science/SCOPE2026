#!/usr/bin/env python3
"""Exact-rational checks for two-reset covariance reconstruction in planar diffusions.

Requires Python 3 and SymPy. These finite checks supplement, not replace, the proof.
"""
import sympy as sp

J = sp.Matrix([[0, 1], [-1, 0]])
I = sp.eye(2)


def covariance(K, D, rate):
    a,b,c = sp.symbols('a b c')
    C = sp.Matrix([[a,b],[b,c]])
    E = K*C + C*K.T + rate*C - 2*D
    M,z = sp.linear_eq_to_matrix([E[0,0],E[0,1],E[1,1]], [a,b,c])
    solution = M.inv()*z
    return sp.Matrix([[solution[0],solution[1]], [solution[1],solution[2]]])


def reconstruct(C1,C2,r1,r2):
    delta = C1-C2
    Q = r2*C2-r1*C1
    K0 = (Q/2)*delta.inv()
    M = delta.inv()*C1
    h = sp.factor(M[1,1]-M[0,0])
    d0 = sp.factor(((K0*C1+C1*K0.T+r1*C1)/2)[0,1])
    if h == 0:
        return None,h,d0
    omega = sp.factor(-2*d0/h)
    K = sp.simplify(K0+omega*J*delta.inv())
    D = sp.simplify((K*C1+C1*K.T+r1*C1)/2)
    return (K,D,omega),h,d0


def eq(A,B):
    return all(sp.simplify(x-y)==0 for x,y in zip(A,B))


def main():
    tests = 0
    cases = []
    for a,d in [(1,2),(2,1),(2,3),(3,2)]:
        for b,c in [(sp.Rational(1,3),sp.Rational(-1,4)),
                    (sp.Rational(-1,5),sp.Rational(2,5)),
                    (sp.Rational(1,4),sp.Rational(1,3))]:
            for dx,dy in [(1,2),(2,1),(1,3)]:
                cases.append((sp.Matrix([[a,b],[c,d]]),sp.diag(dx,dy)))
    for K,D in cases:
        assert K.trace()>0 and K.det()>0  # 2x2 positive stability
        for r1,r2 in [(sp.Integer(1),sp.Integer(2)),
                      (sp.Integer(1),sp.Integer(4))]:
            C1,C2=covariance(K,D,r1),covariance(K,D,r2)
            delta=C1-C2
            assert delta[0,0]>0 and delta.det()>0
            result,h,d0=reconstruct(C1,C2,r1,r2)
            if h!=0:
                K2,D2,_=result
                assert eq(K2,K),(K2,K,D,h)
                assert eq(D2,D)
                assert eq(covariance(K2,D2,r1),C1)
                assert eq(covariance(K2,D2,r2),C2)
            else:
                assert d0 == 0
            tests += 1

    # Nonidentifiability for all rates and all single-time marginals, even unequal baths:
    for d1,d2 in [(sp.Integer(1),sp.Integer(1)),
                  (sp.Integer(1),sp.Integer(3)),
                  (sp.Integer(2),sp.Integer(5))]:
        D=sp.diag(d1,d2)
        for kappa in [sp.Integer(1),sp.Rational(3,2)]:
            for omega in [sp.Integer(-2),sp.Integer(0),sp.Rational(3,2)]:
                K=kappa*I+omega*J*D.inv()
                assert eq(K*D+D*K.T,2*kappa*D)
                assert K.trace()>0 and K.det()>0
                for rate in [sp.Rational(1,2),sp.Integer(1),sp.Integer(4)]:
                    expected=2*D/(2*kappa+rate)
                    actual=covariance(K,D,rate)
                    assert eq(actual,expected)
                    tests += 1
                C1=covariance(K,D,sp.Integer(1))
                C2=covariance(K,D,sp.Integer(2))
                result,h,d0=reconstruct(C1,C2,sp.Integer(1),sp.Integer(2))
                assert result is None and h==0 and d0==0
                tests += 1

    K=sp.Matrix([[2,sp.Rational(1,2)],[-sp.Rational(1,3),1]])
    D=sp.diag(1,3)
    r1,r2=sp.Integer(1),sp.Integer(2)
    C1,C2=covariance(K,D,r1),covariance(K,D,r2)
    recovered,h,d0=reconstruct(C1,C2,r1,r2)
    assert h!=0 and eq(recovered[0],K) and eq(recovered[1],D)
    print('PASS exact-rational scenarios:', tests)
    print('illustration C1 =',C1.tolist())
    print('illustration C2 =',C2.tolist())
    print('illustration h =',h)
    print('recovered K =',recovered[0].tolist())
    print('recovered D =',recovered[1].tolist())
    print('blind family: K = kappa I + omega J D^-1; all-rate C_r=2 D/(2 kappa+r)')

if __name__=='__main__':
    main()
