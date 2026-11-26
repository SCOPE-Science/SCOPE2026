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

After m shifts, every constraint with j≤m is established by the update and inherited by shifts; at m=d−k the last k coordinates are precisely the original first k. For 0≤m<d−k the constraint at j=m+1 still compares the independent initial coordinates x1 and x(k+1) for uniform input and holds with probability zero, so the stationary pushforward is not reached earlier. On the graph the first new trailing coordinate is T of the old last trailing coordinate, giving G and hence G^k=T×…×T. The graph is bi-Lipschitz to the k-cube via its projection, and hence has ambient measure zero. T^m has 2^m equal-length full branches; the transfer iterates take cylinder-constant functions to their mean and approximate arbitrary L¹ densities by contraction. The same holds in product cylinders, and the bounded residue of iteration of G modulo k preserves this limit. The first k marginal of an ambient density is absolutely continuous, and the graph parametrization preserves the TV comparison. Ergodicity also gives Birkhoff convergence for these initial densities; a delta at the all-(1/3) fixed point is a concrete singular exception. On the stationary graph each time residue modulo k depends on a different independent uniform seed, with each strand undergoing T. Direct inverse-branch averaging gives Pt=0 and Pb=b/4−t/2 for b=t²−1/3, so ∫b²=4/45 and ∫tb=0 give the exact covariance including lag zero. The Fourier series is absolutely convergent and gives the stated Poisson kernel in kω, not point masses. For the CLT, v=b/3−2t/3 satisfies Pv=v−Pb, and m=b+v−v∘T has Pm=0. Thus m∘T^j is a bounded stationary reverse martingale difference for T^{-j} of the Borel σ-field; conditional variance averages converge by ergodicity. The telescoping difference is bounded, so the martingale variance is the covariance sum 4/27. Independence of the k strands and their sizes N/k+O(1) gives the claimed fixed-k limit.

## originality

PASS

The recurrence, its dimension reduction and standard tent-map tools are established. No distinct inspected source specifies the endpoint's exact uniform-in-trailing-coordinates stationary graph law with the fixed-lag squared-coordinate fluctuation statistics. The assessment is limited to the stated endpoint and the named observable.

## value

PASS

At a natural rank-degenerate boundary, the exact collapse clock and TV law explain why ambient densities reach a singular stationary regime. The observable contrast is substantive: every nonzero linear lag is silent, while centered squares reveal the delay through the spectrum and inflate the variance of the time average by 5/3. The finding covers all fixed d>k≥1; it does not imply a nearby-parameter or growing-delay theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
