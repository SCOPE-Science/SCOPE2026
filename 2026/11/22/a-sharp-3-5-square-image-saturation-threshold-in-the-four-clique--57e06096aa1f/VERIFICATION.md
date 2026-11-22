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

Execute `python3 check_k4_square_image.py` with Python 3. The script checks the five monic defining polynomials for irreducibility, constructs every element of the finite fields \(\mathbb F_{3^r}\) for \(1\le r\le5\), computes every quadratic residue including zero, and checks all \(q^3\) targets in the characteristic-three derived hyperplane. This is **exhaustive** at those five field sizes. It also directly enumerates all quadruples of squares for \(q=3,9,27\) as an independent image check. `verification_output.txt` contains the captured actual output. The checker is standalone and imports only Python's standard library.

The all-large-field conclusion is a mathematical use of the classical Weil bound applied to squarefree products of at most four distinct linear factors; no extrapolation from finite experiments is used. Nonresonant-field image sizes follow from the adjacency determinant and finite-field square cardinality. Source-priority comparisons and the absence of an independent audit are distinct from the finite-code certificate.
