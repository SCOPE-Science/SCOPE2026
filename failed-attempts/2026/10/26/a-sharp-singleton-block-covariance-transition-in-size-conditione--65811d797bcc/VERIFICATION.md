---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Kreweras block-profile enumeration gives exactly the same multiset-of-part-sizes law as a uniform ordered positive composition of n into k parts. Marking a size-s part gives p_s=C(n−s−1,k−2)/C(n−1,k−1); under its size bias the other k−1 parts have n−s total and singleton mean (k−1)(k−2)/(n−s−1). This produces the asserted covariance k(k−1)p_s[ks−2(n−1)]/[(n−1)(n−s−1)] and sign crossing. Fixed-s binomial-ratio asymptotics give the density limit. Independent exhaustive noncrossing partition enumeration for n=5..8 reproduced conditional covariances. Correctness is established but does not establish originality relative to the stronger prior joint profile distribution.

## originality

FAIL

FAIL: Kreweras 1972 complete exact block-size profile enumeration, explicitly recalled as Arizmendi 2012 Proposition 1.4, is stronger than the proposed conditioned covariance. The source proof differentiates/marks that very distribution and performs a routine subtraction to obtain factor ks−2(n−1). This is a readily implied numerical corollary, not independent mathematical originality merely because the sign threshold is not written verbatim in a prior title.

## value

PASS

The natural conditioned noncrossing ensemble exhibits a sharp covariance sign reversal, including zero but dependent cases and a density limit. This gives a meaningful qualitative boundary, even though the exact conditional profile distribution is classical and the derivation is short.

The dated certificate retains the supplied scientific assessment, sources and limitations.
