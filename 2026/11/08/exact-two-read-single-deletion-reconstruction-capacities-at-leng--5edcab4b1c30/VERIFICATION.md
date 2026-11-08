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

# Reproducibility of finite certificates

Run `python3 verify.py certificates.json` with Python 3. The checker requires no third-party dependencies and regenerates the exact confusability relation from deletion outputs. For each of seven canonical support graphs it verifies complete vertex membership, a pairwise nonconfusable set, a vertex-disjoint matching of forbidden pairs, and the equality `independent_count + matching_count = vertex_count`. The last equality proves sharpness of each table entry without assuming a graph optimizer is correct.

The actual run returned `VERIFY_OK cases=7 independent_set_and_matching_certificates=7 q_formula_checks=48 direct_support_check_q=3`. Additional algebraic tests check the formula through alphabet size forty-nine, and an independent direct scan checks support separation for ternary words of lengths three and four. The finite checks are not used as a proof for infinitely many alphabet sizes; that extension follows from the symbol-support lemma and the binomial sum in the proof.

Limitations: no independent human or externally certified audit was performed. The set of possible traces is distinct, not a multiset of read multiplicities. The source model allows a word to have fewer than two distinct one-deletion traces; the requirement applies to any pair of traces if it exists.
