# Scientific review: triangular record–excedance covariance

## Correctness — PASS

The theorem has a complete finite-sample proof. Independence for \(j>i\) follows by conditional relative-order symmetry. The diagonal follows from the unique initial set \(\{1,\ldots,i\}\), and the negative lower triangle follows from a conditional sample and a hockey-stick binomial identity. Exact summations establish the row and column results and monotonicity proves the one-time aggregate sign change. The complete, extracted `verify.py` passes 640 exact finite comparisons. Finite enumeration corroborates, rather than substitutes for, the all-size proof.

## Originality — PASS, qualified

The checked indexed results contained no record-versus-excedance position matrix; the most related indexed entries concern record versus fixed-point indicators and record versus inverse-record indicators, which use different events and do not imply the present value-threshold formula. The strongest external prior art is Sokal and Zeng (2020), whose Theorem 2.1 gives a joint generating function for **aggregate** record and excedance counts. Hence the present aggregate covariance is already implied by that work and is only a consequence of the genuinely indexed result. Their count-marking polynomial does not supply separate variables for \((i,j)\), so it does not by itself yield the pointwise matrix or both positional sign profiles. Ehrenborg–Steingrímsson (2000), Brändén–Claesson (2011), Gnedin–Gorin (2012), and Jin (2022) supply substantial nearby results, but their inspected statements do not explicitly establish the indexed formula. Historical implicit positional coverage remains a genuine risk; novelty is a best-knowledge assessment, not a certification of uniqueness.

## Value — PASS

This is a complete natural classification of dependence between two classical permutation statistics, resolving every pair of absolute positions. It distinguishes the loss of earlier exceedances after a later record from the independence of future exceedances, yields opposite signs for record-conditioned and excedance-conditioned aggregate responses at the boundary, and explains the nonobvious aggregate sign transition at size five. These are structural finite-sample facts not captured by an unindexed marginal distribution.

## Source coverage and limitations

Closest assessed literature: Sokal–Zeng, arXiv:2003.08192, Theorem 2.1 and Section 2.3; Brändén–Claesson, arXiv:1102.4226, Sections 1–2; Ehrenborg–Steingrímsson, *Advances in Applied Mathematics* 24 (2000), Sections 1–3; Gnedin–Gorin, arXiv:1202.3680, Sections 1–3; Jin, arXiv:2210.08789, introductory theorems. The aggregate joint distribution is acknowledged as prior coverage. Some historical refinements may already encode the indexed result in a less obvious form. The proof addresses uniform permutations only; no nonuniform or infinite-dimensional extension is asserted.

Self-review: passed. Independent audit: not yet performed.
