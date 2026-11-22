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

## Reproducing the finite proof

Place `archimedean_majority.py`, `archimedean_independent.cpp`, `reference_census.json`, and `verify.py` in the same directory. Run `python3 verify.py` with Python 3.9+ and a C++17-capable `g++` installed.

The Python implementation constructs two twelve-vertex graphs, enumerates all 4096 binary configurations for each, computes successor arrays and traverses the functional graphs to their exact first repetitions. It also enumerates the full 24- and 48-member spatial automorphism groups, checks their adjacency preservation, computes fixed-state and temporal two-cycle classes, and independently checks Burnside's count. The computed machine-readable census must match the frozen `reference_census.json` bytewise as decoded JSON structures.

The C++ program independently builds the graphs and uses indegree peeling, rather than path following, to obtain the precise period/first-entry table. Its recorded final marker is `INDEPENDENT_CERTIFICATE_OK`. The top-level replay prints `VERIFY_OK` only after the expected totals agree. In the actual replay, the truncated graph produced entry populations `(494,1502,996,816,216,72)`, with period-two basin 2366 and consensus basin 1360; the cuboctahedron produced `(186,1606,1200,1008,96)`, with period-two basin 40 (all 40 at entry zero) and consensus basin 2064.

The proof is a complete finite 8192-input enumeration, not a statistical experiment or an assertion about infinite graph classes. Success is a reproducible program-level check, not independent formal certification or peer review. The unrelated classical finite-threshold eventual-period theorem is not independently reproved.
