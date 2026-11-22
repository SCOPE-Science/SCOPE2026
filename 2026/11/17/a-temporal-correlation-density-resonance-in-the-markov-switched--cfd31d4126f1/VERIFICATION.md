---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS. Reconstructed post-transition E/C dyadic-shell transfer equations c_0=0, c_{k+1}=u e_k+(1-v)c_k, e_k=(1-u)e_{k+1}+v c_{k+1}+(1-u)e_0 2^{-(k+1)}; the top-shell E reinjection has geometric weights 2^{-(k+1)}. Eliminating their generating functions independently with symbolic rational algebra gives E=2(1-u)e_0[1-(1-v)z]/[(2-z)(1-u-(1-v)z)] and C=2(1-u)u e_0z/[(2-z)(1-u-(1-v)z)], and E+C exactly the claimed M. M(1)=1 forces e0=(v-u)/(2(1-u)(u+v)). For v<u the noncanceled positive pole lies at z=(1-u)/(1-v)<1; at equality nonnormalizable, so no probability in specified density subspace. For v>u both geometric poles outside the unit disk and coefficientwise nonnegative masses exist, verifying stationarity and uniqueness. Collision of poles r=(1-v)/(1-u)=1/2 gives k2^{-k} and exact log resonance. Fixed p=v/(u+v)>1/2 yields threshold s*=1/(3p-1) strictly in (0,1/p), independent of Lyapunov value. Independently evaluated exact rational examples in all 3 regimes. Caveat: no global uniqueness for singular measures or atomic zero; no total-variation mixing claim.

## originality

PASS

PASS best of knowledge. The closely related iid Pelikan results explicitly choose maps independently with fixed p, so cannot directly imply the Markov-environment joint stationary law depending separately on u and v or its fixed-frequency correlation threshold. No indexed exact equivalent in the searches; this is not proof of absolute priority.

## value

PASS

PASS. Stationary regularity at a fixed positive Lyapunov exponent is a motivated structural distinction between temporal correlations and mean expansion. The complete exact probability-generating function and pole-collision trichotomy for the non-iid mode-conditioned transfer operator are nontrivial, explicitly parameterized, and usable to distinguish stochastic processes sharing their one-step mode frequencies; not a change of symbols in the iid formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
