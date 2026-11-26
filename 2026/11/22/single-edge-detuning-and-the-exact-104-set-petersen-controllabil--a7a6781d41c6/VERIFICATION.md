---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Exact rational reconstruction gives E_2 and E_5 dimensions 5 and 4, and U_2 and U_5 dimensions 4 and 3. For delta=t−1, L(t)=L(1)+delta bb^T. The constant direction and U_2,U_5 are fixed; on the span of the two projections a,c of b the quadratic is lambda^2−(2t+5)lambda+6t+4. Its discriminant is 4t^2−4t+9>0, and evaluating at 0,2,5 excludes all collisions for positive nonunit t. The split block is invisible if S misses T. If S meets T and the restrictions are independent, neither split eigenvector vanishes there. If the restrictions are dependent, the only candidate invisible lines are c−2a and b: the first is orthogonal to b and is not an eigenline of L(1), hence not of L(t); on the second the rank-one update adds only a multiple of b and L(1)b is not parallel to b. These cases establish visibility for every fixed positive nonunit t. Independent rational tests of all 1024 coordinate subsets confirm that injectivity on U_2 implies injectivity on U_5, and that of the 105 rank-four four-sets only {3,7,8,9} misses T. At t=1 the unperturbed PBH ranks apply. The reconstructed count vectors by size 0–10 are [0,0,0,0,104,210,203,120,45,10,1] nonunit and [0,0,0,0,0,162,195,120,45,10,1] unit, giving both polynomials and the sharp minima.

## originality

PASS

The supported distinct claim is the exact coordinate-placement classification and enumerators, with an identical placement criterion throughout the positive nonunit regime. The unweighted minimum of five and the general multiplicity bound are already covered and receive no separate originality credit. Among the inspected claims none gives the full unit census or the positive-nonunit Petersen result.

## value

PASS

The canonical Petersen graph has highly repeated Laplacian eigenvalues; breaking symmetry at one link naturally raises the question of whether fewer chosen vertices suffice and whether placements change at special weights. The full PBH census answers both, distinguishes 104 placements from the multiplicity prediction alone, and excludes placement transitions anywhere in the positive detuned regime. The explicit finite rank criterion is reusable without computing parameter-dependent eigenvectors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
