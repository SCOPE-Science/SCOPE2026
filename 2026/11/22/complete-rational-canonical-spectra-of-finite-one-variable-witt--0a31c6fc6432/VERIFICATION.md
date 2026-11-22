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

Run `python3 verify_witt.py` from the directory containing the script. The program requires only Python 3's standard library and writes the captured scientific data to `verify_full_output.json` in the same directory. Its records include exhaustive enumerations for finite fields of sizes 3, 9, and 5 in characteristics 3, 3, and 5, plus 900 seeded checks in characteristic 7. All reported tests passed. The output was compared byte-for-byte with the embedded captured JSON after replay.

The code checks the restricted-power identity, unit-coefficient cyclicity, nilpotent power-rank formulas, and the exhaustive exact coefficient counts. These finite tests are not proofs for arbitrary primes or field extensions: the symbolic argument in `RESULT.md` establishes all quantifiers. No external independent mathematical audit is represented by these artifacts.
