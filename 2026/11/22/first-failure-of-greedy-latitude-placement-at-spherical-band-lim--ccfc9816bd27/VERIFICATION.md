---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Verification procedure
From this directory, run `python3 verify.py`. The script uses only Python's standard library. It produces certified, outward-rounded rational intervals for every sine, cosine and Lagrange cardinal weight; it checks the stated greedy and optimum chains, all strict comparisons with their bottleneck values and the exact absence of a cheaper chain. The polar term is identically zero for every nonzero harmonic order and is excluded by construction.

The argument covers the finite domain of co-latitude placements at band-limits \(2\le L\le12\). It does not certify any infinite-size generalization, real-data roundoff performance, global optimality over continuous latitudes, or independent mathematical validation.

## Recorded execution
The standard-library checker completed all ten nontrivial band-limits \(3\le L\le12\), reporting `CERTIFIED: first greedy failure occurs at band-limit 12`. At \(L=12\), the strict-threshold cut has 30 lower-cost subsets and no full inclusion chain, while the provided improved chain attains the certified threshold. The greedy chain has a separate, strictly larger bottleneck. No external certified proof assistant was used or claimed.
