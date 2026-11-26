---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The three nodal hat integrals give the stated Gram matrix and determinant a(1-a)/36. The kernel reproduces constants, and its absolute row integral is convex on each mesh interval, so a global maximizer is among the three nodes. Independently, the inverse has knot row (-2,4,-2) and endpoint 1 row (1,-2,1+3/(1-a)). At 1 the signed row has negative triangular areas 2a/3 and 2(1-a)^2/[3(2-a)]; their sum is 2/[3(2-a)]. Reflection and the knot row give the other two norms, producing the exact profile, unique balanced minimum and nonattained supremum. The sign and negative-set indicator of a maximizing row attain the two claims. Smooth strict-range approximations preserve negativity by boundedness of the fixed row. For the strong limit, subtract the affine projection of v_a=(a-y)_+ from v_a. Bounded affine basis functions give ||P_aff v_a||_2=O(a^2)=o(||v_a||_2), and the normalization of v_a converges weakly to zero by Cauchy–Schwarz on [0,a]. The difference projector is the rank-one projection onto the normalized residual and thus tends strongly to zero in L^2. Reflection treats the other endpoint. The affine kernel at 1 is 6y-2, whose negative integral in magnitude is 1/3; convexity gives norm 5/3. This is a jump of sharp norms, not a claim of L-infinity operator-norm convergence. The frozen checker was inspected but the continuum and limit steps were established analytically.

## originality

FAIL

The central exact one-knot norm and range defect are mechanically covered by the previously published metric-star calculation 01f1cffc69a6. Its headline theorem states m>=3, but the proof is explicitly dimension-independent: the sole indicated use of m>=3 is to ensure each arm is shorter than the total, also true at m=2. Its verification explicitly includes two-arm length vectors. The strong-L^2 limit is not asserted in that record, but here it is a routine consequence of the extra normalized hat concentrating on the vanishing interval; the numerical gap follows directly from the prior row formula and the affine case. This is a concrete proof-level overlap, not a verdict based on an inaccessible historical paper.

## value

FAIL

The exact parameter profile for a natural projector is useful, but the submitted profile, extremal witnesses and range defect reduce mechanically to existing leaf-row formulas. The additional strong-L^2 observation is a standard shrinking-support argument for an added rank-one direction; together with the prior row formula and the elementary affine norm it explains the numerical gap, without providing a further nonroutine invariant or classification that would justify a standalone repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
