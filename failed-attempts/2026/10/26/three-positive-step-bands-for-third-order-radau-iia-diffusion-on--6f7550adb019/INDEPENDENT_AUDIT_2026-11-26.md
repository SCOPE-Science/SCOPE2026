# Independent mathematical audit

## correctness

PASS

Computed r(z)=1−z bᵀ(I+zA)^−1 1 from the two-stage Radau IIA tableau, obtaining (6−2z)/(z²+4z+6). On constants, leaf differences, and the hub-versus-leaves vector (m,−1,…,−1), the Laplacian eigenvalues are 0, 1, and m+1. Write p=r(h), q=r((m+1)h). The hub diagonal and hub–leaf entry are (1+mq)/(m+1) and u=(1−q)/(m+1). Mass conservation and the leaf-difference eigenvalue give leaf off-diagonal (1−u−p)/m and leaf diagonal p+(1−u−p)/m. Symbolically clearing positive denominators independently gives all four numerators in RESULT.md; both off-diagonal numerators are strictly positive for h>0. The hub discriminant changes sign between m=10 and m=11, and the two roots for m≥11 lie in (0,2). For the leaf polynomial, coefficient regrouping in m gives strict positivity for h∈[0,3] and concavity in m beyond h=3. The positive endpoint certificates at m=2 and 10 ensure positivity throughout that range. For m≥11, the exact negative evaluation F_m(m) is minus a polynomial with positive coefficients in m−11. Positivity at 3 and infinity forces two distinct roots, which are simple and exhaustive by the two sign variations in Descartes' rule. The two open failure intervals are disjoint and all four endpoints belong to the admissible set; h=0 gives the identity. This is endpoint entrywise positivity, not internal-stage positivity or accuracy. Read verify.py and verification_output.txt without executing the frozen script; replay `python3 /workspace/branches/independent_checks.py` (section 4; SymPy and mpmath) for exact symbolic derivation and the m=11 numerical illustration. The root count is analytic.

## originality

FAIL

The identical full classification is demonstrably covered by distinct indexed results 17146a0a41df and 3d0ba37aabda: same scheme, graph domain, cutoff, quadratic and quartic thresholds, sign mechanisms and safe endpoint set. They are listed under later dates than the frozen record; this establishes exact equivalence and lack of a distinct contribution in the current catalogue, not that either comparator historically preceded the frozen result or that there was copying. The simple root-location bound using h=m is a sign certificate for the same thresholds, not a distinct classification. In contrast, the same-date balanced multipartite and rook results do not imply the star classification. No earlier historical priority is assigned by this review.

## value

PASS

The mathematical classification is useful: it shows that unconditional spectral stability and conservation do not preclude two separated failures of the discrete maximum principle, identifies the first failing star, and specifies exactly when each vertex class needs a smaller or a larger step. This is a structural graph-family result, not a numerical instance check. That usefulness does not make the frozen classification distinct from the exact catalogue matches.

The dated certificate retains the supplied scientific assessment, sources and limitations.
