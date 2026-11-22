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

# Exact reproducibility

Run `python VERIFY.py` with `INCIDENCE.json` in the same directory and a compatible SymPy installation. The script checks all pairwise line intersections in the number field defined by \(e^2+e+2=0\), the two separately constructed incidence graphs, the explicit labelled graph isomorphism, the full Laplacian characteristic polynomial, integral Smith reductions in both presentations, and an independent \(2\)-, \(3\)-, and \(7\)-adic elimination. Its successful terminal output is `KLEIN_BITANGENT_LEVI_SMITH_AND_LOCAL_CERTIFICATE_OK`.

Exact checks in the packaged program: 378 bitangent line pairs, 210 Klein line pairs, the resulting 252 double and 21 quadruple points, 28 triple and 21 quadruple points respectively, 84 incidence edges in each graph, equality of all 84 mapped edge incidences, two integral Smith forms, and 144 local Smith valuations. The characteristic-polynomial/Kirchhoff calculation rules out any other prime torsion. These are finite, deterministic computations, not infinite mathematical certification and not an independent review. The 1994 primary source remains an originality access risk.
