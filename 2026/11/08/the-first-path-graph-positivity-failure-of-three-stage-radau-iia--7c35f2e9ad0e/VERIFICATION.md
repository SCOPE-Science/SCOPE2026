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

The completed [2/3] Padé step uses P(hL)/Q(hL), with Q positive on the nonnegative spectrum of the full path Laplacian. In a spectral basis, det(Q) times this step has eigenvalues P(h lambda_j) times the product of all other Q factors. The unique zero Laplacian eigenvalue shows the degree is at most 3(n−1) both for the zero mode and for each nonzero mode. Independent replay with python3 /workspace/reproductions/3.py (SymPy) reconstructed every numerator from exactly 3(n−1)+1 integer evaluations using exact determinant/inverse arithmetic and Newton interpolation, rather than the frozen log-trace recurrence. It confirmed nonnegative coefficients and a positive coefficient for every entry after the stated degree elevations for n=2 through 13. Degree elevation uses a strictly positive factor and proves the full positive-real-step assertion, not just positivity at the interpolation nodes. T_n(0)=I and L_1=0 handle the endpoints. A separate bordered determinant at n=14 and h=5/2 gives exactly the stated negative fraction. No larger sizes, Dirichlet restriction or stage signs are inferred.

## originality

PASS

Best-of-knowledge pass for the exact all-step cutoff on symmetric unit-weight full paths. The strongest inspected related indexed findings change the rational map or graph family/generator. No distinct exact match or dominating theorem was established. Some historical primary text could not be retrieved, a limitation rather than negative evidence.

## value

PASS

An unweighted path is the canonical conservative finite diffusion test with no boundary killing. The completed step's positivity determines whether nonnegative data can become negative even on this minimal kind of domain. The exact 13/14 boundary and strict all-step positivity below it are useful sharp facts not supplied by generic positivity restrictions or failure on a different generator. The finite certificates settle the invariant for real h, not just representative step sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
