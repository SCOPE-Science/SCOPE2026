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

With w=1/R and C shared and symmetric, scale the positive eigenvector (x,y) so x+y=1−w. The state (x,y,y,x) solves all four equations and has both vacancy fractions w>0; d=w(a+by/x)<D=w(a+bx/y) forces x>y. For the monoculture, the component equations imply h>ℓ. Its existence and uniqueness follow from the known monomorphic threshold, or by iterating the monotone strictly subhomogeneous map z_i ↦ (Cz)_i/[d_i+(Cz)_i] between a small multiple of the Perron vector and (1,1), then comparing scaled fixed points. With w_0=1−(h+ℓ)/2, the difference between z^TCz and (dh²+Dℓ²)/w_0 at z=(h,ℓ) is a(h−ℓ)²(h+ℓ)/(2w_0)>0: the cross terms cancel using dh²/(1−h)−Dℓ²/(1−ℓ)=a(h²−ℓ²). The symmetric generalized Rayleigh quotient gives R>1/w_0 and hence Q>h+ℓ; the other monoculture is its mirror. In coordinates that exchange the habitat and species labels together, the symmetric and antisymmetric linearized blocks have strictly negative traces and determinants bw(x+y)(ax²+ay²+2bxy)/(xy) and abw(x−y)²(x+y)/(xy), respectively. Both are Hurwitz, proving local exponential attraction in all four coordinates. At (a,b,d,D)=(2,2,1,3), R=8/3 and setting λ=2(h+ℓ) in the monoculture yields λ²=5, verifying the exact gap. The independently computed witness eigenvalues −5/2±√5/2 and −5/2±√5 are negative.

## originality

PASS

Best-of-knowledge pass for the exact strict equilibrium capacity comparison throughout the mirror family, supported by the Rayleigh identity and full local stability. The colonization model, monomorphic threshold and generic positive-equilibrium results are background. Neither inspected positive-equilibrium results nor indexed stability claims in other models supplied the strict total-occupancy comparison.

## value

PASS

The theorem gives a parameter-wide capacity gain despite preemption, relative to the relevant same-system monocultures, and shows that the gain is attained at a full locally stable equilibrium rather than only along a symmetric restriction. The Rayleigh comparison gives the mathematical mechanism for a structural complementarity effect in a minimal model; the exact witness is supplementary, not the extent of the result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
