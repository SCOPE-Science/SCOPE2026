---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Independent construction of the complete nine-real-coordinate no-click Lindblad generator gives det L=-(2g+1)(4g^3+4g^2+9g+2)/2 and exactly the claimed rational mean for all g>=0 and Δ real, not just sample values. Differentiation yields F'=-2(8g^4+8g^3-2g^2+7)/Q^2<0 and F''=4(2g+3)P/Q^3>0. Independently verified Bernstein coefficients [21,114/5,141/5,501/20,6/5,66] on 0<=g<=3/2 and shifted coefficients [66,216,394,324,120,16] for g>=3/2 prove P>0. Thus strict convexity, derivative signs at g=0 and infinity, unique positive global minimizer, d g*/d z>0, and g*(z)/sqrt(z)->1. Finite-dimensional CP trace-decaying semigroup has no nonzero dark invariant positive state, so the integral equals -L^{-1}P2 even at zero dephasing; this is an analytic proof, not solely verifier success.

## originality

PASS

The clean central-starting mean-time formula was published in 2017 and is acknowledged as z=0; the detuned central-input strictly convex homogeneous-dephasing optimum with all z>=0 and its monotone/asymptotic law was not located in the inspected closest source texts. Best-of-knowledge assessment, not an absolute priority certificate.

## value

PASS

A central initial excitation and central detuning form a natural extension of the known clean-middle transport setup. The exact single-parameter all-detuning convexity and monotone noise-control law are nontrivial because the detuning correction has a degree-three rational denominator and a degree-five global positivity certificate. A useful exact robust optimizer for matched extraction is not merely a reparameterization of an earlier source-end result. The three-site restricted scope and priority risks are explicitly retained.

The dated certificate retains the supplied scientific assessment, sources and limitations.
