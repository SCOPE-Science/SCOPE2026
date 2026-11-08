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

# Verification of the finite claim

The complete state spaces have size \(3^8\) and \(4^8\) before properness filtering; both checkers enumerate these exhaustive finite spaces by independent methods. All claims concern this exact eight-vertex graph and palettes \(3\) and \(4\).

Run:

```
python3 wagner.py
c++ -O2 -std=c++17 wagner_direct.cpp -o wagner_direct
./wagner_direct
```

`wagner_direct.cpp` prints `INDEPENDENT_EXHAUSTIVE_PASS`. The verified three-colour graph has \(48\) states, \(48\) undirected moves, and two connected \(24\)-vertex components, with degrees all two. The four-colour graph has \(2160\) states, \(7872\) moves, one connected component, all \(2160\) eccentricities equal to \(12\), and \(5160\) unordered pairs at distance \(12\). Both independently reproduce the complete all-distance pair census.

The correctness of BFS as shortest-path enumeration and completeness of the base-\(k\) scan are elementary. Neither code is a claim about infinite families. The known chromatic counts are not claimed original; no external independent validation has been performed.
