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

# Verification and limits

The proof in `RESULT.md` independently derives the coprime Chebyshev node count, transversality, the region count, the signed vertical-ray formula, the alternating-derivative bound, and the three exceptional winding witnesses. The winding-basis identification \(\ker\gamma_{\mathbb Q}=\mathbb Q\mathbf1+\mathbb Q w\) is explicitly attributed to Yoshinaga, Corollary 5.4.

Run `python verify.py` with a Python 3 interpreter and no third-party dependencies. It checks 12,032 coprime pairs in the displayed finite parameter range, the node parity formula, the numerical inequality, the root-sign pattern, and exact algebraic relations for the three-level exceptional witness. Its output is `CHEBYSHEV_CHAMBER_CHECK_OK 12032`.

The finite check does not establish the theorem for unbounded parameters; that follows from the uniform proof. It does not compute the precise dimension of the generated subalgebra for all parameters. Historical priority and independent mathematical review have not been exhaustively established.
