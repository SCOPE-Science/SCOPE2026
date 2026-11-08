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

# Finite proof replay

`python check_order_certificates.py order_certificates.json` reconstructs each of the five complete decision trees from its embedded JSON and verifies the exact permutation witness for **every** leaf. The program checks tree shape, all comparison signs on every root-to-leaf path, pair-domain validity, witness distinctness, the expected leaf and internal-node counts, and the strict counting upper bound for one additional level.

`python build_order_certificates.py` rederives the certificate using exact minimax memoization over the entire finite concept family for each label count from two to six; it reports memoization-state counts 3, 19, 219, 4231, and 130023 respectively. This is exhaustive finite construction and not an infinite-parameter certification.

Observed executed output is saved in `order_verification.txt`. No external audit, randomized approximation, or proof assistant was used. The forest characterization and the cardinality upper bound are proved mathematically in RESULT.md.
