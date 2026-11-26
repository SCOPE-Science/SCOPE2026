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

For fixed positive A,B, solving the two backward equations on x<L with boundedness at −∞ and the right-moving boundary value 1 gives the displayed positive root for s>0. At s=0 monotone convergence leaves (A−B)_+/v in the transport exponent. The Laplace difference law then gives half plus 1/[2(1+β)] as the hit probability. The near-tie singularity is also obtained without special functions: write d=|A−B|, u=2 min(A,B)/λ and h=sqrt(sλ). The square-root increment over d is Δ=sqrt(d²+4s(s+d+λu))−d. In the d<h portion its averaged contribution is O(h²)=O(s); for d≥h use Δ=2s(s+d+λu)/d+O(s²(s+d+λu)²/d³). The integrated error is O(s), as is the error from linearizing 1−exp(−LΔ/(2v)). The signed-rate averaging weight at d=0 is 1/λ and E[u]=1, giving (L/(2v))s log(λ/s) with O(s) remainder. Monotone convergence of the difference quotient gives the infinite first moment on finite hitting paths. Fresh independent episodes make success probability φ(r) and mean episode length (1−φ(r))/r. Expanding the reciprocal gives exactly the claimed small-r coefficients. At high r, T_L≥L/v and the atom at L/v is the no-switch flight, of mass E exp(−AL/v)=1/(1+β). Bounded convergence after removing exp(−rL/v) gives the large-r prefactor. The two divergences and continuity prove existence, not uniqueness, of an interior minimizer.

## originality

PASS

The supported distinction is the defective annealed first-passage law with a sharp near-tie logarithm and the resulting fresh-rate Poisson-reset mean asymptotics. Known conditional Markov solutions, the geometric-clock transport definition and the generic renewal identity are not credited as new. The closest transport paper leaves first passage open, and its reset convention in position/velocity alone should not be read as an independently established refresh of the hidden rates.

## value

PASS

Equal directional clock marginals conceal a trajectory-specific drift: the exact defect quantifies that distinction, and the successful trajectories still have infinite first moment because of nearly balanced episodes. The two sharp reset regimes quantify how restarting cures the defect but eventually suppresses the earliest ballistic flight. These limits provide a meaningful existence result for a positive optimal rate, beyond a formal substitution of a generic renewal formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
