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

The proof in `RESULT.md` is analytic and holds for every integer \(n\ge3\), every \(0<\rho<1\), and every integer \(k\ge0\) in the fixed-data identity. Independently, `verify.py` constructs the actual rectangular Gram inverse block projectors and exact-rational volume weights using SymPy. Its finite test grid includes dimensions 3 through 6, five rational parameterizations of the correlation and exact multi-step propagation; 646 exact identities passed. Run `python verify.py` with Python 3 and SymPy. This is a finite algebra check, not exhaustive testing over real parameters or infinity, and does not constitute independent validation. No external computational or audit certificate is asserted.
