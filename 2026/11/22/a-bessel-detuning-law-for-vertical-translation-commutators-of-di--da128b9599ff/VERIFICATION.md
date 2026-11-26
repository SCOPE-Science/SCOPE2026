---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The positive-characteristic symbol criterion applies also at the comparison symbol with c=a, where Re(a+a2^−s)>0 on Re s>0. Factoring off the compact diagonal n^−(c−a) proves compactness. Translation multiplies e_{2^k n} by n^−iτ exp(−ikθ); distinct k within a single column are orthogonal, and different columns need not be. The k=1 coefficient proves the converse to exact resonance. The exact column Bessel formula follows, and for a fixed nonzero representative |θ|≤π the complex I_0 term has smaller exponential rate by the angular integral, including θ=π; the positive diagonal part is asymptotic to e^(2a log n)/sqrt(4πa log n). This gives the endpoint-divergent test ∑n^−2(c−a)/sqrt(log n). Independently reobtained both limit constants using the angular integral: at c=a+1/2+ε, sum the Bessel series over n by integrating ζ(1+2a+2ε−2a exp(iθ/2)cos t)−1 against dt/(2π). For ε>0 the positive majorant permits the interchange. Subtracting the pole leaves a uniformly bounded integral as ε→0 (the pole-subtracted zeta function is entire and its arguments lie in a fixed compact set). The integral of the pole is [(2a+2ε)^2−4a² exp(iθ)]^−1/2, with the branch continued from zero cosine coefficient; this follows from the real angular integral and analyticity for |2a exp(iθ/2)|<2a+2ε. Its radicand is 4aε(2−iav)+O(ε²) when θ=εv. The positive pole on θ=0, the factor two in the norm, and the real part of the complex pole give exactly both stated profiles. The principal branch agrees near detuning; for x>0, Re(2−ix)^−1/2 is strictly decreasing since its derivative is −(1/2)|2−ix|^−3/2 sin[(3/2)arctan(x/2)]. No general p or boundary c=a claim is needed. The packaged numerical tail uses a sum-to-integral approximation only and was not used to certify the theorem.

## originality

PASS

The supported mathematical contribution is the quantitative Hilbert–Schmidt threshold and the critical two-parameter scaling for this characteristic-one translated pair, not compactness of the individual symbols or the Bessel identities alone. No equivalent was found in the inspected primary results and successful indexed comparison. An unavailable lookup is not counted as negative evidence.

## value

PASS

In a compact operator family, the ideal threshold alone says when the squared norm is finite but not how resonance cancels its blow-up. The explicit nonconstant crossover quantifies this loss under a natural vertical action and exposes the scale on which arithmetic cancellation changes the norm. The compactness and exact commutation subcases are background for, not the sole basis of, the value assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
