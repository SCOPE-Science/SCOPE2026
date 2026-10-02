# Review status

Independent audit completed on 2026-10-01 UTC.

Disposition: **failed**.

## Correctness — PASS

Given the interleaved-track decomposition, each nondegenerate map is affine-equivalent to a Cartesian power of ordinary odd chi. Every divisor \(\ell>1\) of the odd part \(n_0\) is realized, and the known inverse degree \((\ell+1)/2\) separates distinct block lengths under affine equivalence. Walsh transforms factor multiplicatively over Cartesian products; choosing one nonzero output-mask block and zero masks elsewhere gives equality in the maximum, yielding the exact normalized correlation identity. The committed exhaustive checks corroborate the formulas for tested small parameters but are not used as an infinite proof.

## Originality — FAIL

The revised source already supplies the direct-product track decomposition and canonical-family equivalence. The earlier 2026-09-18 SCOPE record then explicitly transfers the known ordinary-chi inverse degree to the same blocks. From those prior facts, the divisor-indexed class count follows immediately by listing possible \(\ell\) and separating them by inverse degree. The Walsh identity is the standard tensor-product factorization of a vectorial Boolean transform. These are mechanically implied corollaries of prior structure, so implication-based originality fails even though the exact count and normalized-correlation sentence are not stated verbatim in the source.

## Value — FAIL

An exact affine-class count is normally a natural classification invariant, but here its value is obtained by a one-line divisor enumeration once the prior block decomposition and inverse degree are known. The Walsh scaling is generic Cartesian-product algebra. Under the required bar excluding mechanically implied narrow invariants and routine deductions, the surviving claim does not independently qualify.

## Sources and residual risk

Assigned package, verifier source and saved output inspected from the frozen Git tree.; Full published 2026-09-18 SCOPE generalized-chi RESULT.md inspected.; arXiv:2609.19548 abstract/revision metadata inspected; full v2 text unavailable through lawful routes.

Residual risk: Primary v2 full text was inaccessible, but this does not rescue originality because the needed decomposition and inverse-degree implication are already established in the published record inspected..

The dated independent-audit files contain the structured claim-versus-prior comparison and full evidence record.
