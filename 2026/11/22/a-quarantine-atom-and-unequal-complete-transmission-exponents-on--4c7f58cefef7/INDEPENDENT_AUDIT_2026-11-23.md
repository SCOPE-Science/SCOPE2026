# Independent mathematical audit

## correctness

PASS

Under the usual independent per-contact transmission clocks conditional on contact paths, the shared-hub process is a binomial mixture over stopped active occupation, not over an independent recovery time for each leaf. For the Laplace transforms F_off,F_on starting from the two states, first-event conditioning gives (a+μ)F_off=μ+aF_on and (b+μ+s)F_on=μ+bF_off. Eliminating F_off gives F_on=r/(r+s); stationary mixing adds the mass d at zero. Substitution x=exp(−λu) in the continuous part gives the stated beta integral and gamma ratio. Link independence is conditional on the same hub recovery time: the one-link survival ν(t) comes from the two killed eigenvalues. The quadratic evaluated at λπ equals −λ²ab/(a+b)²; thus ρ<λπ<R, and initialization ν(0)=1, ν′(0)=−λπ gives strictly positive modal weights. In the full-infection integral, z=kc exp(−ρt) gives kν(t)→z at fixed z because R/ρ>1; the factor (1−ν)^k is bounded by exp(−z), giving the claimed gamma prefactor including c^(−μ/ρ). In the zero-infection integral, the near-zero scaling t=z/k is dominated by exp(−λπ z/2) on a sufficiently short fixed interval; the rest is exponentially small. Since λπ<λ(a+μ)/(a+b+μ)=λμ/r, the inequality of exponents is strict throughout the positive regime. At fixed recovery time the mean is unchanged; Bernstein's second-difference identity proves the convex-order comparison, and both endpoint functions are strictly convex for k≥2. Active occupation is nonconstant for t>0, making both inequalities strict. For replay the transform equations, beta substitution and the two rescalings suffice. At unit rates the one-link survival transform at s=1 gives 7/10, confirming the illustrated LI none/all relation 1−2(7/10)+47/88=59/440. The finite checker was inspected, not run: its finite-state solves are rational but its comparisons with formula evaluations and quadrature are numerical. Conclusions are for a single hub, stationary switching, common independent exponential recovery and fixed positive rates, not general contact graphs or population-level thresholds.

## originality

PASS

Limited to the paired stationary Markov switching comparison under matched full one-edge availability law and common recovery: the nonvanishing zero-offspring mass for the shared gate versus the vanishing independent-link probability, and the strict inequality of the two complete-transmission exponents with their constants. Generic convex order, beta-binomial endpoint powers and the use of a two-state survival matrix are already established.

## value

PASS

This gives an exact mathematical counterexample to using marginal contact dynamics or mean offspring as a surrogate for final-size extremes when comparing two idealized public-health contact models. The exponent gap and zero-count atom distinguish them even as degree grows; the contribution is stronger than merely showing dependence matters. The comparison is a theoretical model diagnostic, not a prescription or an extrapolation to population risk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
