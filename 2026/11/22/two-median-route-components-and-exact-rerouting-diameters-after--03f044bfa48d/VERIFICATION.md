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

# Finite verification and mathematical scope

Run `python3 VERIFY.py` with Python 3 standard library. Rebuilt from the local package, the checker produced `PASS 208 punctured rectangular meshes; 519072 ordered pair BFS distance comparisons`. It separately constructs all monotone routes, filters paths containing the fault, reconstructs their geometric adjacency, tests connected components, performs breadth-first searches for all ordered pairs through rectangular sizes five by five, and checks the exact distance and diameter formulas. Additional finite instances through eight by four test the diameters and counts. The infinite all-parameter claim is established by the interval and rank arguments in `RESULT.md`; the finite runs do not certify unbounded inputs. No independent mathematical audit has been performed.
