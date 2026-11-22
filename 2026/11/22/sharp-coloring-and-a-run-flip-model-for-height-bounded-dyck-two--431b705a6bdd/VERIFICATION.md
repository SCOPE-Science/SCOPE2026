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

# Verification record

`python3 verify_decks.py` generated every Dyck word up to semilength eight, separately calculated each set of distinct one-deletion descendants, tested all unordered pairs, compared the height-two graph with the derived constant-block model, verified counts and checked the modular coloring for all heights. Output reached the semilength-eight case with 1,430 Dyck words and 769 height-two graph edges without an assertion failure.

`python3 verify_structure.py` independently enumerated every bit vector up to dimension eleven, verified every degree against its maximal-run decomposition, checked the exact edge totals, the weight coloring, the explicit maximum clique, and the induced five-cycle for all tested dimensions. All assertions passed. Complete enumeration at these finite dimensions corroborates the formulas only within these dimensions; the universal proof is in `RESULT.md`.

The Type-A intersection characterization is cited as a published theorem rather than re-proved. Graph perfection is negated by the explicit induced five-cycle, rather than inferred from numerical experiments. Individual reconstruction-code capacity and full unrestricted-Dyck degree distributions remain unproved.
