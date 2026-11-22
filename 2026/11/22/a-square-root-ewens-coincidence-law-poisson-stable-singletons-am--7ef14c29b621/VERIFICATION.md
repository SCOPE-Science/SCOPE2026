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

The standalone `verify.py` uses only the Python standard library and `Fraction` arithmetic. Executed as `python3 verify.py`; it passed 45 exact identity assertions across 15 exhaustively enumerated paired-partition laws (all set partitions on 2–6 labels, at concentrations 1/2, 1 and 3). The checked identities are the exact mean and second factorial moment of common singleton counts and the expected pairwise co-membership. These finite checks are not an asymptotic certificate.

The infinite proof rests separately on the Ewens specified-block probability, fixed-order factorial moments, the method of moments, exchangeability of labels, and a conditional union bound using the expected Ewens block count. The probability of an identical non-singleton block is controlled as \(O_c(\log n/\sqrt n)\). The limit assumes \(\theta_n/\sqrt n\to c\in(0,\infty)\), and the point-process convergence is weak, not total variation on spatial coordinates.
