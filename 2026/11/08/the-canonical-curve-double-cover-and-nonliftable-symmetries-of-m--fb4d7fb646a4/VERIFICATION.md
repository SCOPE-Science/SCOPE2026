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

The accompanying `verify.py` uses only the Python 3 standard library. Running `python3 verify.py` prints `VERIFY_OK` if all assertions pass.

The checker verifies coefficientwise identities for the exchange automorphism in rational samples, exact integer identities for the two values of the octahedral parameter, and the canonical-moduli polynomial identity. It reconstructs all 120 possible ordered-image triples for six branch points and, using a complex tolerance of \(10^{-7}\), counts respectively 6, 12, 24 and 24 reduced symmetries at four selected configurations. This enumeration is complete at those sampled inputs only, is numerical rather than a formal certificate for the algebraic numbers, and does not establish the all-parameter theorem.

The all-parameter proof uses the hyperelliptic branch-set reduction, the finite-subgroup classification of \(\operatorname{PGL}_2(\mathbb C)\), and the published complete automorphism and isomorphism classification of the surface family. This verifier does not independently reprove that input or provide independent mathematical auditing.
