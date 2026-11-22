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

All verification is finite, exact, and reproducible from the included source files. The original defining criterion requires two detectors in each closed neighborhood and asymmetric two-sharp separation for each vertex pair. Independent C++ and set-based Python enumerators test every one of the \(65{,}536\) subsets on each graph. Their cardinality histograms are

- Rook: \((10,720),(11,1920),(12,1496),(13,560),(14,120),(15,16),(16,1)\).
- Shrikhande: \((10,256),(11,1392),(12,1424),(13,560),(14,120),(15,16),(16,1)\).

A separate obstruction-hypergraph algorithm proves the entire low-omission classification using only the sixteen closed neighborhoods and adjacent-pair directed differences. Its direct tests give \(324\) and \(396\) distinct four-subset obstructions, and no admissible omitted set of size seven. The same algorithm enumerates explicit automorphisms, all optimal orbits, and exact exchange components; a sixteen-entry adjacency-isomorphism witness certifies the six small exchange components as rook graphs.

Reproduction commands from the extracted root:

```sh
g++ -O2 -std=c++17 code/direct_checker.cpp -o direct_checker
./direct_checker
python3 code/set_checker.py
python3 code/obstruction_exchange.py
```

The programs use standard C++17 and Python 3 without downloaded libraries, data files or randomness. The verifier source paths listed are complete and independently executable. Enumeration of a finite sixteen-vertex graph proves only the two specified cases. Historical novelty is assessed separately and external mathematical audit has not occurred.
