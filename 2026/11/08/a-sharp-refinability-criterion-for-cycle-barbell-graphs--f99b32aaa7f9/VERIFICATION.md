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

# Reproducibility and boundaries

Run `python3 verify_barbell.py` from the directory containing the embedded files. It uses only Python's standard library, constructs every cycle barbell with integers `3 <= m <= n <= 17` and `1 <= d <= 23`, computes the stable 1-WL partition by exact integer-color refinement, and compares it with the asserted three-case stable partition and orbit-class count.

The verifier also enumerates actual adjacency-preserving permutations in 70 cases (`3 <= m <= n <= 6`, `1 <= d <= 7`), forming exact automorphism orbits independently of the asserted orbit formula. The verification output is included verbatim as `verification_output.txt` and ends `VERIFY_OK`. No heuristic graph-isomorphism routines or random sampling occur.

A finite experiment does not prove the unrestricted infinite result. The general proof uses the precisely stated universal-cover characterization (Krebs and Verbitsky, arXiv:1407.3175, Lemma 2.6), followed by a case distinction on the two cycle lengths and connector length, and a direct computation of finite automorphism orbits. The proof, assumptions, and limitations are documented in RESULT.md. No machine-checked infinite formalization or independent audit has been performed.
