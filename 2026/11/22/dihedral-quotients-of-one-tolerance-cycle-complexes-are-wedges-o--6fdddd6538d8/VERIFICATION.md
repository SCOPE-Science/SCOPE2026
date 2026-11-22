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

# Reproducible finite checks

The supplied `verify_cycle_tolerance_quotient.py` reconstructs all one-tolerance faces of each unfilled cycle for orders 4 through 20, then enumerates orbits of flags under all 2n rotations and reflections. The resulting quotient is a barycentric cell decomposition respecting stabilizers. Exact integer boundary matrices are formed and checked for zero composition. Eliminating a spanning tree and computing Smith normal forms yields the integral first and second homology, including possible torsion.

All seventeen tested orders pass: first-homology rank zero, no torsion, second-homology rank equal to `floor((n-4)/2)`. A separate stabilizer enumeration also agrees. The program uses Python 3 and SymPy and can be run with `python verify_cycle_tolerance_quotient.py 20`.

The unbounded homotopy theorem relies on the direct geometric analysis in RESULT.md, not on the finite checks. The script verifies homology, not fundamental groups or infinite-order assertions; the mathematical proof supplies those facts. External independent validation has not been performed.
