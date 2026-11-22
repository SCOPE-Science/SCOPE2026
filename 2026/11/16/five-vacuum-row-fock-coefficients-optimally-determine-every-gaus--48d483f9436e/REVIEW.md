# Independent mathematical audit

## correctness

PASS

PASS. Work from the frozen RESULT.md: each full-dimensional unit-contrast ellipse has a unique trace-one normalized quadratic Q=s+b·X−XᵀAX, with tr A=1. Differences Q1−Q0 cancel the otherwise unobserved radial |X|² term, leaving precisely the five measured real Gaussian harmonic features (1,x,y,x²−y²,2xy). On the symmetric difference of interiors, (1_E1−1_E0)(Q1−Q0)>0, giving injectivity even when centers and anisotropy vary; same boundary implies identical normalized Q. The five-dimensional open ellipse parameter manifold cannot inject continuously into R^4 by invariance of domain. The convex positive-part potential F(θ)=∫(Qθ)+dγ has gradient the moment map for a nonempty ellipse; equality in its support inequality forces the same positivity set, so the data's minimizer is unique. Boundary coarea gives J=(2 sqrt(detA))^(−1)∫_0^{2π} ψψᵀ e^(−|X(φ)|²)/π dφ; a traceless harmonic quadratic cannot vanish on the entire ellipse unless zero, proving J positive definite. Independently expanding the angular Gram on principal axes gives det J≥R^12/[64(detA)^(13/2)]exp[−5(|c|+R/sqrt(λ_min A))²], including the stated constant. The inspected 2932-byte numerical checker uses finite differences on three noncircular ellipses, supporting only those examples, not the universal proof. No reconstruction for unions, unknown contrast or uniform noise condition number follows.

## originality

PASS

Best-of-knowledge original residual scientific increment after explicitly excluding known prior coverage; exact historical priority is not certified. Material compared at the statement and implication level; finite or generic overlaps are acknowledged.

## value

PASS

PASS. A five-dimensional natural aperture family is determined by exactly five calibrated Fock coefficients even though the radial second moment is missing; optimal count, global constructive convex inversion, positive boundary Gram and explicit degeneration-sensitive bound are substantial inverse-moment facts beyond textbook moment identities. The precise coefficient set matters for finite-rank Fock localization and cannot be obtained by blindly naming ellipse parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
