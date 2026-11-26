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

Each peripheral vertex has just two neighbors, its partner and the hub. A new excitation at time one is therefore either a hub activation with at least two initially excited peripherals, or a peripheral activation requiring an initially excited hub and an initial 0/1 pair. The two modes exclude each other. In the first, there are no excited peripherals at time one; in the second, the hub is at state 2, is not resting, and cannot excite a peripheral. No excitation is created at time two, and after that no excited vertex remains. Thus a time-one activation lasts until update k, whereas an initially positive state r lasts to update k-r absent reactivation. The two trigger counts subtract respectively zero or one ones from all peripheral words, and words avoiding both ordered 0/1 pairs from all petal words. These give the stated C_(k,m); each trigger is possible already for one petal. Without time-one activation the minimum initial positive state determines the first hitting time. The alphabets excluding successively smaller positive states give the lower layer differences, and subtraction gives the layer at k-1. The early-layer probability is ((k-1)/k)^(2m+1); the three excluded terms of C_(k,m), after normalization by k^(2m+1), decay exponentially for fixed k, giving the two-layer limit. The argument includes k=3: at time one the previously excited hub is already refractory even if it will return to rest at time two. For (k,m)=(3,1) the proof gives (1,7,16,3), consistent with the supplied census.

## originality

PASS

The supported distinct claim is the depth-one trigger and full labelled all-k extinction-time census for friendship graphs at absolute threshold two. Eventual extinction is covered by a prior general criterion, and the analogous 2/k mass from two hub-state channels is known for multistate wheels. Neither observation is credited as a new general phenomenon here.

## value

PASS

Friendship graphs isolate the effect of a universal hub and degree-two petal vertices in a natural family. The full labelled counting law gives more than qualitative extinction: it identifies precisely when any new excitation can occur and partitions all initial conditions by relaxation time. Contrasting the cone over a matching with a wheel shows how identical limiting top-layer masses can arise from different trigger states and different sharp clocks. The all-color polynomial makes that comparison exact rather than an empirical observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
