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
# Computational and deductive verification

The complete proof establishes the theorem for arbitrary finite state sets and finitely many independent atomic predicates. The required nonstandard step is that a maximal nonrobust signature block must contain a negative example, and that one negative in each such maximal block covers every lower nonrobust signature. The proof derives this from the exact subbase minimal-neighbourhood identity.

Run `python3 verify_robust_cores.py` with standard Python. The program independently (a) enumerates all labelled topologies through four states; (b) checks the exactness criterion and forcing/saturation for all two-predicate nested label datasets through four states; and (c) evaluates the proposed count from signature blocks and compares it with brute-force truth-set enumeration for all two-predicate prescribed robust families through five states.

Observed output: topology counts 1, 4, 29, 355; 7,380 nested-label datasets, 564,869 admissible topology comparisons, 4,194 incompatible datasets and 8,454 extra forced positive label occurrences; all checks pass. The exact count agrees on 1,364 prescribed robust-region pairs through five states. Finite computation is corroboration and is not used as a proof for unbounded state or predicate counts. The theorem does not address priorities in unindexed sources.
