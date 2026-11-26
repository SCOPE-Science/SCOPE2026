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

In residual coordinates each exact all-but-one update projects onto the normal to the retained columns. The two nonorthogonal normals can be chosen with dot product rho; all others are mutually orthogonal and orthogonal to the pair. For a fixed sample string the squared norm is its first-direction squared projection times the squared overlaps of successive normals. Averaging gives a pair block h_1 P_1+h_2 P_2 and the separate eigenvalues p_j^K for j>=3. Fix positive pair mass t. The bisector tests the pair block at (1+rho)(h_1+h_2)/2, attaining its top eigenvalue at balance. In the path expansion for h_1+h_2 each selected bond set forces the selected field factors to be precisely its odd-degree vertices. Hence only even powers of the imbalance appear, all with nonnegative coefficients; one selected bond gives a positive quadratic term when K>=2. This proves strictness at all imbalances, including boundary probabilities. For K=1 the pair trace is fixed and the determinant (1-rho^2)p_1 p_2 is uniquely maximized at balance. At t=0 the block is zero. The two lower bounds on the K-th root, C_K t/2 and (1-t)/(n-2), intersect at a unique interior pair mass; both are active and enforce exact balance in each group at an optimum, including n=3 with only one orthogonal direction. This gives the claimed sampler and sharp value. For the one-step law its orthogonal block dominates at every K and has retention r_1^K; the K-th root of the ratio tends to r_1/r_infinity>1. The proof concerns exact fixed iid sampling and terminal expected objective, not adaptive or pathwise extrema. The shipped verification was inspected, not rerun; its reported 864 finite checks support the projection and recurrence, not the minimax proof.

## originality

PASS

The distinct claim is the exact unique optimizer and sharp value for each K>=2 and every 0<rho<1 in the specified one-pair family, with quantified loss from the one-step law. The K=1 case is already covered, and the broad horizon-dependence phenomenon also occurs in a same-day result; neither is credited as independently new here.

## value

PASS

One nonorthogonal pair is the smallest residual geometry where mixing two types of errors can change the optimal law with the horizon. The exact optimum, strictness, and exponentially growing worst-case penalty of a one-step-optimal fixed law quantify a real distinction between tuning a one-step contraction and tuning terminal performance. The evidence does not generalize to dense Gram matrices, nonstationary or adaptive sampling, or time-based costs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
