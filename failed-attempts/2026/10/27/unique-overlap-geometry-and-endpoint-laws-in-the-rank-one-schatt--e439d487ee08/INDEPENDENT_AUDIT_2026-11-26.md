# Independent mathematical audit

## correctness

PASS

Normalize the common nonzero singular value to one. For input/output overlaps c,d the squared singular values have product (1-c²)(1-d²) and trace maximized at 2+2cd by aligning the phases. At fixed product their p/2-power sum increases strictly in trace (differentiate for unequal positive eigenvalues and use continuity or the one-nonzero-eigenvalue formula at the boundary). Real two-dimensional vectors realize every aligned c,d. Setting c=tanh z and d=tanh w reduces the conditional log derivative in w to a positive factor times tanh((p/2)(z+w))-tanh w, so the interior maximum is w=kz; c=0 or 1 can only give an optimum of one. The reduced objective H has H>1 for finite z>0 by strict convexity of log cosh and the exact weighted-mean relation, and tends to one at both ends. Its derivative changes sign where the ratio of integrals of sech²(az) over [1,p] and [p,k] crosses one. The ratio is strictly increasing because the ratio of these integrands at z₂>z₁ strictly decreases with a; its limits are 1/k and infinity by the dominant lower endpoints. This checks existence, uniqueness and all equality conditions in the stated class. With ε=p-1, expand the derivative bracket to 2ε²z sech²(z)(1-z tanh z)+O(ε³) on compact intervals and bracket its root at z₀. The second-order log-objective term is ε²z² sech²(z)/2, yielding (z₀²-1)/2; an independent scalar bisection gave 0.2196144199453. The Hilbert endpoint also follows without tracking z: the aligned squared quotient converges uniformly on [0,1]² to (1+cd)/(1+c²), whose unique maximum is at c=√2-1,d=1. Compactness then gives convergence of both maximizers and the optimal constant. Frozen verification code was inspected, not run; the reported finite tests do not certify the universal optimization. No unrestricted low-p sharp bound follows.

## originality

FAIL

A distinct indexed finding explicitly gives the identical balanced rank-one class, sharp constant, unique root and full equality geometry, and strengthens the trace-endpoint expansion. The remaining Hilbert limit and overlap are not stated there in the inspected passages but follow directly from its two-variable quotient including the compact boundary. This finding of current coverage is not a determination of discovery or publication priority from catalogue dates.

## value

FAIL

The optimization and full equality geometry would be useful as a genuinely uncovered exact restricted result. Here they are already covered with a stronger trace expansion. The residual p↑2 statements follow from a compact two-variable maximization at the known Hilbert endpoint and contain no new rate or other nontrivial invariant there. No valuable independent remainder justifies repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
