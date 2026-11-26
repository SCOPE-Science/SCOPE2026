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

Let d=m−1. The degree-three zonal harmonic comes from (x·z)³−3|z|²(x·z)/(d+2) for unit x; normalizing to 1 at z=x gives P₃=( (d+2)t³−3t)/(d−1). The addition theorem with probability surface measure yields K=D_m⁻¹EE* as the matrix of this polynomial at the pairwise inner products. Direct dot products give (m−4)/(2(m−2)) for overlapping pairs and −2/(m−2) for disjoint pairs. With B the unsigned incidence matrix, BB*=(m−2)I+J, so constants, B*(1⊥), and ker B split sample space orthogonally with the stated dimensions. The overlap adjacency is B*B−2I, and the disjoint adjacency is J−I−(B*B−2I). Their joint weights are (2(m−2),(m−2)(m−3)/2), (m−4,−(m−3)), (−2,1). Substitution and clearing 8(m−2)⁴ give the three stated factors; exact integer substitution also matched for 5≤m≤80 in a fresh bounded replay, which does not replace the factorization. All factors are positive for m≥5 except the middle eigenvalue at m=8. There the diagonal spectrum by sector is 4/3,0,4/3 and the nullity is 7; feasible y are exactly those with By constant. The minimal interpolant is (3/(4D_8))E* y because EE* acts on feasible data by 4D_8/3, and it is perpendicular to ker E. D_8=77, yielding the stated norm squared and kernel formula. λ₀−λ₂ factors with the sole zero m=8 on the integer domain, excluding any other flat case. The three sectors refer to invariant summands, not three distinct numerical eigenvalues at resonance. The frozen supporting script was inspected, not executed.

## originality

FAIL

Two distinct indexed findings provide exact coverage rather than merely using the same method. The hypersimplex result specializes at k=2 to these very nodes and degree, with the first-sector defect at (8,2). The simplex-edge all-degree record has the same explicit three eigenvalues, multiplicities and isolated cubic rank defect. Their exact Gram data also fix the flat projection and canonical minimum-norm reconstruction by the pseudoinverse. Both entries have later catalog dates; this is a finding of exact/stronger catalog coverage, not a finding of prior authorship, precedence or dependence. No separate substantial remainder of the frozen claim is left by retaining only the reconstruction or its norm constant.

## value

PASS

The natural simplex midpoint orbit yields a uniform interpolation criterion and a unique, structurally explained loss of incidence modes with tight reconstruction on the quotient. This is useful spectral information about harmonic sampling across dimensions; it is not just a table of ranks or an arbitrary numeric case. The failure is on distinct catalog coverage, independent of that mathematical significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
