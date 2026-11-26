---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

# Verification of the six-dimer classification

`python3 check_six_orbits.py` uses the standard library and checks the derangement description at every nonincident unmatched point–line pair. It enumerates all remaining six-by-six bijections, tests each incidence, and checks class counts and stabilizer transitivity. It checks exact priorities by summing the probabilities of all accepted orders for a representative in each of the three classes. The proof in `RESULT.md` gives the structural classification, including why no type-swapping graph automorphism can merge the classes. The numerical matching weights themselves are already reported by the exact matching-output census cited in `RESULT.md`.
