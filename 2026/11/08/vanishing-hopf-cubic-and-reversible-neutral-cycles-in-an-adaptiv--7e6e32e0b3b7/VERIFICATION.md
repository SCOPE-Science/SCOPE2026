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

# Reproduction and scope

The result is supported by an analytic computation of the first Lyapunov coefficient, an exact parameter-independent binomial derivative identity, and a planar time-reversing symmetry. `verify.py` evaluates the key identity in exact rational arithmetic on six sample group quotas, tests the symmetry for balanced quotas, and diagnoses the half-return construction by numerical integration.

Run `python verify.py` in the directory containing the file; prerequisites are Python 3, SymPy, and SciPy. Expected output contains `VERIFY_OK`. The finite checks do not prove the theorem in arbitrary dimension/parameters; the full universal argument appears in `RESULT.md`.

The first Lyapunov coefficient is asserted to be zero at the specified critical parameter only. It is not asserted that every asymmetric case is a center, nor that an isolated small cycle exists away from criticality. The balanced center and nonisolated-cycle arguments are purely deterministic and local to interior periodic orbits. No independent external audit has been performed.
