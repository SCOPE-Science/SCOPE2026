# Scientific review

## Correctness — PASS
The record-weighted rank encoding is a bijection, and the product of its independent rank weights is exactly the normalized record-weighted permutation law. The peak-event equivalence uses only the three consecutive ranks; conditional enumeration separates the record case from the nonrecord cases and yields a rational expression whose difference from \(1/3\) factors as \(-\theta(\theta-1)(\theta-2)\) times a positive denominator. The finite expectation telescopes exactly. All boundary conditions \(n\ge3\), \(\theta>0\), and \(2\le i\le n-1\) are explicit. Independently, `verify.py` replayed 270 assertions in exact fractions through permutation order 8. The proof, rather than the finite checks, covers all sizes.

## Originality — PASS (qualified)
Bouvel–Nicaud–Pivoteau, arXiv:2409.01692v1, give the biased law, sampling construction, and expected descent statistics. The relevant complete preprint passages on local ranks and descents were inspected, together with an internal document-text search for peaks; they do not state the two-threshold local peak formula. Billey–Burdzy–Sagan, arXiv:1209.0693, treat uniform peak-set enumeration. Gessel–Zhuang, arXiv:2001.00654, treat peaks with cycle type and are not directly about record weighting. Three targeted published-finding corpus similarity searches for record-biased peaks, two-threshold invariance, and record-weighted peak distributions found no comparable established claim; they are not a novelty proof. Residual risk: a different paper or unrecognized transform may implicitly contain the formula. No claim of independent historical-priority certification is made.

## Value — PASS
The source model has an asymmetric record-dependent law with genuinely biased adjacent descent rates. Nevertheless, the interior local-peak probability exactly reproduces its uniform value at a second, nonuniform bias, \(\theta=2\), and its deviation changes sign twice. This is a natural, uniform-in-position probability classification for a widely studied nonuniform permutation law; it clarifies that local maxima and local descents react differently to record-biasing. The result is a complete finite-size, all-parameter statement, not a single numerical instance. It does not imply a whole peak-set identity.

## Limits and closest literature
The model/rank construction originates in arXiv:2409.01692. Potential implicit formulas in wider peak-enumerator literature remain a historical-priority uncertainty. The result does not address full peak-set laws, covariances, limit distributions, or independent validation.

Self-review: passed. Independent audit: not yet performed.
