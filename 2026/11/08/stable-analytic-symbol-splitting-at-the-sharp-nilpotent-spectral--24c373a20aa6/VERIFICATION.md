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

The analytical proof uses Hardy-multiplier compression, Parseval column and row energies, and an explicit disk-automorphism witness. No finite computation is used to establish the universal assertions. The standalone `check_schur_jordan.py` uses only the Python standard library and checks the scalar extremal family and exact rational coefficient normalizations. It was run successfully with the result:

`SCHUR_JORDAN_CHECK_OK 2616 finite assertions`

The principal calculations needed to reproduce the theorem by hand are: first, \(\|\mathscr J(F)\|\le1+\|F'(0)\|\); second, each of the input-column and output-row Hardy errors is at most \(2(1-\|F'(0)\|)\); third, the full matrix-symbol squared error is no larger than their sum; fourth, the disk-automorphism witness has functional-calculus deficit \(\tfrac32b^2+O(b^4)\) and squared symbol distance \(2b^2\). All claims concern arbitrary finite dimensions and all Schur functions; boundary integrals are understood almost everywhere.

Known limits: the coefficient of the squared-error bound is not proved sharp, and the function-level result is proved only at the square-zero Jordan block. Literature-priority assessment is necessarily limited by the breadth of operator-valued Schur interpolation theory. Independent audit has not been performed.
