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

The weighted Laplacian cofactor Schur complement gives the product degree enumerator. The unit-current equations give R_uv=1/(x_uY)+1/(y_vX)-1/(XY); multiplying by x_u y_v and the total degree polynomial splits the weighted tree sum by membership. After shifting the degrees by one and normalizing the two positive event masses, both PGFs and the three-atom coupling follow, valid also when either binomial has zero trials. Conditional on the atoms U,V, the independent binomial noises eliminate conditional cross-covariance and the two conditional means are affine in U and V. Their slopes are the asserted expected differences; Cov(U,V)=-(a-1)(b-1)/(a+b-1)^2. Every increment has positive binomial weight, proving strict sign for nonconstant nondecreasing functions on the full support. For a=b=r the binomial variance tends to 1, the binary increment variance to 1/4, and the covariance to -1/4, giving correlation -1/5. Independent bounded replay (python3 /workspace/branches/reproduction/tree.py) separately computes full and deleted weighted Laplacian cofactors by fraction-free elimination and verifies both normalized PGFs at 64 rational evaluations; the exact algebra, not finite testing, proves the laws.

## originality

FAIL

The complete edge-present degree law is an exact distance-one specialization of the earlier Resultary path-conditioned law. Both factored edge-condition laws also follow immediately from the 2004 weighted Ferrers tree enumerator applied to the complete rectangle and the same rectangle with its final corner removed. Reading the three coefficients of the residual binary PGF gives the coupling, and conditional covariance with independent noises and binary increments gives the nonlinear rank-one identity by an affine two-point calculation. The failure is demonstrated prior coverage and direct implication, not incorrectness or an inaccessible-paper concern.

## value

FAIL

The conditional independence switch and nonzero limiting conditional correlation are interpretable, but the claimed precise invariant is already determined by the earlier weighted Ferrers formulas and path law. The binary coupling, arbitrary-function covariance and balanced limit add routine coefficient and moment calculations, not a distinct structural lemma, boundary or useful new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
