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

Run `python3 verify.py` (standard-library Python 3). The script reconstructs the blowup graph from the base adjacency, enumerates all induced matchings from original graph edges, and tests inclusion-maximality by attempting to append every unused graph edge. Separately it enumerates all base-graph dissociation supports and domination, then compares all cardinality coefficients. It also checks the cyclic run formula against a four-state transfer trace.

Recorded successful result:

```text
VERIFY_OK base_profiles=150 cycle_profiles=11 independent_edge_matchings=14589 transfer_formula_cases=434 direct_all_and_maximal=PASS maximal_spectrum=PASS
```

The base-graph enumeration covers all labelled graphs on one through four vertices at clique sizes two and three; the cycle enumeration covers orders three through nine with clique sizes as indicated in the checker. Transfer/formula equality is tested for \(3\le n\le64\) and \(2\le m\le8\), a total of 434 parameter pairs.

**Scope of evidence.** Finite computation corroborates but does not establish the general statements; the mathematical proof is contained in RESULT.md. No independent audit has been performed.
