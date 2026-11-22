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

# Reproduction of the two-boson star crossing

The standalone programs need Python 3 and SymPy (no data downloads). From the directory containing the extracted files, run `python3 verify_blocks.py` and `python3 verify_full.py`.

`verify_blocks.py` builds two three-dimensional Jacobi matrices, evaluates their determinants independently, checks the exact cubic difference and common-root equation, checks root sign values, and confirms the algebraic crossing for 27 integers \(4\le m\le30\). Successful terminal marker: `BLOCK_IDENTITY_OK symbolic_cubics=2 symbolic_crossing=1 resonance_sizes=27`.

`verify_full.py` independently reconstructs the complete occupation-space Hamiltonian with integer hopping weights. It compares 15 exact characteristic polynomials across \(4\le m\le8\) and interactions \(U\in\{1,3,6\}\), and proves by exact rational rank calculation that the common eigenvalue has multiplicity four at \((m,U,E)=(4,3,1)\) and seven at \((7,6,2)\). Successful marker: `FULL_TWO_BOSON_OK polynomial_checks=15 exact_resonance_ranks=2`.

The mathematical all-size proof is in `RESULT.md`: direct construction of the symmetry blocks, incidence-map rank, polynomial root signs, and the exact crossing elimination. Finite examples are supporting checks, not proof for arbitrary \(m\). Historical-priority assessment is based on inspected literature at the stated levels and does not substitute for independent scientific validation. The same-star 2022 attractive-interaction article was available only by abstract.
