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

# Reproducibility

The fixed vertex set has five roots \(0,1,2,3,4\) and ten subdividers \(x_{ij}\) in the edge order \((01,02,03,04,12,13,14,23,24,34)\). Each subdivider is adjacent to exactly its two indexed roots. Every five-color strong odd coloring has all five original roots differently colored, hence a unique color-name-free normalization assigning root \(i\) color \(i\).

Execute `python3 verify/exact_cover_dp.py` and `python3 verify/direct_orbits.py` from the extraction root. Both require only Python 3's standard library. Outputs must match `verify/exact_cover_output.txt` and `verify/direct_orbits_output.txt` exactly. The first code computes edge-disjoint odd-subgraph class partitions via a 1024-mask exact-cover dynamic program; the second code checks all 59,049 normalized ten-subdivider assignments in an explicitly constructed 15-vertex graph. Both return 201 strong odd configurations and 6 square configurations. The second script also returns 6 orbit representatives, all 201 partition assignments allocated to exactly one orbit, with sizes 6,15,30,30,60,60. The six-orbit conclusion may independently be checked using Burnside's lemma and the seven conjugacy-class fixed counts in RESULT.md.

The calculation is a proof for this finite graph because the normalized domain and allowed class list are exhaustive, the parity condition is independently checked at every vertex, and both enumerations terminate successfully over every candidate. It establishes neither an infinite-family count nor independent mathematical certification. The general five-color minimum is already in the cited 2025 literature; it is also directly witnessed and lower-bounded here.
