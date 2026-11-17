---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

All base vertices of B^m and apex are exposed. Total covariance gives Cvert=diag(0,t/(t+1) I_m tensor Sigmav)+t/(t+1)^2 w w^T, and volume height Beta(1,d+1) gives analogous weight (d+1)/((d+2)^2(d+3)). The perturbation norm a(1+m||z||^2)->0; Schur complement bounds smallest eigenvalue between a[1-O(ma)] and a. Hence top ->lambda_max(Sigma), min~a: exponential versus d^2. Independently computed exact m=2 B=[0,1] vertex covariance, matching to machine precision 5.6e-17, and volume covariance positive definiteness; this finite check does not prove the general limit.

## originality

PASS

The complete examined cotree theorem gives volume moments for cograph stable-set polytopes, but neither vertex-uniform covariances nor a universal arbitrary-base product-pyramid spectral ratio. General product/body beta facts are classical; the two-measure sharp asymptotic ratio is not a corollary of the reviewed earlier claims. Best-of-knowledge only, given uninspected generic pyramid-moment literature.

## value

PASS

The universal sharp contrast between two common sampling schemes on a geometrically natural repeated-product pyramid, and its explicit clique-windmill stable-set polytope specialization, gives a motivated spectral conditioning invariant; not merely recomputation of a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
