---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Exact conserved-simplex reduction gives I′=-beta I[I+R+(1-sigma)C]; I decreases and converges to zero. Stable R,C equations imply R/I->a=alpha/(mu+delta), C/I->c=delta*a/(mu+gamma), then I~1/(Kt). Stable convolution and defect equations yield R=a I+b I^2+O(I^3), C=c I+d I^2+O(I^3), with b,d displayed in RESULT.md. The cubic I′=-KI^2-LI^3+O(I^4) has integrable reciprocal remainder, giving finite orbit-dependent H. For both feedback laws g=I+O(I^2), so K,L coincide. The check independently recovered K=3 and L=(3-epsilon1)/2 for mu=alpha=delta=gamma=1, beta=2, sigma=1. I(0)=0 and sigma endpoints handled; no claim away from threshold.

## originality

PASS

The underlying SIRCm system and DFE threshold are known, but reviewed source establishes only hyperbolicity off threshold; preceding same-field equilibrium paper excludes trajectory stability/decay. The universal second-order all-infected critical relaxation and two-feedback logarithmic sign change are not consequences of those cited theorems. Best-of-knowledge pass with explicit 2006 SIRC and unindexed priority risk.

## value

PASS

A nonlinear nonhyperbolic threshold is intrinsically important for relaxation rates, and the exact feedback-invariant leading amplitude versus feedback-sensitive sign-reversing log coefficient distinguishes mechanisms not visible from linear stability. It is a substantial parameter-uniform asymptotic classification, not an arbitrary small-case computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
