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

# Evidence and limits

The structural exchange proof in RESULT.md covers every finite election with the stated degree bound. The accompanying standalone C++17 source `verify_quota.cpp` independently enumerates all voter-to-candidate approval incidence matrices for \(1\le n\le5\), \(1\le m\le4\), every eligible size \(k\), and filters to degree at most \(\lceil n/k\rceil\). It checks the final welfare, EJR for all groups, and termination of the exchange algorithm. Recorded execution: `PASS eligible_profiles=1803670 replacement_swaps=508 sharp_family_q=1..100`. Its arithmetic check of the sharpness family is finite, not an infinite certificate. The full theorem depends on the written proof. No independent audit was performed.
