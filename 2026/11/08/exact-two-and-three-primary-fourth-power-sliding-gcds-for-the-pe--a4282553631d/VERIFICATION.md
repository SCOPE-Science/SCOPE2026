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
# Verification of the exact local fourth-power GCD formulas

Use `python3 verify.py` (Python standard library only). The reproducible output is stored verbatim in `verification_output.txt`: the coefficients of the quartic block polynomial and `CHECKED_CASES 2700`, ending in `TWO_THREE_ADIC_CHECKS_PASS`. The finite tests cover both sequences and all lengths \(1\le k\le300\) using twelve windows each, as well as 2100 congruence checks from lengths \(4m\) with \(1\le m\le150\) and seven starting indices per sequence.

The proof in `RESULT.md` is the evidence for arbitrary lengths, and includes exact integral polynomial expansions, the operator binomial identity, divisibility lifting, explicit witnesses for sharp valuations, and residue-class arguments for nonmultiples of four. Finite tests do not establish an infinite theorem and are not used to fill any logical gap. Other prime parts of the gcd are not determined. No independent audit has been performed.
