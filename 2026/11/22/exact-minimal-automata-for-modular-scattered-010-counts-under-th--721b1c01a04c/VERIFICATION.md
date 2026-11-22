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

The proof is a finite-residue, all-modulus argument, not a numerical extrapolation. Its essential checks are the counter transitions, the modulo-two invariant, the two generators \((1,1)\) and \((2,4)\), the identity \(T_0^m=\operatorname{id}\), legal inverse simulation, and the explicit Myhill–Nerode suffixes. They are stated and justified in `RESULT.md`.

Run `python3 checker.py` using Python 3 and the standard library. The program builds and minimizes complete DFAs for moduli 2 through 14 and compares direct position-triple counts with automaton acceptance for all binary inputs of lengths zero through fourteen and moduli two through nine. Actual observed output is provided in `checker_output.txt`. No finite experiment certifies the theorem for all moduli; the general proof establishes that claim.

Relevant scientific limitations: no claim is made for arbitrary forbidden factors, nonzero targets, or different subsequence patterns. Historical literature coverage is limited to the explicitly named inspected sources and accessible bibliographic comparisons.
