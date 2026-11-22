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

The proof in `RESULT.md` reconstructs the global optimization via the sign change of a single auxiliary function, with all stated endpoint and tie cases. The bound controlling the strong-cooperation asymptotic maximizer is included there; no numerical extrapolation is used as an infinite proof.

The standalone `verify.py` uses the standard Python library, tests the threshold equation, the local derivative conditions, representative phase signs, the analytically predicted continuous linear benchmark, and convergence to the large-strength constants. It completed successfully with 66 assertion groups when run from the packaged bytes. These tests provide diagnostic arithmetic evidence only and do not establish historical novelty or independent certification.

Remaining scientific limits include the phenomenological quadratic return, constant policies, fixed annual favorable-season frequency, and unverified applicability to demographic measurements. Some older historical papers could not be inspected in full.
