---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Polynomial vanishing on x^2+y^2=1 forces F=omega Jp+(R-1)G with degree F=degree G+2. The exact periodic adjoint identity s=-(omega/2)h_prime-kh with k=p·G and s=Jp·G follows by differentiating the phase PDE in radial direction. If k has nonzero highest Fourier frequency N>=1, the leading coefficient of kh at m+N forces e^{iθ}(k+is) to have frequency m+N+1; if k is constant and m>=1, imaginary coefficient -(im omega/2+k)h_m is nonzero and forces m+1. The m=0 case uses nonzero mean radial damping to force degree G>=1. Thus degree F>=m+3, and equality makes k constant. The explicit H=(kappa h-omega h_prime)/2 harmonic polynomial makes radial ODE rdot=kappa*r*(1-r^2)/2 and linear transverse exponent -kappa; its adjoint matches Z. Independent SymPy test verified m=4 h=2sin2θ-2sin4θ, exact phase adjoint, logistic radial identity, degree seven.

## originality

PASS

Namura–Ishii–Nakao (2023) already demonstrates this exact target shape with a numerical degree-seven oscillator; the newly claimed mathematical contribution is not degree-seven existence in isolation but sharp necessity for every polynomial field and an exact globally attracting construction with adjustable Floquet exponent. General polynomial limit-cycle realization results prescribe periods/stability without infinitesimal phase-response gradients. No stronger specified-h Fourier minimum-degree theorem was found in the searched indexed sources; priority remains qualified.

## value

PASS

The exact inverse design problem couples a prescribed physical-time orbit, infinitesimal phase response, and polynomial complexity. A sharp universal degree obstruction and realizability at equality provide a natural certificate of minimal model complexity, and show that a known seventh-degree numerical design was optimal for its target.

The dated certificate retains the supplied scientific assessment, sources and limitations.
