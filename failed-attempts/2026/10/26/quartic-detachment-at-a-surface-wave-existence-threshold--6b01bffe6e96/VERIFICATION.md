---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

FAIL

FAIL: The reviewed RESULT.md asserts that the exact normalized determinant equals beta*gamma*(gamma²−beta²)=alpha²*xi⁴ and derives beta=(xi⁴/gamma0³)alpha²+O(alpha⁶), Vsurf−Vbulk=−(cs*xi⁷/(gamma0⁶ S'(k0)))alpha⁴+O(alpha⁸). The cited Gourgiotis–Georgiadis arXiv:1509.06590 Eq.(40), visually verified on page 16, actually gives beta*(ell² gamma²−abar3 xi²)²−gamma*(ell² beta²−abar3 xi²)²=0. Its Eq.(56) defines alpha=abar3/ell². The exact reduction (for beta≠gamma) is beta*gamma*(gamma²+beta*gamma+beta²−2alpha xi²)=alpha² xi⁴, NOT the audited determinant. For fixed characteristic-root functions S,T as stipulated in the audited proof, gamma=gamma0+O(beta²) and beta=(xi⁴/gamma0³)alpha²+(2xi⁶/gamma0⁵)alpha³+O(alpha⁴). The cubic coefficient is nonzero for xi,gamma0>0. Squaring to obtain k-k0 consequently generates a nonzero order-alpha⁵ phase-speed correction. Thus both O(alpha⁶) and O(alpha⁸) remainders in the *submitted final claim* are false. An independent symbolic expansion of the source determinant confirmed the missing order-alpha³ term (when cubic beta is omitted, the determinant has coefficient −2xi⁶/gamma0 at alpha³). The leading quadratic beta and quartic speed coefficients may survive after substantive repair, but no complete corrected research files and renewed final claim were supplied.

## originality

FAIL

FAIL for the submitted final claim: the source Toupin–Mindlin dispersion determinant is already published as Eq.(40), and the asserted replacement is not equivalent to it. The leading physical coupling coefficient is not explicitly listed in the inspected source, but the purported *exact* determinant and asserted higher-order error bounds are incorrect; there is no valid original all-orders statement to accept as presented. Any novelty judgment for a properly corrected leading-term theorem would require a different final claim and all amended files.

## value

PASS

The question of how the decay exponent and phase-speed gap detach at a simple physical surface-wave threshold is mathematically and physically motivated, and a true leading-order quadratic/quartic law would be valuable. This V assessment does not validate the false remainder estimates, and cannot override C/O failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
