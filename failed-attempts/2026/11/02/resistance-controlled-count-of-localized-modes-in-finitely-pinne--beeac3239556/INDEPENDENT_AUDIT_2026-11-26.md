# Independent mathematical audit

## correctness

PASS

Staggering interchanges the band edges and removes signs from the finite-site resolvent by an orthogonal conjugation. The weighted Birman–Schwinger matrix decreases strictly in positive offset μ because the derivative quadratic form is the negative squared norm of the resolvent applied to a nonzero sum of distinct site vectors. The top-edge singularity is a positive rank-one logarithmic divergence plus the finite weighted Green difference −R/2, by dominated convergence for the difference. For any comparison level t off the limiting compression spectrum, a Schur complement of B_μ−tI in the divergent direction has exactly the limiting compression's inertia for sufficiently small μ, plus one positive direction; this identifies all finite limits with multiplicities. The positive congruence y_i=√κ_i x_i sends its complement to sum y_i=0 and transforms B−I's limiting finite form into Q. Strict decrease to zero gives exactly one crossing per limit above one and no crossing for equality. The two-point form on (1,−1) evaluates to R−1/κ_1−1/κ_2; the adjacent and diagonal resistances are 1/2 and 2/π, the latter also obtained by the torus change (x,y)=(u+v,u−v) and averaging sin²u/(1−cos u cos v). The compressed corner eigenvalues on the two displayed directions are 1/π and (π−1)/(3π). This verifies the thresholds and handles p=1 and all equalities without claiming a threshold-state classification. The above-band free resolvent decays exponentially and its convolution against finitely supported sources gives exponential localization. Independent finite-grid FFT-resolvent tests (python3 /workspace/review_evidence/reproduce.py 2) gave above-one counts [1,1,2,2,2,3,3] for seven mixed and equal noncritical pin sets; they are only corroboration.

## originality

FAIL

Shown already covered, not merely a plausible match: Hayashi–Higuchi–Nomura–Ogurisu, Theorem 1.1 (DOI 10.1007/s11005-016-0876-0), gives the same exact spectral count under a sign/scale change and for strictly more general potential signs. The prior theorem maps to every site and strength in the frozen claim, with the same strict convention at equality. The two-pin and three-corner examples are direct finite evaluations of that prior theorem with known resistances, not independent surviving results.

## value

FAIL

The resistance interpretation is useful exposition for this natural physical model, but the frozen central assertion is a positive-pin specialization of an established exact (and stronger) theorem. The two- and three-pin claims are immediate one- and two-dimensional evaluations of the earlier compression using already known resistances. The package supplies no independently valuable unknown remainder that would justify a scientific repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
