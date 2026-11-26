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

Grouping matrix entries by row and by lag gives the cross Gram series F(ts)=(ζ(2)−Li₂(ts))/(1−ts). Integrating −log u/(1−u) from 0 to the deficit gives F(1−h)=1−log h+O(h|log h|). In its three-term difference the constants and −log ε cancel, leaving 2log(a+b)−log(2a)−log(2b) with the stated remainder. Independently, the embedded kernel has denominator ε(n+1) on (n,k) cells; for x>y the mesh powers tend to the two exponentials. A direct domination is also available: for j=n−k≥1 the numerator is bounded by |a−b|jε exp(−min(a,b)(j−1)ε); jε≤x, and for x>1, jε differs from x−y by at most ε. Thus the kernels are bounded on 0≤y<x≤1 and bounded by a constant times exp(−min(a,b)(x−y)/2)/x on x>1, both square-integrable on their regions. Cells with j=0 have zero numerator. This independently gives L² convergence, consistent with the frozen weak-plus-norm proof. Tonelli in u=x−y and Frullani evaluate the squared kernel norm as the same logarithm. The Schatten-2 singular-value inequality controls the entire zero-padded ordered list and the isometry preserves nonzero singular values. The equality case a=b vanishes; the identity with 2log cosh(log(a/b)/2) and scale invariance follow by algebra. The strong limit uses entrywise domination by the bounded C₁ and finite supports; normalized indicators of successive escaping intervals [N,2N] give a norm bounded below for C₁ on a weakly null sequence, verifying noncompactness. Frozen check.py was inspected, not executed: its finite rational identity and quadrature diagnostics are not the kernel or spectral proof.

## originality

PASS

The supported distinction is the two-rate endpoint blow-up of C_t−C_s in Hilbert–Schmidt norm on a common step-function embedding, with identification of the complete limiting singular sequence via the continuum operator. Fixed-parameter compactness, individual Hilbert–Schmidt norms, spectral edge laws and operator-norm endpoint discontinuity are prior work; the logarithmic scalar calculation from the Gram formula and the standard singular-value inequality are not standalone novelty claims.

## value

PASS

The natural family of compact matrices has a common strongly convergent, noncompact endpoint. The identified nonzero Hilbert–Schmidt continuum operator resolves how a fixed ratio of approach rates is visible despite that strong limit; the scale-invariant distance and convergence of the whole singular list provide a quantitative model of that boundary. This is not merely an endpoint norm recomputation or an isolated number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
