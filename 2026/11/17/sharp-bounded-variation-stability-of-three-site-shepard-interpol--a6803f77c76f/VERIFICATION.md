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

The claimed exact sharp operator norm is proved analytically in `RESULT.md` for every positive exponent and every positive pair of adjacent gaps. The independent Python test script checks representative finite parameters but does not certify continuum or asymptotic statements.

The proof uses constant reproduction, two exact step responses, the uniqueness of each nonlocal weight maximum, a strictly monotone gap-ratio comparison, and explicit limiting estimates. Equality is attained by a specified step triple. Numerical checks of 220 independently selected gap and power triples compared the exact formula with derivative-free direct optimization of both step responses. Additional checks cover the uniform \(p=1\) identity, mesh monotonicity, shape-parameter reversal and the predicted logistic transition.

The statement is restricted to three distinct real sites on their convex hull. Relevant older shape-preservation literature was not entirely available in full text; priority remains qualified. No independent mathematical audit has been performed.
