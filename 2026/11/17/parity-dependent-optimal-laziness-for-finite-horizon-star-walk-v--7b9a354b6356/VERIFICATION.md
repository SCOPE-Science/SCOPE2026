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

On the quotient of vertex functions by constants, leaf-to-hub gradient g in R^k maps as B_alpha g=[alpha I-(1-alpha)Q]g with Q=11^T/k. Orthogonal idempotents give B^m=a(I-Q)+bQ, a=alpha^m, b=(2alpha-1)^m. Its induced edge-TV norm equals the common l1 column sum [|(k-1)a+b|+(k-1)|b-a|]/k, algebraically equal to max(|b|,[2(k-1)a-(k-2)b]/k), and leaf-indicator gradients attain it. On alpha>=1/2 the active branch strictly increases. For even m the contracting |1-2alpha|^m branch crosses at 1/3 and then the other strictly increases; at 1/3 B^m=3^{-m}I exactly. For odd m, the cusp alpha0=1/[2+(k-1)^(1/m)] competes with the F derivative, whose positive/negative sign produces unique cusp at k=2,3 and unique interior stationary optimum at k>=4 for m>=3. Direct rational independent iterations corroborated 320 parameter cases with k=2,3,4,6,m=1..5 and alpha=j/15.

## originality

PASS

The earlier exact K_p,q edge-TV theorem is one step and for p,q>=2; its formula extends to the isolated star m=1 but not to the all-horizon parity and k=4 cusp-to-interior threshold. Tree-TV regularization and fastest spectral mixing address different functionals. The multi-step global optimization appears new to the inspected primary and published material.

## value

PASS

The precise laziness parameter is mathematically important for finite-time smoothing of edge oscillations. A uniform optimizer 1/3 for all even horizons, parity-dependent sharp odd optimum, and structurally explained k=4 cusp/interior transition resolve a nontrivial natural extremal problem for every star size and horizon, beyond one-step textbook spectral decompositions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
