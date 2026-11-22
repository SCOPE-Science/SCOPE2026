"""Exact rational certificates for three-level gate Mpemba crossings.
Run: python3 checker.py. Only the Python standard library is required.
"""
from fractions import Fraction as Q
from math import sqrt, log


def gibbs(u):
    z = 1 + u + u**3
    return (1/z, u/z, u**3/z)


def data(u, pi):
    p, r, s = pi
    o = 1-r
    x, y, z = gibbs(u)
    m = y-r
    n = p*z-s*x
    return dict(m=m, n=n, A=m*m/(r*o), B=n*n/(p*s*o),
                theta=s*m if m>=0 else -p*m)


def unscaled_tv(z, c, pi):
    o = 1-pi[1]
    return abs(c['m']) + max(Q(0), c['n']*z-c['theta'])/o


def finite_difference_checks():
    # Exact forward generator and exact two-mode decomposition.
    for ub in (Q(2,5), Q(1,8), Q(1,4)):
        pi = gibbs(ub)
        p,r,s = pi; o=1-r; a=Q(1); c=Q(5)
        rates = ((Q(0), a*r, c*s),
                 (a*p, Q(0), a*s),
                 (c*p, a*r, Q(0)))
        def forward(vec):
            return tuple(sum(rates[j][i]*vec[j] for j in range(3) if j!=i)
                         - sum(rates[i][j] for j in range(3) if j!=i)*vec[i]
                         for i in range(3))
        assert forward(pi) == (0,0,0)
        slow = (-p/o,Q(1),-s/o)
        fast = (-Q(1)/o, Q(0), Q(1)/o)
        lam = a*r+c*o
        assert forward(slow)==tuple(-a*t for t in slow)
        assert forward(fast)==tuple(-lam*t for t in fast)
        for u in (Q(1),Q(4,5),Q(2,3),Q(1,2)):
            if u<=ub:continue
            v=gibbs(u); d=data(u,pi)
            assert tuple(v[i]-pi[i] for i in range(3))==tuple(d['m']*slow[i]+d['n']*fast[i] for i in range(3))
            # Orthogonality in stationary-weighted inner product.
            assert sum(slow[i]*fast[i]/pi[i] for i in range(3))==0
            assert sum(slow[i]*slow[i]/pi[i] for i in range(3))==1/(r*o)
            assert sum(fast[i]*fast[i]/pi[i] for i in range(3))==1/(p*s*o)
            for z in (Q(0),Q(1,100),Q(1,10),Q(1)):
                v = tuple(d['m']*slow[i]+z*d['n']*fast[i] for i in range(3))
                tv = sum(abs(x) for x in v)/2
                assert tv == unscaled_tv(z,d,pi)


def witness(uh,uw,ub,expected):
    assert uh>uw>ub>0
    pi=gibbs(ub); h=data(uh,pi); w=data(uw,pi)
    assert abs(h['m'])<abs(w['m'])
    assert h['B']>w['B']
    z2sq=(w['A']-h['A'])/(h['B']-w['B'])
    assert 0<z2sq<1
    # Evaluate F at 0, 1 exactly, and certify unique TV zero analytically:
    def f(z):return unscaled_tv(z,h,pi)-unscaled_tv(z,w,pi)
    assert f(Q(0))<0 and f(Q(1))>0
    assert h['n']>w['n']>0
    if expected=='later':
        # Only the hot hinge is active at the crossing.
        ztv=((1-pi[1])*(abs(w['m'])-abs(h['m']))+h['theta'])/h['n']
        assert h['n']*ztv>h['theta'] and w['n']*ztv<w['theta']
        assert ztv*ztv<z2sq
    else:
        # Both hinges are active at the crossing.
        ztv=((1-pi[1])*(abs(w['m'])-abs(h['m']))+h['theta']-w['theta'])/(h['n']-w['n'])
        assert h['n']*ztv>h['theta'] and w['n']*ztv>w['theta']
        assert ztv*ztv>z2sq
    assert f(ztv)==0
    # The two hinge activation orders leave F nonpositive until its
    # final strictly positive-slope segment; hence it has just one zero.
    t2=-log(sqrt(float(z2sq)))/(4*float(1-pi[1]))
    ttv=-log(float(ztv))/(4*float(1-pi[1]))
    if expected=='later':assert ttv>t2
    else:assert ttv<t2
    print(expected, 'z_TV=',ztv,'z_2^2=',z2sq,'t_TV=',round(ttv,9),'t_2=',round(t2,9))


if __name__=='__main__':
    finite_difference_checks()
    witness(Q(1),Q(2,3),Q(2,5),'later')
    witness(Q(1),Q(4,5),Q(1,8),'earlier')
    print('all exact generator, mode, TV, and crossing-sign tests passed')
