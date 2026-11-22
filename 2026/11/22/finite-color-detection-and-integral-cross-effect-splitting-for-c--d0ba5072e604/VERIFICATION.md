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
# Verification record

Run `python3 check/verify.py` with a standard Python 3 installation. Its output is preserved verbatim in `check/verify_output.txt`. The file checks color-merger face preservation and signed chain-map identities, the integral orthogonal-projection identity on sampled chains, the explicit cone boundary identity, and mod-two Betti-number samples. Exact sample scope and limitations are disclosed in `RESULT.md`. All mathematical assertions for arbitrary \(G\), \(n\) and \(d\) rely on the symbolic chain proof and its explicit cone lemma, not finite enumeration.

No external independent audit or independent validation is claimed.
