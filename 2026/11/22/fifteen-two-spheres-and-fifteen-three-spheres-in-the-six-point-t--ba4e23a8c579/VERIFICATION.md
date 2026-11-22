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

# Exact verification

Running `python3 verify.py` regenerates all faces by graph-shortest-path admissibility, independently compares with induced clique components, and replays each finite collapse and chain reduction. Expected completed checks are 180 forbidden triples, face vector (15,105,275,240,66,10), 76 valid elementary collapses to a three-dimensional complex (15,105,265,174), 91 nonabelian triangle relations killing its fundamental group, 159 integral unit Smith pivots with zero residual, and independent mod-two original boundary ranks (14,91,169,56,10).

These finite computations prove a statement about this one finite simplicial complex. They do not prove any larger-order assertion, symmetry decomposition, or publication priority. The step from the explicitly verified chain groups to a wedge-of-spheres homotopy type additionally uses the stated theorem for simply connected three-dimensional CW complexes with free integral homology.
