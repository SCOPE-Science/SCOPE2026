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
# Verification and reproducibility

Run \(\texttt{python verify.py}\) using Python 3 and its standard library; no external packages, downloads or sources are needed. The code implements exact rational Gaussian elimination for the full Gram matrix, compares it against the parity-reduced closed weight formula for 220 seeded symmetric rational designs, verifies the exact witness maxima for all \(2\le n\le50\), and tests the bias inequality. The completed execution printed \(\texttt{VERIFY_OK 269 exact-rational tests}\).

The analytic argument in RESULT.md, rather than the finite script, proves the exact all-design extremum for arbitrary real nodes and every integer \(n\ge2\). The proof uses two rank-one inverse identities, an elementary completed-square bound, convex endpoint maximization and positive-semidefinite inverse order. Test coverage does not establish universal correctness on its own. The model uses the full interval and three Legendre features; no general domain-padded rate conclusion, arbitrary-design claim or external independent review is asserted.
