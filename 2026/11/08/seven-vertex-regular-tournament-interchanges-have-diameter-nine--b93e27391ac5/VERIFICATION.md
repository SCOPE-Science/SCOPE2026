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

# Reproduction and limits

Two standalone finite enumerators are included. They use no input datasets, external program packages, network access, or cached graph files.

Run in the same directory as the code:

```sh
g++ -O2 -std=c++17 verify_full.cpp -o verify_full
./verify_full
python3 verify_orbits.py
```

The first checker iterates all \(2^{21}\) orientations, keeps every orientation of outdegree three at all seven vertices, constructs the entire legal directed-triangle reversal graph and performs all-source breadth-first search. It independently confirms \(2640\) states, \(18480\) undirected edges, constant degree \(14\), radius \(8\), diameter \(9\), eccentricity counts \(1920\) and \(720\), the nine distance frequencies, \(360\) diameter pairs, and that each eccentricity-nine source has precisely the bitwise-complement tournament at distance nine.

The second checker uses an independent recursive enumeration of row outdegrees, explicitly relabels by \(S_7\), verifies three orbits \(720,1680,240\), and checks their full distance distributions and unique antipodes. All checked quantities are finite and exact. This does not certify a general-order theorem, novelty in inaccessible historical sources, or independent external audit.
