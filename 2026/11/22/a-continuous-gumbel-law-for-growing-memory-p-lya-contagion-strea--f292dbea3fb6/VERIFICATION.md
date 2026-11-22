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

The accompanying `checker.py` enumerates exact finite rational laws and validates the stationary block identity, run probabilities and normalization. Run `python3 checker.py`; a completed run prints 936 passing assertions. It checks \(M\in\{1,2,3,4\}\), \(\alpha,\beta\in\{1,2,3\}\), and sampled word lengths through \(M+4\). It does not establish the infinite extreme-value theorem.

The analytical verification consists of: (1) invariant beta-mixture memory blocks, (2) exact event probabilities, (3) uniform shared-uniform coupling with exponential forgetting on scale \(M^2\), (4) mixed factorial-moment cluster bounds under \(M^{\beta+3}\log n=o(n)\), and (5) a vanishing initial-boundary contribution and disappearing lattice width. Independence or external formal verification has not been asserted.
