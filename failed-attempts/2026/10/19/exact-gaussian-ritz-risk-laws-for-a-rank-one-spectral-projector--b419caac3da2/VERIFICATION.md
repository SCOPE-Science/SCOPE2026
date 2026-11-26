---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The restricted Gaussian sketch has a Haar null line in C^(m+1), represented by independent circular Gaussians h. In the canonical trial basis, with s^2=alpha and c^2=1-alpha, the branch solves mu=s h_1/(s h_1-c h_(m+1)) and z_j=s h_j/h_(m+1). The square mass matrix is invertible a.s.; the m-1 invariant directions and the distinct root account for the entire pencil. Rotating (h_1,h_(m+1)) gives independent Gaussian numerator and denominator for the centered, scaled root, with radial squared density (1+t)^(-2); beta integration verifies the moment threshold and constants. The Rayleigh quotient is alpha/[alpha+(1-alpha)U], where U=|h_(m+1)|^2/sum_(j=2)^(m+1)|h_j|^2 is Beta(1,k). Its decreasing transform gives the stated CDF; integrating via t=1-U gives the finite-sum mean and harmonic correction. Since kU converges to Exp(1), the transition and positive-limit mean follow; the median is at least k alpha/(k alpha+log 2), proving necessity even along nonconvergent subsequences. The probability-to-mean equivalence uses boundedness. These arguments apply only on the stated open angle range and fixed-confidence quadratic accuracy does not control mean risk. The supplied checker was not executed; analytic reconstruction is the evidence, not independent attestation in the package.

## originality

FAIL

A separately asserted principal exact law of the frozen finding is already the complex square-sketch case of the October 12 invariant-spectator theorem, including the centered moment formula and divergence. The refined Beta law, exact mean loss and dimension-angle threshold are not covered by that source and could motivate a narrower statement; this does not validate the frozen package's presentation of the unrefined exact law as part of its distinct contribution. No repaired finding is submitted.

## value

PASS

Independent of the unrefined-law overlap, the refinement model exposes a real gap between fixed-confidence quadratic accuracy and unconditional mean error, with an exact dimension-angle consistency criterion. These quantities can inform sketch dimension and risk interpretation; the standard Gaussian-ratio identity alone is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
