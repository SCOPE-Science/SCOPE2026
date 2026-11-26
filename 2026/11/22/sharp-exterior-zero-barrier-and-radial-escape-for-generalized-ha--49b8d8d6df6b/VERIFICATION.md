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

With C_m(z)=Σ_{j=1}^m j(m+1−j)z^{j−1}, coefficient comparison gives Q=αC_N+(1−α)C_{N−1} and (N+2)C_{N−1}=(1−z)C_N'+(N−1)C_N. The Chebyshev identity e^{−i(m−1)θ/2}C_m(e^{iθ})=U_m'(cos(θ/2))/2 (from the generating function or the finite sum) and Rolle give exactly m−1 simple unit roots, none at 1. An independent strict-exclusion argument uses w=(1+z)/(1−z), A(w)=(w+1)^{N−1}C_N((w−1)/(w+1)). All zeros iβ of A are distinct and imaginary. The transformed Q is proportional to α(N+2)A+(1−α)(w+1)A'. In Re w≥0 off the zeros of A, division by (w+1)A gives α(N+2)/(w+1)+(1−α)Σβ1/(w−iβ), with strictly positive real part; at A=0, the derivative term is nonzero for 0<α<1. The excluded Cayley point z=1 has positive Q(1). For ε=1−α, simple-root differentiation at ζ gives z'(0)/ζ=(1−ζ^{−1})/(N+2); its real part gives exactly the stated radial coefficient, with a quadratic remainder at fixed N. For the kernel, direct monomial integration gives squared norms π²/[j(1+k+j/γ)] for z_1^{j−1}z_2^k, integrable when the denominator is positive. Writing h=j+k reduces π²tK_γ(tv,t) to terms j(1+h−jδ)v^{j−1}t^h with h≥0 and j<(h+1)/δ. The h=0 term is P_δ and the remaining power series converges uniformly on fixed v-disks for t sufficiently small (each h-layer has at most polynomial times exponential growth in h). The normalization (1−t)^2 does not change the limit. A positive minimum of |P_δ| on the closed unit disk proves kernel nonvanishing there for nonendpoint α. At α=1 it gives no such conclusion; small disks around the exterior roots for nonendpoint α retain the zero count by Rouché, with multiplicities. Independent companion-matrix checks passed for 420 interior roots and 105 endpoint roots and radial increments, N=2–15.

## originality

PASS

The vertex limit and kernel zeros near the vertex are known, as are the same polynomial's real-root classification and simplicity information. The supported increment is strict exteriority for every complex zero, the complete unit-circle endpoint location and quantitative endpoint radial motion. The local zero-free core is an immediate, correctly limited application of that new location information to the known uniform limit, not an independent novelty claim.

## value

PASS

The fixed unit disk is the natural diagonal-scale core of the vertex section. Strict complex-root location decides which side of its boundary the nearby zeros occupy, a question not answered by real-root or angular classification. The exact positive speed for each endpoint root quantifies the loss of the barrier margin as the exponent approaches a discrete endpoint. Both facts have a use in local Bergman zero geometry even without any assertion about global kernel zeros.

The dated certificate retains the supplied scientific assessment, sources and limitations.
