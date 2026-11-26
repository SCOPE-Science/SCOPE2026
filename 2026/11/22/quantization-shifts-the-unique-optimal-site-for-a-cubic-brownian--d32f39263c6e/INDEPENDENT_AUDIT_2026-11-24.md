# Independent mathematical audit

## correctness

PASS

For s≤t, Wick pairing gives E[W_s³W_t³]=9s²t+6s³; integrating over both time orders gives 9/5. Independently reconstruct the posterior by putting Z=W_x/√x for x>0 and c=min(x,t). The Gaussian regression of W_t³−3tW_t onto Z is (c/√x)³(Z³−3Z), and that of 3tW_t is 3tcZ/√x. The integrated coefficients of Z and Z³−3Z are b₁=√x(3−x²)/2 and b₃=x^(3/2)(1−3x/4), which recover the frozen cubic decoder. The full scalar reading explains b₁²+6b₃² by orthogonality. The sign datum explains (2/π)(b₁−b₃)² because the signed Gaussian moments of Z and Z³−3Z are ±√(2/π), respectively. This recovers the stated m and both gain/risk formulas; at x=0 the datum is deterministic and its explained variance is zero. The sign gain is maximized at the unique interior zero of 5x²−12x+6, with positive and then negative derivative. For the full gain, 8G'=g and g'=4x(145x²−216x+54); the latter quadratic is positive at 0, negative at 1 and tends to +∞, so g first increases and then decreases on [0,1]. The opposite endpoint signs and signs at 3/4, 4/5 prove one interior maximizer, bracketed by those fractions. Since (6−√6)/5<3/4, the inequality between the sites is also certified without decimal comparisons. Exact substitution gives the sign maximum and explained fraction. Bisection of the displayed g on (3/4,4/5) gives x_full≈0.7886095813305781 and substitution gives the stated numerical fractions and displacement.

## originality

PASS

The inspected indexed and primary sources establish related conditional-expectation methods and nearby designs, but none supplies the optimal-site comparison for the signed cubic Brownian integral from one predetermined observation. The distinct claim concerns the two exact risk functions and their strictly separated unique maxima; no novelty is claimed for conditional-expectation projection, Gaussian regression, sign moments or polynomial root tests themselves.

## value

PASS

This is a benchmark for whether quantization can be treated as a site-independent loss of information in a deterministic one-sample design. For a pure first Gaussian-chaos target the sign gain would be a constant fraction of the full gain, so the optimal site would not move. The signed cubic integral is the first higher odd power with competing first and third Hermite coefficients: the full reading adds their squared contributions, while sign sees one contrast. The two unique optimal sites and the roughly 0.079-horizon separation give a concrete, motivated counterexample to carrying the unquantized site over unchanged, useful for checking sampling methods for nonlinear Gaussian functionals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
