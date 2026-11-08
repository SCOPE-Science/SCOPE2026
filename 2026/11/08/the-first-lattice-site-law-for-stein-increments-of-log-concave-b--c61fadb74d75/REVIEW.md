# Mathematical review: first-lattice-site Stein factor law

## Correctness — PASS

The theorem specifies a positive, full-support, log-concave mass function and the constant-birth Stein operator with its death rates fixed by detailed balance. The centered-sum solution follows by telescoping. The coefficient decomposition for the first difference has exactly one positive coefficient: both negative branches follow by summing the ordered successive-mass ratios. The index-dependent envelope is thus attained by a singleton. Subtracting this envelope from \((1-p_0)/w\) yields an exact sum of nonnegative terms. The first index has zero gap, and strict positivity classifies the other maximizers; the Bessel specialization uses its exact mass and ratio formulas. No finite experiment is used as proof for the infinite assertion. The extracted rational checker passed 21,970 assertions on finite diagnostic examples.

## Originality — PASS, with historical-priority limitations

The general pointwise Brown–Xia increment framework and DeSalvo's explicit Bessel envelope are prior knowledge. DeSalvo's 2026 Open Problems 8.1 and 8.2 request sharp first-difference constants, while Theorem 2.5(a) supplies only a maximization expression and looser closed bounds. Eichelsbacher's 2026 full text recovers earlier pointwise increment formulas but does not state this constant-birth, all-log-concave global optimizer and gap identity. The candidate is a **global optimization of a known envelope**, not a newly invented Stein operator, and its proof is short. The main residual risk is that Brown–Xia (2001) or another classical source may already identify the same global optimizer; that original paper's full text was not available for direct comparison. An earlier exact implicit characterization reduces the novelty margin; the optimized result should not be described as conceptually independent of the established framework.

## Value — PASS

The exact \((1-p_0)/w\) factor resolves a concrete, recently restated sharp-constant problem for the discrete Bessel target and improves the closed \(3/w\) bound to the exact finite-parameter answer. The nonnegative gap formula determines all maximizing lattice indices, not merely an upper bound. The result applies to a naturally defined full class of log-concave constant-birth targets, including non-polynomial death rates; this makes it a reusable structural extremal identity, not an arbitrary numerical slice.

## Literature and limitations

Primary material compared: Stephen DeSalvo, arXiv:2611.00263v1, Sections 2, 8, 9 and 10.1; Peter Eichelsbacher, arXiv:2609.25380, especially Proposition 2.1 and its Brown–Xia comparison. Brown–Xia (2001) is a close earlier framework cited by both, but its original full text was not inspected. The proof does not address zeroth-order Stein factors, non-log-concave targets, or other operator normalizations. This is a self-review only; no independent audit or validation was performed.

Self-review: passed. Independent audit: not yet performed.
