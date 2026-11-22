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
The complete proof is in `RESULT.md`. The attached `verify.py` tests the polynomial field's endpoint derivative identities symbolically, the gap signs on 3,564 exact-rational samples (including neutral endpoint derivative cases), and the derivative-envelope scaling for 9 combinations of shrinking lengths and highly asymmetric splits. The tests passed in the packaged environment. The proof independently establishes the global differentiability at the arbitrary closed set, the full Lebesgue basin, minimality, and the sharp necessity of the repeller-multiplier decay constraint; no finite test is claimed to prove these universal statements.

Run as `python verify.py` with SymPy installed. There are no external datasets, local system paths or hidden dependencies beyond SymPy. No independent mathematical audit has been performed.
