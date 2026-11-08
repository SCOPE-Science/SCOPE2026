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

# Reproduction and verification

With Python 3.9 or later, run `python3 check.py` from the directory containing these extracted files. No third-party dependencies are required. Exact rational arithmetic checks offspring normalization and equal mean, the cubic difference identity, the threshold at \(c=1/4\), and extinction differences at generations one, two and three. A finite sweep additionally tests small rational offspring-law comparisons for unexpected multiple reversals; it is a consistency test, not an infinite mathematical proof.

The universal theorem follows from: (1) the factorization forced by equal mean and normalization; (2) the one-interior-crossing, order-preservation argument; (3) the sign of the generating function at the crossing compared with its nontrivial fixed point; and (4) the exact cubic example proving sharpness. Inspect `RESULT.md` for definitions, quantifiers, hypotheses, endpoint cases and the complete proof.

The independently unreviewed status is deliberately unchanged. Historical priority is provisional, as explained in `REVIEW.md`.
