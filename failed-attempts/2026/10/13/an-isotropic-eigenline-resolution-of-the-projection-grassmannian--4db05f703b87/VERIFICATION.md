---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Friedman–Hoşten–Rosana Theorem 3.3 establishes the repeated-root set equality in the stated range of k. Over C, a repeated eigenvalue of a symmetric matrix has an isotropic eigenline either because its eigenspace has dimension at least two or because a Jordan predecessor u of an eigenvector v gives v^Tv=v^T(Q-lambda I)u=0. Conversely a simple root with isotropic eigenvector would give a Jordan predecessor, since the image is v-perp. Assigning a symmetric form any row and matching column in a basis beginning with v proves surjectivity of Q->Qv mod Cv. The incidence is a smooth rational kernel bundle of rank N-n+1 and dimension N-1 over the smooth irreducible quadric; the projection is proper. The discriminant is a nonempty hypersurface by the nonzero characteristic discriminant polynomial. The dense open one-double-root stratum can be defined by degree one of gcd(p,p') (a Sylvester rank condition), and defectivity on that stratum by cyclicity of Q (linear independence of I,Q,...,Q^(n-1)). The given square-zero block plus distinct simple roots lies in this open set, and there is precisely one isotropic eigenline there, proving birationality in characteristic zero. The frozen perturbation has quadratic discriminant eps^2+4i*eps and all cross-resultants nonzero at eps=0, so the irreducible support has multiplicity one. Scaling gives exact degree. The n=2 factorization is correct. The frozen finite checker was inspected, not executed; these conclusions follow analytically.

## originality

FAIL

The apparent additional geometry is covered by the classical regular-pencil criterion combined with projective conormal reflexivity. This is statement-level implication, not an inference from a search miss. On the quadratic Veronese image X of the isotropic quadric, the conormal condition for a matrix functional Q is exactly Qv in Cv; the repeated-det-root locus is precisely the dual by the two-quadric regularity criterion. The claimed affine bundle and its projection are the affine-lifted conormal resolution of that dual, not just analogous to it. The same bundle gives the reduced degree by the standard projective bundle formula. The inspected ED paper does not itself state the resolution, and no exact duplicate Resultary record was identified. Neither fact negates broader coverage.

## value

FAIL

The affine eigenline coordinates give a useful exposition of the dual geometry, but the claimed result stops at the standard conormal resolution, textbook degree computation, and two-by-two factorization. It supplies no distinct singularity, exceptional-fiber, or other geometric result beyond that specialization. Those more substantive questions are expressly outside the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
