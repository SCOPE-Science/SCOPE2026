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

# Reproducibility and limits

The two supplied independent checks are `check_transfer.cpp` and `check_rings.py`. Compile and run the former using `g++ -std=c++17 -O2 -Wall -Wextra check_transfer.cpp -o check_transfer && ./check_transfer`; execute the latter using `python3 check_rings.py`. Compare stdout bytewise to `transfer_output.txt` and `rings_output.txt` respectively.

The C++ certificate constructs all legal time-history edges for the five indicated odd heights, applies iterative Kosaraju strong-component decomposition, and asserts the unique cyclic component is the single all-zero vertex. Its reported component counts are complete finite enumeration of the graph, not an inference from log length. The Python certificate follows every configuration's update path on each ring of size three through eleven, and checks direct eleven-step witnesses. The first method proves all-circumference exclusions; the second method proves a finite sharp onset and orbit multiplicity.

The exact graph-edge correspondence and the absence of all nonzero directed cycles are the two critical lemmas of the argument. Different code paths avoid reliance on a single implementation of the local rule for both halves, but do not constitute independent external mathematical review. The assertion is silent about odd temporal periods above eleven, large-ring eleven-orbit counts, attraction probabilities, and infinite spatial configurations.
