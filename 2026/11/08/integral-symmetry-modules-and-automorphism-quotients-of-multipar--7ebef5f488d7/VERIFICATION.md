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

# Verification record

The proof is the five-step symbolic argument in `RESULT.md`: exact face decomposition; augmented simplicial chain identification; integral direct-summand proof; permutation determinant character; invariants under within-part and equal-part symmetries. No computer experiment proves the general theorem; the finite tests below corroborate it.

Run with standard Python 3: `python verify.py`. The deterministic printed output is in `verify_output.txt`.

The script constructs all graph automorphisms for ten complete multipartite cases, including exchanges of equally sized parts; 9,030 triples of group element and threshold are checked against the signed reduced Lefschetz character computed by face enumeration. It verifies the identity rank formula for the identity map and checks the predicted invariant dimension by averaging character traces. A separate module enumerates the oriented orbit-sum chain basis and computes its reduced homology over the prime field \(\mathbb F_{1009}\) for 26 cases, without using the character formula as an input. The finite-field computations alone cannot rule out integral torsion or certify arbitrary parameters; the proof addresses those issues separately.

The full integral \(\operatorname{Aut}(G)\)-module formula and quotient rational Betti formula are proved algebraically for every \(s\ge3\), every \(m_i\ge1\), every \(r\ge1\). No independent external audit or formal proof assistant certification was performed.
