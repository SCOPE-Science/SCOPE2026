---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Productive updates have P(K->K±e_i)=K_i/(2M) for M=sum leaf counts until absorption. The aggregate M is a fair gambler ruin chain. Pathwise predecessor sums preserve equal mass on positive count vectors conditional on aggregate trajectory; extinction cannot reverse. Product H=prod_i K_i is bounded harmonic martingale and its optional-stopping expectation is one. The weighted composition sum [z^n](z/(1-z)^2)^r=binom(n+r-1,2r-1) normalizes each positive terminal probability. Independent exact rational Markov-chain calculations on (r,n)=(3,4),(3,5),(3,6),(4,5) agree. Unlimited result relies on pathwise proof, not these cases.

## originality

FAIL

The 2026-10-25 full published primary theorem on the identical productive/unproductive EdgeVOG star, identical initial counts and any d>=2, n>=d+1 already proves each positive terminal composition has (n-d)!(2d-1)!/(n+d-1)! = 1/binom(n+d-1,2d-1), the same all-survive probability, conditional uniformity and even a Dirichlet limit. Setting d=r>=3 exactly matches every submitted final claim. Different proof via product martingale cannot rescue originality. Strong coverage is decisive.

## value

FAIL

The full joint terminal law and all its stated consequences were already established for a broader range of star degrees in the 2026-10-25 theorem. The submitted product-martingale proof is elementary and useful pedagogically but provides no additional natural invariant, cutoff, boundary, or nontrivial improvement beyond the complete known formula. Its verification alone is not sufficient value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
