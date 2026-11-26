---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Inverting the killed two-state generator gives h(c+qu)/(u²+Su+P), h=sd, S=c+e+h, P=ch. The two decay rates are positive and distinct, with λ−<min(c,h) and λ+>max(c,h), by evaluation of the quadratic at c and h. For q=0 the reduced transform fixes S and P exactly; the complete positive fiber is h=P/c, e=S−c−P/c on (λ−,λ+), and AM–GM gives the attained maximum of e. For known q>0, cancellation occurs exactly at the single admissible root λ−/h of c−qS+hq²; the larger root λ+/h is above 1. Cancellation leaves Exp(qh), and at fixed q and exponential rate r, h=r/q and e=(1−q)(c−r)/q with c>r describe the whole positive alias family. Outside cancellation the density initial derivatives follow from f(t)=(1−q,q)e^(tQ)(0,h)^T and Cayley–Hamilton, giving the asserted jet inverse. The cancellation expressions at distinct efforts differ by d(s₂−s₁)q(q−1), so at least one is nonzero for interior q; q=1 is never exceptional. For q=0, differentiating at u=0 gives m_s=1/c+(c+e)/(scd) and v_s=m_s²−2/(scd); the two means recover U,V and the variance recovers K=cd, with the positivity inequalities both necessary and sufficient. The proof is structural, assumes exact population summaries and identical known initialization across groups, and provides neither finite-sample robustness nor an unknown-q identification theorem. Supplementary code was inspected but not used as proof.

## originality

PASS

Phase-type waiting times, general Markovian arrival nonidentifiability, and exponential survival under quasi-stationarity are prior and not credited as discoveries. The surviving result is the fixed-known-initialization classification together with identifiability under any two distinct calibrated efforts and the explicit three-summary inverse at zero initial availability. The inspected sources do not give this experiment-dependent claim.

## value

PASS

Separates exact structural ambiguity from statistical uncertainty in a natural first-detection design. The full-law aliases show why collecting more replicates at a single effort can fundamentally fail; the exact threshold and the two-effort guarantee tell an investigator what intervention changes identifiability. The three-summary inverse and its positivity region are usable population-level criteria without observing recurrent detections. No operational finite-sample guarantee or general summary-minimality claim is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
