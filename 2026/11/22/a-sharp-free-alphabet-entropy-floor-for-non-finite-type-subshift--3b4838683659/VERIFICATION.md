---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For each arbitrarily long minimal forbidden A-word of length n, splice two points of X realizing its prefix and suffix on their common overlap. The resulting z contains the obstruction but agrees with a point of X on each half-line through the overlap. Every forbidden block of z must cover the whole obstruction, giving at most ℓ−n+1 starts at length ℓ. Any word in any generator of the product must have an absent A-projection, since B is completely free. For a uniform independent B-coordinate the union over all matching events has probability one, so 1≤Σ_{ℓ≥n}(ℓ−n+1)|H_ℓ|q^(−ℓ). If the generating-list rate were below log q the right side would be bounded by tails of a convergent exponentially weighted series, contradicting arbitrarily large n. Lifting all banned words by all B-words proves the upper bound, with the −∞ convention and the SFT boundary preserved. In the source example 3 is right-absorbing and 2 left-absorbing: any point containing both would contain 2u3^(|u|²+1) for a nonempty binary gap u, or the forbidden adjacent pair 23. Thus the two-sided language really is the union of the 2-prefix and 3-suffix binary families. Their sizes give 3·2^n−2; the minimal words 2u3 give rate log 2, and the sparse quadratic-length list gives generating rate zero (a non-SFT cannot have negative generating rate). Language and minimal-forbidden counts scale exactly by q^n, giving the triple. VERIFICATION.md and check.py were inspected, not executed. Their finite checks do not replace the arbitrary-generator argument.

## originality

PASS

The arbitrary-generator lower bound for adding a free full-shift coordinate is the distinct claim. The entropy definitions, source example and its base entropies, and the antecedent upper-bound lifting method are credited to Wu and Zhang. The exact product triple includes a genuinely new forced generating entropy, not new base-system counts.

## value

PASS

An unrestricted independent coordinate raises the best possible forbidden-description rate to a sharp positive floor for every non-SFT base, even when the base has zero generating entropy. This universal obstruction to recoding the product by sparse decorated forbidden patterns is not supplied by the usual product-language count. Its exact sharp family and the SFT contrast make the result useful when interpreting the generating-list entropy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
