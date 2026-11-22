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

# Verification

Run `python3 verify_steiner_lattice.py` using standard Python 3 with no third-party dependencies. It reconstructs the complete anticanonical tritangent configuration from the Picard divisor classes of the \(27\) lines. It then reconstructs all \(120\) Steiner nine-line supports as exactly those nine-line unions with two partitions into disjoint tritangent triples.

The actual execution obtained \(45\) tritangents and \(120\) Steiner pairs, with \(5{,}040\) nine-line supports admitting only one tritangent partition. Each of the \(27\) lines belongs to \(40\) Steiner supports, and each Steiner support has divisor class \(3(-K_X)\). Exact Bareiss determinant checks return \(-1\) for the selected tritangent minor and \(+3\) for the selected Steiner minor on the same \(21\) rows. The script exits with `VERIFY_OK` only after checking every assertion.

An independent calculation using SymPy's exact integer Smith routine returned \(21\) unit factors and six zero factors for the tritangent incidence matrix; the Steiner incidence matrix returned \(20\) unit factors, one factor three, and six zero factors. This is a cross-check rather than a substitute for the determinant-and-saturation proof in `RESULT.md`.

The computation is universally applicable because smooth cubic surfaces have the same standard line and tritangent class configuration over an algebraically closed field in characteristic zero. It does not establish positive-characteristic uniformity or geometric Galois-descent claims. External independent audit has not occurred.
