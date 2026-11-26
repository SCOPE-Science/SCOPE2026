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

The algebraic classification in RESULT.md is correct. Each coordinate solves the same monic quadratic X^2-e1 X+e2. For two distinct block values a,b the equations reduce to e1=a+b and e2=ab. With A=m-1 and B=l-1 these are A a+B b=A a^2+B b^2=0; distinctness makes the equivalent conditions A a=B b=0. For the all-equal nonzero case the gradient vanishes just at n=1,2 mod 3 and the cubic just at n=0,1,2 mod 9. A single nonzero block has size 1 mod 9; two blocks of sizes 3u+1,3v+1 give e3=(ua+vb)^3. The residues yield the stated support, including the diagonal (on a qualifying line) when n=2 mod 9, and the antipodal partitions in the two finite residues. At a distinct two-block point of sizes 1 mod 3 the cross Hessian entries are zero and each diagonal block is a nonzero scalar times J-I, with nullity one. Thus the gradient ideal is locally the smooth plane ideal: the plane is contained in the gradient scheme and the equal tangent and local dimensions give a regular local ring. The cubic then cuts a linear cube in the finite case and vanishes identically on the surviving planes. In the other residues the complementary block is invertible and the Hessian has corank one; at an all-equal surviving point (n=1 mod 9), the Hessian is a nonzero multiple of J-I with corank one as well. A projective chart removes the radial coordinate and gives the asserted local lengths. Complementation and top-cycle multiplicities give the two degree formulas.

## originality

FAIL

A material part of the frozen novelty claim is already implied by Xie: the positive-dimensional partition lines, their generic multiplicities and hence their count and exact degree are a direct specialization of Theorem 1.3. RESULT.md:74–78 and the accompanying self-review do not correctly delimit the claim to finite scheme degrees and genuinely additional support information. This is verified partial prior coverage, not a claim that the whole theorem is old. The later Resultary overlap independently duplicates the finite reduced classification, but is not evidence of earlier priority. No corrected claim is submitted here.

## value

PASS

The finite scheme degrees and noncoordinate local lengths address a real gap beyond dimension and extremal geometry: a support count alone misses the threefold thickness at all 35 antipodal points for n=8. The absence of additional isolated support in the line regime is also useful. The positive-dimensional top cycle as a stand-alone invariant is already covered, so its recomputation is not a source of distinct value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
