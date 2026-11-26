---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The tridiagonal B=DM⁻¹Dᵀ is positive definite and has nonpositive off-diagonals; its weighted column sums are exactly the stated inequalities, with the two zero boundary weights. An independent direct nonsmooth check is possible: the proximal optimality difference gives d=z+Bη for input differences d, output differences z, and differences η of edge subgradients. By monotonicity choose θ_i in sign(z_i) with θ_iη_i=|η_i|, also when z_i=0. Then wᵀ|d| is at least θᵀdiag(w)d, and θᵀdiag(w)Bη is at least Σ_j (wᵀB)_j|η_j| by the off-diagonal signs. This proves the asserted inequality directly, without imposing a secant at a kink. Apply the same bound to each scaled potential in implicit Euler and pass to the subgradient-flow limit. If a column fails, the unit step across that edge and the single quadratic give edge vector e_j−γBe_j with γ=a/(1+aB_jj) for the resolvent or γ=(1−exp(−a B_jj t))/B_jj for the flow. This vector is nonnegative, so the variation increases strictly, including all positive flow times. With equal masses the criterion is the zero-boundary concavity condition; the identity penalty attains the universal constant one. Independent bounded replay: python /workspace/replay/checks.py 3 checks 15,625 exact subgradient comparisons with asymmetric nonsmooth energies and an admissible weight on the boundary. It supplements the proof rather than establishing the all-energy theorem.

## originality

FAIL

The strongest comparator proves the identical sharp criterion for the whole family of positive-conductance linear path heat semigroups, not just one diffusion. The full nonlinear conclusion follows from that family by the semigroup-resolvent integral, coordinatewise convex secants, smoothing, and implicit Euler. Although the comparator does not state a nonlinear theorem, these standard operations cover the submitted universal claim, not only its quadratic specialization.

## value

FAIL

Pairwise stability in an independently chosen variation metric is useful, but the exact new-scope claim depends only on the already sharp all-conductance condition by standard secant and resolvent closure. The single-edge strict witness makes that condition concrete but is a rank-one calculation along the same already identified failing column. No independent structural advance remains in the audited scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
