# Independent mathematical audit

## correctness

PASS

Expanding the exact EOS third iterate at x=-1/2+u/a for epsilon=e^-a/6 and b=1/3+(2/3)epsilon*t gives normalized return H=2(t-sinh u)+O(a epsilon) in C1; strict negative derivative yields unique local primitive 3-cycle. Return derivative gives multiplier gap 2a epsilon sqrt(1+t²)+O(a²epsilon²), and implicit differentiation yields dx_j/db=(3/(2a epsilon sqrt(1+t²)))(1+O(a epsilon)). Correctness holds uniformly for bounded t, sufficiently large a, not all detunings.

## originality

FAIL

DECISIVE PRIOR COVERAGE: the earlier published Nov 2, 2026 inverse-hyperbolic-sine resonance profile uses sigma with b=1/3+sigma*epsilon, positions asinh(3sigma/2)/a, multiplier 1-2a epsilon sqrt(1+9sigma²/4), and dx0/db=3/(2a epsilon sqrt(1+9sigma²/4)). Setting t=3sigma/2 makes these formulas IDENTICAL, and derivatives for other cycle points follow routinely by chain rule since F′→1. Earlier full proof contains the same uniform local uniqueness and attraction.

## value

FAIL

The singular crossover is mathematically motivated, but the submitted theorem is a reparameterization and routine coordinate-derivative corollary of the already published full result. It supplies no independent non-implied exact fact; originality and independent value therefore fail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
