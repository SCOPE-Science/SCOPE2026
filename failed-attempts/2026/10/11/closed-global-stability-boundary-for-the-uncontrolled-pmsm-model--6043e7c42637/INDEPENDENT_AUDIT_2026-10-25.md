# Independent mathematical audit

## correctness

PASS

For real gamma<=1 and sigma>0, V=(x²+y²+(2−gamma)z²/sigma)/2 is positive definite and radially unbounded. Independent SymPy expansion of grad(V)·f +x²+(y−z)²+(1−gamma)z² gave exactly zero. For gamma<1 the dissipation is negative definite, implying global existence and GAS. At gamma=1 the zero-derivative set {x=0,y=z} has only the origin as invariant subset because xdot=y², so LaSalle proves all-solution convergence. For gamma>1, substitution of E±=(gamma−1,±sqrt(gamma−1),±sqrt(gamma−1)) into all three field components is exactly zero, prohibiting global attraction. Invariant compactly supported stationary measures are delta_origin, by integrating the nonnegative derivative defect and support invariance; equivalently global convergence and bounded convergence imply the same for any invariant probability. Normalization and endpoint are respected. No claim for controlled/load-forced PMSM, nor rates at gamma=1. The included verifier algebra is consistent but is not independent external certification.

## originality

FAIL

The full closed global-attraction claim is already implied by published Lorenz results. Zhang–Liao–Mu (2017), Remark 1(i), explicitly gives the exact coordinate swap (X,Y,Z)=(z,y,x) from this uncontrolled PMSM system to Lorenz with r=gamma,b=1. Kuznetsov–Mokaev–Kuznetsova–Kudryashova (2020), Theorem 1 and proof case r<=1, establishes all Lorenz trajectories converge to the unique origin for 0<r<=1 and every sigma>0,b=1; the endpoint follows by the standard invariant-set argument even though the article prints a strict derivative sign there. The regime r>1 has explicit nonzero equilibria, so no global attraction. The claimed compact invariant-probability rigidity follows as a general corollary of global attraction by invariance and bounded convergence for test functions, irrespective of whether this exact wording appears in prior papers. Negative gamma is outside the 2020 physical-positive-r statement but is a routine extension of the same classical quadratic argument, not a new motivated mathematical phenomenon. This is mathematical implication coverage, not a bibliographic title match.

## value

FAIL

As a mathematical finding, the sharp origin global-attraction threshold is already a standard classical Lorenz result transported by the exact variable permutation explicitly published for this PMSM in 2017. The invariant probability assertion is an immediate generic consequence of convergence to a single equilibrium, not a new structural invariant or separately motivated classification. The gamma<=0 endpoint extension is the same elementary energy calculation and was not motivated as a distinct physical or mathematical gap. This is a useful engineering restatement but the claimed research contribution amounts to known theorem specialization/renaming plus a routine corollary, which does not meet the mathematical-value bar independently of correctness. This judgment is not based on the size of the result or on computational reproducibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
