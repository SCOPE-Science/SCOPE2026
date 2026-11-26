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

Counting convolution on the binary group is self-adjoint and diagonal in the normalized Walsh basis. At support weight s, the contribution of all triples is the degree-three Krawtchouk value; removing the ten triangles subtracts 10−2o, where o is the number of triangles meeting the support in an odd number of edges. Complementation negates the multiplier because the base size is odd. The independent exact calculation constructed all 110 bases, obtained all 1,024 multipliers both by signed sums and by the Walsh–Hadamard transform, and reproduced the signed histogram including the 72 zeros. As a structural cross-check, if w is the number of selected two-edge wedges and t is the number of selected triangles, then o=3s−2w+4t by counting selected edges and wedges within each triangle of K5. At s=5 a zero requires w−2t=5. For t=0 this forces all degrees to be two; for t=1 it forces degrees 3,3,2,1,1, with the two nontriangle edges attaching two leaves at distinct triangle vertices. Two triangles on five edges instead give a diamond plus an isolated vertex and w−2t=4. Thus the two zero motifs have 5!/10=12 and 5!/2=60 labelled realizations. The exact histogram excludes all other zeros and gives inertia (476,476,72), rank 952, and absolute nonzero extremes 2 and 110. On the orthogonal complement of the kernel the Euclidean condition number is therefore 55, and the pseudoinverse norm is 1/2; these use the singular values, irrespective of sign.

## originality

PASS

The incidence model and the generic character formula are established or elementary ingredients. The exact signed spectrum and the graph-motif description of the Fourier kernel on this particular ten-coordinate operator are the supported distinct result. The strongest same-motif catalogue result is genuine prior mathematical overlap but uses a different operator, predicate and sign data. No equivalent spectrum or stronger statement supplying it was established by the inspected sources.

## value

PASS

The standard rank-three Desargues matroid is a natural small symmetric base kernel, and Fourier invertibility is intrinsic to its convolution rather than a hand-picked evaluation. The exact support of the unresolved characters tells which data cannot be recovered, and the nonzero gap gives sharp Euclidean noise amplification on the recoverable part. The complete histogram and structural zero description supply information beyond the known incidence geometry or the shared D5 motif labels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
