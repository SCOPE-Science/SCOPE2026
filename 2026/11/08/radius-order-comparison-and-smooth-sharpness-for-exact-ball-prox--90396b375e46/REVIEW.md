# Independent mathematical audit

## correctness

PASS

PASS: In orthogonally transformed nonnegative coordinates, the exact strictly convex Euclidean-ball subproblem has a unique KKT multiplier λ and scalar equations p_i+λφ_i’(p_i)=w_i. Scalar outputs are monotone in inputs and inverse-monotone in λ; the displacement norm is nondecreasing in inputs and λ, so the λ adjustment gives an order-preserving ball map at fixed t and coordinatewise output monotonicity as radius grows. Induction compares any ordered radius schedules. Each nonterminal radius-t step reduces transformed ℓ1 by at least t, giving N_t≤ceil(||w0||1/t). The explicit diagonal SPD quadratic with coefficient ε^{i-d} has exactly d nonterminal/terminal steps from ones for sufficiently small ε by a feasible-comparison induction; the construction establishes sharpness for every d≥2 without numerical extrapolation. Independent scalar-KKT bisection comparisons tested 1600 ordered-radius trajectory steps for independent diagonal quadratics in d=2..6.

## originality

PASS

PASS best of knowledge: The primary Richtárik–Li paper proves general convergence, an O_d distance/radius bound, a nonsmooth polyhedral sharpness family and counterexamples to radius ordering for arbitrary coupled convex functions. Neither it nor the original Broximal paper proves a coordinatewise radius-order comparison for *all* orthogonally separable strictly convex objectives or a smooth SPD sharpness witness. The statement is restricted enough to avoid contradicting their general nonmonotonicity. Primary Richtárik–Li complete preprint was inaccessible here; this remains a concrete priority risk.

## value

PASS

PASS: Choosing exact ball radii is a structural convergence question, and larger radius does not improve general coupled convex trajectories. The result identifies a natural sufficient geometry where coordinatewise comparison is rigorous for all schedules, strengthens a useful finite-length guarantee, and establishes sharp dimension dependence within smooth strongly convex functions rather than a polyhedral limiting example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
