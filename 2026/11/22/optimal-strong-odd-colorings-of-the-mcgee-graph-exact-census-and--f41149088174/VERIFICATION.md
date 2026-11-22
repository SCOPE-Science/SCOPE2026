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

## Direct computational checks

Use a C++17 compiler to compile `search_colorings.cpp` and `exact_cover.cpp`; `analyze_orbits.py` requires Python 3 and NetworkX. From the directory containing those files, execute the commands in `RESULT.md` in order. The complete census certificate `search_colorings_5.txt` contains one 24-digit canonical coloring per line. The two independent strategies report \(0\) admissible four-color partitions and \(1304\) five-color partitions. The Python program compares all two lists as sets, enumerates all \(32\) automorphisms, reports \(54\) partition orbits of size \(8,16,32\), and reports \(320\) square colorings.

The two enumerators do not rely on a solver's incomplete output: one recursively explores color assignments and proves pruning from the cubic neighborhood condition; the other explores all independent odd-neighborhood color classes and all exact covers. The base graph is exactly defined in `RESULT.md`. Counts are finite, exact integers, not estimates. A separate external mathematical audit has not occurred.

## Scope

The claimed conclusions concern the McGee graph defined by its 24-vertex LCF edge rule and strong odd open-neighborhood condition. No infinite-family extrapolation, independent certification, or comprehensive publication-priority determination is asserted.
