# Independent mathematical audit

## correctness

PASS

The original macroscopic equations (41)–(43) under equal rates/capacities and the stated normalization give the sum of the two separate crowding terms, with prey fractions x/(1+y) and xy/(1+y), and the stated predation and recruitment terms. At positive equilibria the predator equation forces λ=b/μ−1>0 and x=(1+y)/λ. The prey reaction on it is −P(y)/λ² with P=y²−By+1−λ and B=λ−aλ²/(1+λ). Root signs give the complete census: opposite signs for λ>1, the root 1−a/2 alongside zero at λ=1, and positive double or distinct roots precisely when B equals or exceeds 2√(1−λ) for 0<λ<1. The predator x-derivative G_x is positive along the positive nullcline, so det J=G_x P′/λ². This gives the lower saddle; the diagonal signs give negative trace and a sink at the upper root. The prey-only eigenvalues are −1 and μ(λ−1)/2. At the fold use r=x−(1+y)/λ as transverse coordinate: the second Jacobian column in (r,y) is zero, the trace is strictly negative, and a left zero eigenvector has nonzero first component since G_x>0. The reduced second derivative −2/λ² and a-derivative −y_f/(1+λ) project nontrivially, giving a generic fold. The rational witness follows by factoring P=(y−1/5)(y−1/2); the frozen standard-library checker and verification notes were inspected, not executed. These are homogeneous ODE results, not PDE stability or a global basin theorem.

## originality

FAIL

The strongest matching catalogue theorem 76d54fcca7fd addresses the same Bisi et al. homogeneous reaction law with additional free parameters, and directly implies the entire claimed equilibrium census, wedge, stability and nondegenerate fold. The reports share a date; equivalence and direct coverage, not an inferred date ordering, decide this assessment.

## value

PASS

The complete sharp classification is mathematically informative as a description of a motivated reaction law: it separates local failure of predator invasion from existence of a stable coexistence state and identifies the fold bounding that region. That structural value is already present in the covering theorem. The different rational witness alone is a routine illustration and supplies no valuable standalone repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
