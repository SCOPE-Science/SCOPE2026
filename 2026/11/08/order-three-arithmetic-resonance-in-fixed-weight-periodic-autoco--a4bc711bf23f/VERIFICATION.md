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

Run `python verify.py` in the same directory as this file using the Python standard library. The actual run passed 827 exact rational comparisons across 274 exhaustively enumerated configurations for all \(6\le N\le12\) and allowed \(k,d\), including an independent raw-moment triple-edge census and balanced-sign checks at \(N=6,12,18\). The code reconstructs exact expectations from the finite sample space; it does not claim to enumerate arbitrarily large \(N\). The mathematical proof independently establishes the all-parameter claim by finite-population sampling probabilities and a complete enumeration of edge-triple union types.

The independent audit status is not performed. This result does not certify historical uniqueness, complete autocorrelation laws or applicability to antipodal distances.
