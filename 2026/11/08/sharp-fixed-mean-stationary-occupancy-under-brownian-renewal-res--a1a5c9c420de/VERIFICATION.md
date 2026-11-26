---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For the equilibrium clock the age has density P(S>t)/mu, including lattice and deterministic S. Tonelli gives E[H_x(S)]/mu, the continuous Gaussian-mixture density at nonzero x. With h=p_s(x), R=H_x-sh satisfies R'=-sh', so R decreases from zero until x²/sigma² and then increases strictly to infinity. Thus H_x(s)/s has one strict maximum; the line to the tangency followed by H_x is a concave majorant. Below tangency, strictly positive clocks of mean below tangency must pay a strict majorization loss; clocks on epsilon and the tangent time approach the bound. At tangency, upper equality excludes waits below it and the mean excludes waits above it; above tangency strict concavity gives uniqueness. For the lower bound, H_x(s)>0 and the tail weight on M is O(1/M) while H_x(M)=O(sqrt(M)), so the two-endpoint limit proves the positive-but-unattained infimum zero. Independently quadrature and scalar root finding give s*=2.66988552687754032, threshold 0.61200318096248076, and optimum 0.20245649018802463 versus deterministic 0.16663094117537260 at x=sigma=mu=1. Replay: python3 /workspace/branches/independent_checks.py (brownian_check); finite diagnostics only. The uploaded checker was read, not run.

## originality

PASS

Best-of-knowledge pass for the explicit nonzero-position Brownian envelope and its equality/nonattainment classification, not the renewal density formula or the abstract one-moment envelope method. The inspected related models do not determine the Gaussian tangency and its strict-positive equality cases.

## value

PASS

Pointwise stationary density is a natural occupation objective at a specified nonzero location and is inequivalent to first passage. The result decides when timing randomness is useless and when deterministic resetting is strictly suboptimal, quantitatively, and explains why vanishing intervals are needed in the latter regime. This is an exact all-law comparison, not a numerical improvement for one parametric family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
