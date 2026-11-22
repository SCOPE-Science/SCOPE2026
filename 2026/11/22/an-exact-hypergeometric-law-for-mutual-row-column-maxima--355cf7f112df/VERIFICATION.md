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

# Reproduction and scope

Execute `python3 verify_rook_maxima.py` with a standard Python 3 installation. The program enumerates every distinct rank array for \(1\times1\), \(1\times2\), \(1\times3\), \(1\times4\), \(2\times2\), \(2\times3\), \(2\times4\), and \(3\times3\), thereby checking sample spaces of sizes up to \(9!=362880\) exactly. The count histogram, the exact factorial moments of every possible order, the probability-normalized variance and the row/column matching-orbit symmetry are tested against exact fractions, with no floating-point tolerance. Result: 68 exact assertions passed. These checks are finite; the all-dimensions theorem is proved by the joint integral, its recursion and uniqueness of finite-support factorial moments in `RESULT.md`. Neither the checker nor the proof evaluates the arbitrary-score marked distribution of local maxima beyond their cell locations.
