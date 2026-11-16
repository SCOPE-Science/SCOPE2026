"""Exact identities and independent moment checks for cubic spherical harmonics
on disjoint equal caps about the signed coordinate axes.

Requires Python 3, SymPy and mpmath. No external data or network is used.
"""
import sympy as sp
import mpmath as mp

D, z = sp.symbols('d z', real=True)
S2 = z**2 + 3*(1-z)**2/(D+1)
S3 = z**3 + 15*(1-z)**3/((D+1)*(D+3))
K = {
    'A': S3-6*S2/(D+2)+9/(D+2)**2,
    'B': ((D+1)*S2-D*S3-1)/(D-1),
    'C': (1-3*S2+2*S3)/6,
}
N = {
    'A':6*(D-1)/((D+2)**2*(D+4)),
    'B':2*(D-2)/((D+2)*(D+4)),
    'C':(D-1)*(D-2)/(6*(D+2)*(D+4)),
}
R = {s:sp.factor(K[s]/N[s]) for s in K}
M = {'A':D,'B':D*(D-2),'C':D*(D-1)*(D-2)/6}
dimh = D*(D-1)*(D+4)/6
assert sp.cancel(sum(M[s] for s in K)-dimh)==0
assert sp.cancel(sum(M[s]*R[s] for s in K)-dimh)==0

# Independently sum the squared norms of three representative harmonic cubics,
# conditioned on which cap coordinate has the large squared value z.
c=sp.Rational(3)/(D+2)
m1=(1-z)/(D-1)
m2=3*(1-z)**2/((D-1)*(D+1))
m3=15*(1-z)**3/((D-1)*(D+1)*(D+3))
HA = z*(z-c)**2+(D-1)*(m3-2*c*m2+c*c*m1)
HB = 4*z*(1-z)**2/((D-1)*(D+1)) + 2*(z*z*m1-2*z*(1-z)**2/((D-1)*(D+1))+3*(1-z)**3/((D-1)*(D+1)*(D+3))) + (D-3)*4*(1-z)**3/((D-1)*(D+1)*(D+3))
HC = 3*z*(1-z)**2/((D-1)*(D+1)) + (D-3)*(1-z)**3/((D-1)*(D+1)*(D+3))
full_norm={
    'A':6*(D-1)/(D*(D+2)**2*(D+4)),
    'B':4/(D*(D+2)*(D+4)),
    'C':1/(D*(D+2)*(D+4)),
}
for kind,integrand in [('A',HA),('B',HB),('C',HC)]:
    assert sp.cancel(integrand/full_norm[kind]-D*R[kind]) == 0,kind

QAB=(D+4)*((D+2)*(D+6)*z*z-(4*D+6)*z-3)/(3*(D+1)*(D+3))
QBC=(D+2)*(D+4)*(1-z)*((D+6)*z-3)/((D-1)*(D+1)*(D+3))
QAC=sp.factor(QAB+QBC)
def beta_derivative_poly(q):
    return sp.diff(q,z)*z*(1-z)+sp.Rational(1,2)*(1-D*z)*q
for a,b,q in [('A','B',QAB),('B','C',QBC),('A','C',QAC)]:
    assert sp.cancel(beta_derivative_poly(q)+R[a]-R[b])==0,(a,b)

assert sp.cancel(QAB.subs(z,sp.Rational(1,2)) - (D+4)*(D*D-12)/(12*(D+1)*(D+3))) == 0
assert sp.simplify(QAC.subs(D,3)) == -sp.Rational(7,48)*(15*z*z-48*z+17)
root=(sp.Integer(3)+2*sp.sqrt(6))/15
assert sp.simplify(QAB.subs({D:3,z:root}))==0
assert sp.simplify(root-sp.Rational(1,2))>0
assert sp.simplify(root-1)<0
C_asym=(D-1)*(D+1)*(D+3)/(18*(D+2))
ka1=sp.factor(R['A'].subs(z,1))
kc2=sp.factor(sp.cancel(R['C']/(1-z)**2).subs(z,1))
assert sp.cancel((ka1/kc2)*(D+3)/(D-1)-C_asym)==0

# Independent numerical integration of the representative squares; this
# calculation avoids the symmetry-projector kernels R entirely.
mp.mp.dps=45
for d0 in (3,4,5,8,13):
    beta=mp.beta(mp.mpf('0.5'),mp.mpf(d0-1)/2)
    for t0 in ('0.505','0.53','0.65','0.85','0.97'):
        t=mp.mpf(t0)
        def eig_from_representative(k):
            g=sp.lambdify(z, {'A':HA,'B':HB,'C':HC}[k].subs(D,d0),modules='mpmath')
            v=mp.quad(lambda u:g(u)*u**(-mp.mpf('0.5'))*(1-u)**((d0-3)/2)/beta,[t,1]);
            return v/mp.mpf(str(full_norm[k].subs(D,d0)))
        ev={k:eig_from_representative(k) for k in 'ABC'}
        factor=d0/beta*mp.sqrt(t)*(1-t)**((d0-1)/2)
        for a,b,q in [('A','B',QAB),('B','C',QBC)]:
            expected=factor*mp.mpf(str(q.subs({D:d0,z:sp.Rational(t0)}).evalf(43)))
            assert abs(ev[a]-ev[b]-expected)<mp.mpf('2e-32'),(d0,t0,a,b)
        assert ev['C']<ev['A'] and ev['C']<ev['B']
        if d0 >= 4 or t > mp.mpf(str(root.evalf(40))):
            assert ev['A']>ev['B']>ev['C']
        else:
            assert ev['B']>ev['A']>ev['C']
print('CUBIC_COORDINATE_CAPS_EXACT_PASS symbolic=all_d independent_cases=25')
