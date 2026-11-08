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

Execute `python3 verify_projection.py` with Python 3 and no third-party dependencies. The script uses exact `fractions.Fraction` arithmetic to check the interpolation constraints, the five row sums, the complete coefficientwise dual identity, the inequality between the new norm and the previously exhibited one, and several direct-sum projection matrices. The proof of the universal quantifier over all dimensions is symbolic, in `RESULT.md`; checking finitely many dimensions is not substituted for that proof.

The project does not claim independent audit, publication priority, a result on complex scalar fields, or an optimized Banach–Mazur distance. The only accepted mathematical claim is the explicitly stated projection-constant theorem.
