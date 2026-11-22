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

The proof is an exhaustive symbolic partition into both-cliques-positive and three disjoint zero-containing configurations. The coefficient identity is reproduced using integer convolution in `verification/formula_check.py`; no external Python packages are needed. `verification/direct_enumeration.cpp` explicitly constructs all graph-neighborhood conditions for \(3\le n\le6\) and checks every four-label assignment. `verification/crosscheck.py` compiles the direct checker and matches every coefficient in this range, returning `CROSSCHECK_OK`.

The symbolic check covers \(3\le n\le14\) and verifies the closed total formula, positive coefficients and the interval spectrum for \(n\ge4\). These finite experiments are supporting checks only; the unrestricted proof is the bijective case decomposition in RESULT.md. The boundary \(n=3\) is not included in the theorem because it has additional minimum types. Historical priority and external independent mathematical review have not been certified.
