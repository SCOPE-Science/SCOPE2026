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

# Reproducible checks and limits

Run `python verify.py` with NumPy and SciPy. The executable builds the same \(2n\)-normal, \(n+2\)-vertex configuration independently from the formulas and asks SciPy for its full facet decomposition for each \(4\le n\le40\). It verifies equality of normals to node points, all facet offsets and areas, normalized surface area \(4\pi\), polytope volume, polar-support bounds, circumsphere and inball radii, degree-three quadrature monomials, and the fourth-degree obstruction. In addition, it compares successive analytic heights for \(4\le n\le300\).

Actual execution: `PASS 16023 checks; n=4..40 hulls; n=4..300 monotonicity`. The verification output is reproducible from the embedded script, not a formal infinite certificate. Floating-point hull checks allow explicitly stated small tolerances. The proof's exact inequalities, including \(\sin x\cos x<x\), provide the all-integer mathematical argument. Independent audit has not been performed.
