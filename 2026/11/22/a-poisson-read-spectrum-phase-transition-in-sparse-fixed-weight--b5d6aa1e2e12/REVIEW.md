# Scientific review: sparse fixed-weight read histograms

## Correctness — PASS

The proof uses an exact stars-and-bars law for specified zero gaps and obtains every joint factorial moment of the finitely many short-gap counts. It verifies that triple-marker windows and boundary effects vanish at the stated critical scale, reconstructs every histogram coordinate, and proves injectivity using a pair-pattern coordinate. Total variation transfers the joint Poisson limit to the two-word equality probability; an exact gap count establishes the separated-reference probability. The included finite checker reproduces the affine histogram and binomial separated-word formula in 12,365 and 379 directly enumerated cases, respectively. Its finite simulation is illustrative rather than an infinite proof.

## Originality — PASS against checked evidence

The most relevant 2026 spectrum-preserving-set paper (arXiv:2602.19408) treats the presence set and its compression rather than multiplicity histograms of randomly sampled fixed-weight words. The substring-count deletion-code paper (arXiv:2609.19493) establishes coding bounds, not a sparse critical-window count vector or the Bessel two-word collision expression. General pattern-occurrence Poisson approximations do not directly supply the injective affine profile, independent gap orientation counts, and complete histogram collision probability. A known fixed-three-marker trigram spectrum classification has fixed marker count, not the growing square-root regime. Residual risk: an equivalent result might occur in unindexed rare-pattern or genomic-read literature.

## Value — PASS

There is a concrete statistical-reconstruction motivation: multiplicity-preserving short-read observations discard essentially all positional information in a sparse source, and at the square-root marker density the surviving differences have a nondegenerate universal law. The result supplies a full finite-dimensional histogram limit and explicit collision probability, with a sharp threshold and exact finite separated-event count. The formula quantifies readout ambiguity rather than merely bounding a single motif's expectation.

## Scope and limitations

The proof requires fixed read width, uniform fixed-weight binary input, and linear overlapping reads. It does not address growing widths, independent noisy reads, or uniqueness of source reconstruction. No quantitative convergence rate or independent third-party validation is claimed. Literature inspection is limited and cannot certify global priority.

Self-review: passed. Independent audit: not yet performed.
