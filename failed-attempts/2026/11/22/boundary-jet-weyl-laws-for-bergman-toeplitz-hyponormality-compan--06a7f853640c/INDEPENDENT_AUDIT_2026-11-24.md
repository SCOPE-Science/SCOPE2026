# Independent mathematical audit

## correctness

PASS

For standard normalized Bergman area, d_n=(n+1) integral t^n g(t) dt and the self-commutator is diagonal with entry 1/[(n+1)(n+2)], including n=0. Inserting the shift weight gives the stated zero-diagonal J_g with bond ell sqrt((ell+1)(ell+2))(d_(n+1)−d_n), ell=n+1. Integration by parts gives the t^ell(1−t) g'(t) moment; the endpoint terms vanish by absolute continuity. After normalizing to Beta(ell+1,2), Taylor expansion and its beta moments yield the coefficients and O(ell^−r−1) error; the integral over the complement of the endpoint neighborhood is exponentially small times ||g'||_1. The frozen Weyl argument is for the actual zero-diagonal K_g; read its introductory Jacobi lemma in that setting, not as allowing arbitrary diagonals. Rank bounds for head excision and block cuts, a tail norm below threshold, and the norm margins on frozen blocks yield the cosine-symbol integral by Riemann sums. Strict thresholds cause no ambiguity because the integral level set has zero measure. This step also follows exactly from Pushnitski Theorem 1.2. Integrating powers of |2 cos theta| and inverting the count give the stated constants and Schatten cutoffs. At a=s/2 the exact rational-square-root bond gives c1=a(1/2−2a), whose only positive zero is a=1/4; expanding its square there gives c2=−7/64. A direct polynomial realization is g(t)=(1−t)^(r+1): its derivative starts at order r so the normalized beta expectation has leading coefficient −(r+1)!, with lower orders zero. Own exact checks /workspace/branches/independent-replays.py 5 obtained the exceptional squared-bond series 1/16−7z²/128 and verified 40 pure-jet beta integrals. The frozen finite checker was read, not executed.

## originality

FAIL

The complete spectral conclusion is a direct instance of verified prior banded-matrix asymptotics, not just an analogy with fast-variation Jacobi theory. The companion entries are already available from Le–Simanek and Simanek. The strongest same-day counterpart b8745f13efaa gives the identical power bonds, explicit first correction and a positive polynomial difference giving the exceptional second coefficient. Combining these with Pushnitski's exact theorem produces the whole displayed power-symbol law without a new spectral argument. The residual smooth-symbol calculation is the direct Taylor expansion of an exact classical beta moment of the established entries, and the arbitrary polynomial orders are immediate from pure powers of 1−t. These are mechanical implications and not independent new spectral invariants. No precedence between the same-day records is inferred.

## value

FAIL

Quantitative ideal membership of the companion is a motivated question. In this case, however, the exact asymptotic is a banded-law specialization, and the advertised half-power transition for the compact remainder follows by one coefficient extraction from already matching bonds. After removing the covered spectral statement, the all-order coefficients are a direct Taylor moment calculation and the polynomial construction is an immediate pure-jet example. No substantively new useful exact invariant remains for a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
