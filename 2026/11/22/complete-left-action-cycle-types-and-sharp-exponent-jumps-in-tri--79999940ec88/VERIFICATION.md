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

# Verification of individual left-action cycle laws

The proof in `RESULT.md` provides the infinite-range result. The standalone program `check.py` supplies finite independent checks and requires Python 3 with no external libraries. Run `python check.py` and compare with `check_output.txt`.

For seven pairs of dimension and prime characteristic, it exhaustively constructs each \(a\) in the strictly upper-triangular algebra; for every \(a\), it builds \(b\mapsto b+ab\) on every \(b\), explicitly walks permutation cycles, and compares to the independently computed powers and ranks of the principal corners. The largest exhaustive example checks 1024 distinct left actions, each acting on 1024 points. Additional checks compare powers to the sharp order-jump superdiagonal criterion; experiments at larger sizes are sampled and explicitly labeled nonexhaustive in the recorded output.

The code checks only prime fields, while the proof uses field-linear algebra valid over every \(\mathbb F_q\). Numerical experiments do not prove the universal statement. Historical priority and scientific interpretation have not been independently audited.
