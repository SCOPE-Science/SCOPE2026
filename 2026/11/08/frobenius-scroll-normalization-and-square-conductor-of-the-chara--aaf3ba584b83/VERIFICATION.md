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

# Reproducibility and checks

Run `python3 verify_schur.py` from the directory containing the embedded script. It requires only Python's standard library. The included `verification_output.txt` is the recorded successful output from this exact script.

The script independently enumerates all projective points over \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\), as well as all projective lines over the first two fields. It tests the exact defining quartic on every enumerated point or line; the line test is coefficientwise in the two line parameters, not merely pointwise. The script checks the algebraic monomial pattern underlying the conductor and the stable Hilbert polynomial. Its output concludes `CHECK_OK`.

The normalization, conductor equality, completeness over algebraically closed fields, and zeta formula for all extensions are established by the symbolic proof in RESULT.md; finite enumeration alone is not used to infer those statements. The documented proof leaves open the nonreduced structure of the line Hilbert scheme and historical priority against uninspected specialist sources.
