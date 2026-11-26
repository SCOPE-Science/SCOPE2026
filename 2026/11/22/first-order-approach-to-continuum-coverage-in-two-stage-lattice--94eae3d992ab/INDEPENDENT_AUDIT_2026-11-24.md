# Independent mathematical audit

## correctness

PASS

The first accepted short rod splits an interval into two smaller ones with uniform feasible starts. The resulting first-placement recurrence gives B_s(z)=A_s(z)/(1−z)^2 with A_s entire, A_s(1)=p_s and A_s′(1)=s−(s−1)p_s. Subtracting the poles gives b_s(n)=p_s n−s(1−p_s) plus an absolutely summable error. Conditional on the first-stage gaps, expectation is additive even though the global short-rod sampling interleaves gaps: conditional on selecting a gap, its feasible starts are uniform. The zero-gap-inclusive sum identities give counts p_k/k and empty length 1−p_k per site. Splitting the integral for the maximal gap density at 1−1/k bounds it by O(log k/k²), so the summable remainder gives exactly the stronger stated intermediate estimate. For p_k, the change t=e^(−x/k) and trapezoid expansion on x≤L=k^(1/4) leave first-order integrand (1−e^(−x))W(x); the integrated remainder multiplied by k is O(L/k) using W=O((1+x)^−2), and integration by parts gives p∞/2. On x≥L the harmonic prefactor and geometric-logarithm approximations have scaled integrated error tending to zero (the prefactor alone contributes O(1/L), and the remaining tails are exponentially small in L). After scaling x=ky, the difference e^(−y)/(1−e^(−y))²−1/y² has integral −1/2, so the tail contributes −exp(−2γ)/2. This produces the stated p_k coefficient and, after substitution, the positive defect for each fixed s≥2. In fact the single-site gap density is positive, so 1−p_s>0. Independent quadrature gives p∞=0.7475979202534115 and the s=2 coefficient 0.1730958919649851; the scaled defect at k=4096 is about 0.17308409. The quadrature is a diagnostic, not the asymptotic proof.

## originality

PASS

Credit Pinsky for the exact Model I equations and the limiting density, and credit the classical one-stage literature for the lattice-to-continuum law and known inverse-length scale. The supported distinct claim is the exact two-stage inverse-length defect and short-rod boundary penalty for fixed s. The closest distinct Resultary item takes both rod lengths to infinity at fixed ratio; it does not retain this finite-short-length correction. No priority claim is needed for the intermediate one-stage coefficient.

## value

PASS

The signed rate refines an established limiting model and answers a concrete approach question not answered by convergence alone. It quantifies the competition between a positive first-stage lattice correction and a larger negative finite-gap short-rod penalty. This supplies a reusable boundary estimate and shows eventual approach from below for each fixed short rod, without claiming monotonicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
