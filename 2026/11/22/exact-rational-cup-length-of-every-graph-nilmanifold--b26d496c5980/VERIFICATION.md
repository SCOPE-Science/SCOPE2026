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

## Executed checks

`python3 check.py` completed successfully and printed:

```
PASS: 1099 graphs on 1..5 vertices; 198316 individually distinguished pure-central differential targets.
For each: all constructed vertex-assigned cocycles closed; product is top exterior form.
General proof uses injectivity of d on positive pure-central algebra and nilpotence of vertex ideal.
```

The calculation uses integer signs in an exterior basis and exhaustive labelled graphs with one through five vertices. It verifies precisely the finite instances and constructive identities; it is not evidence that infinitely many graphs were enumerated. The all-graph result requires and has an independent symbolic proof in `RESULT.md`.

## Scope and limits

The key symbolic points are the injective identification of every target monomial of the pure-edge differential by its unique graphical edge, separation by vertex degree of the differential on the vertex ideal, and the fact that a differential cannot produce a term containing every edge variable. One should not infer an integral cohomology calculation, categorical lower bound sharpness, or unexamined priority from these checks.
