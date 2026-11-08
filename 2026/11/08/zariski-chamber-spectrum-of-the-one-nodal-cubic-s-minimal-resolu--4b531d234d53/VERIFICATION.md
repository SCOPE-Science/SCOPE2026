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

# Exact verification and limits

Run `python3 verify_chambers.py` from a directory containing the extracted standalone program. The program requires Python 3 and no third-party libraries. It constructs all 22 negative-curve classes in the integral Picard lattice with intersection matrix \(\operatorname{diag}(1,-1,-1,-1,-1,-1,-1)\). It checks every principal subset of at most six classes, uses exact Bareiss integer determinants and Sylvester's positivity criterion on the negative intersection matrix, then independently evaluates a combinatorial star/triangle formula. It checks the \((-2)\)-conic incidence identities, the rank-refined chamber vector \((1,22,156,490,725,447,57)\), the 648 chambers containing the conic, and the total 1898. Its recorded stdout is in `verification_output.txt` and ends `NEGATIVE_DEFINITE_ENUMERATION_OK`.

The cutoff at six is exhaustive by the rank-seven Picard lattice's signature \((1,6)\); a negative-definite support cannot contain seven linearly independent negative vectors. The program does not enumerate plane curves and therefore does not prove that the 22 listed curves exhaust all geometric negative curves; that proof uses Bézout and adjunction in `RESULT.md`. It also does not prove the absence of previous published equivalences, and no independent audit has been conducted.
