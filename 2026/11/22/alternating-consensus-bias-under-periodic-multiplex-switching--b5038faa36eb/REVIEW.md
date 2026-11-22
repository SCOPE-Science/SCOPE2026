# Scientific review

## Correctness — PASS

The complete-graph transition matrix has exactly two eigenspaces, giving the exact identity \(A^k=U+r_k(I-U)\). This leads to the stationary resolvent \(\pi_k=(1-r_k)u(I-r_kB)^{-1}\) and the exact error series. The \(\ell^1\)-contraction bound certifies eventual sign alternation, and uniqueness of the invariant distribution of a connected undirected network identifies irregular degrees as the precise condition for a nonzero bias. The symmetric three-vertex example has an exact rational formula for every block length, with verified strict parity inequalities. Independent rational arithmetic checks pass for the first 31 lengths. The statement is limited to the declared hypotheses, not arbitrary networks or time-varying opinions.

## Originality — PASS (bounded literature comparison)

The originating Shiu–Naghizadeh study (2026, arXiv:2603.07633) already includes this example at \(k=1\) (its Example IV.2), a general sufficient primitive-block criterion, and \(O(\rho_2(A)^k)\) convergence in Proposition IV.4. Those statements neither give the exact formula for every block length nor distinguish odd and even block lengths for arbitrarily large \(k\). The contribution is the across-period parity theorem for nonregular second-layer graphs, its explicit finite onset condition and the all-\(k\) identity, not the familiar stationary-vector formula, the \(k=1\) overshoot or classical Markov perturbation. The 2014 multiplex consensus article addresses convergence of a different coupled transition scheme and does not establish the described alternating-block sign theorem from inspected material. Residual risk: obscure general periodic-Markov-chain results might contain an equivalent signed first-order expansion, and 2014 full text access was limited.

## Value — PASS

The result exposes a concrete social-model blind spot in convergence-rate estimates: two switching schedules that differ only by one complete-network update can shift the ultimate consensus to opposite sides of the same baseline, for arbitrarily long periods. This is not a transient periodic orbit but a reproducible change in the limit. The all-graph statement and finite exact example make the effect testable and identify precisely when a layer heterogeneity is necessary. No practical claim about measured human behavior is made.

## Scientific boundaries

The universal parity theorem concerns sufficiently large deterministic block lengths and the complete-first-layer family; the all-block overshoot relative to both single-layer values is limited to the specified three-person graph. The results do not classify general multiplex networks or stochastic schedules. Full historical priority has not been independently established.

Self-review: passed. Independent audit: not yet performed.
