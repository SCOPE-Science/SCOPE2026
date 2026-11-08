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

# Finite verification

The graph has 16 named vertices and 24 edges. The first standalone script enumerates all graph matchings by including or excluding each edge subject to disjointness. It tests maximality exactly through unmatched vertices and enumerates every candidate one-edge substitution among optimum states. The second script independently enumerates all independent possible unmatched sets and all perfect matchings on their complements, then builds exchanges by shared five-edge submatchings. Both use Python 3 standard library only and independently verify all reported sizes and components.

Executed commands:

```sh
python3 verify_gp_matching.py
python3 verify_lcf_complement.py
```

Both runs ended `VERIFY_OK`; the exact captured outputs are embedded alongside these scripts. Each assertion was checked in the run where its corresponding program executed. The first also checks all finite graph distances from all nonisolated states. The second verifies the fixed relabeling to the LCF model by equality of all edges.

The finite universe is exhausted; no random trial or selected sample is substituted for a proof. These checks do not extend to other graphs, nor do they constitute an external or independent scholarly audit.
