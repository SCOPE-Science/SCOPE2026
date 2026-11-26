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

Deposition at visit j is independent of sensitivity, so the objective is a fixed baseline plus the sum of r scores h(x_j) for the high positions. Strict one-peak behavior of h on positive x ensures a superlevel set on the sampled ordered grid is an interval. If the cutoff is tied, any two tied indices have strictly larger scores between them and strictly smaller scores outside them; a noncontiguous maximizing set is impossible. The logarithmic derivative of h(x)/h(cx) is strictly negative: y/(exp(2y)-1) is decreasing, so coth(y)-c*coth(c*y)<1-c, giving the bound -b(1-c). The ratio decreases from 1/c to 0, proving unique crossing; taking c=q^r makes the adjacent block differences cross once at increasing loads in ratio 1/q. This gives all load intervals and the exact two-block ties, including r=1 and r=n-1. The golden-ratio substitution reduces to u(1+u)=1. Independent 70-digit enumeration of the 15 arrangements checks the five open regimes and four ties for the example; at L=8 positions 4,5 give 4.241880690637 versus 3.990255637369 for 1,2. Reproducer: /workspace/branches/531794c0-b94a-49b3-87b2-3cf5e1186206/staircase_independent_check.py. The supplied checker was read, not run; the numerical tie comparison corroborates the exact argument but is not its proof.

## originality

PASS

Best-of-knowledge pass for the ordered phase diagram with two fixed recipient classes: neither geometric transfer, the saturating dose response, nor selecting the largest entries of a unimodal list is claimed as new.

## value

PASS

The model makes a specific scarcity-versus-saturation tradeoff: sensitivity is most useful late when earlier doses already saturate both classes, but early when doses are scarce throughout. The theorem resolves every optimizer and transition without a combinatorial search and makes exact spacing independent of the sensitivity values. It is a precise benchmark for idealized ordering under geometric carryover, not a field recommendation or evidence for deterministic free-foraging behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
