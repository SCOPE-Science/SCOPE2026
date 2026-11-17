# Self-review

## Correctness — PASS

The claim concerns one concrete Schur multiplier norm and its induced-subgraph consequences. The core singular values and transitivity yield \(\|C_n\|_\bullet=2(n-1)/n<2\). The weighted trace formula is independently reconstructed from the graph's depth partial isometries and core singular-value multiplicities; its normalization uses \(S=\sum u_k^2\) and the exact layer count \(15R^k\). The finite certificate is checked by the embedded standard-library script: thirteen symmetric rational dual matrices have matrix-square row-sum defects at most \(2/100000\), which rigorously controls their operator norms, and an exact-rational trace inequality yields a lower bound above \(20029/10000\). The strict inequality propagates to every \(n\ge15\) by induced-subgraph monotonicity. Finite diagnostics are not substituted for the universal proof: the only infinite quantifier is discharged by the explicit induced-subgraph embedding. The proof depends on the established general Schur trace formula, whose hypotheses and reduction are restated in RESULT.md.

## Originality — PASS, with residual priority risk

The closest source is Levene, arXiv:2611.08419v1 (2026-11-05), Section 6: it reports precisely the \(J_{15}-I_{15}\), twelve-level, thousandfold-branching inequality only from uncertified numerical maximization, and says that its only proved productive core had a different tensor-product form. The present certificate closes that expressly acknowledged proof gap. The work does not claim to originate the tridiagonal formula, the definition of productivity, or the previously proven global half-line. Comparisons also cover Levene 2014 and the blocky-decomposition results of Beke et al. 2026. published-finding corpus searches, and the accessible local historical claims checked for the source, crown graph, productive-core terminology, factorization norm, and equivalent tree attachments, found no same implication. Numerical evidence in the source does not constitute a proof; nonetheless unknown independent certificates remain a publication-priority risk.

## Mathematical value — PASS

This is not a free numerical example or a routine restatement of an optimization formula. The motivating article makes the exact crown-core cutoff \(n=15\) an explicit prospective new productive family but leaves its numerical evidence uncertified; the verified strict margin closes that gap and gives every \(n\ge15\) by a transparent structural transfer. The result extends the class of proven productive cores from a single tensor-product construction to the natural crown family, making the known interval-producing theorem applicable to each. It does not claim an optimal size threshold, a new global half-line theorem, or a better bound for the first interval.

## Closest literature and limitations

Primary: Levene (2026), Theorem 3.8, Proposition 5.5, Remark 5.6 and Section 6; the precise numerical observation is the point of comparison. Historical: Levene (2014), early small-norm classifications and path calculations. Structural: Beke et al. (2026), decomposition into blocky matrices. A broader unindexed finite spectral certificate could cover this result. No independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
