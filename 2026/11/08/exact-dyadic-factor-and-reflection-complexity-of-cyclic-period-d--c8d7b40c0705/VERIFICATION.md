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

# Reproducible checks

Run `python3 VERIFY.py` (Python standard library). It independently computes the valuation word from integer indices and compares finite-prefix factor sets against exact template factor sets for \(2\le m\le5\) and \(1\le k\le5\). In all \(56\) pairs \((m,k)\) with \(2\le m\le8\) and \(1\le k\le8\), it checks the complete collision multiplicities and exact opposite-center pair list, full factor count, reversal closure, palindromic count and reflection orbit count. In the \(20\) finite-prefix cases it tests set equality rather than comparing only cardinalities.

Expected output: `ALL 56 exact collision, formula, palindrome, reversal cases passed; 20 independent finite prefix comparisons passed.`

These computations are checks at bounded \(m,k\), not a proof of the universally quantified result. The infinite proof follows from the valuation identities, exhaustive center representation and witness-offset collision lemma in `RESULT.md`. No external audit was performed.
