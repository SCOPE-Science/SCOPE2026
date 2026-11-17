---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

For arbitrary nondegenerate stationary mu supported on (0,1), the refresh/retain Markov transition rho delta_v+(1-rho)mu implies the discounted first-break equation F(v)=v^q+(1-v)^q[rho F(v)+(1-rho)m]. Solving and integrating gives the exact integral quotient; at rho=1 direct geometric stick weights give the endpoint under required integrability. Rewriting it as a tilted expectation of R_q(v)=v^q/[1-(1-v)^q], the rho2/rho1 density ratio decreases strictly in v. R_q increases for q>1 and decreases for 0<q<1, giving strict opposite directions via an independent-copy covariance identity, with q=1 constant. For Shannon entropy, the chain-rule reward h(v), discounted by 1-v, yields analogous quotient; R_H=h(v)/v has derivative log(1-v)/v^2<0 and entropy grows strictly. The stated log and fractional-q moment assumptions justify endpoints. Independent exact rational checks at v=(1/4,3/4) gave M2(0)=5/11, M2(1/2)=119/281, M2(1)=13/35. They corroborate the analytic sign, not arbitrary-mu completeness.

## originality

PASS

Gil-Leyva, Lijoi, Mena and Prünster 2026 introduce this exact Markov stick-break family, its properness and beta-law specializations; their full manuscript, Section 5 and appendices, discuss clustering probabilities and illustrations of intermediate rho. The inspected source does not state the candidate all-nondegenerate-mu strict ordering across every rho, all q powers, and expected Shannon monotonicity. Exchangeable break lengths are a distinct dependence mechanism. Classical renewal and likelihood-ratio methods are acknowledged as proof ingredients, not invented.

## value

PASS

The annealed species collision probability is an interpretable central statistic for partition diversity, and the exact strict persistence direction for every q>1, together with entropy order reversal at q=1 and stringent endpoint integrability, classifies a natural dependence-control parameter without assuming beta breaks. It answers a structural comparison not supplied by the model definition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
