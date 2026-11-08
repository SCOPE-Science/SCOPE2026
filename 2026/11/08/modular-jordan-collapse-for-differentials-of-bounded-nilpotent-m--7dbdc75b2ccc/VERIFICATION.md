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

# Reproducibility and limitations

Run from the directory containing the attached artifacts:

```sh
python3 check_jets.py
python3 check_jordan_differential.py
```

Each program requires only Python 3 standard-library functionality. Its recorded stdout is in `jets_output.txt` or `jordan_output.txt`, respectively. The first program enumerates small nilpotent residue matrices, forms direct dual-number products, and compares lift counts and derivative ranks. The second independently constructs differential operators as literal matrix maps, composes them, and compares first-, second-, and third-power ranks and complete Jordan block multiplicities with the formulas.

The checks are exact finite-field computations, including the characteristic-dividing-exponent boundary. They are not exhaustive for arbitrary matrix size or characteristic and cannot substitute for the proof. The assessed claim is the positive-characteristic uniform Jordan-signature theorem in `RESULT.md`; no external independent validation is asserted.
