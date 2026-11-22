---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For the unrescaled covolume-2 D4 root lattice, |x_i|+|x_j|<=1 specifies the exact 24-vertex Voronoi 24-cell with squared covering radius 1. Distinct unit vertices have dot product <=1/2; linear support bounds make the norm²>3/4 superlevel a disjoint union of 24 vertex caps. In the e1 cap, x=(1-t,t u_1,t u_2,t u_3) with 0<=t<1/4, the deficit equals 2t-(1+sum u²)t², yielding a three-cube integral after the exact t³ Jacobian. Catalan/Lagrange inversion and uniform convergence for epsilon<1/4 prove the full rational positive series. Independently recomputed b0=1, b1=2, b2=56/15, b3=152/21 by symbolic uniform moments; finite algebra corroborates the exact derivation.

## originality

PASS

Best-of-knowledge noncoverage after implication comparison; The cited general theory does not deliver the claimed nonlocal epsilon interval and coefficients as a corollary.

## value

PASS

The natural squared-quantization-error tail near deep holes of a celebrated highly symmetric lattice is given not just as a moment or plot but as an exact convergent all-order law on a nontrivial interval. It quantifies rare worst-case errors, useful independently of global optimization theorems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
