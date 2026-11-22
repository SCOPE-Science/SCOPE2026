---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

On each unit interval, Hermite derivative is s_j[Sprime+(m_j/s_j)Aprime+(m_(j+1)/s_j)Bprime], with two normalized endpoint slopes in [0,2] when s_j has nonzero sign, zero otherwise. The four corner polynomials are nonnegative on [0,1], so the interpolation has exactly |s_j| variation on each cell; the infinite sum yields individual variation preservation. H(a,b) has coordinate derivatives in [0,2]; a perturbation of one increment produces one monotone central response (variation 1) and two neighboring humps with variations 8u/27 and 8v/27. Thus a one-edge directional variation <=1+8(2+2)/27=59/27; integrate along finite changes, then telescope l1 increments and use lower-semicontinuity under local convergence. For baseline slopes (1,0,1) and epsilon inserted into the middle, exact ratio=1+32/[27(1+epsilon)] tends to 59/27. Independent symbolic derivative corner checks and exact rational witnesses epsilon=1/100,1/1000 match. No finite actual pair is claimed to attain the limit.

## originality

PASS

The original Fritsch–Butland 1984 construction and later monotonicity theory establish shape and one-input variation preservation, but not the difference of two distinct interpolants under total variation. Related Steffen, minmod and affine blend schemes use different slope selectors; numerical stability results cannot be transferred to the harmonic selector without the derivative calculation. Residual unindexed PCHIP nonlinear-conditioning literature risk is recorded.

## value

PASS

The exact two-input stability factor of the standard harmonic-mean monotone cubic interpolant is a natural practical and theoretical condition number. The surprise that one-signal variation preservation coexists with >2 amplification of differences matters for noise sensitivity and inverse-interpolation analysis; the sharp witness explains mechanism without an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
