---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical reproducibility

Run `python3 check_bell7.py` in the same directory as `gap_histogram.csv`, using stock Python 3. The checker (1) verifies modular-polynomial exponent identities, (2) derives the Bell sequence from the seven initial values and Touchard's congruence, (3) verifies all seven consecutive residues at the proper candidate shifts, (4) evaluates every one of the \(137257\) cyclic positions, (5) reproduces every positive gap count in `gap_histogram.csv`, and (6) cross-checks the same zeros with a separate seven-state sliding traversal. It checks the exact total and weighted gap count, the unique maximum at start index \(85736\), and the forbidden gap seven.

Expected output: `CHECK_OK period= 137257 zeros= 19608 gap_types= 50 max_gap= 65 unique_max_start= 85736 gap_total= 19608 weighted_gap_total= 137257`.

These finite calculations are exhaustive for the entire period, not sampled. Their global consequence depends on the exact period identity given in `RESULT.md`. The theorem applies to ordinary Bell numbers modulo seven; the full histogram is a computed finite invariant and no general formula over varying primes is certified. Independent review has not been performed.
