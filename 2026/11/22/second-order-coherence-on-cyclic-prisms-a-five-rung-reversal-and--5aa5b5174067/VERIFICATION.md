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

On the mean-zero space, the trace of A^(-p) has a strictly positive spectral Hessian for p=1,2 (use the continuous divided difference also at repeated eigenvalues). Off-diagonals identify the weights, loss of connectivity sends an eigenvalue to zero, and uniqueness forces invariance under layer exchange and rotation. Removing either whole orbit disconnects the network, so both weights are positive. The symmetric/antisymmetric Fourier spectrum is a*mu_k and a*mu_k+2b; differentiation under m(2a+b)=1 gives S_p-R_p, where R_p decreases strictly from infinity to zero. Independently reproduced all six small-m sign/equality certificates by rational matrix inversion in /workspace/frozen_review_arithmetic.py (SymPy, no frozen code executed). For m>=7 the zero mode gives t_1>sqrt(12/(m^2-1)) >=30/(m^2+11) using (m^2-49)(m^2-4)>=0. The same barrier holds by the small-case certificates at 5 and 6. Then R_2(t_1)<R_1(t_1)/(2t_1)<S_2, giving the entire finite-size comparison. For t->0 and m*sqrt(t)->infinity, the rescaled Fourier sums are Riemann sums at the two ends of the band: T_q ~ m*(2t)^(1/2-q)/(2*pi) times the integral of (1+x^2)^(-q) over the line. Sine bounds control the tails. Thus R_1~m*(2t)^(-3/2), R_2~3m*(2t)^(-5/2)/4; monotone bracketing at the two trial scales gives c_1 and c_2. Substituting into the budget-normalized trace yields the c_2/108 correction and the larger c_1/180 regret coefficient as stated. The bounded replay checks arithmetic, not the infinite-family argument or provenance. Read the frozen result, verification note and script; no formal verification claimed.

## originality

PASS

Pass for the exact all-size first-versus-second ordering (including equality only at m=4), not as an exclusive priority claim for the fractional exponent or for inverse-trace design. The general real-p same-day record demonstrably covers the m^(-6/5) allocation exponent as a specialization; its indexed wording treats the endpoint laws as known and establishes no same-day priority. The available asymptotic comparison gives eventual order, not the finite reversal threshold or the exceptional small sizes. No checked prior statement supplies the latter. The exact scope of overlap in the asymptotic constants and regret is less secure than for the threshold.

## value

PASS

The threshold tells a designer exactly when a first-order optimum over- or underinvests in rungs relative to second-order coherence. It resolves the entire natural prism family under unrestricted allocation, with a genuine small-size exception and a cube equality that large-size power laws alone cannot predict. The regret analysis further identifies why absolute losses can grow despite vanishing relative losses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
