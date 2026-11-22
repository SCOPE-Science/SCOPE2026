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

# Mathematical verification

Run `python verify_tripartite_potts.py` with Python 3. It enumerates all group color-count triples, weights every group count by its exact multinomial coefficient, and compares the exact rational minimizing energy and preferred-color population histogram against the formula for eight rational fields in each of six ordered shore triples. The completed run printed `EXACT_TRIPARTITE_CENSUS_PASSED 48`.

The proof's decisive infinite-family checks are mathematical, not computational: (i) majorization gives the sharp induced-edge lower bound for every preferred-set size; (ii) its equality cases limit the configurations to explicit shore-filling patterns; (iii) nonpreferred colors must avoid all remaining cross-shore equalities; (iv) case counting gives the two critical occupancy polynomials. Field boundaries and ties are included exactly. Finite tests cover only the six named graph sizes and eight fields each, and do not establish the infinite quantifiers or uniqueness of the historical claim. No external or independent scientific audit was performed.
