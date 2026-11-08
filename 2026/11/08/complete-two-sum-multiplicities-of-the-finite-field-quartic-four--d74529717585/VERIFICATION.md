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

The proof is the pointwise reduction to \(z^2+6s^2z+s^4-8t=0\), the \(s=0\) fourth-power fiber count, the unique odd fiber at \(s\ne0\), and two collision identities that determine the multiplicity-two and multiplicity-four counts. This proof is valid for every finite field of characteristic greater than three.

Run `python CHECK.py` in a directory containing the file. It performs exact finite-field enumeration (not floating point), comparing every target multiplicity on 46 checked fields against all formulas. Successful output:

`CHECK_OK fields=46 prime_fields=42 extension_fields=4 exact_target_entries=519934`

Exhaustive finite-field tests establish only the stated finite cases. The general theorem requires the analytical character-sum argument in `RESULT.md`; it is not inferred from the test coverage. The previous published quartic energy is used only as a consistency check and credited. No independent mathematical audit has been performed.
