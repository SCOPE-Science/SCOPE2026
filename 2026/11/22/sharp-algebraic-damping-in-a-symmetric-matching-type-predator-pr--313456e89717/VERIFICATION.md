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

Reconstructed the positive equilibrium and all four equations for the total deviations Z=(A,B) and contrasts (X,Y). In the entropy derivative the matching interaction cancels, leaving -c A²-(pγ/ρ) B². Entropy sublevels are compact inside the positive orthant. On A=B=0, staying there requires XY=0; the nonzero harmonic-oscillator flow does not stay on either axis. LaSalle gives convergence. The exactly symmetric plane is invariant and its remaining linearization J has negative trace and positive determinant. A nonsymmetric solution never reaches that plane by uniqueness. An independent tracking argument avoids any ambiguity about the choice of center manifold: the contrast equations give |(log R)'|+|θ'-ω|=O(|Z|), which tends to zero. The stable Z equation has constant linear part J, quadratic remainder in Z, and forcing R²F sin(2θ). After a sufficiently late time, variation of constants (absorbing the small coefficient multiplying Z) bounds |Z| by O(R²), since R(s)/R(t)≤exp(ε(t-s)) for s≤t and ε can be taken below a quarter of a stable decay exponent. The residual of R² Im(W exp(2iθ)) in this equation is then O(R⁴); another stable convolution yields Z=R² Im(W exp(2iθ))+O(R⁴). The entropy is R²/(4u)+O(R⁴) by the cancellation of pure cubic contrast terms between opposite types. Thus (1/V)'=16u² G(θ)+O(R²), with angular mean of G equal to D/2, and θ'→ω makes the time mean equal to this angular mean. It follows that tR²→1/(2uD). The inverse defining W is nonsingular and F≠0, giving strict D>0. Independently recomputed the symbolic ODE and entropy and the unit response (-19/260+11i/130,17/260-3i/130), hence D=9/520 and limit 260/9. Two finite integrations at a distinct parameter set approached 30.53888017 progressively, giving 30.06715369 and 29.74237062 at t=24000; these are finite-time diagnostics only.

## originality

PASS

The same model, Lyapunov calculation and global attraction are already in the originating work; these are not distinct claims. Neither the matched source nor the closer structural analogues inspected supply the explicit harmonic-resolvent constant, or the exact contrast envelope for this flow from all strictly positive initial states off its symmetry plane. The verdict is best-of-knowledge, not priority certification.

## value

PASS

The established persistence and convergence leave open whether contrasts damp exponentially when the totals are dissipative but the contrast linearization is purely imaginary. The universal nonzero prefactor and the exact exceptional plane quantify this gap in a deterministic ecological model. It is not just an example of the general Hopf exponent: the computed prefactor and its strict positivity for every positive parameter choice resolve the model question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
