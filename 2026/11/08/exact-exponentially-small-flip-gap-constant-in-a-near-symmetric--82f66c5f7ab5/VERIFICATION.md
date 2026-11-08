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

The finite check is replayable with `python3 verify.py` from a Python 3.11+ interpreter; it requires no third-party modules. It runs 132 exact rational identities and six parameter scenarios using 92-digit decimal arithmetic. The program explicitly solves the positive two-cycle equation and brackets the neutral multiplier crossing, then compares normalized rational-threshold margin, cycle endpoint, and crossing width with the new constants. A successful run ends in `VERIFY_OK rational_multiplier_identites=132 high_precision_parameters=6`.

This is not exhaustive verification over a continuum of parameters. The proof of the limiting theorem uses the exact cycle identity, the exact multiplier expansion, and the published near-symmetry existence/uniqueness and endpoint estimates stated in RESULT.md. The \(o(1)\) limit is not inferred from the six finite examples. There is no independent scientific audit.
