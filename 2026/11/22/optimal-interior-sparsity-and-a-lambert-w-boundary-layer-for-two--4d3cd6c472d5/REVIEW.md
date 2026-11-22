# Scientific review

## Correctness — PASS

The four projective lines exhaust all nonzero two-entry signed rows, and their pairwise intersection consists of the zero row. Inclusion-exclusion gives the exact probability. The derivative argument proves strict global uniqueness for every integer \(m\ge2\); the bound \(\delta_m\le W(m-1)/(3(m-1))\) justifies the asymptotic logarithm expansion. The standalone exact-rational enumerator checks 15 finite parameter combinations without assuming the formula. The proof covers all stated finite row counts; the finite experiments alone do not.

## Originality — PASS, with priority uncertainty

Actual searches compared sparse signed two-column rank failure, its four-direction projective formulation, density optimization, geometric versus Bernoulli rank laws, and Lambert-\(W\) sparsity boundaries. The accessible source articles focus on generic embedding guarantees, random matrix rank in joint large dimensions, or different entry models. Closest searchable research records about rank-two pure Rademacher Nyström, signed CountSketch, two-block SparseStack, and stochastic-rounding rank restoration do not imply the independent-entry ternary density optimum. The dense \(p=1\) endpoint can be recovered from pure-sign results; novelty is not claimed for that endpoint. Several specialized results were available only by summaries, and possible unindexed exact two-column formulas remain a risk.

## Value — PASS

A rank-deficient sketch cannot preserve an exact two-dimensional coordinate space or yield a full-column-rank sketched QR factor. The exact all-row-count density optimizer makes precise a consequential design choice: dense signs can have exponentially worse **exact rank-survival** failure probability than a sketch using fewer expected nonzeros. The universal limiting density and Lambert-\(W\) correction reveal the finite-budget adjustment needed to halve the leading failure coefficient. This does not assert superiority for numerical stability, conditioning or generic subspaces.

## Limitations

The application is a model benchmark in exact arithmetic, not a uniform oblivious embedding theorem. Independent publication-priority checks may find a stronger source; no independent validation was carried out. No experiments are presented as infinite proofs.

Self-review: passed. Independent audit: not yet performed.
