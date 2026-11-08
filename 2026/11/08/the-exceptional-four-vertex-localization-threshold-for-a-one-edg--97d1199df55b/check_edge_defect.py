"""Exact algebra checks for the one-edge-deformed complete metric graph theorem.

Run: python check_edge_defect.py  (requires sympy).
The finite network tests complement, rather than replace, the universal proof.
"""
import sympy as S
from itertools import combinations

n,h=S.symbols('n h', positive=True)
d=2+(n-2)*h
L=n*(n-1)/2-1+h
rd=2*h/d
rm=(2*n*h-3*h+3)/(n*d)
ro=2/n
Ds=n-2+h
Do=n-1
H=(h*(h-rd)+2*(n-2)*(1-rm)+(n-2)*(n-3)/2*(1-ro))/6
Fs=H+(Ds*rd+(n-2)*Do*rm)/2
Fo=H+(2*Ds*rm+(n-3)*Do*ro)/2
Cd=L*(h-rd)-h**2
Cm=L*(1-rm)-1
Co=L*(1-ro)-1
Delta=Fs-Fo
Md=Fs+Cd/4
Mo=Fo+Co/4
Mm=Fs+(Cm-Delta)**2/(4*Cm)
T=n**3*h-2*n**2*h+2*n**2+2*n*h**2-3*n*h+n-2*h**2+4*h-2
Q=-n**4+n**3+12*n**2-16+h*(4*n**3-12*n**2-8*n+32)+8*(n-2)*h**2

def eq(x,y):
    assert S.cancel(x-y)==0, str(S.factor(x-y))

eq(rd, 2/(n+2*(1/h-1)))
eq(rm, 2/n - (1/h-1)/(n*(n+2*(1/h-1))))
eq(Delta,(n-3)*(h-1)*(n+2-2*h)/(2*n*d))
eq(Cd,n**2*h**2*(n-3)/(2*d))
eq(Cm-Delta,(n-3)*(n**2*h-2*n*h+2*n+2*(h-1)**2)/(2*d))
eq(Cm+Delta,(n-3)*(n**2+2*h-2)/(2*n))
eq(Co,(n**3-3*n**2+2*n*h-2*n-4*h+4)/(2*n))
eq(Md-Mo,(h-1)*(n**3-n**2-4*n-8)/(8*n))
eq(Mm-Md,-n*(n-3)*(n+1)*(h-1)*(n**2*h-n*h+2*n+2*(h-1)**2)/(8*T))
eq(Mm-Mo,-(h-1)*Q/(8*n*T))
eq(Q.subs(n,4),16*(h*h+4*h-1))
eq(Q.subs(h,1),n**3*(5-n))
print('GENERAL_SYMBOLIC_EDGE_PEAK_IDENTITIES_PASSED')

# Exact independent resistance network: subdivide each edge into two halves,
# ground the final node, and solve Dirichlet equations using rational arithmetic.
def resistances(N, length):
    edges=[]; nextid=N; mid={}
    for a,b in combinations(range(N),2):
        ell=length if (a,b)==(0,1) else S.Integer(1)
        mid[a,b]=nextid
        edges.extend([(a,nextid,ell/2),(nextid,b,ell/2)])
        nextid+=1
    lap=S.zeros(nextid)
    for a,b,ell in edges:
        conductance=1/ell
        lap[a,a]+=conductance
        lap[b,b]+=conductance
        lap[a,b]-=conductance
        lap[b,a]-=conductance
    reduced=lap[:nextid-1,:nextid-1].inv()
    def r(a,b):
        if a==b: return S.Integer(0)
        if a==nextid-1: return reduced[b,b]
        if b==nextid-1: return reduced[a,a]
        return S.factor(reduced[a,a]+reduced[b,b]-2*reduced[a,b])
    return r,mid

for N,z in [(4,S.Rational(1,5)),(4,S.Rational(2,5)),
            (4,S.Integer(1)),(4,S.Integer(2)),
            (5,S.Rational(1,2)),(5,S.Integer(2))]:
    r,mid=resistances(N,z)
    values={n:N,h:z}
    eq(r(0,1),rd.subs(values))
    eq(r(0,2),rm.subs(values))
    eq(r(2,3),ro.subs(values))
    # With the same endpoints on the chosen edge, the exact midpoint
    # resistance follows from the asserted edge interpolation identity.
    for edge in [(0,1),(0,2),(2,3)]:
        a,b=edge
        ell=z if edge==(0,1) else S.Integer(1)
        m=mid[edge]
        rab=r(a,b)
        eq(r(a,m),ell/S.Integer(2)-(ell-rab)/4)
        eq(r(m,b),ell/S.Integer(2)-(ell-rab)/4)
print('INDEPENDENT_RATIONAL_SUBDIVISION_RESISTANCES_PASSED 6')

# Q_n(t) strict negativity for n>=5, 0<t<1 follows from convexity,
# its explicit nonpositive endpoint values and strict negativity at zero.
eq(Q.subs(h,0),-n**4+n**3+12*n**2-16)
eq(Q.subs(h,1),n**3*(5-n))
eq(S.diff(Q,h,2),16*(n-2))
eq(S.diff(Q.subs(h,0),n),-4*n**3+3*n**2+24*n)
assert (-5**4+5**3+12*5**2-16)<0
print('ALL_ONE_EDGE_COMPLETE_GRAPH_CHECKS_PASSED')
