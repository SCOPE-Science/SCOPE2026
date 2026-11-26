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

The skew-polynomial PBW rule yields the displayed commutator matrix after division by the nonzero zeta-1; the only outputs are xy, x²y, xy² and x²y². For a nonzero linear part, the first row, the independent degree-two restrictions in the middle rows, and the nonzero degree-three restriction in the last row give rank four. With zero linear part, the middle block has determinant zeta ce-d². If (c,e) is nonzero the last row adds one to its rank; if c=e=0 and d is nonzero the last row adds nothing to rank two. The zero quadratic part gives rank one precisely when the degree-three part is nonzero. The cone has (q-1)²+(2q-1)=q² points, so the rank-two triples count as q²-1 on the cone plus q-1 off it, and the rank-three triples number (q-1)(q²-1). Free coefficients then give the full table, valid also in characteristic two since the root identities and the independence arguments do not divide by 2. Commuting in 1+J is equivalent to commuting in J; scalars do not affect ranks, and an element of rank r has class size q^r. Dividing the element counts by q^(r+1) and summing reproduces k=q^4+2q³-2q and the stated probability. The frozen verification documents and output cover slices over F_4, F_7 and F_13, not full enumeration of all q^9 elements; the uploaded checker was not executed.

## originality

PASS

A distinct, broader same-day record proves a table whose generic row exactly covers the primitive-cube adjoint ranks and thereby the group class-size counts through orbit–stabilizer. It expressly identifies that specialization as prior work and credits the primitive-cubic adjoint-rank and conjugacy-class census, which the matched title resolves to this frozen record. That is substantive coverage by an extension, not evidence of an independently antecedent discovery. The pass rests on that explicit direction of attribution and the comparison with other accessible prior claims, not on the date or a lack of exact hits. The group reweighting is not independently novel once the adjoint distribution is given.

## value

PASS

The exact adjoint spectrum is a natural invariant of this local algebra and determines the complete class-size distribution in its algebra group. The quadratic cone and the off-cone pure-xy exceptions give the nontrivial middle ranks; neither a generic-rank computation nor the available left-multiplication invariant determines their multiplicities. The result gives a characteristic-uniform exact census at the primitive cubic twist, useful as the baseline against which the separate order-four rank disappearance is visible. Value lies in the whole census, not in the routine summation or class-size conversion by themselves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
