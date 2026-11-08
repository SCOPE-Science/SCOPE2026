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

The proof is analytic. The finite checker is supplementary and does not establish an infinite limit.

Run `python3 check.py` in a directory containing the standalone files. Only Python's standard library is needed.

The program compares the full ordered-pair definition with the independent critical-school counting implementation. It exhaustively checks all two-student and three-student preference/priority permutation profiles for each admissible fixed threshold, then checks the exact rational first moment. It also performs seeded randomized comparisons at market sizes 4, 9, and 28.

Recorded test outcome: 93,328 exhaustive profile-threshold checks passed; 36,000 seeded finite profile-threshold checks passed. In the exhaustive three-student case, the zero-event probabilities are exactly \(505/864\) for \(h=2\) and \(5027/23328\) for \(h=3\). These finite probabilities are not asserted to equal their asymptotic limits.

For an independent proof examination, check the priority rank-difference count, the uniformity of each critical incumbent rank, the collision union bound, the conditional independence of distinct students' pairwise preference comparisons, and the multinomial-to-independent-Poisson rare-mark limit. No external theorem prover or certificate is claimed.
