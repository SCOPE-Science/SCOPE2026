---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The final newly seen symbols of successive greedy complete arches form a test subsequence whose earliest embedding reaches the arch boundaries; appending a letter missing in the remainder proves the greedy index bound, including no complete arches. For the palindrome, the same terminal-symbol test from both ends forces any inserted middle test word to embed in the reflected remainder with or without the center. That core has index zero when it misses a letter and otherwise index one: in the latter case the center is the sole occurrence of the letter missing from the half-remainder, so a double of that letter is absent. Concatenating the complete arches and using this core proves the quoted index rule in all cases. First-appearance orders give the displayed A_q and R_{q,j} factors (allow repetitions between discoveries and, for remainders only, after the last discovery). For q-1 remainder symbols precisely one center contributes u instead of 1 in the residual weight. The minimum m for 2h even index is qh and yields (q!)^h half-words; for 2h+1 odd index the minimum half-length is qh+q-1 with forced center and (q!)^(h+1) choices. The candidate minima increase strictly with k, so the at-least-k formulation gives the same extremals. Under uniform sampling of the half, the iid arch intervals are coupon-collector times with the stated mean and variance and exponential tails. The finite-moment renewal mean, variance and inverse-sum CLT apply; doubling N(floor(n/2)) multiplies its variance by four, and an extra term in [0,1] changes variance by at most O(sqrt(n)) and does not change the scaled limit. At q=2 this gives 4/27. The supplied exhaustive finite checker and its recorded scope were inspected, not run; the independent arch and renewal argument settles the general claim. No uniformity in growing q is established.

## originality

FAIL

The central claimed enumeration is already represented exactly in a distinct indexed result as a pair of even/odd series. The finite extremal lengths and multiplicities are immediate coefficients of those series. The explicit Gaussian limit is not stated in the compared finding, but follows by standard iid renewal asymptotics from its half-word arch representation and the bounded midpoint correction; it does not establish a distinct nonroutine contribution for the record as submitted. This is a scientific coverage finding, not a claim that the matched record predates the frozen result or that one was derived from the other.

## value

PASS

The mathematical question is worthwhile: the joint law for this natural symmetry-constrained word class gives meaningful extremal and typical statistics, including a fluctuation comparison with uniform unconstrained words. This is the value of the full profile as mathematics, not an independent contribution of the standard renewal CLT alone or a reason to discount the demonstrated exact overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
