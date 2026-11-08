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

The mathematical assertion is the combined weighted-census and edge-spectrum theorem for all positive integers \(m,n\) and finite reflexive chains. The proof establishes (1) equivalence between confluence quantifiers and antitone minimum profiles, (2) a non-overlapping partition of admissible matrices by compulsory and optional cells, (3) explicit edge-by-edge realizations of every intermediate cardinality, and (4) universal entropy bounds.

Reproduction: run `python checker.py` using Python 3. The script contains independent direct checks of the two confluence quantifiers, direct brute enumeration of every matrix shape with both dimensions at most four, coefficient-by-coefficient comparison to the weighted formula, and construction checks of the edge-size realization chain. Output: `FULL_CHECKS_OK`. No external dependencies.

This finite replay is a consistency check, not an exhaustive proof in unbounded sizes. In particular, the entropy bounds and exact spectrum are proved symbolically. Originality comparisons are limited by absence of the full text of three closest indexed published records. No independent audit has been performed.
