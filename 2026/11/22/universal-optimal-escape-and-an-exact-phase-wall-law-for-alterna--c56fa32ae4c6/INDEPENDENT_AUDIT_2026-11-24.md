# Independent mathematical audit

## correctness

PASS

Reconstructed the substochastic path sum in RESULT.md lines 28–60. Both matrices have determinant −r; nonnegativity and positive stationary weights give S_N ≥ min(π) times the sum of the product entries, at least min(π) r^(N/2). The alternating product is rI plus the square-zero lower off-diagonal with coefficient b(a+1−b). Multiplying its power by π and by either the all-ones vector or K_0 times that vector gives both parities with the stated normalization, including S_0=1. If a periodic word is not alternating cyclically, its doubled word contains an equal consecutive pair. The equal-symbol square is positive and multiplication by other factors preserves positivity; the period product is therefore primitive. Its Perron eigenvalue strictly exceeds the geometric mean of the two eigenvalue moduli, and its contribution to survival is positive. Survival monotonicity sandwiches lengths between successive period multiples, so the strict rate comparison holds along all horizons. The only even-skeleton change is 1→0; each of its n possible placements has mass γr^n, the two constant paths together have mass r^n, and the conditional location is uniform for n≥1. Independent rational checks gave S_4=4/27 at a=b=2/3 and S_4=7/256 at a=3/4,b=1/4, the latter with crossing mass 3/256 at each of two locations. CHECK.py was inspected, not executed; its finite tests are supplemental.

## originality

PASS

The fair iid doubling case is already covered and is not credited as new. The supported distinct scope is arbitrary strictly positive binary Markov transitions: the optimum over prescribed schedules for asymptotic escape, strict periodic equality classification, and exact Markov-dependent survival and conditional wall law. The inspected fixed-hole and time-dependent frameworks do not give those joint conclusions.

## value

PASS

The comparison over arbitrary predetermined words and strict periodic classification go beyond evaluating a single Perron root. The same exact product explains why a linear survival prefactor and an asymptotically uniform switching location coexist with optimal exponential escape. The failure of finite-horizon optimality for a biased source makes the distinction between finite and asymptotic optimization substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
