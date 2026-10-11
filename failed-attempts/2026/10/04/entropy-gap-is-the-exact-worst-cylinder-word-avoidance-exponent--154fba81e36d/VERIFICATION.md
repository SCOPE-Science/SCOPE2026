---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The avoidance language is factorial and its counts are submultiplicative, so their exponential growth rate is the survivor entropy. Entropy minimality makes the gap positive when the survivor is nonempty, while compactness forces eventual emptiness when it is empty. The empty word realizes the global avoidance ratio inside each follower/predecessor supremum; the bi-balance lower bound on every follower/predecessor denominator gives the matching upper constant factor. For an invariant Gibbs measure, each conditional cylinder ratio is bounded by the quotient of the Gibbs estimates, and the empty history supplies the matching lower bound. The claim correctly excludes occurrences straddling the conditioning boundary.

## originality

FAIL

The assigned theorem is mathematically correct, but its substantive combinatorial content is a direct constant-factor extraction from Hong–Kim Lemma 4.9's published proof. That proof already introduces the same factorial avoidance language \(D\), identifies its survivor shift, obtains the strict entropy gap, and compares \(|D_n|/|\mathcal B_n(X)|\) with the same uniform follower/predecessor balance constant. Retaining the exact submultiplicative entropy limit and using the empty history supplies the two-sided exponent with no new structural lemma. The Gibbs conditional extension is likewise the immediate cylinder-by-cylinder application of the invariant Gibbs inequality already available for bi-balanced shifts. Under the required implication/corollary standard, this is covered even though the exact exponent is not stated as a named theorem.

## value

FAIL

The entropy gap is a natural recurrence scale, but in this package the exact exponent and Gibbs conditional version require only retaining the exponential rate in the very same avoidance proof and applying the standard Gibbs cylinder inequality. No new structural mechanism, boundary, classification, or nontrivial comparison beyond the source's argument is needed. Under the shared value bar this is a routine quantitative corollary of the initiating proof rather than an independently valuable result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
