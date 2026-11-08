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

# Verification evidence and limits

The executable files `verify_small_orders.py` and `verify_orbit_certificates.py` are standalone, using only the Python standard library. The first exhausts every unordered triple of vertices and all eight adjacency patterns for each of the primes 29, 37 and 41, then asserts that every two-element subset is the full witness set for at least one triple and pattern. Its exact output is `finite_census.txt`. The second reconstructs quadratic-residue adjacency independently and verifies six explicit witness sets, one per orbit of two-vertex sets at each exceptional order. Its output is `orbit_certificates.txt`.

Both files were executed successfully and their exact outputs compared with the included text. No randomized tests or heuristic search are needed to interpret the exhaustive assertions. The six orbit representatives cover all deletion pairs because translations and multiplication by nonzero field squares act transitively on the adjacent and nonadjacent unordered pairs separately. All six witness sets are disjoint from their base triples.

The infinite part is a mathematical argument rather than a finite computation. Expand the three indicators, use the exact quadratic character sums and Hasse's bound for the separable cubic character sum. The resulting lower bound \(8N\ge q-15-2\sqrt q\) gives \(N\ge3\) for every eligible \(q\ge49\). A four-pebble back-and-forth strategy connects the three-extension property to the specified first-order fragment. The proof assumes standard finite-field character identities and the standard elliptic-curve Hasse bound; it does not constitute independent formal certification.
