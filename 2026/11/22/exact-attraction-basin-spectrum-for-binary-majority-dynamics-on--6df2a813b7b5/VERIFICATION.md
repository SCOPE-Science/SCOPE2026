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

# Exact reproducibility checks

The full, standalone checking sources are embedded as `direct_enumerator.cpp` and `verify_lift.py`; their only input is the explicit Petersen and Desargues edge lists contained in the files.

Run the graph-level census using `c++ -std=c++17 -O2 -Wall -Wextra direct_enumerator.cpp -o check && ./check`. Its recorded exact output is `direct_output.txt`. It loops over every one of the 1,024 Petersen and 1,048,576 Desargues binary configurations, checks every vertex degree is three, and follows each configuration until \(F^2(y)=y\); it forms actual temporal orbit identifiers and counts basins without relying on the cover formula.

Separately run `python3 verify_lift.py`. This verifies a 20-element explicit graph-isomorphism permutation to the Petersen bipartite double cover, checks \(f^6=f^4\) for every Petersen configuration, computes all eventual even-phase preimage multiplicities, and reconstructs every lifted orbit basin by exact integer convolution. Its final output includes `PASS` only if every expected count agrees.

The exact first-entry counts for update times zero through four are 15,376; 132,080; 467,200; 202,560; 231,360. No entries after time four occur. Fixed-state basin types are 1 (72 times), 100 (50 times), 51,076 (twice); two-cycle basin types are 2 (2,556), 20 (3,600), 200 (1,225), 452 (144), 4,520 (100), 102,152 (once). All states are accounted for. The direct code and cover-convolution checker employ different computational strategies, but both share the explicit same mathematical model and do not constitute independent external validation.

The cited threshold-model paper already proves the general bipartite orbit-count identity; only the particular Desargues basin and entry-time numerical classification is presented as new. Checks here cannot establish absolute historical priority.
