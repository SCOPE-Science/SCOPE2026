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

The theorem is proved from the even-subset theta-characteristic correspondence, the classical cardinality of Aronhold heptads, an explicit equivariant graph parametrization, and the invariant-three-subset count. Its final inverse step is finite and exhaustive over the \(22\) partitions of eight.

Reproduce the arithmetic classification with `python3 verify_aronhold.py`, which requires only Python's standard library and `aronhold_22_types.csv` in the same folder. The program checks that the \(288\) graph configurations coincide exactly with heptads obtained from the odd-theta triple criterion, checks all \(22\) Frobenius permutation actions and their power-fixed counts, and reproduces the \(12,19,21,22\) prefix-signature sequence. It also verifies the two polynomial constructions over \(\mathbb F_3\) by trial division.

The finite computation is a complete proof of the claimed eight-point classification when combined with the symbolic fixed-count formula; it is not an argument about all finite sets, higher genera or uniqueness in the literature. The embedded data and code have received a self-review, not independent validation.
