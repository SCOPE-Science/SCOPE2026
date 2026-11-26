---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For g=X+pQ and nonzero displacement d of valuation v, the first p iterates differ from the starting point by id modulo p^{v+1}. Taylor expansion, divisibility of the sum of i by odd p, and 2v+1≥v+2 give g^p(x)-x=pd modulo p^{v+2}. The argument iterates, and a prime-to-p iterate does not raise the valuation. The quadratic map is bijective by its difference factor 1+p(x+y). Consequently the number fixed by the p^t-th power is p^{t+1}R_{L-t}; successive differences divided by p^t give the exact primitive-cycle counts. The valuation and simple unit-root lift give the stated strata; the first level beyond the smaller valuation distinguishes types, and the triangular map recovers the root-count vector, including at N=2. Conditional counting of possible lifts makes R_j a martingale. The invertible change (x−y,x+y) reduces the second moment to uv=0; each of the j nonzero-u valuation strata contributes (p−1)p^{j−1}, besides p^j for u=0. Thus the martingale increments have common variance b and are orthogonal. In the form C_t=(p−1)R_{L−t}−(R_{L−t+1}−R_{L−t}), these facts give precisely the variance, covariance and strict sign formulas, with C_0=pR_L. Haar root counts stabilize except at a=0, a null event; the square-unit strata provide the listed masses. The nonzero masses sum to p/(2(p+1)), their weighted first moment is p−1, and each contributes the same positive amount to the second moment.

## originality

PASS

The supported distinct contribution is the valuation-stratified distribution of cycle vectors, complete cross-parameter covariance and common stabilized law for this family. Individual periods, quadratic root lifting, and standard martingale identities are not new. The bounded statement-level comparisons do not establish priority, but identify no prior result covering the combined parameter statistics.

## value

PASS

The natural quadratic near-identity family is fully classified across its shift parameter, not only along an individual orbit. In particular the strictly negative correlation with the longest length versus strictly positive shorter-length covariances is not implied by the marginal mean or by the deterministic local period law. The common Haar limit with infinite second moment explains the exact variance growth despite almost-sure stabilization, giving a useful benchmark for parameter ensembles and for distinguishing levels from limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
