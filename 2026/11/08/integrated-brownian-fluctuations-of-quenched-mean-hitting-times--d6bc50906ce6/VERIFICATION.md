---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For fixed 0<p<1, geometric independent success gaps K have exact joint ray advance H=floor(K/2)+1 and tooth reward A=ceil(K/2); D=A-qH is centered with E D²=q/(1+q), E H=1/[p(1+q)], so renewal-reward variance rate pq. Independently summed exact geometric terms to K=299 at p=1/3,1/2,3/4, matching these constants to tiny tail errors. Tree edge first-passage identity H_m=m²+2 sum_{h=1}^m C_h follows from 2e+1 crossing times. Renewal-reward Donsker/time change and max-block O_P(log m) imply functional CLT; integrating gives 2sqrt(pq)∫B and t=1 variance 4pq/3; strong law gives 1+q. All results are tree-environment fluctuations of quenched MEAN, not walk path hitting distribution.

## originality

PASS

The original Bernoulli recursive-tree source studies one end and collisions, not this quenched mean-time functional law. A full prior same-model result studies an annealed Brownian distance field in birth-time coordinates, with height/diameter variances, but does not provide conditional hitting-mean weighted tooth reward or its pq coefficient. General regenerative CLTs and tree edge hitting identities provide tools, not the entire evaluated model-specific limit. Full original primary text inaccessible here and is explicitly a priority risk.

## value

PASS

Conditional mean first-passage cost is a natural transport observable on the unique infinite ray. The exact regenerative block dependence and integrated Brownian fluctuation profile, including variance 4pq/3, distinguish environment disorder from path noise and give a quantitatively useful all-parameter (fixed p in (0,1)) second-order law beyond general qualitative recurrence results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
