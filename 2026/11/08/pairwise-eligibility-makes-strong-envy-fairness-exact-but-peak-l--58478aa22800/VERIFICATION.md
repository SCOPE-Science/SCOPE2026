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

# Verification

Run `python3 verify.py` in the extracted directory using Python 3. No nonstandard dependencies or external data are needed. The script separately evaluates the exact induced-subgraph formula and enumerates literal feasible allocations; it deliberately does not call the proof's network-flow construction.

Actual output from the packaged source in its staging directory:

```
n3_full= 3375
n4_random= 3500
online_weighted_sequences= 1200
all finite tests passed
```

The first count exhausts all \(5^3\cdot3^3=3375\) pairs of three-agent edge-multiplicity and singleton-count parameter vectors, with all feasible assignments enumerated separately. The second samples 3500 reproducibly seeded four-agent parameter vectors and enumerates their allocations. The final test directly rechecks both ordered strong-EF1 inequalities after each step of 1200 positively weighted, pair-eligible online streams.

**Logical verification limits:** No finite enumeration proves the theorem for arbitrary numbers of agents, arbitrarily many jobs, or arbitrary positive real job sizes. These domains are handled by the last-job argument and Hall's theorem in `RESULT.md`. The peak-load equivalence assumes strictly unit-size jobs; the arbitrary-size online assertion does not claim strong EFX. No independent external mathematical audit or formal proof assistant was used.
