# Independent mathematical audit

## correctness

PASS

For fixed start/reset position x, the cover time is pathwise the maximum of the two first hits, including an endpoint occupied initially. For a target, let φ be its no-reset first-hit Laplace transform at r; a renewal attempt succeeds with probability φ and lasts on average (1−φ)/r, giving mean (1−φ)/(rφ). Solving the Dirichlet/Neumann problems (two Dirichlet conditions for either endpoint) and taking the sum of the two target means minus the either-hit mean gives the stated objective. In z=cosh(sqrt(r/D)(x−L/2)), b=cosh(sqrt(ρ)), the derivative has positive denominator and numerator b F_b(z²); re-expansion gives F_b(y)=(3−4b²)y²+4b²(b²−1)y+(b²−1)². Its roots have opposite signs and its positive root is simple, so only z=1,b can minimize. The difference H_b(1)−H_b(b)=−(b−1)(2b²−b−2)/b gives all ties, locations and the stated minimum. F_b(b²)=1−2b²<0, F_b(1)=5(b²−1)²−1; hence endpoints are always strict one-sided minima and each half gains exactly one maximum when F_b(1)>0. At equality H''_b(1)<0 and z−1 is quadratic in displacement, giving strict quartic flatness. At b_s the crossing polynomial is 2/sqrt(5)−b_s<0, confirming b_s<b_c. Replay: frozen RESULT.md proof lines 43–113. VERIFICATION.md reports 748 finite assertions, including boundary-value discretization; verify.py was inspected, not executed, and is not needed for the continuum proof.

## originality

FAIL

A distinct indexed Resultary record contains the same global and local optimization at exactly the same parameters, with the same rational shape reduction and sign polynomial. This is demonstrated equivalent coverage in the inspected corpus, not a claim that the later catalogue path establishes historical priority. Linn–Lawley independently supply the underlying mean, but are not credited with stating the optimization classification.

## value

PASS

As mathematics, a complete classification of all competing reset locations for a natural design problem is useful: the global switch, persistent endpoint minima and distinct midpoint stability threshold answer questions not conveyed by reporting either the mean or the midpoint optimum alone. This value judgment does not credit the frozen record with originality over the indexed classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
