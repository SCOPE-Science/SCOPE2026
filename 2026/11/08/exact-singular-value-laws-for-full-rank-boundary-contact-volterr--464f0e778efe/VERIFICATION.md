---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

On normalized ball Bergman monomials, radial derivative contributes N and integration t^(N+k-1) gives N/(N+k); multiplication by z_(h+1)^k yields monomial norm ratio sqrt((alpha_(h+1)+k)!/alpha_(h+1)!*(N+d)!/(N+d+k)!). Distinct target multi-indices make T*T diagonal. Group transverse beta and undamped total M; each asymptotic weight is A_beta M^(-k/2) with C(M+h-1,h-1) multiplicity. Cumulative undamped count ~L^h/h! yields t^(2h/k) N(t)->(1/h!)sum_beta A_beta^(2h/k), summable by geometric transverse damping. Monotone counting inversion proves s_n~C^(1/q)n^(-1/q), sharp p>q, weak endpoint and C log n q-sum. For d=2,h=k=1,r=.5, independent cutoffs t=.05,.02,.01,.005 give scaled counts 1.6825,1.7572,1.7715,1.775925 approaching exact C=16/9. Examined frozen check.py; no finite test replaces dominated convergence.

## originality

PASS

The original Dong-Xu generalized Volterra-companion setting overlaps, and its rank-deficient projection example has a similar threshold; however the frozen claim requires nonzero full-rank transverse contractions and an all-parameter exact Weyl coefficient with damping-product and factorial series. Nearby published anisotropic all-compact family concerns epsilon->0 Schatten norm blow-up and has no undamped boundary direction at fixed epsilon. No read source establishes this full-rank exact coefficient, with residual risk from inaccessible Dong-Xu manuscript.

## value

PASS

The complete full-rank boundary-contact singular list and exact weak-Schatten coefficient quantify a natural transition between compact interior maps and boundary-touching self-maps. Critical exponent 2h/k and dependence on all damping parameters supply reproducible nontrivial spectral data beyond an illustrative cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
