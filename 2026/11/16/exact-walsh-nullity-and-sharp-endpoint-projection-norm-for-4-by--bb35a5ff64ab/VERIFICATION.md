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

# Reproducibility and boundaries

`check_asm4.py` performs a complete exact enumeration from the ASM definition, direct reduced character sums, independent Walsh butterfly transforms, an exact projector-kernel transform, and direct checks at every frequency of the ambient binary matrix cube. The provided CSVs list all \(42\) support masks and all \(512\) reduced Fourier and projection-kernel numerators.

Run: `python3 check_asm4.py`. Expected marker: `ASM4_WALSH_PROJECTION_EXACT_PASS asms=42 quotient=512 zeros=120 rank=50176 lambda=199/32 ambient_checks=65536`.

The sum of squared reduced Walsh coefficients is \(21{,}504\), matching Parseval. The sum of absolute reduced projector-kernel numerators is \(3184\), giving the sharp \(199/32\) norm. Full ambient coefficients have the predicted \(128\)-fold absolute multiplicities. These checks are exact integer operations, not floating-point approximations. No checks for higher orders and no independent human validation are claimed.
