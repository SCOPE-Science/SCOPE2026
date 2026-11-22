# Scientific review

## Correctness — PASS
The expected squared error is exactly the largest eigenvalue of an explicit positive-semidefinite two-by-two matrix. Exact calculation groups all six orders into three symmetry classes; an equal-trace determinant comparison rules out the central-last class, and a common-eigenvalue resultant gives the quintic for the only possible optimal-order crossing. The positive-root count follows from a one-sign-change transformed polynomial, with an exact isolating bracket and upper-eigenvalue checks. The analytic proof covers every delivery probability including endpoints. Separately coded finite mask enumeration and symbolic identities in `verify.py` reproduce all required formulas. Risk: only this model and one complete attempted sweep are covered.

## Originality — PASS, provisional priority
Full text of the 2022 papers of Keinert–Weber and Dax was inspected. Neither uses the independent per-attempt erasure model with a fixed three-row order and exact worst-case one-sweep mean-square optimization. Relevant public comparison records on equiangular tight-frame reshuffling and three-row greedy Kaczmarz–Motzkin were read to the specific theorem/proof statements; neither objective or sampling mechanism implies the present quintic crossover. Direct semantic published-finding corpus queries for delivery loss, erasures, row permutations, planar frames and minimax contraction returned close but different results. Risk: general older results about products of random projections could subsume this small-instance classification, so historical priority remains provisional.

## Value — PASS
Fixed equal-budget update ordering under unreliable communication is a genuine algorithmic design decision; the result gives an exact reliability threshold on a natural minimal redundant (three rows in two dimensions) consistent system with small integer row directions. A preferred order changes even though row probabilities, costs and projection strength do not, establishing a substantive counterexample to using the best perfect-delivery schedule under erasures. It does not claim broad-dimensional performance or an algorithm-sized contribution.

Self-review: passed. Independent audit: not yet performed.
