# Scientific review

## Correctness — PASS

For any fixed component size, the Cayley injection count is \(\frac{k^{k-2}}{k!}n d_n^{k-1}(1+o(1))\); the exact per-tree isolation probability is \(p_n^{k-1}q_n^{k d_n-2(k-1)-h}\). These imply the Poisson mean. Distinct tree-component events cannot share vertices, and joint probabilities for disjoint sets differ from products by at most \(q_n^{-O_{k,r}(1)}=1+o(1)\), proving every fixed factorial moment. An internal extra-edge union bound makes cyclic fixed-size components negligible. The case of isolated vertices and the concentration assertion at \(k=2\) have independent exact moment proofs. The source code checks 96 finite cases/numeric expressions, but no infinite claim rests solely on computation.

## Originality — PASS, with residual historical risk

The initiating 2026 cycle-power manuscript proves the isolated-vertex Poisson law at connectivity (\(k=1\)); it does not state the off-connectivity fixed-\(k\) windows. Penrose's 2015 Theorem 2.2 is an important **broader-looking** fixed-order Poisson result for random point-process connection graphs: its hypotheses do not directly encompass an arbitrary preassigned regular host. Diskin–Krivelevich treat a different (near-critical) regime with expansion assumptions. Searches using fixed-size component synonyms and comparison against earlier accessible research records did not identify the exact universal extinction law for deterministic regular hosts, although absence in a search is not proof of uniqueness. A future independent literature review may find an implicit reduction or earlier special cases.

## Mathematical value — PASS

The theorem determines an entire hierarchy of natural component-disappearance windows, the sharp logarithmic-logarithmic correction, and a geometry-independent nontrivial mean \(1/(k\,k!)\). It extends a recent geometric connectivity phenomenon to disconnected and arbitrarily structured regular hosts and quantifies how size-two components disappear while isolated vertices remain abundant. Such fixed-component obstructions are natural to connectivity and percolation studies and this is not an arbitrary finite invariant.

## Closest literature and limitations

See the full citations and precise model distinctions in `RESULT.md`. The boundary \(d_n\asymp\log n\), growing component size, nonregular hosts and complete component geometry are outside the theorem. Historical-priority confirmation is not an independent assessment.

Self-review: passed. Independent audit: not yet performed.
