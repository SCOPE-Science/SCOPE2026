---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Gaussian radial factorization independently recovers the sphere moments. For a standard Gaussian vector G, the quadratic-form generating function is det(I−2zA)^(-1/2), and inserting (u·G)^2 multiplies it by uᵀ(I−2zA)^(-1)u. Dividing the resulting moments by the appropriate radial moments and using tr(A^4)=(tr(A²))²/2 gives the frozen mixed and pure terms. Odd-parity terms vanish. For each eigenvalue λ, the remaining two eigenvalues contribute at least λ²/2 to tr(A²); equality forces both equal. The real deficit and optimizer s/(s+t)=15/32 follow, and alignment with the unique simple eigenline is necessary since both degree energies are positive. On that axis the normalized linear and P2 coefficients are the square roots of 3·15/32 and 5·17/32; sign and phase are absorbed by axis reversal and scaling. In the complex case Cauchy–Schwarz forces squared real and imaginary parts to be proportional when both are nonzero. The sphere is connected and the parts are real analytic, so the product of the sum and difference being identically zero forces one factor to vanish identically. This exhausts equality. Independent symbolic moment and square completion checks replay with `python /workspace/replay_frozen_reviews.py 1`; those calculations verify identities, not the equality logic by enumeration.

## originality

FAIL

The distinct indexed result c4d958a1c378 exactly covers the real upper endpoint, the same deficit, and its equality spectrum on the identical normalized real band. The complex bound and all its equality cases then follow mechanically by Cauchy–Schwarz and analytic proportionality. This is a finding of equivalent coverage in the inspected corpus, NOT a finding that the other record has earlier priority: its listed date is 2026-11-08, after the frozen record. The inspected older single-degree papers and records do not establish earlier priority for the mixed result.

## value

FAIL

The sharp finite-band problem and axial rigidity are themselves mathematically useful. As a distinct contribution against the inspected corpus, however, the reproduced real theorem has no independently useful complex remainder: the full upper statement including equality follows by ordinary complexification on analytic real functions. Narrowing to the complex case alone does not repair that overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
