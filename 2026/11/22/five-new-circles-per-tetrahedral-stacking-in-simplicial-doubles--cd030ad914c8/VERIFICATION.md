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

# Verification of the tetrahedral stacking theorem

From the directory containing this file, execute `python verify_stacking_double.py` and compare standard output byte-for-byte to `EXPECTED.txt`. Python 3.9 or newer is sufficient; the script uses only the standard library.

The program enumerates opposite-edge pair adjacencies from the tetrahedral facets, independently reconstructs a facet subdivision, and checks the changes in vertices (four), graph edges (nine), components (one minus the number of originally touched components) and free first-homology rank (six minus that number). For all distinct resulting labeled facet sets of stacked four-polytope boundaries with five through nine vertices, it also confirms connectedness and \(\beta_1=5n-19\). It checks 1,002 additional arbitrary pure tetrahedral-complex moves, including disconnected cases. The exact expected numerical output is in `EXPECTED.txt`.

The independent mathematical justification of the infinite assertions consists of the local subdivided-\(K_4\) correspondence, the graph rank identity, the connected Petersen/Kneser base case, and induction on the number of facet stackings. No finite enumeration is asserted to prove the infinite family, and no computer calculation is needed to show graph acyclicity beyond the connected graph structure. These checks do not establish any unclaimed equivariant characterization, a result about non-facet stellar moves, or publication priority. Independent external review remains unperformed.
