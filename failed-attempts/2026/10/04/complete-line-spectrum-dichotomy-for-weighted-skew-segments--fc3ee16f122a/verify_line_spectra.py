from fractions import Fraction
import cmath, math

# The skew pair used in the paper's Example 2:
# I1={(t,0,0):0<=t<=1}, I2={(0,t,1):0<=t<=1}, each with mass density 1/2.
# A second normalized direction u=(1/2,1/2,1) projects the two segments to
# [0,1/2] and [1,3/2], the exceptional equal-mass two-interval configuration.

half = Fraction(1,2)
u = (half, half, Fraction(1,1))
# |<u,e1>|=|<u,e2>|=1/2, as required by density balance.
assert abs(u[0]) == half and abs(u[1]) == half
J1 = (Fraction(0), half)
J2 = (Fraction(1), Fraction(3,2))
assert J1[1] <= J2[0]
assert J1[1]-J1[0] == half
assert J2[1]-J2[0] == half
gap = J2[0]-J1[1]
assert gap == half
n = 2*gap + 1
assert n == 2

# The one-dimensional exceptional spectrum Sigma=2Z union (1/2+2Z).
# Differences within a coset are nonzero even integers; cross-coset differences
# are half-integers modulo 2.  The Fourier transform of [0,1/2] union [1,3/2]
# vanishes in both cases for distinct frequencies.
def interval_ft(delta, a, b):
    delta = float(delta)
    if abs(delta) < 1e-15:
        return b-a
    return (cmath.exp(2j*math.pi*delta*b)-cmath.exp(2j*math.pi*delta*a))/(2j*math.pi*delta)

def omega_ft(delta):
    return interval_ft(delta,0.0,0.5)+interval_ft(delta,1.0,1.5)

sigmas=[]
for k in range(-8,9):
    sigmas += [Fraction(2*k), Fraction(1,2)+2*k]
sigmas=sorted(set(sigmas))
max_off=0.0
for i,s in enumerate(sigmas):
    for j,t in enumerate(sigmas):
        val=omega_ft(s-t)
        target=1.0 if i==j else 0.0
        err=abs(val-target)
        max_off=max(max_off,err)
        assert err < 2e-13

# Check the lattice branch used by the recent source: u0=(1/2,1/2,1/2)
# projects onto [0,1/2] union [1/2,1]=[0,1], whose spectrum is Z.
u0=(half,half,half)
assert abs(u0[0])==half and abs(u0[1])==half
for k in range(-12,13):
    for m in range(-12,13):
        d=k-m
        val=interval_ft(d,0.0,1.0)
        target=1.0 if k==m else 0.0
        assert abs(val-target) < 2e-13

# Non-lattice witness: the scalar spectrum has alternating gaps 1/2 and 3/2.
gaps=[sigmas[i+1]-sigmas[i] for i in range(len(sigmas)-1)]
assert Fraction(1,2) in gaps and Fraction(3,2) in gaps
print('projected_gap=1/2')
print('exceptional_n=2')
print(f'max_gram_error={max_off:.3e}')
print('non_lattice_gaps=1/2,3/2')
print('VERIFY_OK')
