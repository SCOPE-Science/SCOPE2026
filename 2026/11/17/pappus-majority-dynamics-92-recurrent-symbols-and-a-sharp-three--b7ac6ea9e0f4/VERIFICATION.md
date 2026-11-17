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

# Reproducibility and scientific limits

The complete 512-subset incidence certificate is `check_pappus_projection.py`; run with `python3 check_pappus_projection.py`. It checks all nine-bit shore assignments, all core and fiber claims, an explicit isomorphism to the independent graph construction, and the weighted orbit-basin calculations. Assertions fail on disagreements.

The independent 18-bit functional-digraph census is `check_pappus_full.cpp`; compile with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic check_pappus_full.cpp -o check_pappus_full` then run `./check_pappus_full`. It evaluates all 262,144 states, checks the complete period/orbit and depth/basin histograms, and verifies \(F^5=F^3\) on every state. The `.out` files contain captured successful outputs of the exact packaged sources.

These computations are **complete finite proofs/checks for this particular graph**: the script's loops cover every nine-bit shore input and the graph checker every 18-bit input. Neither establishes an infinite-family statement. No independent external audit has been performed.
