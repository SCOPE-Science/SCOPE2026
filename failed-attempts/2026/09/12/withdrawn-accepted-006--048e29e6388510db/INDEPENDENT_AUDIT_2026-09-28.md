# Independent Audit — 2026/09/12/006

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `df7c2565d4aa788e57ee97842ffd83272f4c7c18`  
**Audited current source tree:** `df7c2565d4aa788e57ee97842ffd83272f4c7c18`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** failed

The current `main` record tree matches the assigned tree SHA.

## Correctness

PASS. Independent enumeration gives exactly 81 fields and reproduces the claimed 13 ordinary 4-rank-one pairs and the four (Legendre symbol, unit norm, r4) counts. The arithmetic table is internally correct.

## Originality

FAIL AS A NEW RESEARCH RESULT. For two-prime real quadratic discriminants, Rédei–Reichardt theory reduces the narrow 4-rank to a 1x1 symbol computation, while ordinary class numbers and fundamental-unit norms are standard exact computations. PARI exposes qfbclassno/quadclassunit/quadunitnorm directly, and contemporary OEIS tables explicitly combine the same class-number, two-prime and unit-norm data. The bounded 81-row table is therefore a routine finite extraction of established invariants rather than a new structural result.

## Scientific value

FAIL UNDER THE RESEARCH-VALUE STANDARD. The bound pq<2500 is a small arbitrary window; the record does not prove a new theorem, asymptotic, classification principle, or unexpected phenomenon beyond refuting an unspecified “naive rule.” Explicit witnesses improve reproducibility but do not raise this standard computation to an independently valuable research finding.

## Independent checks

- independent enumeration of 81 admissible p,q pairs
- independent class-number/unit-norm cross-check of all 13 rank-one cases
- comparison with Rédei theory, PARI capabilities and public class-number/unit-norm tables
- current main tree equals assigned tree

## Limitations

- Failure is on originality/scientific value, not arithmetic correctness.
- No claim is made that every individual witness is already printed in a prior source; the issue is that the bounded census is mechanically generated from standard invariants.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/12/006
- https://doi.org/10.1007/s00222-006-0021-2
- https://pari.math.u-bordeaux.fr/dochtml/html/Basic_number_theory.html
- https://oeis.org/A391530
- https://arxiv.org/abs/1310.6607

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain unchanged.
