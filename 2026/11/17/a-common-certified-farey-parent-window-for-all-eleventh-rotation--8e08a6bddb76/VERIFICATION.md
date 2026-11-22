---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Read RESULT.md in full at the frozen commit and the complete 4271-byte verify_eos.py, including exact S=10^55 interval operations, positivity/root brackets, mean-value propagation, pairwise phase separation, derivative products and 2-critical-point capture tests. The Taylor enclosure of exp(z/2^h) through degree 55 and remainder <10^-55, with outward rounding, supports finite strict inclusions. Independent 70-digit mpmath evaluations from the five rational seeds give least-period closure errors <5e-26, positive counts 1,1,2,3,4, return multipliers 0.0605941,0.0642574,0.0642620,0.0606024,0.0606005, and critical center 0.05279705509222091216546506637678692694 inside the 1e-35 bracket. Numerical recheck corroborates but does NOT independently reproduce the claimed exact interval certificate. Contraction gives each hyperbolic cycle; negative Schwarzian for a>4, its critical-basin theorem and repelling interval endpoints rule out further attracting/neutral cycles after both critical orbits are captured. Reflection covers k=6..10; finite strict inequalities and continuity give a common epsilon>0. It does not prove global convergence or exclude repelling/chaotic invariant sets.

## originality

PASS

Best-of-knowledge novel rigorous rational-parameter, ten-numerator simultaneous window, not the already known numerical Farey phenomenon or map. Explicit scientific comparison and risks follow.

## value

PASS

The 2024 numerical simultaneous Farey-parent window is a specific unsettled dynamics observation. Turning ten observed cycles into certified exact inequalities, unique sink basins, exact least periods and a robust common parameter neighborhood closes a meaningful rigorous finite-parameter gap; this is not merely rerendering the plot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
