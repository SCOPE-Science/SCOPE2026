---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The independent uniform interior-point difference decomposes into independent side-square-scaled W_i=(U_i-V_i)^2. Exact cumulants (1/6,7/180,11/945) recover the three power sums; Newton identities uniquely reconstruct the positive squared edges. The normalized sum-one, sum-squares-q circle has a sharp product range with an open zero-volume endpoint when q>=1/2. The extremal profiles (1-r,1-r,1+2r) and (1+r,1+r,1-2r), divided by 3, cover all positive-volume endpoints. Inspected RESULT.md and check_cuboid.py; independently rederived cumulant and fixed-q factorization algebra. Finite Monte Carlo in the package is not proof.

## originality

FAIL

Exact same observable, box class and theorem were published October 25, 2026 in Sharp three-moment tomography of rectangular solids. Its complete RESULT.md was read. It already gives these identical moment/cumulant power-sum identities, cubic reconstruction, optimal two-vs-three-moment count, all normalized feasible (u,v) triples, and the volume formula. Projecting the known two-dimensional feasible set at fixed u gives exactly the later conditional volume interval and q=1/2 threshold. The prior theorem is strictly stronger, adding optimal 1/3-Hölder reconstruction stability. No surviving independent original claim in the submitted package.

## value

FAIL

The conditional volume bounds and equality cases are an immediate algebraic projection of the October 25 exact feasible moment region, not an additional unknown invariant or new boundary classification. The submitted result has expository value but no independent mathematical finding after precise prior coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
