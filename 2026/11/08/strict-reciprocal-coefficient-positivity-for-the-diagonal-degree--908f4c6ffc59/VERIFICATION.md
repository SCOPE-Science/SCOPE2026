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

# Reproduction

Execute `python3 verify_pade77.py` using Python 3 and its standard library. The program's initial line is `VERIFY_OK q_7_7: 7 disjoint Rouche root discs; exact residues; n=0..31 positive; tail n>=32 positive`.

All comparisons controlling the proof use exact rational `Fraction` arithmetic. Decimal centers are treated as exact rationals. Root isolation is supplied by explicitly bounded Taylor remainders and Rouché's theorem, not a root-finding success flag. The program checks seven simple root disks, conservative modulus and residue bounds, the strict rational majorant at index 32, and 32 exact recurrence coefficients. The analytic proof in RESULT.md explains why those finite checks cover every index.

The computation does not prove positivity for any other Padé order; it is not a floating-point stability or accuracy certificate for a matrix-exponential implementation. Independent validation has not been performed.
