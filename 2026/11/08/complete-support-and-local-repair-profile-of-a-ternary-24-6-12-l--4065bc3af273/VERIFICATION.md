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

# Reproducibility

Execute `python3 checker.py` using a standard Python 3 interpreter; no packages or data downloads are required. The standalone script contains the 6-by-24 generator as rows of base-three digits. It verifies exactly 729 words, 56,631 nonzero message subspaces, all 276 distinct column pairs, 2,024 triples and 10,626 quadruples. It asserts the published dimension and minimum distance, full weight enumerator, all support histograms, unique minimum support-sixteen two-dimensional basis, the three minimal triples, 102 minimal four-circuits and the exact nine-versus-fifteen repair partition. Any failed assertion terminates with an error rather than reporting success.

Finite exhaustive computation proves a finite claim only if the stated row-echelon and modular-rank algorithms are sound and their code is faithfully executed. It does not prove a statement for unrelated matrices, establish global optimality of locality, or settle historical priority. No independent review or external formal certification has been performed.
