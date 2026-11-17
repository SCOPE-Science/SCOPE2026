---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For complex d>=2, block degrees n_i>=2 and N=sum_i n_i, the Plucker ruling map P1->Gr(d,N+d) is injective degree N. For a nondegenerate frame B the cut incidence rank condition is det(A(t)B)=0, a degree-N homogeneous section. Independent matrix coefficients in each block have degree n_i. A real block-diagonal squarefree specialization with positive Gram determinant shows generic N distinct roots. At t1!=t2, each row-wise coefficient-to-two-evaluations linear map is surjective; the ordered-pair incidence is an affine bundle over two irreducible determinant-zero hypersurfaces and an irreducible parameter base, hence generic monodromy is 2-transitive. Varying the constant term of a diagonal factor with a simple double root produces a local transposition while preserving Gram nondegeneracy. A 2-transitive group containing one transposition contains all transpositions, hence S_N. The roots are frame-GL_d invariant, so descends to the Grassmannian. Independently symbolic discriminant check of (t^2+eps)(t-2)(t-3)(t-4) gives a simple zero at eps=0 (derivative -5308416), corroborating the local model. No finite computation alone proves global incidence irreducibility.

## originality

PASS

The motivating Friedman-Hosten-Rosana work counts Euclidean/Grassmann DISTANCE critical points (derivative of trace objective), a distinct enumerative problem from intersections with the Schubert cut divisor det(A(t)B)=0. Esterov-Lang root-monodromy results for coefficient-support-generic polynomial families cannot automatically be pulled back along a constrained determinant coefficient map; its image need not be generic. The source proves S_N via pair incidence plus transposition for this particular frame/Grassmann family. Full motivating primary text unavailable under current access (Oxford VPN disconnected); this is a specific residual priority risk, not an automatic failure.

## value

PASS

Degree-N cut intersections and their full symmetric Galois group determine a natural enumerative and algebraic obstruction for geometric projection data on rational-normal scrolls. It distinguishes cut geometry from nearby distance-critical enumeration, and full symmetric monodromy yields radical unsolvability for N>=5. This is an all-degree and all-block structural result, not a small numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
