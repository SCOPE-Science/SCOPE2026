---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The ordinary Hasse matching complex is the directed rooted-forest complex by Chari–Joswig Proposition 3.1. Jojić Corollary 3.1 gives R_m=(2m-1)(m-1)^(2m-2) even-dimensional sphere summands, hence reduced trace equals reduced Lefschetz. For the diagonal swap, invariant arcs come in pair-orbits indexed by i->j with i!=j, equivariant acyclicity is exactly rooted-forest acyclicity on m indices, and each selected two-arc orbit contributes chain orientation -1. The forest determinant sum_F(-1)^|F|=det(I-L_Km)=(1-m)^(m-1) yields -det=(-1)^m(m-1)^(m-1), including m=2 boundary. For K4,4, fresh independent orbit-Laplacian computations, not execution of the original verifier, reconstruct all 20 conjugacy class traces, their weights sum 1152, weighted sum 6912, and fixed subspace dimension six. General all-m follows symbolically, finite tests alone would not prove it.

## originality

FAIL

The complete submitted character is a direct specialization of the already published all-graph equivariant matrix–forest theorem. For any graph automorphism g, that theorem gives reduced Lefschetz number -det(I-L_g). On K_{m,m}, Jojić’s 2012 wedge theorem concentrates reduced homology in even degree 2m-2, so the Lefschetz number IS the actual top homology trace. The diagonal swap yields m vertex orbits, each of size two, with orbit Laplacian mI-J, hence -(1-m)^(m-1)=(-1)^m(m-1)^(m-1). For every K4,4 conjugacy class, the same theorem determines the character by evaluating a finite 1-to-8-dimensional determinant. The exact twenty-entry table may not be explicitly printed in the earlier statement; absence of a printed table is not novelty when a stronger theorem implies it. No repair of this already-covered final claim was made.

## value

PASS

The full natural automorphism representation of the ordinary Morse-matching complex on K4,4, together with a uniform canonical bipartition-exchange trace for K_{m,m}, is a mathematically motivated equivariant invariant not recoverable from rank alone. The twenty-class evaluated table and six-dimensional invariant subspace may be useful as explicit reference data. This mathematical usefulness is separate from originality: the existing general equivariant determinant theorem already determines these data, so the submitted work fails O and cannot be accepted as a new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
