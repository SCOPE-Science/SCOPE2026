---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Use P(x,y,z)=(x,y,y,z), W=diag(w,w,1,1), element lengths r,1, and no end-node elimination. The local mass and its inverse give the stated M and B_w. The difference between either weighted restriction and the mass-orthogonal left inverse vanishes on range(P); the mixed terms with the mass-orthogonal inverse vanish. Thus B_w−M⁻¹ is positive semidefinite of rank at most one, and the SPD similar product has two unit eigenvalues. In the trace of B_wM the end nodes supply 8/3 and the two interface couplings subtract 2/3, leaving trace 2+4(r+1)(r+w²)/(3r(1+w)²). Subtraction of 4/3 leaves a positive factor times (w−r)², so the spectral ratio is minimized uniquely at w=r. For w=r^γ the correction is invariant under r↦1/r; at infinity it grows like r for γ<0, r/4 at γ=0, and r^(1−2γ) for 0<γ<1, vanishes identically at γ=1, and decays like 1/r for γ>1. At γ=1/2 it is exactly ((√r−1)/(√r+1))² before multiplication by 4/3, so the spectral-ratio supremum 8/3 is not attained at finite contrast. The Jacobi comparator is consistent: the squared normalized adjacent off-diagonals sum to 1/4. This is a three-DOF spectral ratio result, not an ordinary matrix two-norm estimate or a many-cell sufficiency theorem. Replay: RESULT.md displayed assembly/rank/trace and power analysis; verify_weighted_bras.py inspected, not executed, exact-rational finite checks only.

## originality

FAIL

The arbitrary-weight nonunit eigenvalue is a direct scalar specialization of the previously stated exact weighted BRAS constraint-space spectrum, not just compatible with its upper bound. The remaining optimum and power threshold follow from a square completion and elementary tail limits in that scalar formula. The known construction, rank result and exact spectrum reduction already cover the decisive invariant; no distinct mathematical step remains that supports the claimed originality.

## value

FAIL

This is a natural graded-mesh sanity check, and the exponent is convenient for interpreting the example. But the decisive invariant is an immediate local substitution into an existing exact reduction, and the residual minimization and exponent test are elementary consequences of that expression. The record supplies neither a new obstruction not already available from the reduction nor a many-cell conditioning implication. It is useful as a worked specialization, not a distinct valuable finding under the contract.

The dated certificate retains the supplied scientific assessment, sources and limitations.
