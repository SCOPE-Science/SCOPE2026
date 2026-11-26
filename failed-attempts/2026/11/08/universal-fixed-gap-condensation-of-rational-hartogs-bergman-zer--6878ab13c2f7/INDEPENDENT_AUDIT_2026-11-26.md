# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md §§1–4. Centering the two triangular weights gives the convolution in (1): any nonzero summand has |mB| ≤ (n+1)(m−1), hence |B| ≤ n, so extending the range adds nothing. The support bounds give |j| ≤ k, and A=m−1 gives a positive endpoint summand at j=k since k<m; reflection supplies the other endpoint. The normalized coefficients are whole-line trapezoidal sums of compact tent products. Off their finitely many corners the per-cell error is O_k(m^−3); at corners Lipschitz continuity gives O_k(m^−2). The three tent integrals give normalized coefficients 1 at |j|=k, 6(k−|j|) for 0<|j|<k, and 6k−2 at j=0, exactly the asserted factorization. For (4), use V=nA+mB and j=(kA+V)/m; the congruence indicator yields two nonnegative Fejér factors. The first factors sum to m² by coprimality, and the second factors have lower bound sin²(θ/2), with θ=0 handled directly. Rouché gives one root in each simple-root cluster at scale m^−2 and two in each double-root cluster at scale m^−1. Conjugate reciprocation preserves each unit-point cluster for large m (use fixed disjoint neighborhoods and then the shrinking estimates); no roots are on the circle, so the two roots in each such cluster are distinct, one inside and one outside. The slice is realizable for 0<|z|<1 by taking the two points with equal coordinate moduli sqrt(|z|) and appropriate phases, and the denominator there does not vanish. No uniformity in growing k is inferred. CHECK.py and requirements.txt were inspected, not run; the reported finite tests in VERIFICATION.md are not inputs to the analytical proof.

## originality

FAIL

A distinct indexed finding establishes material mathematical coverage of the advertised arbitrary fixed-gap advance: its k≥2 coefficient law and outlier rate match, and its residue-dependent boundary expansion is stronger. Both entries bear the same date, which does not establish order or historical priority; the failure is that a distinct contribution beyond the matching indexed result is not established, not an attribution of precedence. The remaining k=1 case is covered by the explicit gap-one family of Edholm–Mathew and does not salvage the advertised claim.

## value

PASS

The quantitative fixed-gap statement is mathematically useful on its merits: it separates one persistent interior zero from boundary-bound families and resolves simple-root counts despite multiple roots of the limit. The oblique slice consists of actual kernel arguments and is not an arbitrary restriction. This scientific relevance is distinct from the failure to establish a distinct contribution relative to the stronger matching record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
