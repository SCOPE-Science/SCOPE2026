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

Parking validity is invariant under permuting the entries of the preference word, so the conditional distribution is uniform over all words with the given labelled counts. Prescribing r distinct diagonal matches samples distinct labels from that multiset, giving factorial moment r!e_r(c)/(n)_r. Pollak's unique circular representative preserves the number of colliding preference pairs, yielding E sum c_j²=2n²/(n+1). For iid samples from the probabilities c_j/n, the complement of the all-distinct event has probability at most binom(r,2) sum c_j²/n². This establishes every fixed conditional factorial-moment limit on any deterministic sequence with sum c_j²/n²→0; Poisson moment determinacy and tightness give weak convergence, which is TV convergence on the nonnegative integers by finite-set truncation. Markov's inequality, the subsequence criterion and boundedness of TV then give convergence in expectation without any simultaneous moment requirement as r grows. Conditioning the joint probability on the histogram bounds the error by that expectation, uniformly over the two events.

## originality

FAIL

The earlier October 18 exchangeable-mapping result already covers the same conditional law for every complete labelled indegree profile and proves a stronger TV classification. Classical Pollak occupancy ensures that the diffuse-profile condition holds in probability for parking functions. The expectation and decorrelation statements follow directly from the bounded deterministic TV conclusion. This is verified prior implication, not an inference from marginal parking-function results or a lack of access.

## value

FAIL

Conditional decoupling from a growing labelled vector is meaningful in isolation, but in this case it is the diffuse-profile case of the known complete classification, plus a classical occupancy moment and conditioning. The frozen claim adds no distinct quantitative estimate or new mechanism for the parking model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
