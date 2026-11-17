---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS: The prescribed global-max norm relaxation for rows a1=(1,0), a2=√(1−τ²)(ρ,√(1−ρ²)), τ,ρ∈(0,1), is ω1=1 and ω2=1+τ. In exact arithmetic U=I−uuᵀ, V=I−vvᵀ, W=I−(1+τ)vvᵀ. Enumerating four iid uniform two-step words gives second-moment matrices B_Z=1/4[U(U²+Z²)U+Z(U²+Z²)Z], and difference D=B_W−B_V. Direct exact product yields tr D=τ²(τ²+2s²)/4>0, det D=(ρ²s²τ²/16)[τ⁴+τ(τ+2)s²−1], s²=1−ρ². A symmetric 2×2 matrix with positive trace has negative eigenvalue iff determinant<0; equality or reverse means positive semidefinite, proving the all-initial-errors classification including equality and strict worse directions. One-step difference τ²(eᵀQe)/2 is nonnegative for every e and strictly positive unless Qe=0; the source correctly says 'never better', not strictly worse for all. Independently enumerated exact rational four-word matrices for τ=s=3/5, ρ=4/5, e=(0,1) to get Eunit=1681/2500, Erel=10297/15625, difference −837/62500. The τ0 quartic derivative is positive, so unique threshold root. No claim beyond two steps or all initialization improvement.

## originality

PASS

PASS (qualified): The Oct 8 2026 Entezari–Banerjee–Kalantari source introduces the volume-normalized relaxation rule and provides generic contraction and simulations, but does not state this sharp two-step fixed-initial-error benefit region or the counterintuitive contrast with the nonimproving one-step effect. Published related two-row Kaczmarz studies optimize dependent row-selection coupling at a common relaxation or compare reshuffling and independent selection; those change the policy, objective, or parameterization. No exact equation for this specific unequal norm-induced ω1=1,ω2=1+τ comparison was found. Strong antecedent warning: all calculations are simple 2×2 second moments and might be derivable from general prior MSE formulas; no full historical exhaustion.

## value

PASS

PASS: The new adaptive overrelaxation is an actual recently introduced algorithmic policy; its apparent uniform one-step disadvantage makes the exactly characterized two-step strict-benefit and strict-harm region a meaningful cautionary finite-horizon boundary. The continuum of τ,ρ with an exact spectral if-and-only-if and a rational witness is motivated and not just an arbitrary isolated numerical example. It does not promise worst-case or asymptotic improvement, and mathematical utility is narrower than a general algorithmic convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
