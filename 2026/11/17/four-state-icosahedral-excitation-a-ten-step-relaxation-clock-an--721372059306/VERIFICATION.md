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

# Reproduction and scope

The result is a complete exact calculation on one twelve-vertex graph. Each C++17 program can be compiled with `g++ -O3 -std=c++17`, or an equivalent standard-compliant compiler; the symmetry program uses only the Python 3 standard library. Run in a directory containing the embedded program files, and compare the printed output with the correspondingly named embedded text files.

- `icosahedron_census.cpp` uses full successor-map construction, indegree elimination and reverse-depth propagation. It checks all \(16777216\) configurations, identifies the sole fixed point and \(208850\) primitive four-cycles, and finds maximum first-entry depth ten.
- `icosahedron_direct.cpp` uses a separate literal graph description and evaluates all fifteen iterates from time zero through fourteen for every state. It verifies the identity \(F^{14}=F^{10}\) state by state and counts all twenty nonzero time/period cells. It also writes `extremal_codes.txt` with exactly 240 entries.
- `icosahedron_phase.cpp` enumerates all colorings using successor-neighbor bitmasks rather than the transition map; it counts exactly \(835400\) four-phase recurrent states.
- `symmetry_extremal.py` constructs and checks all 120 automorphisms and partitions all 240 maximal-delay configurations into two 120-state classes with representatives 75769 and 441799.

For each checker, exhaustiveness derives from an explicit interval \(0\le\operatorname{code}(x)<4^{12}\) and one-to-one base-four decoding. The computed maximum is a *finite mathematical certificate*, not an empirical extrapolation. The analytic part establishes why the only permitted nonconstant cycle under the verified iterate identity has primitive period four, and why four-phase recurrence is exactly the local successor-neighbor condition.

Limits: no general all-graphs theorem, no claim about stochastic variants, no verification by a separate outside auditor, and no claim that semantic searches prove historical uniqueness.
