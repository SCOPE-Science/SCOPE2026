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

Exact finite graph certificate: `python verify_graph.py`. The standalone script enumerates every one of the \(16^4\) four-column constraint tuples and constructs the 4,096-vertex directed three-step-return graph. It checks exactly 10,824 edges; sorted cyclic strongly connected component sizes \(1,1,3,3,8,136\); all cyclic-component local fixedness; both exceptional directed three-cycles; and the three-step return of both seed configurations. The edge-stream SHA-256 is `bee9571a222b202d87194ab67c8a685114cc14b3dea77a2ac79cbee421c98b26`. The all-circumference claim follows by the proved equivalence between space-cyclic configurations and closed graph walks. The program ran successfully.

Independent cell-level finite tests: `python verify_direct.py`. For all labelled binary states, \(n=3\) gives 22 fixed and 28 three-step-fixed states; \(n=4\) gives 42 and 42; \(n=5\) gives 266 and 266. It ran successfully. Finite state enumeration alone is not a substitute for the graph certificate and mathematical closed-walk proof. Independent third-party audit has not been performed.
