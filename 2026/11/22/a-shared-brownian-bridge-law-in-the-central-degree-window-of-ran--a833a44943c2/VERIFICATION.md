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

Run `python3 verify_mesoscopic.py` using Python 3 from the directory containing this file, RESULT.md and the checker. The checker exhaustively enumerates all permutations at sizes 2 through 7 and compares all individual degree means and pairwise covariances with the exact rational formulas. It separately verifies the Brownian bridge covariance integrals and checks the normalized finite degree second moments at sizes 10001, 40001 and 160001. A successful run prints `PASS: 186 exact/integral/asymptotic-second-moment assertions`.

The unbounded limiting argument is mathematical, not computational: the two half-sample empirical processes converge by the standard empirical-process Donsker theorem, finite deletion makes them asymptotically independent of designated vertex ranks, and the remaining local block has conditional variance \(O(\sqrt n)\). Evaluation at independent ranks and Slutsky's theorem yield the joint law. Exact finite covariances and limiting bridge integrals are independent consistency checks. Experiments cannot establish the infinite theorem or historical novelty.

The prior 2015 and 2019 center-degree results are explicitly credited. This package reports self-review, not independent verification or historical-priority certification.
