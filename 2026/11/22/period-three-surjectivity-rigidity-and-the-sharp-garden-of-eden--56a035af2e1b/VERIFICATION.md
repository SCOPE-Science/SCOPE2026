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

# Reproducible checks

The two complete source programs `checker_grouped.cpp` and `checker_windows.cpp` each enumerate all ordered triples of the 256 elementary binary rules and compute the exact minimal length of a missing phase-aligned output word. Their independent transition-construction methods yield identical full histograms, with a second constituent-surjectivity classification.

Build separately using an ordinary C++17 compiler:

```sh
g++ -O3 -std=c++17 checker_grouped.cpp -o checker_grouped
./checker_grouped
g++ -O3 -std=c++17 checker_windows.cpp -o checker_windows
./checker_windows
```

Expected counts for shortest forbidden lengths zero (surjective), one, two, three and four: `12888`, `7476480`, `8825488`, `453144`, `9216`. Expected surjective constituent masks in binary order \((f,g,h)\): `000:0`, `001:0`, `010:0`, `011:928`, `100:0`, `101:928`, `110:928`, `111:10104`. The sum of all shortest-length bins is \(16{,}777{,}216\).

The output-word witness `010010010010` for rules `(22,22,90)` has the reachable-subset sequence `0xF, 0x7, 0x6, 0x2, 0x0`, giving sharpness. The source codes test the full language and not merely periodic input configurations or a bounded selection of output words. The equivalence between the subset automaton and all bi-infinite target configurations is proved in the result; the programs alone are not treated as an abstract theorem without this reduction.

Limits: no formal proof assistant or independent external audit was used; the code requires no third-party libraries or datasets.
