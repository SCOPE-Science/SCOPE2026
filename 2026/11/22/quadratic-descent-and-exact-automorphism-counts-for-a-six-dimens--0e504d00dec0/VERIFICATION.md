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
# Computational verification

Run `python3 verify.py` with Python 3 standard library; save stdout and compare against `verification_output.txt`. The checker encodes \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\) as binary polynomial-quotient fields. It exhaustively enumerates all invertible quotient maps for \(q\in\{2,4,8\}\), computes their quadratic similarity constraints and square-zero vectors, tests the finite-field extension parity criterion, and independently multiplies algebra basis images to validate homomorphism constraints.

For \(q=2\), it exhaustively constructs and checks all \(256\) and \(768\) possible algebra-automorphism lifts of the respective quotient similitudes. For \(q=4\), it verifies the count of possible lifts algebraically and tests representative lifts directly rather than enumerating all \(294912\) maps. All 16 parameter pairs over \(\mathbb F_4\) are tested against the claimed two-class and automorphism-similitude distribution. It also directly verifies an explicit \(\mathbb F_4\)-linear isomorphism between the two binary models. It checks associativity of all radical triples over \(\mathbb F_2\).

The recorded output ends with `EXPLICIT_F4_ISOMORPHISM_OK` and `VERIFY_OK`. These finite computations corroborate, but do not replace, the general proof in RESULT.md. No independent mathematical audit has been performed.
