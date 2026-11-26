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

Write s=H restricted to [0,1), π for fractional part, and G(t)={1111t}. Integer gains give H=sπ and G=πs pointwise, including all discontinuities (thus the globally typed relation is πH=Gπ). The identity H^n=sG^(n−1)π gives the unique lift of each G^n-fixed point, hence the stated census and zeta. Invariance makes s_* and π_* inverse on invariant probabilities; the two factor maps preserve ergodicity and give entropy equality by monotonicity in both directions, not by asserting pointwise conjugacy. Lebesgue on the circle is the exact uniform 1111-symbol shift, and s pushes it to an absolutely continuous law by affine change of variables; any absolutely continuous invariant law projects to an absolutely continuous invariant circle law, which is unique by exactness. Birkhoff applied to s composed with a countable convergence-determining set of bounded continuous tests gives physicality. The branch formula gives nonuniform density (near zero only the first affine interval contributes); the total variation is 1111+999+99+9, so coupling a uniform t with the grid point immediately to its left establishes the W₁ bound. For the covariance I also obtained P( {at}−1/2 )=({at}−1/2)/1111 for the Lebesgue transfer operator P of G when gcd(a,1111)=1: the residues a j modulo 1111 permute the branches. This gives the all-lag scaling directly. The sawtooth pair integral from matching Fourier harmonics gives Var=(4+2(3/10+2/100+1/1000))/12=2321/6000; geometric summation gives the normalized spectrum in the stated convention. The frozen checker was inspected, not executed; analytic identities establish the universal claims.

## originality

PASS

The map itself and the basic circle-map and sawtooth tools are prior art. Credit is for the explicit arithmetic identification and the joint periodic, stationary-law and all-lag consequences for the published map. No inspected different result evaluates this package or makes the claimed specialization directly available as its stated corollary.

## value

PASS

The gains and map come from a published example, not an arbitrary numerical slice. The factorization determines all invariant laws and all fixed-point counts rather than just the instability of a typical orbit. The exact variance, density and all-lag spectrum give a benchmark for a concrete nonuniform observable: a simple geometric law for memory despite the nonuniform one-time distribution. They can be used to distinguish exact dynamics from numerical artifacts without treating them as evidence about security.

The dated certificate retains the supplied scientific assessment, sources and limitations.
