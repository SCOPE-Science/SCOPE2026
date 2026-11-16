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

Run `python CHECK.py` using Python 3 and its standard library. It outputs `UNITARY_STEINBERG_EXACT_CHECKS_PASS` after exact rational coefficient calculations for fields of orders 2, 3, 4, 5; direct enumeration of the 648 unitary matrices in \(U_3(2)\); the distribution of Steinberg character values through the action on nine isotropic projective lines; and the sharp norm \(112/27\) obtained without using the centralizer product.

The arbitrary-rank result is proved analytically from the classical Steinberg character-value theorem and semisimple unitary centralizer classification. Exhaustive enumeration of a finite matrix group is not a proof of the general result. The checker needs no datasets or third-party packages. Independent external validation has not been performed.
