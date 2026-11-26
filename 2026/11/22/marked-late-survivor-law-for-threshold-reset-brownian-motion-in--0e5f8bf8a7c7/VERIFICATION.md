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

With ν=π/α=2β, the radial kernel and the angular Dirichlet normalization give the prefactor 1/(αDt) in the free-wedge heat kernel. Substituting r=√(4Dt)v and expanding the principal Bessel term gives the stated A_0 from the angular integral 2/ν and the radial integral Γ(1+ν/2)/2. In the flux, the inward normal derivative uses 1/r; the principal angular derivative at each edge has the same magnitude ν. The remaining radial integral is Γ(ν/2)/2, giving βA_0/2 on each edge. Integrating the current gives H_j(t)∼(A_0/2)t^{−β} for both marks; higher modes have larger powers, with summable integrated gamma-ratio bounds from the Bessel series. The marked renewal identity is exact: after k reset-ended durations with sum s≤t, the chance of the specified active mark and no exit by t is H_j(t−s). On s≤t/2 dominated convergence applies; on s>t/2 the fixed-k convolution density has order t^{−β−1} by splitting each convolution in half, so its contribution is o(t^{−β}) even when β≤1. The signed-test wording after Eq. (93) should read 'when the integral is zero' for the zero limit; the signed scaled convergence already follows from (79)–(86). Unconditionally, N is geometric, and a fixed-N sum of independent mark-conditioned durations has tail asymptotic to the sum of the individual regularly varying tails: two durations exceeding t^γ for 1/2<γ<1 have negligible probability, and the remaining shift of the largest is o(t). The union bound at t/(n+1) provides a summable polynomial envelope times the geometric probabilities for all n, yielding the A_0/a normalization. The resulting limiting fixed-(k,j) masses sum to one, so there is no escaped mass; the epoch variable has the k-fold reset-duration law independently of the fair mark, given k. On a reset-marked active excursion its completion adds one reset and a fresh independent geometric count. The resulting PGF, mass and moments agree algebraically; finiteness of the epoch law, not finiteness of its mean, gives S_t/t→0.

## originality

PASS

The same model, equal leading free-exit currents, absorption-survival tail and unconditional reset-count laws are explicitly prior. A geometric count under survivor conditioning and the single-large-excursion mechanism also have substantial prior analogues. The distinct claim retained is the joint conditional physical-time law: completed count, nontrivial unscaled last-reset epoch, retrospective active-edge mark and total future-inclusive count. The strongest verified wedge and general-source passages do not supply that joint law or a theorem whose hypotheses directly give it for the mark-dependent geometric stopping rule.

## value

PASS

The joint law distinguishes past interventions from total interventions for the same selected late-surviving trajectory and places the last reset on its actual, unscaled time axis. It identifies a fair retrospective exit edge despite biased unconditional splitting, and explicitly links this mark to a different total-count law. These observables are not interchangeable with the unconditional count or one-dimensional survival tail and form a quantitative benchmark of the threshold-reset model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
