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

# Reproducibility and scope

Execute `python checker.py` from the extracted package directory with Python 3, NumPy and SymPy available. The checker tests exact beta-binomial normalization, exact agreement of finite-age reset recursion with renewal coefficients, exact generating-function polynomial recurrence, and exact reversal at swapped parameters. It also constructs the full complex tridiagonal matrix separately to compare against the unit-circle coherence polynomial, numerically checks all roots for several strengths and degrees, and checks the balanced Legendre identity.

Actual execution of the packaged code: `PASS: 835 checks (exact rational recursions, determinant, roots, Legendre).`

The source of the all-degree proof is the strict positive definiteness of the real diagonal matrix in the imaginary part of the continuant, followed by polynomial-root continuity and reciprocity. Finite computation does not establish the universal quantifiers. The exterior-root statement is about all complex polynomial zeros, not a finite mesh of gate phases. No numerical root solver is used to prove the theorem.

The critical cases \(\gamma=0\) and \(\gamma=1\) serve only as limiting root-location arguments and are not included in the physical theorem. The proof does not claim uniform control as the degree grows and the strength approaches \(1/2\).
