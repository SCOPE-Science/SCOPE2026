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

# Reproducibility and limits

Run `python3 artifacts/verify.py` from the extracted package root. The checker uses only the Python standard library and builds the labelled tree edges directly. For each \(m=1,\ldots,7\), it enumerates all \(2^{2m}\) edge orientations, counts vertices with outdegree zero and compares the full histogram to the binomial coefficient formula. It then checks the integer coefficient identity, total number of orientations and exact rational signs through \(m=40\).

Observed output:

```text
INDEPENDENT_EDGE_ORIENTATION_ENUMERATION_PASS m=1..7 orientations= 21844
EXACT_COEFFICIENT_AND_RATIONAL_SIGN_CHECK_PASS m=1..40
VERIFY_OK
```

The unrestricted parity classification is established by strictly monotone equations in the proof, not by extrapolation. The asymptotic escape and bounded-root limits are consequences of the displayed inequalities. This package records the scientific checks and their bounds; it does not represent an independent mathematical audit.
