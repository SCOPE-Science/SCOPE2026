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

From the extracted package root, execute `python verification/check_interstage.py` using Python 3 and SymPy. The script must report **139 passed assertions** and the two approximate positive source-strength \(r=43/100\) switch concentrations. It proves an exact rational identity with symbolic cancellation and checks critical coefficients with exact rationals. No finite list of tests establishes the all-real phase diagram; that theorem is proven in `RESULT.md` from strict positivity of denominators, concavity, Descartes' bound and endpoint signs. No independent review or external certification has been performed. The named numerical roots are approximate and used only illustratively.
