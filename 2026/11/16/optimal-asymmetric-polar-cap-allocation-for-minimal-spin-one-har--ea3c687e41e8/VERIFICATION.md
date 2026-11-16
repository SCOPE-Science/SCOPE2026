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

The proof reduces the spin-one concentration spectrum to three exact beta-polynomial integrals and the maximin objective to the minimum of one strictly increasing and one strictly decreasing algebraic function. The unique crossing is analytically located, and the mirror allocations exhaust all maximizers. All parameter quantifiers and excluded endpoints appear in RESULT.md.

Independent numerical cross-checks compared the polynomial eigenvalues to direct angular Wigner-function integrals, rather than repeating the beta-polynomial integration. The standalone checker `check.py` executed successfully with SymPy and SciPy, checking 150 designs, 199 area fractions and 20,099 grid comparisons. The numerical checks alone do not certify an all-area theorem; the included monotonicity proof does. Historical priority is provisional; no independent mathematical audit is asserted.
