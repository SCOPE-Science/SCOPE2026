---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For Itô redistribution model J>0, 0<d_l<d_h,0<β<1 and μ>0, the physical smallest determinant root q=α−1 lies in (J/d_h,J/dbar). Exact isolation gives μ=G(q)=(1+q)(J−d_l q)(d_h q−J)/(J−dbar q); direct signs show G′>0, G′′=2 d_l d_h/dbar+2 dbar² P(J/dbar)/(J−dbar q)^3>0. Hence α′=1/G′>0 and α′′=−G′′/(G′)^3<0. Endpoint q=J/d_h has G′=(J+d_h)/β, while q↗J/dbar yields the precise positive variance-proportional 1/μ deficit. Independently checked symbolic identities, not merely graph samples.

## originality

PASS

The source Arutkin–Vallée paper gives the physical determinant and fast/slow exponent bounds; these are credited as prior. Direct algebra supplies the inverse rational calibration map, strict all-rate derivative signs from a positive-pole partial-fraction decomposition, and both exact endpoint sensitivity constants. The general Beare–Toda first-order comparative-static result does not itself imply strict global concavity and these coefficients in the two-channel redraw model. No known exact equivalent coverage found in the targeted Resultary semantic comparison; residual historical risk retained.

## value

PASS

The global strict concavity/identifiability structure answers a natural calibration question for a physically defined tail exponent, gives sharp endpoint sensitivities, and separates slow sensitivity independent of d_l from fast variance-dependent response. It is more informative than a monotonicity plot, but remains a model-specific refinement, not a universal Markov growth theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
