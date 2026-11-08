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

The self-contained `verify.py` performs exact arithmetic with explicit irreducible binary polynomial encodings of \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\). It enumerates every invertible upper triangular matrix in its tested sizes, then all field-coordinate vectors; it checks the equations \(x^2=x\) directly and counts nonzero idempotents. The observed exact frequency distribution is compared to the independently stated recurrence, and all first and second moments are checked against the symbolic formulas.

Run `python3 verify.py` with a standard Python 3 interpreter; expected output is embedded in `verification_output.txt`. Tested configurations are \(q=2,1\le n\le6\), \(q=4,1\le n\le3\), and \(q=8,1\le n\le2\): 11 cases, 36,033 matrices. No randomness and no external libraries are required. The all-\(n\), all-\(s\) result is supported by the proof; finite tests are not a substitute for that proof.
