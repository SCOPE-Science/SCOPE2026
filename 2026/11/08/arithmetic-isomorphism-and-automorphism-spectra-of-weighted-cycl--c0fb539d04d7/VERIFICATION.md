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

# Verification

Run `python verify.py` from the same extracted directory containing this file. The checker builds weighted cycle parameter words in exponents of a cyclic multiplicative group; for each included pair of cycle length and multiplicative-group order, it independently generates the entire orbit from elementary diagonal changes and a rotation. It compares orbit stabilizers against the predicted \(\gcd(q-1,2^n-1)\) doubling-orbit law. As a separate check, it verifies all square identities for the explicit twisted \(\mathbb F_4\) automorphism and its predicted powers at every even dimension up to \(100\). The observed run printed `VERIFY_OK 45 independent orbit enumerations, 50 exact F4 operator checks, and 180 direct GL2(F4) maps checked`.

No external packages, data files, or remote services are needed. The parameter tests are finite. Because the underlying multiplicative-group action makes sense for any cyclic group, a few formal group orders checked by the program are not themselves multiplicative groups of finite fields; all such checks remain valid tests of the algebraic orbit argument, but do not assert the existence of a corresponding field. The universal mathematical statements are justified by the proof in `RESULT.md`, not by extrapolating the checked instances. No independent audit has been performed.
