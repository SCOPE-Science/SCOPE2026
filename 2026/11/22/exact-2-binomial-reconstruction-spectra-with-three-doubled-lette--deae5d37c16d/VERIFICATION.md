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

# Verification record

The mathematical certificate is the finite six-row table in `RESULT.md`, independently recomputed in `verify_spectrum.py` from all \(90\) distinct six-position ternary words and all \(2^5\) interior cut sets. It records the full key of ordered nonempty-gap Parikh tuples and the three ordered core pair counts, checks every fiber cardinality and source mass, and verifies the closed formulas via exact polynomial arithmetic. This enumeration is exhaustive over the **finite** base object; the proof separately establishes a bijection from arbitrary marker words to marker order, selected nonempty gap positions, and the finite certificate's classes.

The second program `verify_independent.py` directly generates actual marker-augmented words in a fixed marker order and computes the entire vector of length-one and length-two scattered-subsequence counts. It checks fiber spectra for \(r=0,1,2,3,4,5\) without using the finite table.

Executed checks: both programs completed with their PASS outputs. These checks establish the finite lemma and confirm the independent implementations; the all-\(r\) conclusion depends on the proved marker decomposition and symbolic binomial-sum identity, not on testing finitely many \(r\).

Restrictions: exactly three doubled core letters, each additional marker unique; labeled linear words; full scattered two-deck. No external independent audit has been performed.
