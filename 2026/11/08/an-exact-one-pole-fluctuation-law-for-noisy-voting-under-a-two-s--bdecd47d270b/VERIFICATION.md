---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

C PASS. The finite 2(N+1)-state CTMC is irreducible. Spin-reversal symmetry fixes mean N/2. For m=i−N/2 and conditional state s, the count generator gives L_s(m²)=b_s−c_s m² with b_s=N(a_s+h/2), c_s=4a_s+2h/N. Stationarity of m² 1_{environment=s} closes a 2×2 system with determinant c0c1+λ(r0+r1)bar c>0. Solving and subtracting fast-switch mean gives the positive numerator 8h(N−1)π0π1(a1−a0)². Differentiating its one-pole denominator yields strict negative first and positive second derivatives when a0≠a1. Equal-noise case constant; λ=0 used only as limit, never as unique-stationarity claim. Independent exact-rational finite CTMC stationary solutions for N=2,3,4 match the formula; proof is algebraic for every N.

## originality

PASS

O PASS with qualified priority. The full accessible text of Caligiuri–Galla (2023), Section IV, gives precisely the count jump rates (Eq.22), environmental stationary weights, slow/fast-switching limits, and explicitly says intermediate λ analytical characterization is not easily available (Sec. IV.4), using simulations. Its Section IV assumes equal environmental transition speeds. The new statement is an exact all-N, all-λ, asymmetric-rates moment identity and strict monotonicity of a natural pairwise agreement observable, not a claim to the full distribution or its mode transitions. Other PDMP/LNA and ordinary noisy-voter publications concern approximations or different settings. Method (second-moment closure) is classical, and equivalent telegraph-modulated exact moment results remain a realistic priority risk.

## value

PASS

V PASS. Quantifying how exogenous switching changes a precisely defined finite-population polarization indicator is motivated by the observed bimodal/trimodal stationary shapes. The exact one-pole interpolation, crossover scale λ*, strict monotonicity, convexity and pair-agreement consequence supply a global finite-N law absent from the initiating simulation-based phase diagram. This is a useful exact benchmark even though only one moment, not the full distribution, is determined.

The dated certificate retains the supplied scientific assessment, sources and limitations.
