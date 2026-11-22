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

# Reproducibility

Run `python3 verify.py` with Python 3 and SymPy installed, then compare its stdout with `verification_output.txt`. The executable independently enumerates vertices/edges of the critical-color tupling for parameters 2 and 3, reconstructs components, and uses exact integer Smith normal form for the coordinate-flip relations. It also builds and checks the complete integral action of signed coordinate symmetries when the parameter is 2.

All exact calculations were run from the packaged verifier source. The tests do not prove the all-parameter result; the graph decomposition, cycle-lattice identification, augmentation-ideal identities and permutation transitivity in `RESULT.md` provide that proof. Nothing beyond degree-one homology or the explicitly stated orbit-space comparison is asserted.
