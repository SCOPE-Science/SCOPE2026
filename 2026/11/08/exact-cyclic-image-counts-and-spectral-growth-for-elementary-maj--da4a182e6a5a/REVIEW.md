# Scientific review

## Correctness — PASS

The output/predecessor equivalence is exactly the closed-walk criterion in the four-state pair graph. The script builds every reachable Boolean relation from the identity, finding 120 distinct states and 75 nonzero-diagonal states. It verifies the full vector identity \(P(T)f=-9e_0\), where \(P(X)=X^{10}D(1/X)\) with \(Te_0=0\), which proves the order-ten recurrence for all positive lengths. The ten initial counts coincide with \(-zD'(z)/D(z)\), yielding the exact formula. An independent direct enumerator checks indexed cyclic configurations through length 16. The leading term follows from root separation by a numerical interval and explicit exact coefficient inequalities. There is no finite-to-infinite extrapolation.

## Originality — PASS, with historical priority limits

The closest primary study is Jen (1989, §4, Case e), which gives the number of *preimages of any specified word*, not the number of *distinct cyclic images at every ring length*. Jen (1988) counts fixed points and periodic attractors, and Li (1987) studies attractor spectra rather than one-step image sets. A later online census records finite-ring orphan counts but does not present the proved logarithmic-derivative formula or its factorization. The known tools could in principle be combined to calculate the present invariant, but the statement is not an immediate corollary of a stated earlier formula: counting distinct accepted cyclic labels requires deduplication and an exact all-length count. Restricted full-text access to Jen (1988) and the possibility of older unpublished specialized tables are residual risks.

## Value — PASS

A full-ring one-step image count is a natural compression invariant of a canonical binary majority cellular automaton. The formula gives every length, a short recurrence, a ten-root trace representation and the exact image growth entropy, whereas a finite census gives isolated values. It distinguishes a one-step reachable-state invariant from the better-studied fixed-point and attractor invariants; it is not a known-parameter renaming or a trivial single-length increment.

## Limits

The statement covers one synchronous update only and fixed-radius majority on indexed binary cyclic rings. It does not give all preimage multiplicities or multistep images. Comparison of Jen (1988) relies on the accessible abstract, not a read complete article, and independent mathematical verification is outstanding.

Self-review: passed. Independent audit: not yet performed.
