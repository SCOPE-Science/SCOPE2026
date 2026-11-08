"""Standalone arithmetic checks for the exact inertia theorem for matrix conjugate gradients.

Only standard Python and SymPy are required. The general theorem is proved algebraically;
these finite checks are not a substitute for its proof.
"""
from math import comb
from random import Random
import sympy as S


def polynomial_kernel_matrix(coeffs, nodes):
    x = S.Symbol('x')
    p = sum(S.Rational(a)*x**j for j,a in enumerate(coeffs))
    return S.Matrix([[S.expand(p).subs(x, u+v) for v in nodes] for u in nodes])


def cg_lyapunov(A,b,steps):
    F=b*b.T
    X=S.zeros(A.rows)
    R=F.copy(); P=R.copy(); rho=(R.T*R).trace()
    iterates=[]
    for k in range(steps):
        W=A*P+P*A
        alpha=rho/(P.T*W).trace()
        X=X+alpha*P
        R=R-alpha*W
        rhonext=(R.T*R).trace()
        iterates.append(X.copy())
        if rhonext==0:
            break
        P=R+(rhonext/rho)*P
        rho=rhonext
    return iterates


def inertia(M):
    # Exact signature via sign variations of characteristic roots for small rational matrices.
    # Characteristic polynomial rational real-root isolation is used only as a supplementary test.
    z=S.Symbol('z')
    P=M.charpoly(z).as_expr()
    # count_neg_roots returns number of strictly negative real roots, with multiplicity.
    zeros=M.rows-M.rank()
    P=S.Poly(S.cancel(P/z**zeros),z)
    return (P.count_roots(0,S.oo), P.count_roots(-S.oo,0), zeros)


def main():
    tests=0
    rng=Random(7231)
    for n in range(2,7):
        for rep in range(2):
            vals=sorted(rng.sample(range(1,35),n))
            bs=[rng.choice([-3,-2,-1,1,2,3]) for _ in range(n)]
            A=S.diag(*vals);b=S.Matrix(bs)
            for k,X in enumerate(cg_lyapunov(A,b,n),start=1):
                want=((k+1)//2,k//2,n-k)
                got=inertia(X)
                assert got==want,(vals,bs,k,got,want)
                tests+=1
    # A repeated eigenvalue and a rational orthogonal change of basis.
    U=S.eye(4)
    U[0,0]=S.Rational(3,5); U[0,2]=-S.Rational(4,5)
    U[2,0]=S.Rational(4,5); U[2,2]=S.Rational(3,5)
    A=U*S.diag(1,1,3,7)*U.T
    b=U*S.Matrix([1,2,-1,3])
    for k,X in enumerate(cg_lyapunov(A,b,3),start=1):
        assert inertia(X)==((k+1)//2,k//2,4-k)
        tests+=1
    for d in range(0,9):
        coeffs=[S.Rational(rng.randint(-9,9),1) for _ in range(d)] + [S.Rational(rng.choice([-1,1]),rng.choice([1,2,3]))]
        C=S.Matrix(d+1,d+1,lambda i,j: S.binomial(i+j,i)*coeffs[i+j] if i+j<=d else 0)
        detwant=(-1)**(d*(d+1)//2)*coeffs[d]**(d+1)*S.prod(S.binomial(d,i) for i in range(d+1))
        assert C.det()==detwant,(d,C.det(),detwant)
        wantplus=(d+2)//2 if d%2==0 and coeffs[d]>0 else (d//2+1 if d%2 else d//2)
        # for d odd every paired +/-; for d even, the central sign depends on c_d.
        if d%2==0:
            wantplus=d//2+(1 if coeffs[d]>0 else 0)
        else:
            wantplus=(d+1)//2
        assert inertia(C)==(wantplus,d+1-wantplus,0)
        tests+=2
    for d in range(0,7):
        coeffs=[S.Rational(rng.choice([-2,-1,0,1,2])) for _ in range(d)]+[S.Integer((-1)**d)]
        nodes=[S.Integer(i+1) for i in range(d+1)]
        K=polynomial_kernel_matrix(coeffs,nodes)
        assert inertia(K)==((d+2)//2,(d+1)//2,0),(d,inertia(K))
        tests+=1
    print('PASS:',tests,'independent exact rational rank/inertia/antitriangular checks')

if __name__=='__main__': main()
