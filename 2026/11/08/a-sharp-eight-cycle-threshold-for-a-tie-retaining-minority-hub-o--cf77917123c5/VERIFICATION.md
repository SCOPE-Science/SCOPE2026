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

# Reproducibility and limits

Run `python3 check_bitwise.py` and `python3 check_graph.py` using Python 3.8 or later. The programs are standalone, require no third-party packages, and deterministically print the results in `bitwise_output.txt` and `graph_output.txt`. The former bit-packs the rim update using cyclic bit shifts, while the latter uses explicit adjacency and each node's neighborhood votes. Both enumerate every initial binary state within their stated finite ranges.

For \(3\le n\le12\), every one of the \(2^{n+1}\) configurations is tested for equality after eight updates and inequality after four. These conditions are equivalent to least period eight. Both programs return zero below \(12\) and \(288\) at \(12\); there are therefore \(36\) temporal eight-orbits at that size. Additional lengths \(14,16\) have reproducible counts, but no general formula for these counts is claimed.

The infinite construction is proved symbolically by the consecutive-block length recurrence, and the odd-size exclusion relies on the specified published Theorem 10. Spot checks at finite even lengths up to \(100\) only supplement that proof. The checks do not establish priority, basin counts, other periods, or an independent audit.
