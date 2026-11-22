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

The exact-orbit derivation checks that the original median minimizer interval stays invariant under each synchronous update, including half-weight ties, and then solves the scalar affine recursion for each individual. The probability calculation partitions all possible orderings by their unique balanced-weight prefix and uses the Dirichlet law of independent uniform spacings.

Run `python3 verify_rankone.py` with Python 3 (standard library only). The source verifies 3,267 exact-rational interval/trajectory configurations and 1,089 subset-versus-permutation probability configurations. All executed tests passed when the package was assembled.

Finite diagnostics do not prove the result for all population sizes. The unlimited-size conclusions depend on the explicit proof in RESULT.md. The conditional Beta law uses atomless uniform initial opinions; no test suite on simulated samples can establish the exact continuum distribution. The single weighted-average agent comparison uses the published type-dependent cohesive-set consensus criterion, rather than an independently developed convergence proof.
