# Scientific review: heterogeneous directed-cycle RK4 positivity

## Correctness — PASS

The proof covers every integer \(n\ge5\), every strictly positive real rate vector, and all nonnegative timesteps. Exact path combinatorics derive the only five possible nonzero matrix-entry types. The two-jump quadratic has strictly negative discriminant, and the one-jump cubic has a strictly negative derivative, yielding the unique sharp interval and no reentry. The four-maximum-rate plateau equivalence follows from the exact identity \(F_{a,b}(2/(a+b))=1/3\); the universal sharp improvement factor follows from diagonal mass accounting and a single-defect limiting family. The standalone checker reproduces 14,200 exact matrix entries, 1,800 exact row sums, 1,200 two-sided numerical boundary cases, and six exact single-defect phase identities. Such finite tests supplement rather than substitute for the proofs.

## Originality — PASS on inspected evidence, with residual priority risk

The nearest methodological antecedents are Gottlieb–Shu–Tadmor (2001) on linear SSP methods, Horváth (2005) on positivity step-size thresholds, Horváth–Song–Terlaky (2015) on general sufficient polynomial-root invariance bounds, and Blanes–Iserles–Macnamara (2021) on nonsymmetric positivity-preserving graph-Laplacian integration. The 2015 framework supplies a generic algorithmic sufficient bound but not this exact closed local-rate classification, the proof that distance two never obstructs, the sharp four-consecutive-maximum criterion, or the optimal gain \(2.7852935634052818\ldots\). Compared published mathematical claims concern different integrators or symmetric networks. Targeted published-finding corpus and literature searches found no identical or stronger special-case statement. Unindexed sources and the risk of a differently formulated specialization remain.

## Mathematical value — PASS

This is a complete, sharp, all-size numerical-positivity classification for finite irreducible nonreversible Markov generators with arbitrary positive directional rates. It computes the admissible step from only \(O(n)\) local rate windows, identifies exactly when the forward-Euler constraint is improvable, and quantifies the best possible factor. The single-defect contrast produces a nontrivial sharp switch between one-jump and three-jump failure mechanisms. These properties are directly relevant to positivity-safe integration of nonuniform cyclic transport and Markov models.

## Relationship and limits

The result is a linear autonomous endpoint theorem, not an unconditional positivity scheme. The universal gain is approached in a singular high-contrast limit but never attained at finite positive rates. Published general SSP results and generic polynomial-threshold algorithms are acknowledged, and exact publication priority cannot be certified from bounded searching.

Self-review: passed. Independent audit: not yet performed.
