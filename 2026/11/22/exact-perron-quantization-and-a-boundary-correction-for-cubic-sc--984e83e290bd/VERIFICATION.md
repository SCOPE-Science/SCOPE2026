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

In the scaled coordinate the first nonendpoint Greville nodes are 1/3 and 1. On [0,1] the relevant cubic basis pieces include B₀=(1−z)³, B₁=3z−(9/2)z²+(7/4)z³ and B₃=z³/6; partition of unity and reflection give the stated outer rows. The interior gives the three cardinal entries 1/6,2/3,1/6, including the last piece of B₂ evaluated at z=2. Thus the interior block Q is irreducible substochastic with strict endpoint deficits and positive diagonal; it has simple Perron root below one. Eliminating v₁ gives v₁/v₂=(λ+3)/(3(9λ−5)), and substitution in the second equation gives the stated v₃/v₂. For λ=(2+cosθ)/3, matching the reflection-even cosine profile gives the tangent equation. On the specified interval the tangent strictly increases and g(cosθ)/sinθ strictly decreases (g and g′ positive there), with opposite endpoint order, so there is a unique root. Its interior and boundary coordinates are positive, identifying the Perron eigenvalue rather than another cosine mode. On functions vanishing at the two endpoints the spline synthesis and interior evaluation factorization shares its nonzero spectrum with Q, and on affine functions S_n−L is zero. Since S_nL=LS_n=L, the operator norm-root limit is its spectral radius. The phase equation is nθ+θ³/3+O(θ⁵)=π; hence θ=π/n−π³/(3n⁴)+O(n⁻⁶) and the cosine expansion gives the stated coefficients, including −π⁴/9 at order n⁻⁵. Separate exact collocation replay and numerical residual/asymptotic diagnostics agree; they do not prove the universal result and the submitted script was not executed.

## originality

PASS

Credit is for selecting and uniquely quantizing the cubic Perron root, identifying its norm convergence rate, and evaluating its boundary-phase correction. The exact collocation block and the rational boundary algebra are genuinely shared with the distinct same-day low-edge result. The low-edge theorem is not a broader theorem for the top branch: continuing its proof algebra reproduces the equation, but selecting the positive top solution and extracting its finite-size phase and coefficient are not delivered by its stated sub-band classification. No priority is assigned based on date.

## value

PASS

The asymptotic norm rate is a natural invariant of the classical approximation operator and directly answers the earlier spectral convergence question for a standard clamped degree. The positive-mode quantization gives an exact rate for each allowed mesh and reveals the first boundary contribution that is absent from a bulk-dispersion estimate. This remains useful without determining any other eigenvalue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
