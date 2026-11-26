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

The scope is one scalar terminal output, not full-state controllability; no renormalization of the indicator functions is used. Limits are along endpoint-aligned meshes only. The continuum overlap is zero through T*=g/v and equals vt-g on the rising part ending at (g+a)/v. For the upwind system the nilpotent shift exponential gives a Poisson kernel. The number of source–target pairs of cells at offset n+r is min(r,2A-r) for 1≤r≤2A-1; in particular the first term is at n+1, not n. The output contributes exactly one factor of h. This gives strict positivity and Cauchy–Schwarz gives minimum squared input norm 1/G_h. For fixed subcritical T, the response divided by h times the Poisson mass at n tends to ρ/(1-ρ)² near T, by the geometric ratio bound, where ρ=vt/g. The same upper bound with ρ replaced by its maximum below T-δ controls the earlier integral by a strictly larger exponential rate. Stirling gives the response scale h^(3/2); squaring and integrating on the endpoint scale h/[2(g/T-v)] gives the asserted h^4 prefactor and exponential. In the arrival window the centered Poisson law converges to Z+s with bounded second moments; since A/√n tends to infinity, the triangular truncation contributes vanishing error after division by √n. For z≤0 with λ=n+z√n≥0, Cauchy–Schwarz bounds E(N_λ-n)_+ by √λ times √Pr(N_λ≥n), at most √n exp(-z²/4) by the Poisson rate inequality -log(1-u)-u≥u²/2. This justifies an integrable bound for the squared rescaled response over the growing negative half-window; on bounded nonnegative z the second moment bound suffices. The time scaling supplies the remaining √(gh)/v. For the critical integral let Q(w)=Φ(-w) and J=∫₀^∞φ²=1/(4√π). Integration by parts gives ∫wQφ=1/(2√(2π))-J and ∫w²Q²=(2/3)[1/√(2π)-(5/2)J], with both integrals over w≥0. Expanding (φ-wQ)² yields (1-1/√2)/(3√π). Above arrival, the overlap as a function of the physical Poisson shift is bounded and Lipschitz, while hN converges in mean square to vt, yielding the stated Gramian limit on the stated interval. Inspected checks/upwind_gramian_check.py without executing it: finite matrix exponential and numerical asymptotic diagnostics, not a limit proof.

## originality

PASS

The indicator travel-time example, numerical-diffusion artifact, and probabilistic description of upwinding have prior coverage. The supported distinct contribution is the sharp subcritical scalar Gramian prefactor and rate with the unit-target energy reciprocal, and the integrated Gaussian moving-arrival law with evaluated critical constant for the stated fixed geometry and semidiscrete mesh family.

## value

PASS

The problem measures when a scalar reachability test on an upwind grid conflicts with finite physical propagation. Exact positivity alone hides an exponentially large energy cost whose power and prefactor are now specified. The arrival-window law distinguishes that artifact from genuinely reachable output and gives a testable scale for the transition. The leading constants being independent of a fixed positive interval width makes this more than a numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
