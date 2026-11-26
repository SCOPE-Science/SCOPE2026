---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Finashin–Kharlamov's Theorems 1.3.1–1.3.2 give the relevant invariance for fixed s=8 and nonempty real locus and W=M/4. In §§7.1–7.2 the first-degree theta sum F gives ΣG_n q^(n+1)=FP. Coordinate symmetry on a norm-s shell converts the root weight 2x_1² into s/4 times the unweighted shell count, so ΣW_n q^(n+1)=(DF)P/16 with D=q∂_q. For q=e^(−w) the Poisson and eta transformations give amplitudes w²/π² and w/(4π²) times exp(π²/w), respectively. Jacobi's identity gives F(−q)=−θ_2(q)^4 θ_4(q)^4, so the negative cusp is only polynomial even after differentiation. On the other arcs the log-product bound gives an exponential loss at least c t^(−2ε) outside the two windows t^(3/2−ε); the theta factors cost only powers of 1/t. At t=π/√(n+1) the linear term vanishes, the cubic remainder is uniformly o(1) for ε<1/6, and the Gaussian factor is t^(3/2)/(2π^(3/2)). The constants, powers, ratio and no-leading-parity conclusion follow. I inspected the finite coefficient checker without executing it; it is not the proof. Independent application of published coefficient estimates below also yields both constants.

## originality

FAIL

The complex row is exactly a four-coloured overpartition sequence. The signed row is a difference of two eta-quotient coefficient sequences (one multiplied by 2n), each covered with sufficiently precise published Bessel estimates. The standard Bessel recurrence evaluates the cancellation and gives the same signed asymptotic on all indices. The failure is explicit prior implication, not absence of an exact conic-bundle statement or inability to retrieve a paper.

## value

FAIL

The fixed-degree signed growth is well motivated and the contour proof is correct, but the exact signed constant, power, parity statement and growth ratio all follow from existing coefficient estimates once the published geometric series are rewritten. No distinct valuable asymptotic claim survives in the finding; there is no repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
