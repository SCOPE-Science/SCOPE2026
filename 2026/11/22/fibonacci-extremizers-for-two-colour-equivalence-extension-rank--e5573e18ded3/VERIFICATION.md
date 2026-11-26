---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

From the directory containing `verify_colored_equivalence_rank.py`, execute `python3 verify_colored_equivalence_rank.py` using Python 3.9 or newer. The code uses only the standard library and produces exact integer and Boolean checks.

The implementation directly evaluates the defining universal-request/existential-response game without the relative-capacity separation formula. For each two-colour equivalence host type through seven vertices, it enumerates the selected red and blue counts in every class, treating a class as marked exactly when at least one vertex is selected. It compares the formula to the direct game at each depth from zero through seven. This gives 573 host types, 24,963 selection-profile visits (not necessarily distinct up to automorphisms), and 199,704 exact relative-rank comparisons. Separately, the code enumerates every partial matching of the two forced staircase marginals for levels zero through five and compares the actual rank outcomes with the recursive classification. These levels have 1, 2, 7, 34, 209 and 1,546 possible marginal couplings, with respectively 1, 2, 3, 5, 8 and 13 extremizers.

All-size correctness rests on the mathematical induction in `RESULT.md`, not on a finite experiment. The scripts do not certify novelty or perform an independent audit. The package's `verification_output.txt` records the actual execution output.
