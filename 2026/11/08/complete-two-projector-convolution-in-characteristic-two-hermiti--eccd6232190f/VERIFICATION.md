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

# Reproduction of the finite checks

Run `python3 checker.py` with standard Python. This script uses polynomial-basis realizations of the binary fields of sizes \(4\), \(16\), \(64\), and \(256\), whose quadratic fixed subfields have orders \(q=2,4,8,16\). It independently enumerates all rank-one Hermitian projectors by the determinant-zero equation and all their ordered pair sums, and checks the theorem at every trace-zero target. It additionally checks field inverses, projector cardinality, sumset size, the complete positive-value histogram, and exact additive energy.

Expected final marker: `HERMITIAN_BINARY_PROJECTOR_PAIR_PASS`.

The script does not establish the result for untested field sizes or check the historical originality of the theorem. Those require the symbolic proof and source comparison in `RESULT.md` and `REVIEW.md`; independent validation has not been performed.
