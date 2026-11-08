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

Run `python3 verify.py` in a standard Python 3 environment. The verifier uses only the Python standard library. It exhaustively reconstructs the \(n^{n-2}\) Prüfer-coded trees at every size \(3\le n\le8\), computes each marked-path length, and checks the entire family of conditional mixed factorial moments. It checks the exact conditional mean and finite-difference identities through size \(74\), as well as several controlled numerical instances of the asymptotic formula.

The observed run terminated successfully with **3013 exact/controlled assertions** and no exception. The finite brute-force range, exact rational checks and controlled floating-point tolerance are visible in the attached program; no bound beyond the checked range is inferred solely from execution. Infinite statements are supported instead by the general rooted-forest count, algebraic difference and uniform asymptotic estimates in `RESULT.md`.

The oldest selected source is publicly dated September 1, 1996; its downloadable text is marked as a later revised version. An independently conducted mathematical audit has not been performed.
