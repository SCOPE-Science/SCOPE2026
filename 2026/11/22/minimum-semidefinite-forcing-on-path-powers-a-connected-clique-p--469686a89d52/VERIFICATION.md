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

# Reproducible verification

Run `python verify_psd_path_powers.py` with Python 3 and no external dependencies. The checker enumerates all vertex subsets of size \(k\) and \(k-1\) for each tested pair \(4\le n\le14\), \(2\le k\le\min(n-2,6)\), independently implements the PSD white-component rule, compares the full set of optimal seeds with the three theorem families, separately implements ordinary zero forcing, and constructs the one-exchange graph for exhaustive shortest-path and edge-count tests. Expected final output is `VERIFY_OK` after the named `PASS` assertions.

The checker is finite corroboration (45 pairs), not a proof for unbounded \(n,k\). The all-order proof uses path-power vertex separators, boundary forcing, and exact exchange-intersection counts. Independent mathematical review has not been performed.
