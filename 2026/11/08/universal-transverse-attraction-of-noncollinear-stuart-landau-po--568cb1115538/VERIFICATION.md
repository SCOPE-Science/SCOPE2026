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

# Reproducible checks

Execute `python verify_reactive_polygons.py` with NumPy. A successful check prints:

`VERIFY_OK noncollinear_heterogeneous_cases=16 nonzero_imaginary_couplings=4 dissipative_cases=8 positive_dissipative_cases=8 normal_eigenvalues_strict=1`

The executable constructs two explicit families: unequal-radius triangles with squared radii \((1,3/2,2)\) at zero dissipation and opposite-pair quadrilaterals with squared radii \((1,4,1,4)\). It checks both families at reactive strengths \(0.05\), \(0.7\), \(3\) and \(-2\), each for \(C_r=0\) and \(C_r=0.001\). In the zero-dissipation cases it checks the complete symmetric Jacobian identity against the explicit radial projector matrix. In all cases it counts the exact geometric neutral dimensions and verifies negative real parts for every other computed eigenvalue.

**Analytic boundary:** These checks sample 16 parameter points. They do not establish the universal theorem, the existence of the local stable foliation, or an interval size for dissipative-coupling persistence. Those statements follow from the full proof in RESULT.md. They do not replace independent scientific validation.
