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

# Reproducible verification
Run `python3 artifacts/verify.py` with Python 3 and no third-party dependencies. Actual replay checked all 256 four-column states, all transitions satisfying the two cubic crossing-degree constraints, exactly four cyclic strongly connected components of sizes \(1,1,5,5\), and internal successor and predecessor uniqueness. It verified every proposed optimum set for \(5\le n\le150\) and, independently of the transition graph, enumerated all \(n\)-vertex subsets of \(GP(n,2)\) for \(5\le n\le10\). The exact optimum counts were \(12,2,2,2,2,12\) for these six lengths.

The exhaustive 256-state lemma, combined with the mathematical equivalence between cyclic words and closed walks, proves the unrestricted classification. Direct bounded enumeration is corroborative only. General published structural lemmas and the distinction between \((1,2)\)- and \([1,2]\)-domination are documented in the finding. Historical priority and independent audit have not been established.
