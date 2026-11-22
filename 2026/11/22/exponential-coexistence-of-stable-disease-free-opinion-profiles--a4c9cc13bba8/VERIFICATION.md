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

The self-contained `CHECK.py` runs with the Python standard library, with exact `fractions.Fraction` arithmetic and finite sign enumeration. The checker was executed successfully with all equilibrium residuals and sign-pattern counts for \(1\le m\le10\), the five equilibrium profiles for \(m=3,w=2\), and algebraic epidemic bounds. The infinite-family proof rests separately on explicit linear-system elimination, elementary inequalities, symmetric positive definiteness and Metzler comparison.

The checked infection parameters preserve positive second-order transmission and explicit opinion feedback. For arbitrary admissible starting states, the comparison matrix has spectral abscissa strictly below zero. Every enumerated equilibrium is separated from each opinion-sign switching surface. Nothing here certifies global opinion convergence across switching surfaces, independent replication or external validation.
