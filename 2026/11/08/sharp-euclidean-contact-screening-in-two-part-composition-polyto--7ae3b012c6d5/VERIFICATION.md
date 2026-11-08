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

# Verification status and reproduction

An explicit proof in `RESULT.md` is the mathematical evidence. The critical inequalities were checked symbolically by substitution: \(D_A-D_B=(2K/q)(-F/(2K)-\alpha)\), \(D_B-D_C=2p(q+\alpha-\beta)>0\), and the origin-distance formulas in each phase. A barycenter of the exact contact vertices equals the proposed unique center, proving minimum-radius optimality.

Run `python3 check_two_part.py` using Python 3 standard library to reproduce exact rational arithmetic checks. The checker reconstructs all vertices from the inequality matrix for small parameters, tests 6,400 pairs of positive integers, checks all four vertex distance types and their equality conditions, and compares individual vertex distances for dimensions at most twelve. Its recorded execution passed 40,131 assertions and examined 1,639 explicit vertex distances. These bounded tests corroborate, but do not replace, the proof for all parameter pairs.

No independent human or third-party mathematical audit has been performed. Novelty comparisons establish no discoverable covering theorem, not global historical uniqueness. The claim is about the standard coordinate Euclidean geometry only.
