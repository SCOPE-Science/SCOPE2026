"""Exact symbolic checks for complex quadratic modulus samples on three rings."""
import sympy as S

def measurement_row(z):
    u = S.expand_complex(z*S.conjugate(z))
    w = S.expand_complex(z*z)
    return S.Matrix([[1,u,u*u,2*S.re(z),-2*S.im(z),
                      2*u*S.re(z),-2*u*S.im(z),2*S.re(w),-2*S.im(w)]])

def sample_nodes(r,s,t):
    d = (1+S.I)/S.sqrt(2)
    return [r,S.I*r,-r,-S.I*r,s*d,-s*d,t,-t]

def null_vector(r,s,t):
    delta = S.factor((s*s-r*r)*(s*s-t*t)/(2*s*s))
    return S.Matrix([r*r*t*t,-(r*r+t*t),1,0,0,0,0,0,delta])

def check_rank(r,s,t,expected):
    rows = S.Matrix.vstack(*(measurement_row(z) for z in sample_nodes(r,s,t)))
    k = null_vector(r,s,t)
    assert rows*k == S.zeros(8,1)
    assert rows.rank() == expected, (r,s,t,rows.rank(),expected)
    if r != s and r != t:
        assert len(rows.nullspace())==1 and S.simplify(rows.nullspace()[0]*k[2]-k*rows.nullspace()[0][2])==S.zeros(9,1)
    return rows

def check_ambiguity(r,s,t,squared_s,expected_sign):
    x = S.simplify(squared_s)
    delta = S.simplify((x-r*r)*(x-t*t)/(2*x))
    assert S.simplify(delta-expected_sign*r*t)==0
    for z in sample_nodes(r,S.sqrt(x),t):
        p=z*z-S.I*delta
        discrepancy=S.simplify(S.expand_complex(p*S.conjugate(p)-(r*r+t*t)*z*S.conjugate(z)))
        assert discrepancy==0,(r,s,t,x,z,discrepancy)

if __name__=='__main__':
    x,r,t=S.symbols('x r t',positive=True)
    core=(x-r*r)*(x-t*t)
    assert S.expand(core-2*r*t*x)==S.expand(x*x-(r+t)**2*x+r*r*t*t)
    assert S.expand(core+2*r*t*x)==S.expand(x*x-(r-t)**2*x+r*r*t*t)
    assert S.factor(((r-t)**4-4*r*r*t*t)-(r*r+t*t)*(r*r+t*t-4*r*t))==0
    check_rank(S.Integer(1),S.Integer(2),S.Integer(3),8)
    check_rank(S.Integer(1),S.Integer(3),S.Integer(3),8)
    check_rank(S.Integer(1),S.Integer(1),S.Integer(3),7)
    check_rank(S.Integer(1),S.Integer(2),S.Integer(1),6)
    for u in [8+S.sqrt(55),8-S.sqrt(55)]:
        check_ambiguity(S.Integer(1),S.sqrt(u),S.Integer(3),u,1)
    for u in [(9+S.sqrt(17))/2,(9-S.sqrt(17))/2]:
        check_ambiguity(S.Integer(1),S.sqrt(u),S.Integer(4),u,-1)
    t0=2+S.sqrt(3)
    check_ambiguity(S.Integer(1),S.sqrt(t0),t0,t0,-1)
    print('THREE_RING_PHASE_RETRIEVAL_PASS rank_checks=4 exact_exceptional_pairs=5 factor_identities=3')
