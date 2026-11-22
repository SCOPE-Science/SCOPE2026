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

# Reproduction and limits

Run `python3 checker.py` with Python 3.8+ and no third-party packages. The checker independently assembles a four-side ordered midpoint quadrature rather than reusing the closed integral formula, then tests the profile at six geometries. It separately checks the first-derivative formula, positive curvature witness, a numerical differentiation of the exact factored derivative of \(H\), and the two endpoint rates.

The proof in `RESULT.md` is universal: its exact integral decomposition and the identity \(H'(z)=(z-1)^2(z+1)/(z^2+1)^{3/2}\) do not rely on these finite tests. The differential identities and endpoint expansions were independently simplified with symbolic algebra before this package was assembled. The public checker does not certify historical novelty, nor does any finite test prove the inequalities for all real aspect ratios.
