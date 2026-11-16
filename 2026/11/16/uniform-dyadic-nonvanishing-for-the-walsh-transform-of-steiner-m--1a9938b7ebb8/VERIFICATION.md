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

The claimed infinite congruence is proved by the exact exact incidence expansion in RESULT.md; finite enumeration is corroborative only. Run `python verify.py` from the directory containing the supplied files with Python 3, using only the standard library.

Checks actually performed: five labelled Steiner triple systems were generated and all pair-incidence conditions verified. Their complements were independently enumerated, transformed by an exact-integer fast Walsh algorithm and compared coefficient-by-coefficient with the separate incidence expansion. The exact Parseval equality was checked in every case. The \(v=7,13,15\) examples passed the \(4\pmod8\) test at all frequencies; the affine \(v=9\) example exhibited a genuine Walsh zero. Two different \(v=15\) systems had different nonzero-value histograms but both had full Walsh support.

The program outputs `STS_COMPLEMENT_WALSH_MOD8_PASS` on success. Executed output is preserved in `verification_output.txt`.

Limits: no computation over every Steiner triple system at larger orders is attempted or claimed. The proof is uniform because it uses only universal pair-incidence parameters. No independent audit has been performed.
