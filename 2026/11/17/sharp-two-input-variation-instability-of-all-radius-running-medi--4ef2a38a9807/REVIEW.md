# Scientific assessment

## Correctness — PASS
The median of affine signals is piecewise affine. Every active selection reads an index within radius \(r\), so a unit-jump perturbation changes at most \(2r+1\) output edges; integration and the discrete jump decomposition yield the bound for every pair. An explicit alternating-rank baseline makes all \(2r+1\) output edges change under a single input jump, and the extension argument preserves the witness at all greater lengths. Exact checker tests corroborate the rank calculations.

## Originality — PASS (provisional)
The classic one-input smoothing property of Restrepo–Chacón does not imply a sharp two-input modulus. Previously recorded radius-one and cyclic statements do not imply the all-radius clamped path coefficient or the optimal path-length threshold. Full archival coverage is incomplete; some older median-filter articles were accessible only through abstracts, so duplicate historical priority remains a specific risk.

## Mathematical value — PASS
The theorem determines the complete sharp high-length law for every odd window width, together with a sharp minimal input size and an explicit adversarial rank construction. It identifies a quantitatively maximal instability under perturbations in an operator used for variation smoothing. This is an all-radius structural statement rather than a single arbitrary finite calculation.

## Scope and limitations
Noncyclic unweighted path variation, clamped endpoints, real inputs. The exact coefficients below the stated minimal length and modified boundary conventions are not determined.

Self-review: passed. Independent audit: not yet performed.
