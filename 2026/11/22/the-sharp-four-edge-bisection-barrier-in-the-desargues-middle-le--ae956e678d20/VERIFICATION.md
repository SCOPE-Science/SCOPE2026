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

Run `python3 verify_middle_levels.py` and independently compile `g++ -std=c++17 -O3 verify_gp.cpp -o verify_gp && ./verify_gp`. Each program constructs its own graph and checks the entire balanced-cut spectrum and the component census at budgets 6, 8, and 10. The Python program additionally proves the internal-incidence maxima by enumerating all 1024 two-subset families and verifies the five coordinate splits.

The scripts were executed before packaging. Their exact captured outputs are `verification_middle_levels.txt` and `verification_gp.txt`.

The exhaustive search has 184756 side-labelled bisections. Each graph-state component is traversed exhaustively by checking all 100 possible balanced one-vertex swaps. This is a complete finite certificate, not an extrapolation to general Desargues or middle-levels graphs. Graph isomorphism between the two standard presentations is supported by the cited graph reference. Independent scholarly evaluation remains unperformed.
