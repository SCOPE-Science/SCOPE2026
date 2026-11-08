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

# Reproducible verification

`verify_prime_fields.py` independently enumerates every ordered pair over \(\mathbb F_3\) and \(\mathbb F_5\) by explicit 2x2 matrix multiplication and compares all target fiber counts with the theorem. Recorded results in `prime_output.txt`: 6561 and 390625 total pairs, respectively, zero-fiber counts 417 and 4705, and seven distinct fiber values in each case.

`verify_extension.py` separately constructs \(\mathbb F_9=\mathbb F_3[a]/(a^2+1)\), builds the four-dimensional Sylvester map from its action on elementary matrices, and uses exact finite-field Gaussian elimination to count preimages of 22 specified or reproducibly sampled targets, considering all 6561 possible first factors per target. Recorded output in `extension_output.txt` confirms equality for all selected targets.

Run `python verify_prime_fields.py` and `python verify_extension.py` from the directory holding these files. They require only Python 3. Exact displayed results are in the two companion text files. These experiments corroborate but do not prove the general statement; the unrestricted argument is in RESULT.md.
