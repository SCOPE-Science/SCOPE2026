---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

On A=1, the tangent-center chart gives B=s²+2su,C=t²+2tv,D=s+u,E=t+v,F=st+tu+sv and determinant Δ=0. Eliminate u,v and t=(F−sE)/(D−s), obtaining P(s)=s²−2Ds+B and resultant/remainder −Δ. In the function field K=k(C,D,E,F) of determinant cubic, D²−B=−(F−DE)²/(C−E²). The irreducible prime C−E² has odd valuation in K, making P irreducible in any characteristic; its derivative is 2(s−D) except when char2, where zero derivative and B nonsquare give inseparable degree2. The rank-three tangent-cone vector bundle has Segre s₂=6; degree of cubic image3 independently gives 2. Generic field-extension degree and image are proved, not an assertion about every fibre.

## originality

PASS

Best-of-knowledge PASS for the exact change of separability of the same tangent-incidence morphism at characteristic two. Classical determinant cubic is prior; Gauss-map results and analogous purely inseparable tangent incidences on different surfaces do not imply this particular function-field calculation. Named older positive-char risks remain.

## value

PASS

The distinction between geometric number of tangent centers and scheme-theoretic generic degree under characteristic specialization is a natural geometric invariant, with explicit inseparable field certificate and intersection-theoretic cross-check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
