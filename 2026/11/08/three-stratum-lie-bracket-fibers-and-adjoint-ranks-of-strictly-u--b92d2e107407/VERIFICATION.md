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

# Reproducibility checks

Run `python3 verify.py` with a standard Python 3 interpreter. Its first two checks enumerate **every** ordered pair of six-coordinate matrices over \(\mathbb F_2\) and \(\mathbb F_3\), compute the bracket by literal \(4\times4\) matrix products, and compare the count for **every** target in the three-dimensional derived ideal with the theorem. These are respectively \(2^{12}=4096\) and \(3^{12}=531441\) pairs. The program also constructs the six-column adjoint action from the same literal matrix products and computes ranks by finite-field elimination.

For \(q=4\), the implementation uses \(\mathbb F_2[t]/(t^2+t+1)\), not modular arithmetic modulo four. For \(q=4,5\), it enumerates all \(q^6\) adjoint maps, verifies rank-population and fiber-mass identities, and checks 50,000 additional seeded pairs using literal multiplication and the independently derived coordinate formula. The seed is fixed, but this sampling is *not* an exhaustive bracket-fiber check in these larger fields.

The executed output, with all asserts enabled, is embedded as `verification-output.txt`. The expected final marker is `UT4_BRACKET_ALL_CHECKS_PASS`. The code does not call out to external sources or require nonstandard Python dependencies.

These are checks of arithmetic and finite cases, not a formal or independent all-field certification. The unrestricted proof rests on the explicit linear-equation counting and the adjoint rank analysis in `RESULT.md`.
