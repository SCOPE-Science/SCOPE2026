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

Analytically differentiate the displayed cubic vector field to confirm zero divergence, and differentiate \(H=q(2z(1-z)-q)\) to confirm the conserved level sets. Express the reduced period as an elliptic integral and verify the complementary-parameter asymptotic gives \(P(h)=2\log(4/h)+o(1)\). The original Euclidean cylindrical volume identity, not a reweighted Hamiltonian area, yields \(V'(h)=-\pi P(h)/2\); direct integration and inversion produce the exact main tail.

Run `python3 check.py` with the Python standard library; expected output is `HOPF_VOLUME_TAIL_VERIFY_OK`. This finite check samples exact identities and sharp asymptotic scales; it does not prove infinite estimates. The accompanying paper gives the analytic quantifiers. The 2023 directly related complete journal text was not accessible; originality is assessed within available evidence only.
