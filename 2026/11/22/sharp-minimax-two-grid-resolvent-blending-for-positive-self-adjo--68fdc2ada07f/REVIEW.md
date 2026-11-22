# Mathematical review

## Correctness — PASS

The scalar multiplier identity follows from the resolvent geometric sum and \(2\coth(2z)=\coth z+\tanh z\). The one-turning-point lemma is proved using an exact quotient of entire positive-coefficient power series: the coefficient ratios \(4^n/[2n(2n-1)]-1\) strictly increase, hence \(J(z)=L'(z)/\operatorname{sech}^2z\) strictly increases. The real minimax objective is the larger of a strictly increasing interior negative-contact height and the strictly decreasing infinite-frequency positive-contact height. Their unique intersection gives \(w_*=1.7443084104\ldots\). The multiplier operator on \(L^2([0,\infty))\) has the exact full half-line spectrum, including both contacts. Real-part comparison and the limiting contact prove uniqueness over complex weights. All parameters, boundary conditions and the truncation distinction are explicit.

The supplementary `check_numeric.py` verifies the root interval, numerical constants, scalar functional-calculus identity and sampled error envelope in 10,008 diagnostic assertions; the infinite spectrum and monotonicity are proven analytically, not from the finite grid.

## Originality — PASS (subject to bibliographic limitations)

Castillo, *Sampled resolvents of \(C_0\)-semigroups: aliasing and sharp rates on the Crandall–Pazy scale* (arXiv:2611.15563v1), was inspected in its full preprint, especially the sampled-resolvent identity, Corollary 5.2 (fixed Romberg extrapolation coefficients), and Proposition 5.10(a) (the scalar Langevin-function sharpness mechanism). These results supply the underlying quadrature formulation and fix the classical Romberg weight \(w=4/3\); the corresponding sharp operator-norm coefficient \(h/6\) follows from the scalar calculation here, not a stated theorem of that preprint. They do not give the best possible all-spectral operator-norm weight and its strict equioscillating minimax proof. The present claim concerns an optimized two-grid *coefficient* and sharp uniform error over nonnegative self-adjoint semigroups, not merely the known first-order decay rate. Berrut–Trummer treat a distinct smooth/jump-integrand quadrature class. The accessible section of Dahal's multi-level extrapolation article concerns smooth expansions, not this spectral minimax objective. Published general approximation principles, such as Chebyshev equioscillation, are credited as prior foundations. An implicit broader minimax theorem is the principal remaining originality risk; no assertion of bibliographic completeness is made.

## Mathematical value — PASS

The two-level discretization is explicitly present in contemporary sampled-semigroup resolvent theory, yet ordinary smoothness-based Romberg coefficients do not minimize the uniform error for unbounded generators. The result gives the unique best implementable affine blend, a universal sharp operator-norm constant, and a single natural continuous-spectrum witness establishing optimality without finite-dimensional truncation. It quantifies a substantial strict reduction from \(1/6\) to \(0.0639228974\ldots\), clarifying which extrapolation objective matters for nonsmooth operator-norm data. The rate remains first order: improving the coefficient is the precise, not overstated, contribution.

## Remaining limitations

The theorem applies to nonnegative self-adjoint generators, real positive Laplace parameters, and infinite-time sampling. Signed blending may magnify independent noise; finite observation horizon, general nonnormality and arbitrary extra levels are outside scope. One older general approximation or weighted-resolvent theorem might imply the formula indirectly. The diagnostic script is not a proof for infinite spectral domains.

Self-review: passed. Independent audit: not yet performed.
