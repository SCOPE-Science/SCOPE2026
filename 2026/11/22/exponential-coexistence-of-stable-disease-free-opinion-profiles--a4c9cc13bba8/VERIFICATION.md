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

The stated epidemic box faces point inward or tangent, as do the opinion faces: at o_i=1/2 the coupling contribution is w times the sum of |o_j|-1/2; at o_i=-1/2 it has the opposite sign. On every admissible absolutely continuous solution the componentwise epidemic comparison with the Metzler matrix -I+(A+I)/(4m) holds almost everywhere, and its spectral abscissa is at most -1/2. There is local forward continuation even at switches: for zero coordinates the two one-sided velocities are x_i-1/2 plus or minus w times the sum of neighboring magnitudes. Choose the branch of the sign of x_i-1/2 when nonzero, and either outward branch when that difference vanishes but the sum is positive. At a zero with both terms zero choose the negative branch: x_i=1/2 has strictly negative derivative (bound its infection term by (m+1/4)/(8m)), and all zero neighbors in the chosen branches have nonnegative initial magnitude derivatives. This gives a strictly negative second derivative of that opinion in the smooth branch extension. Thus a consistent branch exists just after the start; bounded velocities and restart at finite limit points give continuation without a uniqueness claim. The discontinuous equation is understood almost everywhere along trajectories, with equilibria evaluated using the specified pointwise sign at zero, not a convexified differential inclusion. In a fixed sector the signed opinion system is conjugate by its diagonal sign matrix to the positive definite I+wL. Eliminating the leaves gives exactly the stated two strict quadratic inequalities when P>=1, and the linear positive-center test when P=0. For w>=m+3 the positive quadratic coefficients (at least one) always pass, including the endpoint; nonpositive coefficients never pass. A pointwise zero is assigned +: a zero center cannot admit a positive-sign leaf and then requires w(m-1)=1, while any zero leaf requires one of the quadratic equalities. These equalities occur neither for w>=m+3 nor for m=3,w=2. The two binomial sums give the asserted parity-dependent total, including m=1. The regular full Jacobian is lower triangular in its epidemic and opinion blocks, with the epidemic Gershgorin upper bound -3/4 and a symmetric negative definite opinion block, hence local exponential attraction in a fixed sign neighborhood. An independently written rational row-reduction check on the original opinion variables (including pointwise zero as positive), grouped by leaf permutations, confirms all five coordinates/profiles at m=3,w=2 and the high-weight count through m=12 at two weights each. Replay python3 /workspace/checks/5.py; output /workspace/checks/5.txt. The frozen CHECK.py was read, not executed. No assertion of global opinion convergence, uniqueness at switches, or counting generalized inclusion equilibria is made.

## originality

PASS

The epidemic criterion and regular sign gauge are prior or general tools. The distinct contribution is the exact and exponentially large star census in this sign-selected coupled model, with simultaneous full-state attraction while infection decays globally.

## value

PASS

It answers the originating model's unresolved question of whether the healthy state can coexist with multiple robust opinion profiles under eradication. The natural all-star census, parity gap and exact small witness show exponential coexistence of hyperbolic attracting states, not merely multiple algebraic candidates or an artifact of persistent infection. The result does not assert the basins cover all opinion trajectories.

The dated certificate retains the supplied scientific assessment, sources and limitations.
