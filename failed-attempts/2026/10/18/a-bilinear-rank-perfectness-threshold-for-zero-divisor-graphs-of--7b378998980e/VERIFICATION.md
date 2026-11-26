---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The actions of the residue field on m/m² and m² require no embedded coefficient field: changing a scalar lift adds an element of m, and the error vanishes in the corresponding quotient. Multiplication descends and is nonzero because products span m². The radical lifts to Ann(m), of size q^(r+1); its nonzero elements are universal. A nonradical element has a nonorthogonal partner in the quotient and the partner has at least two lifts, ensuring a distinct nonneighbor. Each nonzero projective direction of the nondegenerate quotient has q^(r+1)(q-1) lifts, a clique for isotropic directions and an independent set otherwise. Rank one gives a single independent fiber; rank two gives fixed points or transposed pairs of the projective perpendicularity involution. The binary forms have the stated isotropic-point counts, including char 2 where the diagonal quadratic polynomial is a square of a linear form. The components, clique joins and colorings follow. In odd characteristic diagonalization supplies an orthogonal triple. In finite characteristic two nonalternating, split off nonisotropic lines; any residual nonzero alternating summand decomposes into hyperbolic planes. Combining one diagonal line with one plane, normalized to B(e,e)=B(u,v)=1, gives three orthogonal nonisotropic vectors e+u,e+v,e+u+v, and the construction can absorb additional planes if needed. In the diagonal triple the five consecutive pairings vanish and the other five are c_0,-c_0,d,-c_0,a. The alternating two-plane-pair formula has all consecutive pairings zero and all nonconsecutive ones equal to one in characteristic two. The vectors give distinct projective points and distinct ring-vertex lifts, so C5 is induced with clique number 2 and chromatic number 3. The filtration gives |R|=q^(r+t+2); the rank-three F2 model has unit, associative multiplication since all triple products in m vanish, and realizes equality 32. The frozen verification note and prime-field script were inspected, not executed. The 13 reported finite checks neither cover arbitrary fields or mixed characteristic nor replace the intrinsic proof.

## originality

FAIL

The main threshold assembles already covered projective-orthogonality cases. The key nonalternating rank-three obstruction is the classical graph ER_q, not a new graph family; the 2014 Tait–Timmons Petersen-subgraph theorem plus C4-freeness forces an induced C5 for every q>=3, and the remaining ER_2 is a seven-point graph with an immediate five-point check. Every higher nonalternating rank contains this three-dimensional projective subgraph. The distinct indexed extraspecial symplectic construction already provides the alternating obstruction, and the distinct indexed Gorenstein rank-two decomposition lifts directly to arbitrary radical by the projective fiber counts. Neither lack of coefficient-field embedding nor mixed characteristic changes any of these adjacency decisions. The explicit coordinate witness and length-filtration cutoff are useful self-contained deductions, but no independently distinct structural regime survives the comparison. This judgment credits precise coverage, not chronology of later catalogue entries, and is not based on inaccessible texts.

## value

PASS

As mathematics, the rank criterion classifies a natural family of short local rings and makes the obstruction explicit without assuming a coefficient field. The projective structure and minimal order are interpretable; this value does not establish independent originality for combining the known graph cases and the elementary lift.

The dated certificate retains the supplied scientific assessment, sources and limitations.
