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

The general graph-class equivalence is established by the three-case constructive proof in RESULT.md; neither script is required to extrapolate from the finite Heawood graph to arbitrary graphs.

Run `python3 verify_fano.py`. It explicitly traverses all shortest paths between each of the 91 vertex pairs and computes their vertex and edge unions. It checks every one of the 16,384 initial subsets and all four projective construction families. Expected output begins `PASS geodetic=edge-geodetic on 16384 subsets` and `PASS minimal projective families`.

Run `g++ -O2 -std=c++17 -Wall -Wextra verify_fano.cpp -o verify_fano && ./verify_fano`. This independent checker uses Floyd–Warshall, geodesic distance equalities, and an all-subset enumeration. Expected output begins `PASS: independent all-subset vertex and edge geodetic tests agree on 16384 masks.`

Both programs were run and completed with their assertions satisfied. They reproduce all coefficients and all minimal-set counts. The generic theorem is proved symbolically; exhaustive finite computation is used only for the Heawood specialization. Claims of independent scholarly audit or absolute historical priority are not made.
