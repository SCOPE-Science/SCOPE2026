---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For the stated continuous-time homogeneous ODE and strictly positive active seed, S+I+R is invariant and I remains positive at every finite time. Integrating d log S/dR=−(B+AR) leaves the scalar flow R'=μ[1−R−(1−ε)e^(−BR−AR²/2)]. A bounded increasing R converges to the first positive zero: a positive velocity at the limit contradicts convergence, and uniqueness prevents passage through any equilibrium, including a touch without a sign change. The derivative of the log level function is q(z)/(1−z), q=B−1+(A−B)z−Az². If A≤B the polynomial stays negative; for A>B its vertex is interior and its value becomes positive exactly above the larger discriminant root (1+√(1−B))². This establishes the smooth, cubic and fold regimes. In the fold regime the local minimum u is the first root at ε_c; all earlier seeds select the left branch and all larger seeds select the right branch, with right limit w>v. There is one jump. At the cusp q=−A(z−z*)², and integration gives H(z)−H(z*)=−A e^(s−s²/2)(z−z*)³/3+O((z−z*)⁴), confirming the signed cube-root coefficient; H(z*)<1 follows by strict decrease. At the fold the velocity coefficient in the gap is μA(v−u)/2 at degree two, and at the cusp it is μA/3 at degree three. Integrating the negative gap derivative gives the two time prefactors. Independent high-precision scalar quadrature (/tmp/opencode/frozen_math_samples_a91d.py, μ=1) gives t(u−R)≈3.99816697 at gap 10⁻⁵ for B=1/2,A=3 (limit 4) and t(z*−R)²≈0.66666167 at the same gap for B=3/4,A=9/4 (limit 2/3); the proof, not those samples, establishes the quantifiers. Frozen verify.py was inspected, not executed.

## originality

FAIL

The central final-size geometry is already a direct specialization of a published stronger result for Poisson hypergraph collapse, not just an analogy with unrelated cusp theory. The exact parameter mapping makes the known first-crossing function identical, yielding the same two selected branches away from the fold, the location of their finite positive seed jump, and the cubic crossing. The displayed constants are algebraic/Taylor evaluations of that same function, not an independent classification. The deterministic ODE selects the lower root exactly at the fold, unlike the earlier stochastic branch mixture, and has physical-time tails not stated in that paper. These are real distinctions, not a reason to certify the frozen claim centered on the static threshold and cusp. No substantive repaired finding was made.

## value

FAIL

The mathematical question is natural, but the principal value proposition—an exact finite-seed jump/cusp diagram—evaluates the already known Poisson collapse curve and selected noncritical roots. Isolated from that overlap, deterministic selection at the exact touch is the usual no-passage consequence of scalar ODE uniqueness, and the two remaining power laws and coefficients are routine integrations of the quadratic and cubic zeros of the same curve after a smooth positive time rescaling. The supplied result establishes no independently valuable new dynamical invariant beyond those deductions (for example, no near-critical delay law uniform in seed detuning). This is a scientific rejection of the frozen finding, not a finding that its mathematics is false or that every use of the model lacks value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
