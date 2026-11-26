# Independent mathematical audit

## correctness

PASS

For uniform permutation insertion, root rank is uniform and the subtrees are conditionally independent. Decompose the conditional leaf means into a flat term plus boundary deviations δ_0=−1/3 and δ_1=1/3. For C_n the law of total covariance then gives n C_n=2Σ_{k<n}C_k−(4/3)(H_{n−1}−1), since b_{n−1}−b_{n−2}=2(H_{n−1}−1) for the path-length mean. With C_2=0, subtract consecutive recurrences and divide by n+1 to obtain C_n/(n+1)−C_{n−1}/n=−4/[3(n−1)n(n+1)], which telescopes to the stated expression. This also checks the degenerate n=2 and first nonzero n=3 cases. The leaf-local indicators give the stated variance for n≥4; the classical internal path-length variance, in the same root-depth-zero convention, tends to (7−2π²/3)n² to leading order. Normalization gives the finite correlation and limit. Frozen support was inspected but not run. A separate exact rational mixed-moment recurrence passed n=2 through 80 (replay /workspace/branches/f1bec0d3-8e57-4f7f-9837-e8bb06c0643a/independent_mixed_recurrence.py); the finite test does not replace the recurrence proof.

## originality

FAIL

The main identity was already stated and proved for exactly these variables and all n≥2 in the October 12 Resultary record random-bst-leaf-abundance…2943b7ea14eb. The shifted-looking numerator (n−2)(n+3) is n(n+1)−6. That earlier record also supplies the finite leaf variance. Normalizing its covariance by that variance and the established path-length variance gives the finite correlation immediately; the limiting constant follows from the classical leading variance coefficient. There is no distinct mathematical remainder to repair. This is verified earlier catalogue coverage, not a claim about ultimate publication priority.

## value

FAIL

The exact covariance is a well-motivated invariant and is useful for quantifying the link between leaves and search depth, but this same quantitative gap was already closed by the earlier exact result. Presenting the known covariance and marginal variances as a Pearson correlation is routine normalization; it yields no independent result of comparable value, even though the formulas themselves are correct.

The dated certificate retains the supplied scientific assessment, sources and limitations.
