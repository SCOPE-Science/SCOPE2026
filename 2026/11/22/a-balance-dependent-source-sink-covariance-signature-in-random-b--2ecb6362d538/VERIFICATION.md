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

# Reproducibility

Run `python3 verify.py` with Python 3 (standard library only). The program enumerates all labeled spanning trees of selected complete bipartite graphs and all orientations, using exact fractions rather than floating-point simulation. It checks the covariance identities for nine graph sizes, including 524288 weighted outcomes at \(K_{4,4}\), confirms marked joint source–sink events, and checks additional exact matrix determinant signs. The observed terminal message is `PASS 92 assertion groups; symbolic all-size statements proved separately`.

These finite exhaustive checks independently test the algebra at their listed sizes. They do not establish the infinite-family assertions; those follow from the probability-generating polynomial, edge-inclusion identity, balanced inequality and asymptotic determinant proof in RESULT.md. Neither historical priority nor external/independent mathematical validation is established by this program.
