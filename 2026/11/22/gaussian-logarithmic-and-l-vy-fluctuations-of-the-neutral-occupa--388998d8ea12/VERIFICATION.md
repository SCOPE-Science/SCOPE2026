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

The raw Poisson integral is finite by its first moment, including at the initial endpoint by monotonicity, and centering yields càdlàg independent-increment martingales. For r>2, integrating v E[W²] in the compensated bracket gives ((r−1)/(r−2))t^(2α) and the Lindeberg integral vanishes by domination. At r=2, truncating the raw jumps at b=(β log β)^(1/2) gives bracket t log b/log β + O_T(1/log β), uniformly including t=0. The jumps above εb have intensity O_T(1/log β), their discarded compensation is negligible for ε=1, and the variance between εb and b vanishes, giving the Brownian limit with variance t/2. For 1<r<2 the Jacobian for y=β^(−1/r)t^α w cancels the physical-time power by αr=1; independently comparing the unsimplified and displayed densities at β=37, t=.5, y=1.2, r in {1.25,1.5,1.9} gave relative differences below 5.4e−16. This density is for the stable-scaled, centered process divided by r−1 (centering does not affect jumps). Above ε it converges with its finite first-moment compensator; the Poisson cumulative sums have J1 convergence as limit jump times are distinct and avoid the endpoints almost surely. The small jump error has squared supremum bounded by 4T ε^(2−r)/(2−r), before and after taking the limit. Hence the converging-together argument identifies the stated stable process with full linear compensation, mean zero and exponent Γ(−r)(−iu)^r, on the principal branch. Standard martingale and Poisson limit tools justify the asserted J1 topology; finite checks alone would not. Supplied verification and checker examined without execution.

## originality

PASS

The existing occupation theorem exactly supplies the Poisson family, and the limit tools are classical. The supported distinct result is the centered high-intensity functional classification with its model-specific critical coefficient, physical clocks and exact stable-scaled kernel. The examined occupation and representation theorems do not cover this high-intensity statement.

## value

PASS

The Poisson family is motivated by a specific occupation law, not chosen to restate textbook fluctuation scales. The result classifies whole paths, gives the exact critical logarithmic scale and identifies which limiting increments are stationary in physical time. These resolve behavior hidden by the known deterministic endpoint; they do not imply a joint map/intensity limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
