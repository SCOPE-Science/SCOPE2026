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

# Verification

The theorem applies only to finite blocklengths \(1\le n\le10\). Run `python3 verify.py` in this folder, containing `certificate.json`. It requires only Python 3 standard-library modules, notably `fractions.Fraction`. The script generates binary source words avoiding `11`, derives every output under zero or one adjacent unequal swap, and checks each explicitly listed maximum codebook's source eligibility and pairwise disjoint output balls. It constructs each confusability graph by literal intersection of those output sets.

For each of the 40 fixed-weight subproblems, the script uses the two-way include/exclude independent-set recurrence over all subsets of a finite graph, with memoization and exact integer counts for the number of attaining sets. Separately, it recomputes every rational primal bound, dual bound, and equality of the two objective values. No floating-point linear-programming optimizer or trusted precomputed graph is used for the standalone proof check. At lengths seven and eight it enumerates every optimum at each weight and tests reversal invariance; the class counts follow from Burnside's lemma. The script asserts each resulting global profile value and prints `VERIFY_OK` upon success. This replay completed successfully from the packaged files.

As an additional separate check, all 40 integer maxima were recomputed from independently built output-incidence matrices by binary mixed-integer optimization; all values agreed. That external numerical implementation is corroboration, not a prerequisite for the exact delivered proof. The code does not claim a proof beyond length ten; it also does not independently establish historical novelty or external certification.
