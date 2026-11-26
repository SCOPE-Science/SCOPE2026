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

Conditioning on the last reset gives a renewal term and a no-reset term of weight exp(-rs). The latter vanishes in trace norm as elapsed time s grows, giving the age mixture as the unique stationary state. Transmissivity has density kt^(k-1), k=r/gamma. Pure loss attenuates both coherent amplitudes by sqrt(t) and multiplies their off-diagonal dyads by the environment overlap exp(-2A(1-t)); the resulting Gaussian terms and cosine fringe give the quoted normalized Wigner formula. After factoring out its positive Gaussian, the remaining function is its origin value plus nonnegative cosh-minus-one and one-minus-cosine averages; each average vanishes only on its own coordinate axis. Pairing t with 1-t fixes the origin sign on either side of k=1 and its negative derivative -h(A) at k=1. Near the threshold the second-order spatial coefficients are a=8AB_x and b=8AB_y, both positive. Away from the origin the cosh increment is uniformly positive outside any fixed x interval, and the one-minus-cosine increment is uniformly positive away from y=0 by compactness and the large-|y| Fourier limit; after t=s² the Fourier weights form a compact L¹ family in k near one. Thus no remote negative components contribute near onset. A positive definite Hessian in a fixed ball gives one convex negative component and bounds it within radius O(sqrt(k-1)). After rescaling, uniform convergence of the signed bracket on bounded sets sandwiches the region between nearby ellipses. Integration of the limiting bowl yields pi h²/(2 sqrt(ab)); with the Wigner prefactor it gives exactly C(A). Independent odd-Fock binomial thinning corroborates the origin sign/zero, and independent Gauss–Legendre and polar quadrature for A=1 gives N/epsilon² tending to 0.1185724728353, with value 0.1185403694 at epsilon=0.00016.

## originality

PASS

Best-of-knowledge pass for the strict whole-plane sign classification and amplitude-dependent negative-volume onset of the stationary odd-cat Poisson mixture. The known fixed-loss threshold and general reset formula are credited. The closest distinct Resultary matches have substantial methodological or threshold overlap but their available statements do not entail the complete coherent odd-cat result; several primary passages remain inaccessible.

## value

PASS

In a stationary resetting experiment with an unobserved age, Wigner negativity is a property of the mixture, not a statistic of which trajectories fall on the negative side of the deterministic loss threshold. The amplitude-independent rate threshold and single critical zero determine when the stationary resource survives. The explicit amplitude-dependent quadratic onset then quantifies how small the usable phase-space negative volume is close above threshold, beyond a sign at one point. The single-component statement also identifies the geometry relevant to that onset.

The dated certificate retains the supplied scientific assessment, sources and limitations.
