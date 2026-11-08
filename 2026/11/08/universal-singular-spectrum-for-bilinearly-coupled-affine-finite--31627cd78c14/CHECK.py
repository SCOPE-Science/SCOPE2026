"""Reproduce finite-field incidence spectra for small odd prime powers.

Python 3 standard library only; all matrix annihilator and moment checks are
exact integer arithmetic.  The computation checks cases, not the all-q proof.
"""
from math import isqrt


def field(q):
    if q == 9:
        # F_3[z]/(z^2+1), encoded u+3v.  z^2=-1 is irreducible.
        def add(a, b):
            return ((a % 3 + b % 3) % 3) + 3 * ((a // 3 + b // 3) % 3)
        def mul(a, b):
            u, v, w, z = a % 3, a // 3, b % 3, b // 3
            return ((u * w - v * z) % 3) + 3 * ((u * z + v * w) % 3)
        return add, mul
    return lambda a,b: (a+b)%q, lambda a,b:(a*b)%q


def product(A,B):
    n=len(A); p=len(B[0]); z=len(B)
    T=[[0]*p for _ in range(n)]
    for i in range(n):
        for k in range(z):
            a=A[i][k]
            if a:
                for j in range(p): T[i][j]+=a*B[k][j]
    return T


def gram_direct(q):
    add,mul=field(q)
    M=[[0]*(q*q) for _ in range(q*q)]
    for a in range(q):
        for b in range(q):
            for x in range(q):
                t=add(mul(x,add(a,b)),mul(a,b))
                M[q*x+t][q*a+b]=1
    return product([[M[row][col] for row in range(q*q)] for col in range(q*q)],M)


def transpose(A):return [list(row) for row in zip(*A)]


def annihilator(A,q):
    # Minimal-polynomial multiple F(z)=z(z-2q)
    # (z^2-2qz+q(q-1))(z^2-q(q+2)z+q(q^2+2q-1)).
    f=[1]
    for g in ([0,1],[-2*q,1],[q*(q-1),-2*q,1],
              [q*(q*q+2*q-1),-q*(q+2),1]):
        h=[0]*(len(f)+len(g)-1)
        for i,a in enumerate(f):
            for j,b in enumerate(g):h[i+j]+=a*b
        f=h
    n=len(A); I=[[int(i==j) for j in range(n)] for i in range(n)]
    Z=[[0]*n for _ in range(n)]
    P=I
    for c in f:
        for i in range(n):
            for j in range(n):Z[i][j]+=c*P[i][j]
        P=product(P,A)
    return all(v==0 for row in Z for v in row)


def checks():
    count=0
    for q in (3,5,7,9):
        add,mul=field(q)
        G=gram_direct(q)
        assert len(G)==q*q
        count+=1
        for a in range(q):
            for b in range(q):
                ab=q*a+b
                assert G[ab][ab]==q
                assert G[ab][q*b+a]==q
                count+=2
                for c in range(q):
                    for d in range(q):
                        cd=q*c+d
                        # same slope/intercept => same line;
                        # same slope and different intercept => parallel;
                        # different slopes => exactly one meeting point.
                        s=add(a,b); t=add(c,d)
                        v=q if s==t and mul(a,b)==mul(c,d) else (0 if s==t else 1)
                        assert G[ab][cd]==v
                        count+=1
        assert annihilator(G,q)
        count+=1
        # Check exact multiplicities of all spectral roots by trace power sums.
        # No floating point and no diagonalization is used.
        # Every positive quadratic pair is handled through integer recurrences.
        def rec_power(trace_root_sum,prod_root,k):
            U,V=2,trace_root_sum
            if k==0:return U
            if k==1:return V
            for _ in range(2,k+1):U,V=V,trace_root_sum*V-prod_root*U
            return V
        P=[[int(i==j) for j in range(q*q)] for i in range(q*q)]
        for k in range(6):
            act=sum(P[i][i] for i in range(q*q))
            want=(q*(q-3)//2)*(2*q)**k + (q-1)*rec_power(2*q,q*(q-1),k) \
                 +rec_power(q*(q+2),q*(q*q+2*q-1),k)
            if k==0:want+=q*(q-1)//2
            assert act==want,(q,k,act,want)
            P=product(P,G)
            count+=1
        # Test affine-coupling permutation reduction for nonzero slopes/offsets.
        # Choose all parameters nontrivial for the prime and extension examples.
        one=1
        def inv(a):
            return next(x for x in range(1,q) if mul(a,x)==one)
        alpha=2; gamma=1; beta=1; delta=2; lam=2
        c=mul(lam,mul(inv(alpha),inv(gamma)))
        d=mul(beta,inv(alpha)); e=mul(delta,inv(gamma))
        for x in range(q):
            J=mul(mul(x,x),x)  # arbitrary output shear
            for a in range(q):
                for b in range(q):
                    F=add(mul(alpha,x),beta); K=add(mul(gamma,x),delta)
                    t=add(J,add(add(mul(a,F),mul(b,K)),mul(lam,mul(a,b))))
                    u=add(mul(mul(c,alpha),a),e)
                    v=add(mul(mul(c,gamma),b),d)
                    tp=add(add(mul(c,add(t,mul(2 if q==9 else q-1,J))),mul(x,add(d,e))),mul(d,e))
                    assert tp==add(mul(x,add(u,v)),mul(u,v))
                    count+=1
        print('q',q,'matrix_order',q*q,'rank',q*(q+1)//2,'exact_checks_ok')
    print('CHECK_OK exact_assertions=',count)

if __name__=='__main__':checks()
