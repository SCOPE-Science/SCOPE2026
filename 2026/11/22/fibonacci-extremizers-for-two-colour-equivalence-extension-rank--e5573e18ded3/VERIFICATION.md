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

# Reproducibility and limits

From the directory containing `verify_colored_equivalence_rank.py`, execute `python3 verify_colored_equivalence_rank.py` using Python 3.9 or newer. The code uses only the standard library and produces exact integer and Boolean checks.

The implementation directly evaluates the defining universal-request/existential-response game, independently from the relative-capacity separation expression. For each two-colour equivalence host type through seven vertices, every possible marked induced substructure is represented by colour counts selected from each class; all tested depths up to seven are compared. This gives 573 hosts, 24,963 marked states and 199,704 exact relative-rank comparisons. Separately, the code enumerates every partial matching of the two forced staircase marginals for each level zero through five, compares game outcomes to the complete recursive description, and checks Fibonacci counts. These levels have 1, 2, 7, 34, 209 and 1,546 possible marginal couplings, with respectively 1, 2, 3, 5, 8 and 13 successful extremizers.

All-size correctness rests on the mathematical induction in `RESULT.md`, not on a finite experiment. The scripts do not certify novelty or perform an independent audit. The package's `verification_output.txt` records the actual execution output.
