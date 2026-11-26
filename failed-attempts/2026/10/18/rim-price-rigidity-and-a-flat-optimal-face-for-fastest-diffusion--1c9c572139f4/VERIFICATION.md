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

An independent spectral dual check uses the trace-one normalized projector Z_F on the first real Fourier plane (the plane's projector divided by two). Its quadratic edge strains are 1/n on spokes and c_n/n on rims. The trace-one projector Z_H onto the hub-versus-rim line has strains (n+1)/n and 0. A trace-one positive dual test on the constant-orthogonal subspace upper-bounds lambda_2 by tr(ZL). For t<c_n mix Z_F with coefficient (n+1)t/(c_n+nt) and Z_H with the remaining coefficient; strains are proportional to the prices and give the claimed value. For t>=c_n use Z_F alone, giving B/n and excluding positive rim weights when t>c_n. The uniform Laplacian has hub contrast eigenvalue (n+1)a and first rim eigenvalue a+c_n b, so the stated weights attain each bound. At equality the first harmonic lies in the bottom eigenspace of the constant-orthogonal restriction (the dual gives it positive weight in every regime). The imaginary part of its rim eigenvector equation forces equal rim weights because sin(2pi/n) is nonzero for n>=3. The real part then forces equal spokes. At equality of prices the remaining hub bound is precisely (n+1)a>=B/n. This covers the triangular rim and the full closed critical segment. The segment is an exposed optimal face of the lifted semidefinite problem, not a face of the weight-budget simplex itself.

## originality

FAIL

The main claim, including the critical interval and exclusion of asymmetric optimizers, is covered for n>=4 by a distinct indexed theorem. The sole extra case n=3 is obtained by the same argument verbatim: the rim Fourier vectors are independent with squared norms 3/2 and sin(2pi/3) is nonzero. Neither inverting the relative price nor restoring a budget scale creates a different mathematical result. No priority or provenance claim is needed for this coverage determination.

## value

FAIL

The unrestricted optimizer classification and critical segment would be valuable in their own right, but the assigned contribution beyond the covered result is a price/budget renormalization and the triangular rim. That case is K4 with a designated hub and costs, and the prior proof applies with no new constraint, degeneracy argument or mechanism. No distinct motivation or result for that boundary case is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
