---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS: For T=H+iK, r=||H|| and s=||K||, the centrally symmetrized numerical-range hull C has support h_C(theta)=||H cos(theta)+K sin(theta)||. Reflection across real axis and the Minkowski average D=(C+conj C)/2 satisfy mean h_D^2<=mean h_C^2 by Jensen. D has both axis radii r,s and contains E=conv{+-r,+-is}; hence the exact integral of max(r²cos²,s²sin²) bounds Q_2(T)² below. Quadrant integration gives r²/2+[rs+(s²-r²)atan(s/r)]/pi for r>0, and s²/2 for r=0. Equality in the two nonnegative continuous support differences forces C=D=E. Diagonal operator diag(r,-r,is,-is) realizes all norm pairs; Taylor expansion gives 4s³/(3pi r)+O(s^5/r^3) for fixed r>0. Independent quadrature checked endpoint, symmetry and cubic asymptotics; universal proof is analytic, not numeric.

## originality

PASS

PASS best-of-knowledge with explicit risk: The new claim is sharp simultaneous norm constraints (||ReT||,||ImT||) and exact equality diamond for ALL bounded operators. Earlier angular radius inequalities give unconditional bounds; 2026-11-02 sharp *conditional envelopes* fix u=distance to phase-self-adjoint operators/numerical radius, which does not prescribe r and s and does not imply diamond two-norm optimization. Published cubic-stability result already uses the same four-point diagonal example and 4/(3pi) asymptotic; these are credited, not claimed new. A classical wider geometric support inequality could subsume the result but no direct coverage found in actual searched sources; inaccessible October 2026 primary article is named as residual access risk.

## value

PASS

PASS: A sharp dimension-free two-constraint inequality and complete equality characterization for an operator radius answer a motivated extremal question, distinguishing joint Cartesian-part information from global numerical-radius or phase-distance profiles. The full universal diamond rigidity is more than a known diagonal calculation or a small coefficient gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
