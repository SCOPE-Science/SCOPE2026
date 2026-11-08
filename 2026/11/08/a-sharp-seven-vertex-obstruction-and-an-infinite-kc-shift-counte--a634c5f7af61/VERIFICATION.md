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

# Verification

Run `python3 checker.py` using the Python standard library. It produces an exhaustive labeled-tree KC census for orders four, five and six through Prüfer words, using exact `fractions.Fraction` recurrences; it checks the seven-vertex witness by a second method that explicitly enumerates every ordering of its six edges. It also checks the eight-vertex analogue by enumerating all orderings of seven edges, and checks rational recurrences for arm lengths two through eleven.

The exact labeled comparison census is 24 negative at order four, 480 negative at order five, and 6180 negative plus 2160 equal at order six; no positive transformations occur. Direct witness values are \(26/9\) for the path on seven vertices and 3 for the three-arm spider. The proof for every arm length uses an analytic alternating-forcing inequality; no finite sample is offered as a substitute for that proof. The 1991 historical full text was not available for a complete priority comparison. Independent mathematical audit has not been performed.
