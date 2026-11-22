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

# Finite verification

Compile and run `verify_suffixient.cpp` under C++17. It computes the minimum suffixient-set size by two independent factor-enumeration methods for each of the 32,766 nonempty binary source words of lengths one through fourteen. It checks exact agreement of the two measurement methods for every source, then exhaustively checks all 425,986 directed one-bit flips, outputs the full maxima profile and all sixteen length-fourteen extremal directed pairs.

Execute `verify_positions.py` under Python 3. Its separate prefix-suffix-set hitting test directly enumerates all nonempty subsets of positions in terminated witness strings. It confirms the minimum positions and the number of minimizers for four displayed positive witness pairs, obtaining size five for each source and size eleven for each target.

The files `verify_suffixient.out` and `verify_positions.out` record outputs from actual successful executions. The calculations prove only the explicitly finite range. The mathematical justification for equivalence of the measured statistic and minimum suffixient cardinality is provided in RESULT.md; the output files are not a substitute for that justification. No external audit or independent validation has been performed.
