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

In stationary renewal occupation, a cycle of dimensionless length S contributes one unit of age density at each v<S; division by E S=1 gives f_V(v)=Pr(S>v), including for a deterministic clock with equilibrium random phase. The selected square wave has first-harmonic amplitude 4B/pi; at observation the phase is shifted by the age, and visibility restricts v to at least d=r tau. Thus H is the magnitude of the truncated age transform at z=omega/r. Integration of the tail gives E V=E S^2/2 and E V^2=E S^3/3. The omitted integral equals d+o(d), with imaginary or phase error bounded by |z|d^2/2; expanding the full transform and its modulus gives the joint loss d+Var(V) z^2/2+o(d+z^2). For each fixed positive omega the transform is continuous in r, vanishes at infinity by the age tail and at zero by Riemann–Lebesgue plus the vanishing omitted mass. A rate proportional to omega^(2/3) achieves loss O(omega^(2/3)). Any optimizer then has omitted mass O(omega^(2/3)), hence r=O(omega^(2/3)) since f_V tends to one at zero. The full transform has magnitude within O(omega^(2/3)) of one by the triangle inequality. Its absolute continuity, strict modulus below one away from zero and decay at infinity force z to zero, then its positive quadratic modulus deficit gives z^2=O(omega^(2/3)). This puts every optimizer on a common compact interval after rescaling r by omega^(2/3). The uniform joint expansion there reduces the limit to the unique minimum of tau y+Var(V)/(2 y^2), with the stated optimizer and loss coefficients. Cauchy–Schwarz gives E S^3 >= (E S^2)^2 and E S^2 >= 1 with equality of the latter only for S=1; thus Var(V) >= 1/12 with precisely that equality case. The exponential and Erlang moments give the stated benchmarks. Read the numerical checker without executing it; its finite grid/local optimization is not a certificate for the all-global-optimizers assertion.

## originality

PASS

The equilibrium-age identity and Poisson balance are known, and the prior gamma-maturation result covers the fixed-delay Poisson special case exactly. The inspected sources do not give the sharp arbitrary fixed renewal law optimization, its all-maximizers localization, or the exact comparison of inter-reset laws by the age-variance coefficient. The decision is about the stated step-response model, not a broader claim for nonlinear trajectories or frequency-dependent clock selection.

## value

PASS

The result identifies one interpretable clock statistic that controls both the optimal rate and amplitude loss, and gives a sharp deterministic bound across fixed clocks. It improves on guessing the rate from a Poisson expansion by establishing that no competing global maxima occur on other scales for an arbitrary fixed law under a finite third moment. This is useful for comparing renewal protocols within the stated, reproducible response model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
