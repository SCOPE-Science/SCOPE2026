---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For all n>=2, tracefree symmetric A and real b, diagonal Gaussian cumulants give E F²=2tr A²+||b||² and E F⁴=3(E F²)²+48(tr A⁴+bᵀA²b). The zero-sum spectrum has sharp fourth-power bound ν_n=(n²-3n+3)/(n(n-1)) and maximum eigenvalue square bound β_n=(n-1)/n. The proof handles n=2,3 separately and excludes three-valued maximizers at n>=4 by constrained second variation; the remaining two-level patterns maximize at one outlier. A Rayleigh quotient bound and exact square completion in ρ=||b||²/(2tr A²) force the claimed constant and for n>=3 the positive linear/quadratic energy ratio (n-2)/(n-1)² with principal-direction alignment. I independently verified the rational scalar remainder for symbolic n and boundary cases; finite exact Gaussian checker is corroborative only.

## originality

PASS

The zero-sum spectral fourth-power lemma and Gaussian fourth cumulant are known ingredients, but their sharp joint optimization on the canonical first Gaussian plus tracefree-second-harmonic space, mandatory mixing for n>=3, and explicit three-component deficit are not established by the inspected prior theorems.

## value

PASS

The direct sum of first Gaussian chaos and tracefree harmonic quadratic Gaussian chaos is canonical. Its exact sharp norm, forced nonzero linear mixing for n>=3, explicit energy allocation and spectral/directional/energy deficit decomposition solve a natural complete mixed-degree norm problem not furnished by general hypercontractive bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
