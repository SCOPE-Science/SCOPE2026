"""Self-contained exact checks for phase-profile restrictions to Im(z**n)=c.
No external data or network. Requires SymPy.
"""
import sympy as sp

I=sp.I

def point(t,c):
    return sp.Rational(t) + I*sp.Rational(c)/(2*sp.Rational(t))

def profile_row(z,d):
    v=[sp.expand(z**k) for k in range(d+1)]
    out=[]
    for j in range(d+1):
        out.append(sp.expand_complex(v[j]*sp.conjugate(v[j])).simplify())
    for j in range(d+1):
        for k in range(j+1,d+1):
            t=sp.expand(v[j]*sp.conjugate(v[k]))
            out.extend([sp.re(t).expand(complex=True).simplify(),sp.im(t).expand(complex=True).simplify()])
    return out

def expected(d,n,L):
    return (d+1)**2 - max(0,d-n*L+1)**2

def exact_rank_checks():
    nodes=[sp.Rational(s)*r for r in [sp.Rational(1,2),sp.Rational(2,3),1,sp.Rational(3,2),2,sp.Rational(5,2),3,4,5,6,7,8,9,10] for s in [1,-1]]
    checks=0
    for d in range(1,5):
        A=[]
        for L in range(1,4):
            c=L
            A += [profile_row(point(t,c),d) for t in nodes]
            rank=sp.polys.matrices.DomainMatrix.from_Matrix(sp.Matrix(A)).convert_to(sp.QQ).rank()
            assert rank==expected(d,2,L),(d,L,rank,expected(d,2,L))
            checks+=1
    return checks

def exact_ambiguity_checks():
    X,Y,B,A,c=sp.symbols('X Y B A c',real=True)
    alpha=A+I*B
    ref=A+I*(2*c-B)
    u=X+I*Y
    delta=sp.expand_complex((u-alpha)*sp.conjugate(u-alpha)-(u-ref)*sp.conjugate(u-ref))
    assert sp.simplify(delta-4*(c-B)*(Y-c))==0
    # For Im(z**n)=c the difference is zero; a second level with a different
    # value removes the nontrivial reflected-root ambiguity.
    for n in (2,3,4,5):
        x,y=sp.symbols('x y',real=True)
        z=x+I*y
        v=sp.expand(z**n)
        j=sp.im(sp.expand_complex(v))
        diff=sp.expand((v-(3+4*I))*sp.conjugate(v-(3+4*I))-(v-(3-2*I))*sp.conjugate(v-(3-2*I)))
        assert sp.simplify(sp.expand_complex(diff)-12*(1-j))==0,(n,sp.expand_complex(diff))
    return 5

if __name__=='__main__':
    a=exact_rank_checks()
    b=exact_ambiguity_checks()
    print(f'HARMONIC_LEVEL_PROFILE_CHECK_PASS exact_ranks={a} reflection_identities={b}')
