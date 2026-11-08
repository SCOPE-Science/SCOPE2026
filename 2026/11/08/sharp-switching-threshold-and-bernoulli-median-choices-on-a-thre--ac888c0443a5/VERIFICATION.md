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

# Reproducibility notes

Run `python verify.py` with Python 3 standard libraries; no external dependencies. The verifier constructs the original discrete-neighbor median choice directly from the opinions and compares it to an independently written exact-rational normalized recurrence. Expected output:

`VERIFY_OK 7776 rational recurrence identities; 1022 exact cylinder lengths; 372 low-step switching trajectories; 20 alternating-witness steps`

All calculations use `fractions.Fraction`; no numerical tolerances are used. The length-k cylinders are recursively pulled back on the affine branches and verified to have length \(6/2^k\) for all tested \(1\le k\le9\), rather than inferred from numerical histograms. The finite checks do not establish all time horizons: the complete proof of eventual switching behavior, consensus, and all-cylinder Bernoulli probabilities is in `RESULT.md`. The tie at exactly equal neighbor distance is resolved toward the lower leaf in every verifier case.

The theorem concerns the **original 2024 neighbor-valued median rule** in arXiv:2406.17552v1. The revised 2025 v3 model has an enlarged median candidate set and cannot serve as a direct computational oracle for this original-rule result. There has been no independent external audit.
