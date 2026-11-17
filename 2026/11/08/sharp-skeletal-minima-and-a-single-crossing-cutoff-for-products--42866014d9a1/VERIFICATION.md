---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For m>=2 orthogonal products of m nondegenerate planar triangles containing the centered unit disk, each factor has area>=3sqrt3 and perimeter>=6sqrt3 with rigid equilateral equality by Jensen on half angles; f0=3. Face-volume generating polynomial is exactly product(A_i+L_i t+3t²). Positivity yields every coefficient lower bound [t^k](3sqrt3+6sqrt3 t+3t²)^m; equality rigid for k<2m and automatic at vertex count k=2m. Factor H(t)=3sqrt3(1+u t)(1+v t), u/v distinct with mean 1, and strict Newton inequalities show R_m(0)=R_m(1)>R_m(2)>...>R_m(2m); endpoints straddle 1, so a single integer crossing cutoff K_m. Correct boundary m=2 K=2; exact symbolic coefficient calculation independently checks m=2..8; does not assert all admissible polytopes.

## originality

PASS

Originality PASS for simultaneous complete coefficientwise minima for every codimension and strict one-crossing cube-comparison cutoff for all products of triangles. Prior more general planar product work established ridge (codimension two) only; Zwierzyński supplies product polynomial and higher-codimension counterexamples without this all-k profile. Elementary Jensen/Newton steps are not individually claimed novel.

## value

PASS

Determining the exact feasible codimension range within a natural infinite subclass of a published skeleton conjecture is a substantive structural result; the rigid extremal profiles and sharp change of sign answer which dimensions retain cube bounds. It is not a recomputation of the already-covered ridge special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
