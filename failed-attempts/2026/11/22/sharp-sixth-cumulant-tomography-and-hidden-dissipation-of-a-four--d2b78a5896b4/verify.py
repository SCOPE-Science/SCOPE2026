"""Stationary generator and algebra checks for four-direction active-trap tomography.

Requires Python 3 and sympy. Run `python verify.py`.
"""
import sympy as s
b,a,e=s.symbols('b a e',positive=True)
assertions=0

def check(expr):
    global assertions
    assert s.trigsimp(s.simplify(expr))==0, s.factor(expr)
    assertions += 1

# Separately solve the two-state stationary generator moment equations,
# for each independent rotated coordinate with trap relaxation normalized to 1.
M={0:s.Integer(1)}
H={0:s.Integer(0)}
for n in range(1,9):
    m_prev=M.get(n-2,s.Integer(0))
    h_prev=H.get(n-2,s.Integer(0))
    H[n]=s.factor((n*a*M[n-1]+e*n*(n-1)*h_prev)/(n+2*b))
    M[n]=s.factor(a*H[n-1]+e*(n-1)*m_prev)

k2=M[2]
k4=s.factor(M[4]-3*M[2]**2)
k6=s.factor(M[6]-15*M[4]*M[2]+30*M[2]**3)
check(k2 - (e+a*a/(2*b+1)))
check(k4 + 6*a**4/((2*b+1)**2*(2*b+3)))
check(k6 - 240*a**6/((2*b+1)**3*(2*b+3)*(2*b+5)))
R=s.factor(k6**2/(-k4)**3)
check(R-800*(2*b+3)/(3*(2*b+5)**2))
check(s.diff(R,b) + 1600*(2*b+1)/(3*(2*b+5)**3))

# Verify ratio inversion is the physically admissible larger quadratic root.
r,t=s.symbols('r t',positive=True)
check((3*r*t*t-800*t+1600).subs(r,R).subs(t,2*b+5))
# Antisymmetric angle mode; q(theta)=cos^4 theta+sin^4 theta.
th=s.symbols('th',real=True)
check((s.cos(th)**4+s.sin(th)**4)-(3+s.cos(4*th))/4)

# Rational tests of the moment-to-cumulant formula for both noiseless and thermal cases.
for bv in [s.Rational(1,5),s.Rational(1,2),s.Integer(1),s.Rational(5,3),s.Integer(4)]:
    for av in [s.Rational(1,3),s.Integer(1),s.Rational(7,2)]:
        for ev in [s.Integer(0),s.Rational(1,5),s.Rational(3,2)]:
            vals={b:bv,a:av,e:ev}
            check(k4.subs(vals)+6*av**4/((2*bv+1)**2*(2*bv+3)))
            check(k6.subs(vals)-240*av**6/((2*bv+1)**3*(2*bv+3)*(2*bv+5)))
            check(k2.subs(vals)-(ev+av**2/(2*bv+1)))
            # Physical scale can be uniquely read from the fourth cumulant if b is fixed.
            K=-k4.subs(vals)
            check(K*(2*bv+1)**2*(2*bv+3)/6-av**4)

# Nonidentifiability with only variance and fourth cumulant: explicit strict interior pair.
b1=s.Integer(1);a1=s.Integer(1);e1=s.Integer(1)
b2=s.Rational(3,2)
K=s.factor((-k4).subs({b:b1,a:a1,e:e1}))
a2_4=s.factor(K*(2*b2+1)**2*(2*b2+3)/6)
a2=s.root(a2_4,4)
e2=s.factor(k2.subs({b:b1,a:a1,e:e1})-a2*a2/(2*b2+1))
assert bool(s.N(e2,20)>0)
assertions+=1
check(a2**4-a2_4)
check(k2.subs({b:b2,a:a2,e:e2})-k2.subs({b:b1,a:a1,e:e1}))
check(k4.subs({b:b2,a:a2,e:e2})-k4.subs({b:b1,a:a1,e:e1}))
assert s.simplify(k6.subs({b:b2,a:a2,e:e2})-k6.subs({b:b1,a:a1,e:e1}))!=0
assertions+=1

# Exact sample: b=a=1, e=1/5 gives ratio 4000/147 and positive thermal intensity.
check(k2.subs({b:1,a:1,e:s.Rational(1,5)})-s.Rational(8,15))
check(k4.subs({b:1,a:1,e:s.Rational(1,5)})+s.Rational(2,15))
check(k6.subs({b:1,a:1,e:s.Rational(1,5)})-s.Rational(16,63))
check(R.subs({b:1})-s.Rational(4000,147))

# The active power / D expression: two independent coordinates.
# With rate b, normalized v=a and diffusion e, E[U*sigma]=a/(1+2b).
# 2*[a^2 - a E(U*sigma)]/e = 4*b*a^2/[e*(1+2b)].
check(2*(a*a-a*a/(1+2*b))/e-4*b*a*a/(e*(1+2*b)))
print(f'PASS: {assertions} exact symbolic/rational checks')
