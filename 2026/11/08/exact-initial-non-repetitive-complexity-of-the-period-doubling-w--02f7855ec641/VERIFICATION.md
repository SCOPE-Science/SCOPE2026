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

# Reproducibility

Run `python3 verify.py` in the same directory. No third-party Python packages, external input files, external theorem provers or network access are needed. The expected final line is `VERIFY_OK: 512 direct factor lengths, 320 large-parameter algebra checks`.

The program produces the binary period-doubling fixed-point prefix by literal substitution, verifies the parity identities and no-`11`/no-`0000` forbidden patterns in the generated prefix, and finds the first repeated factor using exact byte-slice comparison for every length from 1 through 512. It independently computes the closed-form and recurrence predictions, compares all three values, then checks the two algebraic expressions at 320 additional large integer inputs.

## Limits of the checks
The computation is finite and is **not** a proof of the infinite recurrence. The standalone argument in RESULT.md proves, for every length at least four, that equal factors have equal starting parity and reduce exactly to shorter factors under the substitution; it then uses the inspected length-1, -2, -3 bases. The checker only tests sample consequences and correct implementations of definitions. It does not verify external historical originality, independent review, or any claim about arbitrary starting positions.
