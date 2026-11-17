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

# Reproducible finite checks

The fourteen labelled vertices consist of seven points and seven lines. Both checkers generate the incidence graph from the Fano plane rather than loading a graph dataset, and enumerate every labelled initial binary state for the intact graph, all 21 single-incidence deletions, and all 210 unordered double-incidence deletions.

`check_all_defects.cpp` implements the majority map with integer neighborhood bitmasks, follows each orbit to a state whose second iterate is itself, records the first periodic entry time, and compares the unanimity-basin indicator of each initial configuration against that of the original graph. It also verifies all five parameter-class histograms exactly. Compile with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic check_all_defects.cpp -o verify`; run `./verify`.

`check_vectorized.py` independently constructs the Fano lines from binary vector addition, builds each transition map using NumPy arrays, identifies the periodic state set directly via a two-step composition, then back-propagates the first-periodic-entry layers and separately computes eventual unanimity. Run `python3 check_vectorized.py` with NumPy installed.

The recorded outputs in `check_all_defects_output.txt` and `check_vectorized_output.txt` match on all five class signatures. Both programs assert complete class sizes (1, 21, 42, 84, 84), fixed-point and two-cycle counts, lost/gained unanimity populations, and the entire transient-entry distributions. Both were executed from these exact source files. The check is exhaustive over 232 finite graph cases times 16,384 initial states; no unbounded generalization, independent audit, or absolute historical-priority certification is claimed.
