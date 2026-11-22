---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Class-B (odd) sublattice Voronoi diamond |x|+|y|<=1 identifies nearest-B distance t. On symmetric wedge x>=y>=0, nearest class-A site is (1,0) and A-distance²=1-2x+t². At fixed t, minimizing admissible x gives diagonal x=t/sqrt2 for t<=1/sqrt2 and boundary x=(1+sqrt(2t²-1))/2 above, so worst A-distance² is 1-sqrt2 t+t² or t²-sqrt(2t²-1). Both decrease in t; taking t>=s gives exact necessary/sufficient F(s), with F=0 for s>=1. For w>0 the objective restricted to s<=1 has unique minimizer s1=1/(sqrt2(1+w)) on lower branch with E1=1-1/(2(1+w)), and unique s2=sqrt((1+(1+w)^-2)/2) above with E2=((1+w)-(1+w)^-1)/2. E2-E1=(w-1)/2 proves the full global threshold and both minimizers at w=1; s>=1 cannot beat the endpoint. Differentiate to give left slope 5/8 and right slope 1/8. Edge cases s=0,1 included.

## originality

PASS

On the stated bounded primary literature and Resultary comparisons, the exact final claim is neither stated nor directly implied by the identified relevant antecedents; known special cases and methodology were credited. This is best-of-knowledge, not proof of global novelty. See four explicit implication checks, actual source inspections, and residual risks.

## value

PASS

Fixed-site heterogeneous sensor deployment with class-specific prices naturally asks for the full cost-price optimal covering frontier. This yields complete sharp geometric resource allocation and abrupt switching under asymmetric prices, explicitly motivated as an open cost-generalization direction by the 2015 foundational design paper; known equal-price special case is not reclaimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
