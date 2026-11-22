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

The included `checker.py` is a standalone finite diagnostic using Python 3 with NumPy, SciPy, and SymPy. Its exact SymPy checks confirm the determinant and characteristic polynomial of the one-step Jacobian and the antipodal period-two identities. Numerical checks at \(A=-3/4,0,3/4\) and the first 30 high sine lobes check root locations and Floquet stability on and off the sink windows, and compare large-lobe widths with \(9/(2m_k)\).

Reproduce: run `python checker.py` after extraction. The expected final line is `all finite diagnostics PASS`. The exhaustive infinite lobe census is supplied by the inequalities and monotonicity proof in RESULT.md; these finite computations are corroboration only. The nonhyperbolic endpoints have not been classified by nonlinear dynamics. Independent mathematical audit has not been performed.
