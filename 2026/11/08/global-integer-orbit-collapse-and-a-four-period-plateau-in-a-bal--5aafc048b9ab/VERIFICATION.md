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

Extract `RESULT.md`, `cycle_certificate.json`, and `verify.py` to one directory and run `python verify.py` with Python 3. The program requires only the standard library and prints `VERIFY_OK checks=210378` when all specified tests pass. It verifies every link in the four primitive-cycle certificates; repeats the parameter-independent certificate for integers through 1000; checks all initial integer states in several specified finite rectangles; confirms the quadratic transient for integers through 80; and searches for extraneous fixed-state predecessors in finite rectangles.

The bound-free conclusion for all positive integer parameters and every integer initial state is established by the case analysis in `RESULT.md`, not by enumeration. Cycle transitions at parameters beyond those tested follow symbolically because their first coordinates are at least \(-4\). No independent audit has been performed. The scope excludes noninteger states, unbalanced parameters, and stability in a real-neighborhood metric.
