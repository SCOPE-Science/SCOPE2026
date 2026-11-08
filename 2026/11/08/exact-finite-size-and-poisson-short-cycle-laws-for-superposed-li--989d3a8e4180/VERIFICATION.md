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

The standalone `checker.py` uses exact fractions, exhaustive permutations, and a rotation-normalized directed-cycle counter. It independently compares the stated inclusion–exclusion expectation with full enumeration for \((n,r)=(2,1),(3,2),(4,2),(4,3)\) and every admissible \(k\). The expected success marker is `ALL_EXACT_CYCLE_CHECKS_PASS`.

The arbitrary-size formula is verified mathematically by a block collapse and two inclusion–exclusion steps. The limit is verified by joint factorial moments and the strict excess of directed arcs over vertices in overlapping-cycle patterns. These proof steps, rather than simulation or the finite tests, support the infinite conclusion. The formula assumes independent uniform spanning *paths*, not random cyclic permutations, and ignores duplicate arcs in forming the union.

No independent audit or historical-priority certification has been performed. The exact first-moment identity does not assert an exact finite-size Poisson distribution. The method covers fixed numbers of orders and fixed short-cycle lengths only.
