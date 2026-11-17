---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The connected GHM 3-cycle local dichotomy makes every nonfixed F^3-fixed vertex advance, hence successor-neighbor 3-color support is necessary and sufficient. Direct independent 9-pair enumeration gives R=[[1,2],[2,3]], initial (3,6), final support flag 1. R²=4R+I yields N1=6,N2=24,Nm=4Nm-1+Nm-2. Direct independent exhaustive dynamics gave 6,24,102,432 for m=1..4; only the transfer proof is all-m.

## originality

PASS

The 2016 finite-graph theorem classifies eventual synchronization/activity but does not count initially periodic phase assignments. The 2015 cactus paper counts ordinary dominating sets without three rotating phase classes. A published singly resonant-cactus product law assumes exactly one 3-divisible cycle: the m>=2 all-triangle chain violates it, so it cannot imply the transfer recurrence. Best-of-knowledge novelty of this exact all-m count survives.

## value

PASS

An exact time-zero primitive-cycle count and graph-family transfer recurrence for excitable dynamics is a natural, structured periodic-state census, not ordinary dominating-set enumeration; the explicit orbit count and growth rate can be used for exact probabilistic and dynamical baselines.

The dated certificate retains the supplied scientific assessment, sources and limitations.
