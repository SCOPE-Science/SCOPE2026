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

The mathematical proof of the general identity is in `RESULT.md`. Execute `python3 artifacts/verify.py` from the extracted package directory using Python 3 standard library only. The verifier independently implements the directed envy graph, directed-cycle detection, exhaustive proper colouring generation, and preference-profile enumeration for small test graphs. It constructs the lifted obstruction for the four-vertex path and other test cases. The computed last line must read `VERIFY_OK`.

The verifier is a finite supplementary check, not the proof of the all-graph/all-profile quantified theorem. The decisive mathematical argument is the apex's top-ranked colour in the upper bound and the universal two-cycle obstruction from the newly last-ranked colour in the lower bound. No external machine, formal system, or independent mathematical audit has certified the result.
