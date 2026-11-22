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

# Computational verification and proof boundary

Run `python3 verify_conic_support.py` using standard Python 3. The code uses exact integers, enumerates all 27 line classes, constructs the complete 27-by-27 incidence matrix, checks the five conic-fiber component pairs at each line, all common-neighbor counts and the identity \(A^2=5I-4A+5J\), and evaluates the integer determinant by fraction-free Bareiss elimination. The assertions include determinant \(156250\), ranks modulo five \(20\) and \(7\), and fiber class \(5(-K_S-[\ell])\) for all 27 supports. Successful output prints `VERIFY_OK`.

The proof separately establishes surjectivity of the parity/Picard-mod-five quotient map, and equality of the kernel with the incidence image by comparing exactly computed indices. An additional SymPy Smith-normal-form check on the same independently constructed matrix gave \(1^{20},5^6,10\). This second check uses SymPy but the shipped verifier does not.

The finite certificate handles the complete universal 27-line configuration. Universal validity for smooth characteristic-zero cubic surfaces follows from the standard Picard classification; finite computation alone would not prove that geometric step. No independent scientific validation is claimed.
