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
# Verification evidence

The exact standalone verifier is `checker.py`. Execute `python3 checker.py` using Python 3, with no external packages. The observed output ends with `VERIFY_OK k=1..7, mixed_lift_k=2..4; proofs extend to all exponents`.

For each exponent from one to seven, the checker constructs all residues of the curve and all allowed pairs, then iterates exact sumset addition for one to five summands. It checks the explicit four-term exclusion for exponents at least three and equality at the claimed sharp order. For exponents two through four it enumerates all five-tuples to find mixed-parity representatives and checks that independently turning each top bit changes the appropriate moment and leaves the other unchanged.

This provides finite computational evidence only. The general result is proved by the parity-preserving lift, induction and the modulus-eight obstruction in RESULT.md. Neither the code nor this report constitutes independent mathematical certification.
