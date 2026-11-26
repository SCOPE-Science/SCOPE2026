---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Because the center is the derived line, write F(z)=λz and F(v)=Av+c(v)z. Bracket preservation gives ω(Av,Aw)=λω(v,w), and idempotence gives A²=A, λ²=λ and cA+λc=c. Over any field λ is 0 or 1. At λ=1, nondegeneracy forces A injective, hence the identity by idempotence, and then c=0. At λ=0, A is a projection onto an isotropic U and c=ηA is determined by its restriction η to U; conversely these data suffice. Thus the image is the specified graph, has rank r=dim U≤n, and meets the center trivially. Every r≤n occurs by selecting vectors from a symplectic basis. Counting ordered isotropic bases gives q^(2n−j)−q^j extensions at stage j; divide by the ordered-basis count to obtain I_(n,r). Graphs over each U are distinct for distinct η, and a fixed graph leaves exactly the choice of a complement to U in V, parametrized by Hom(V/U,U). This verifies the rank formula, the per-image multiplicity, the zero and full-rank cases, and both example polynomials. No division by 2 is used. A fresh replay enumerated all 512 binary 3×3 matrices, tested the bracket on basis pairs and F²=F, and counted spans of the columns: 64 Lie endomorphisms, with retraction counts (1,12,0,1) by rank and two retractions for each of six rank-one images. This is a bounded check, not the unbounded proof. The bound VERIFICATION.md, REVIEW.md and artifacts/check_heisenberg.py were inspected; the uploaded script was not executed.

## originality

FAIL

The prior Resultary record ca6c766006fb is on the identical composition-idempotent objects and field range, not merely on automorphisms as objects. It already classifies these maps in finer automorphism orbits and gives the same coefficient in each rank. Its normal form and complement count also imply the entire specified-graph claim by fixing the free functional, rather than summing it over q^r choices. This is verified coverage, not a conclusion from title similarity or from an unavailable paper.

## value

FAIL

The retraction rank gaps and specified-image multiplicities are natural and could guide work on the endomorphism monoid. In this record, however, the rank enumeration is covered and the proposed refinement is just fixing one of the already free graph functionals while retaining the already counted complements. The tiny examples are checks and do not supply a distinct worthwhile result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
