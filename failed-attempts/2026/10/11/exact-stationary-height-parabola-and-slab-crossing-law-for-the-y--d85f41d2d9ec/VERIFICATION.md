---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For a,b,c>0, compact invariance gives ∫Lf dμ=0 for polynomial test functions. The four exact derivatives are L(x²/2)=a(xy−x²), Lz=xy−bz, L(y²/2)=cxy−xyz, L(z²/2)=xyz−bz². Thus E[x²]=bE[z], E[z²]=cE[z], and Var(z)=E[z](c−E[z])≥0. Independent differentiation also gives L(y²+z²−2cz)=−2bz(z−c). The endpoints E[z]=0,c force zero variance/rigid support at the origin or at (±√(bc),±√(bc),c). If the sign-defect z(z−c) vanishes identically on an invariant support, continuity and tangency imply only these three equilibria; hence a non-equilibrium ergodic measure has positive mass in both q<0 and q>0 regions. For a positive-height nonconstant periodic orbit this means visits 0<z<c and z>c.

## originality

FAIL

A 2026-10-04 published SCOPE/Resultary theorem for the normalized T-system already proves the EXACT Yang–Chen stationary-moment parabola, both endpoint cases, and a stronger slab-crossing theorem. The entire Yang–Chen family with a,b,c>0 becomes that T-system by τ=a t, (X,Y,Z)=(x,y,z)/a and (m,n)=(c/a,b/a). All submitted formulas and quantifiers are inherited, not original. This is definitive implication coverage rather than a failed search or matching title.

## value

FAIL

Exact invariant-measure height laws and slab escape can be meaningful mathematical invariants, but this submission gives only a units/time normalization of a prior complete T-system classification, with no new domain, obstruction, independent boundary case, sharper inequality, unknown invariant or novel structure. The earlier T theorem is strictly stronger (conditional regression and slab crossing for every non-equilibrium-supported stationary measure). Even as a model-specific computation, the precise Yang–Chen fact is mechanically implied and lacks independent scientific value under the requested bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
