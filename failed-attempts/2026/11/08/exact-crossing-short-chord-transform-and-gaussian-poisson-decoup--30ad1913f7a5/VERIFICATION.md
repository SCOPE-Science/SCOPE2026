---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For every n>=2, any selected matching F of k nonincident cycle-boundary edges is crossing-neutral; deleting its endpoints preserves circular order and induces unrestricted matchings on 2(n-k) endpoints. Count F by M_{n,k}=2n/(2n-k) binom(2n-k,k), double count marked simple-edge subsets and expand t^S by binomial theorem. Normalizing gives factorial moments and from k=1,2 the exact covariance/correlation. For fixed k factorial coefficients tend to 1/k! and are bounded by 2/k!, so the published crossing marginal CLT plus dominated convergence yields independent N(0,1) and Pois(1) limit. Separately enumerated n=2..7 complete matchings and verified all deletion coefficients and finite moments by exact arithmetic.

## originality

FAIL

The October 18, 2026 published full factorial-deletion theorem already gives exactly the assigned cycle-matching transform, Corr=-sqrt(5/(n+3)) and independent Gaussian-Poisson limit for the same circular simple chords. The November 2 publication independently repeats the identical complete bivariate transform and adds the conditional no-simple-chords Gaussian consequence. The submitted unnormalized enumerator is the earlier normalized PGF multiplied by (2n-1)!!, since the normalized coefficient is M_{n,k}(2n-2k-1)!!/(2n-1)!!.

## value

FAIL

Complete mixed crossing/simple-chord enumerators are highly natural and valuable in principle, but the submitted transform, covariance and asymptotic decoupling exactly repeat two previously published results. Formatting the full integer enumerator instead of a normalized PGF does not make new mathematical content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
