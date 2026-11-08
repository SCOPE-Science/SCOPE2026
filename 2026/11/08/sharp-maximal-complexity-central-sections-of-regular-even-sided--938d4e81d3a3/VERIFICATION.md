---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification notes

The analytical proof in `RESULT.md` establishes the claim for all even \(n\ge4\). The additional executable `check_even_prism.py` uses direct sign tests on all prism edges, without the order-statistic event formula, to classify sections. It also numerically integrates the unsimplified Haar integral for comparison with the arcsine formula.

Command: `python3 check_even_prism.py` (requires NumPy and SciPy).

Actual completed checks: 190,000 independently generated unit normals were reused for 15 prism configurations (even orders 4, 6, 8, 12, 20 and three heights per order), comprising 2,850,000 direct section classifications. The code checked the even vertex counts, the sharp \(n+2\) bound, the maximum probability against observed frequencies within 0.005 absolute tolerance, the unsimplified azimuth integral to absolute error below \(3\times10^{-13}\), the cube probability identity, and the exact optimal height for the hexagonal prism. Output terminated with `EVEN_PRISM_MAXIMAL_SECTIONS_OK samples= 2850000`.

Selected computed maxima (circumradius-one half-heights): \(n=4\), \(h=0.7071067812\), probability 0.3509593122; \(n=6\), \(h=1.1180339887\), probability 0.1226017195; \(n=8\), \(h=1.2492638519\), probability 0.0643609961; \(n=12\), \(h=1.3412822617\), probability 0.0273202284; \(n=20\), \(h=1.3880146881\), probability 0.0096158100.

Limits: numerical tests are finite, share one sample of random directions across configurations, and do not prove the universal theorem, uniqueness, or novelty. The general proof and stated historical-access risk must be assessed separately. No independent review has been performed.
