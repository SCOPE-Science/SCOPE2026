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

# Verification performed

`python verify.py` ran on the included standalone Python 3 source and passed 2,485 exact finite assertions. It checks the uniform centered-digit variance, both periodic and antiperiodic Fourier trace formulas, the sharp length identity, exhaustive small-case positive digit tilings, absence of forbidden Korobov frequency annihilators, and signed-permutation counts. All arithmetic used by the checks is exact integer or rational arithmetic.

# Analytic verification boundaries

The full theorem for all integers \(d,t\ge1\) and arbitrary rectifiable closed curves is established by the analytic proof in `RESULT.md`, not by finite enumeration. The essential nonstandard steps—the equality case in the Fourier trace inequality, the constant-modulus finite Fourier polynomial lemma, and induction for the integer-digit tiling—are explicitly proved there. The periodic parity obstruction is strict and is not silently treated as an equality case.

The source comparison includes a full reading of Ehler's Section 2 and the publicly available abstract and citation discussion of Kunis; Kunis's full paper was inaccessible and was not represented as fully reviewed. No claim of independent validation or exhaustive scientific priority checking is made.
