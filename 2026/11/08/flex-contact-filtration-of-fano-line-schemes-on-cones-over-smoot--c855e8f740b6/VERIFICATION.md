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

PASS. The Grassmannian line chart writes a nearby ruling as (W,X0,X1,X2)=(s1,s0,a s0+b s1,c s0+e s1); the cone polynomial restricted to this line has coefficient equations f(a,c)=0 and f_x b+f_y e=0 followed by jets u^j h_j(a) for j>=2. Smoothness solves c=phi(a), e=phi'(a)b; tangent contact r means phi(a)=gamma a^r+..., and the jet coefficients have valuation r-j for 2<=j<=r. In char 0 all leading binomial coefficients nonzero, giving completed ideal (t^(r-2)u²,t^(r-3)u³,...,t u^(r-1),u^r); nonflex r=2 has generic square-zero. Global tangent-direction geometry gives first nilradical layer O_C(1) tensor K_C=O_C(d-2). For j>=2 the finite sheaf N^j/N^(j+1) has length r-j at a flex, summing C(r-1,2); Riemann-Roch and Hessian contact total 3d(d-2) give 2dn+d+Σflex C(r-1,2). Checked pinned artifacts/verify_cone.py, and independently computed jet orders for r=2..8, finite lengths and Fermat d=3,4,5 polynomial values (6n+12,8n+40,10n+95), all matched. Full all-curves proof is algebraic, not based on finite checks.

## originality

PASS

PASS with explicit known d=3 special case. A 2026-11-08 published full RESULT.md Nine flex-supported embedded points in the line scheme of an elliptic cubic cone proves exactly the complete degree-three specialization: nonflex u², flex (tu²,u³), O_E(1), nine length-one embedded points, Hilbert 6n+12. It does **not** imply higher-degree contact filtration r>=4, hyperflex correction, or Fermat quartic 8n+40. Eisenbud–Harris's classical nonreducedness example is broader in object type but weaker in local scheme detail, and Ilten's toric surface theorem is outside the non-toric smooth degree>=3 plane-cone class. This all-degree theorem genuinely extends the known cubic case. Specialist unindexed priority remains a stated risk.

## value

PASS

PASS. The full infinitesimal structure of the natural Fano line scheme on a projective cone is a meaningful scheme-theoretic invariant, not just counting its reduced ruling curve. The exact higher nilpotent filtration is controlled by tangent contacts and produces a computable hyperflex correction in the Plücker Hilbert polynomial for every smooth plane curve d>=4. In particular Fermat quartic 8n+40 differs from ordinary-flex 8n+28; this nontrivial extension remains valuable despite prior degree-three coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
