---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The dense parameterization is the toric monomial map (u,v,w)↦(u_iv_j,u_iw,v_jw), which is an immersion up to common scaling. Pulling a hyperplane back gives homogeneous quadratic u^TMv+wα^Tu+wβ^Tv. Its tangency gradient is (Mv+wα,M^Tu+wβ,α^Tu+β^Tv)=0. For generic full-row-rank M and w=1, this is precisely β=M^Tλ and λ^Tα=0, equivalent to rank≤a of T=[M α;β^T 0]; generic solutions with all torus coordinates nonzero exist. The rank≤a locus inside southeast-zero hyperplane is irreducible because each matrix factors PQ with rank factor a and constraint (PQ)_{last,last}=sum_{i=1}^a P_{last,i} Q_{i,last}=0, an irreducible polynomial for a≥2, so its generic tangencies are dense. Its open affine dimension ab+2a−1 in coefficient ambient ab+a+b gives codim b−a+1. The generic maximal-minor determinantal degree binomial(b+1,a) is unchanged by a proper non-contained projective hyperplane section. The Mv=−α solution affine fiber of dimension b−a maps linearly to contact closure P^(b−a); a=b yields adjugate determinant. Direct symbolic balanced a=b=2 and rectangular a=2,b=3 cases independently checked torus tangency, augmented rank, and adjugate identity. General proof independent of these small checks.

## originality

PASS

Classical maximal-minor determinantal degrees and Cayley/toric dual defect theory are established, as is toricity of regular positroids (McNeill). Neither gives the specific full augmented matrix equations, degree, and generic linear contact locus for (a,b,1). Earlier three-class rank-two positroid singular-stratum results concern the primal, not the projective dual. A possible graph A-discriminant alias or a general theorem covering K_{a,b,1} is residual risk, but no exact implication was found in inspected material.

## value

PASS

It determines the entire projective dual variety, degree, defect and contact geometry in an infinite natural family of toric positroid embeddings. This is a genuine geometric classification with balanced/hypersurface phase transition and exact determinantal equations, not a routine isolated numerical calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
