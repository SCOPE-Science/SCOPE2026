# Independent mathematical audit

## correctness

PASS

The theorem's attraction and branch conclusions survive, but the frozen leafwise Jacobian incorrectly multiplies the first row by cos(tr), and the checker reproduced the wrong multiplier. The corrected files take the derivative of the actual shift-and-sine fiber map: first row (0,1), second row (tβ₀ cos(tr),tδ₀ cos(tr)). With q=t cos(tr), the characteristic polynomial is λ²−qδ₀λ−qβ₀, and the root through 1 has derivative 1/(1+β₀) at q=1. At a nonzero branch q=1−2(t−1)+O((t−1)²); the corrected multiplier is 1−2(t−1)/(1+β₀)+O((t−1)²). The other tends to −β₀ with β₀≤1/2. The central branch has q=t and loses stability. At t=1 a unit eigenvalue contradicts any uniform exponential attraction bound by differentiation. The scalar equation r=sin(tr) gives existence for every t>1 and exactly one positive and one negative root near t=1 by strict decrease of sin(tr)/r there; Taylor expansion gives the stated square-root law. Independently, direct cancellation yields W_n=W₀+nα, x and y are bounded after two steps, and a nonzero translation of the real line has no finite invariant probability. Squaring the nonnegative error majorant gives row sums s and β+δs≤s for s<1, proving the graph assertion and rate. The sine Taylor remainder plus the zero-coupling graph error gives s²/2+s² in the irrational Haar estimate. Zero-drift uniqueness, convergence and recurrence on the s<1 planes give exactly the invariant mixtures. The repaired RESULT.md, checker and reproducibility notes preserve the claim and correct the stability calculation; the frozen checker was inspected, not run. The conclusion rests on the analytic proof, not the finite checker.

## originality

PASS

The supported distinction is the exact neutral cancellation and its global and quantitative consequences for the feedback model. The corrected stability calculation does not enlarge that claim. The scalar sine pitchfork and Banach graph-transform method are not themselves original results.

## value

PASS

The cancellation identifies a solvable boundary regime of an existing feedback model. The result separates full-space drift and nonexistence of invariant probability from a global law for the bounded coordinates, with a useful error bound for stationary bias. The corrected leafwise analysis explains exactly where the uniform contraction result stops and avoids conflating leafwise and ambient attraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
