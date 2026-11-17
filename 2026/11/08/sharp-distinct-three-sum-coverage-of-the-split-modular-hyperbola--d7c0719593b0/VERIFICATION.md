---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For char(F)>=5, recalculate yz=x(s-x)/(tx-1) and the quadratic-discriminant correction for y=z and x=y or x=z: the two collision polynomials have discriminant (st-1)(st-9). This gives R=q+sum(chi(D))-4-3(1+chi(Delta)) for st not 0,1,9. Degeneracies st=1, st=0, st=9 and (s,t)=(0,0) give exactly the asserted four branches. The generic squarefree quartic has square leading coefficient, two rational points at infinity, and Hasse |a|<=2 sqrt(q), yielding R>=q-11-2sqrt(q)>0 for q>=23. Explicit tested prime-field missing targets establish sharpness for all smaller allowed field orders. Independently enumerated 4,714 prime-field target fibers; none disagreed. Finite enumeration is corroboration, not the infinite proof.

## originality

PASS

The 2012 scalar coordinate-sum study and 2014 restricted scalar-sum result do not determine two prescribed coordinate sums with three distinct inverse-graph points. Two fully read published split-hyperbola theorems already establish unrestricted 3H_q support (q>=13) and a stronger ordinary ordered convolution formula, but neither their unrestricted coverage nor their three-step support implies distinct summands or the sharp distinct q=23 threshold (q=19 has missing nonzero targets). The new character formula is closely related to subtracting collision contributions from the earlier R3; novelty resides primarily in collision-free exact fibers and the sharp restricted threshold, not in discovery of elliptic convolution itself.

## value

PASS

The canonical inverse graph is a natural additive basis. Requiring three distinct summands changes the uniform covering threshold from 13 to 23 and yields exact representation counts and the structural origin obstruction, substantive additive-combinatorial information that can be used independently. Finite small-field gaps are essential to the sharp infinite classification rather than arbitrary tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
