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

# Verification procedure and scope

The self-contained `verify.py` requires Python 3.9 or newer, with only the standard library. Execute `python3 verify.py` in the containing directory.

It verifies that (i) the sorted-gap algorithm reconstructs the same full BWT string as independent lexicographic rotation sorting for every nonnegative rooted gap triple of sum at most \(35\), excluding the all-one exceptional word; (ii) the adjacency-based classification and exact gap-level census hold for every such triple; (iii) direct indexed-word enumeration gives the predicted two-, four-, and six-run counts for lengths \(4\) through \(23\). Actual output:

```
GAP_BWT_AND_CLASSIFICATION_OK 8435
INDEPENDENT_INDEXED_WORD_CENSUS_OK 10625
ALL_CHECKS_PASSED
```

The full proof is in `RESULT.md`; finite verification does not certify it for all lengths. There are no external datasets, hidden package files, random seeds, symbolic algebra dependencies, or external proof obligations. No independent audit has been carried out.
