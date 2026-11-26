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

The independent exponential backward age of the reset Brownian bath gives the stationary characteristic function r/(r+Λ²q²), hence its Laplace law; coupling at the first reset gives uniqueness. Conditional on A_t=∫_0^t ω_s² ds the tracer is N(0,2A_t), and regeneration gives A_t/t→2Λ²/r for either initialization. Conditional bath second moments give covariance (20Λ⁴/r²)e^{−rs}; integrating it over the time square and multiplying Var(A_t)/(E A_t)² by 3 yields exactly the stated 30 coefficient. Strict decay follows from (z−1+e^{−z})/z²=∫_0^1(1−v)e^{−zv}dv. For the fixed-time tail, on the event sup|B_s|≤δ x^{2/3} the full future noise, including increments between reset times, adds at most 2√2Λδ x^{2/3} to the bound on |ω|; the complementary event is exponentially negligible on the x^{2/3} scale. For the upper Laplace integral one can split the scaled initial amplitude into a fixed compact interval and an exponentially bounded far tail. As δ goes to zero the minima stay away from zero and infinity. The no-reset lower event with a restricted slab of initial amplitudes realizes the matching cost a y+1/(4ty²), a=√r/Λ; its minimum is 3(a²/t)^{1/3}/2^{4/3}. Symmetry gives divergence for both signs of k, and Jensen and the finite stationary bath moments give finite polynomial moments. Independently of the Riccati derivation, the largest covariance eigenvalue of Brownian motion on [0,u] is 4u²/π²; the Gaussian product for exp(2Λ² k²∫ B²) is finite exactly when 4Λ²k² times this eigenvalue is less than one (the remaining eigenvalues are summable). Conditioning on Poisson intervals bounds the subcritical transform by a finite Poisson exponential moment, while the no-reset event proves divergence at and above the cutoff.

## originality

PASS

The supported distinct claims are the exact stationary-bath kurtosis and sharp fixed-time tail for the bath-only reset protocol. The invariant bath law and regenerative Gaussian limit use standard ingredients, and the zero-start cutoff transfers the classical no-reset Brownian quadratic-functional cutoff by elementary conditioning; these are not independently credited as new mechanisms. The model with simultaneous resets explicitly distinguishes the bath-only protocol, and the close indexed 2/3-tail results do not identify the same claimed rate under the same initialization and limit.

## value

PASS

Resetting an environment without resetting the observed coordinate is a distinct protocol explicitly raised in earlier work. The exact kurtosis resolves the crossover to the Gaussian bulk, while a sharp fixed-time displacement rate and the contrast with a zero-start transform cutoff show why the bulk limit does not control rare events or exponential moments. These answer natural model questions at different, explicitly separated limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
