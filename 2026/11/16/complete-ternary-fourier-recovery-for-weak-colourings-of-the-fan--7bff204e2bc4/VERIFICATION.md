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

# Executable verification

Run `python3 check_direct.py` and `python3 check_inclusion_exclusion.py` with standard Python 3 (version supporting `int.bit_count`). No third-party modules or datasets are required. Both programs were executed successfully with exact integer arithmetic after copying their source from the final package.

The direct program enumerates every one of the \(3^7=2187\) ternary colourings, selects the \(882\) whose seven Fano lines are nonmonochromatic, and applies the multidimensional ternary Fourier transform over the exact ring \(\mathbb Z[\omega]\). It tests the complete coefficient histogram, the balanced-support criterion, Parseval, and the minimum nonzero modulus.

The inclusion-exclusion program independently constructs all \(128\) line-subset equivalence partitions and evaluates the resulting integer character formula at each of the \(2187\) frequencies. It enumerates all \(168\) invertible binary collineations and checks the twelve balanced orbit classes, their exact multipliers, and their coverage of \(729\) frequencies.

The rank, kernel, inverse norm, and condition number then follow from the standard finite Fourier convolution diagonalization, with no approximations. The results are limited to the specified Fano incidence hypergraph and three named colours. No independent audit or external certification has been performed.
