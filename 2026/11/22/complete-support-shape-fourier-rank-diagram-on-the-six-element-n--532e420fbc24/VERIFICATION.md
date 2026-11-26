---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For left regular convolution, the two scalar blocks are U+V and U-V, and the two-dimensional block occurs twice. Directly multiplying its entries from diag(w,w^2) and the swap matrix gives determinant Q(u)-Q(v); all entries vanish exactly for two constant triples, including a zero triple. Left/right rotation translates move the two coset subsets independently since (p,q)->(p+q,q-p) is invertible modulo 3, and a reflection switches cosets. On one coset the scalar contributions coincide, giving even ranks, and the standard block vanishes only at full constant triple support. For (1,1) determinant degeneracy forces precisely one scalar zero. For (2,1) the two scalars cannot both vanish and a single scalar zero implies determinant -3*u_0*u_1, so neither rank 2 nor 3 can occur. For (3,1) at least one scalar and a nonzero standard block remain. Two-tap partial triples exclude a zero standard block for (2,2) and (3,2); the full support case only needs faithfulness of the regular representation. Single-tap and same-coset cases give the stated remaining exclusions. I read the frozen witness table and output without executing its checker. /workspace/branches/reproduce_1.py generated exact integer witnesses for all 31 allowed pairs and verified their ranks independently by rational elimination on affine-permutation convolution matrices, including the real (4,1,1;3,3,0) witness for (3,2) at rank 3. These supply attainment, not the all-complex-coefficient exclusions.

## originality

PASS

The exact arbitrary-complex rank diagram for every fixed support is distinct in the inspected evidence. The two nontrivial two-tap rows and both three-tap rows are known, and the unit-weight balanced four-tap case and certain lower bounds are covered; these are not independent contributions. The justified scope is the complete spectra at higher sparsities and their assembly into the full diagram.

## value

PASS

S3 is the first nonabelian benchmark, and rank is intrinsic to recovery by convolution. Same-cardinality supports really do have different attainable sets. Beyond reproducing an uncertainty bound, the diagram identifies all higher-sparsity rank gaps and constructive attainability on each individual support, including the balanced four-point rank-two realization, which the previously known unit-weight case and lower bounds cannot give.

The dated certificate retains the supplied scientific assessment, sources and limitations.
