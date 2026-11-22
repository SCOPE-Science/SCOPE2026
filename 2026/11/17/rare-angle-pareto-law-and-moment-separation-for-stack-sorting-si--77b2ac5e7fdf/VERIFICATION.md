---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the stack-sort orbit of 23...n1 as the identity plus orthogonal d_k vectors, with d_k·d_k=k(k−1), d_j·d_k=0 for distinct indices. Dual normals give precisely (n−1 choose 2) right and n−1 exceptional acute dihedral angles arccos sqrt(n/[(n−1)k(k−1)]); each unordered ridge is one facet pair. Conditional K uniform on 2..n gives nδ_{n,K} ⇒1/U with Pareto(1) tail. Uniform harmonic comparison gives A_n=log n+O(1), dominated square series gives B_n→C₂>0, yielding conditional first and second moments and the unconditional mean/variance coefficient, with all n≥3 and distinct-angle boundaries. Independent fresh orbit/Gram code reconstructed exact orbits and dot products for n=3..18, 168 orbit vertices; finite checks do not prove asymptotics.

## originality

PASS

Best-of-knowledge original finite ridge-measure law and its rare-angle Pareto/moment separation, explicitly crediting existing orbit and altitude/volume descriptions; a generic orthogonal simplex normal computation is standard.

## value

PASS

The canonical stack-sort simplex is a natural enumerative polytope, and a uniformly sampled ridge has an intrinsic Euclidean statistic. The exact exceptional fraction 2/n and its Pareto(1) conditional limit with diverging moments but vanishing unconditional scale resolve a genuine geometric concentration phenomenon not obtained by simply renaming known volumes or altitudes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
