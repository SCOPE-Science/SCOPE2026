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

Reconstructed RESULT.md, Proof 1–4. The Bloch matrix has an x eigenvalue −2κ and a yz pair −κ±iΩ with Ω²=ω²−κ²>0. The causal mild Volterra equation preserves positivity and trace (positive history mean and Lindblad evolution, with weights summing to one), and Volterra iteration gives uniqueness. Multiplying a scalar mode equation by t and differentiating gives tf″+[1+(q−λ)t]f′−λf=0. For z=q−λ and a=q/z, 0<Re a<1; the normalized regular solution is exp(−zt)M(a,1,zt). Its Euler integral after reflection is proportional to the Laplace integral of s^(−a)(1−s)^(a−1) against exp(−zts); Re z>0 gives leading (zt)^(a−1)/Γ(a) and a relative O(t^−1) error. The real and imaginary parts of a nonreal eigenvector are an independent real basis for the yz plane; with nonzero initial projection the leading oscillation has norm bounded away from zero after removing its decay power. Direct subtraction gives βyz−βx=q(ω²−2κ²−κq)/[(q+2κ)(q²+2κq+ω²)]. Its sign proves both strict dominance regimes, equality of orders at qc>0, and no positive crossing at ω=√2κ. The observable switch requires both initial projections and is at fixed q>0 as t→∞, not at q=0 or at/under the exceptional point. VERIFICATION.md and check.py were inspected, not executed; their finite tests are not needed for the all-parameter result.

## originality

PASS

Credit the scalar uniform-history relaxation, Kummer method, and log-periodicity to previous work. The supported distinction is the exact competition of a real dissipative mode and a damped complex pair of this driven dephasing Lindbladian, with a positive-rate reversal precisely above the stated drive boundary. The strongest reviewed precedents each lack a necessary spectral sector or use a different resetting rule.

## value

PASS

A worked open-system mechanism in which memory can change which physical polarization is slowest, even though all positive rates share the same stationary state. The threshold predicts when a leading log-periodic polarization will be visible rather than subleading and excludes a switch throughout an entire nontrivial underdamped regime. Without resetting the yz pair has the slower exponential envelope, yet for strong drive and sufficiently small positive resetting the real x mode wins at late times. The scientific contribution is that sharp distinction, not a general Lindblad theorem or an experimental claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
