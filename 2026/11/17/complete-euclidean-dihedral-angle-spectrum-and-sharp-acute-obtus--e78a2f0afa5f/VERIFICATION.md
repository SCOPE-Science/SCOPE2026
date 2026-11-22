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

C PASS: In the canonical unweighted cycle C_n, n>=3, the n Laplacian columns affinely span the zero-sum hyperplane. Its barycentric facet normals are L_n^+e_i. Directly solving both cyclic difference equations gives (L_n^+)^2_{00}=(n^2-1)(n^2+11)/(720n) and (L_n^+)^2_{00}-(L_n^+)^2_{0d}=d(n-d)[d(n-d)+2]/(24n); their normalized Gram cosine gives the exact claimed interior dihedral angle pi-arccos(1-30u(u+2)/D_n). Increasing u over 1..floor(n/2) proves levels and multiplicities, with n=3,4 acute and n>=5 both signs. Exact angular distribution follows the distance-pair Riemann sum, and integrated cosine moments give 1/(n-1), 3/7. Independent rational matrix inversions and directly reconstructed normals were checked for n=3..12; finite instances corroborate rather than prove all n.

## originality

PASS

O PASS, best of knowledge: The same Euclidean realization and pseudoinverse facet-normal formula, and even the cycle diagonal norm/inradius, are known in the earlier vertex-transitive Laplacian-simplex theorem. That full proof was inspected. Its scalar spectral trace supplies only squared normal lengths, not their off-diagonal Gram matrix, distance-indexed full angle multiset or sharp acute/obtuse asymptotic. Braun-Meyer and Meyer-Pllaha focus on lattice/Ehrhart/coding invariants; Devriendt provides broader generic Gram angle machinery for a differing graph simplex model. The evaluated all-cycle angle spectrum and limiting law were not identified as earlier stated implications. Biharmonic Green-function tables and alternative angular nomenclature remain a priority risk.

## value

PASS

V PASS: All ridge angles and multiplicities form a complete intrinsic Euclidean metric fingerprint of a canonical infinite graph-simplex family. The unexpected sharp mixed acute/obtuse transition at n=5 and a nondegenerate uniform-ridge limit with ~48.07 percent obtuse probability are mathematically meaningful, not just reusing the previously known inradius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
