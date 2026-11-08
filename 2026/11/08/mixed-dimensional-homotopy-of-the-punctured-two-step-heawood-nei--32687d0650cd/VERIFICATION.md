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
# Verification

Recompute by running `python3 verify.py`, Python 3.10 or later, without nonstandard dependencies. The script constructs the Fano incidence graph directly from the parity of binary dot products, takes all exact-distance-one-or-two nine-vertex facet sets, enumerates their nonempty subsets, executes the deterministic free-pair/critical-maximal-simplex matching, and checks acyclicity by a full directed-Hasse-graph topological sort. It then computes the entire critical five-to-four Morse differential by **exact signed integer** substitution along matched pairs, not by finite-field approximation.

Expected facts: 14 vertices, 21 edges, 14 facets, 4,480 faces, 22,974 cover relations, 2,224 matching pairs, and critical counts one in dimension zero, twenty-nine in dimension four and two in dimension five. Both critical five-cell boundaries vanish exactly in the integral Morse complex. An independent mod-two boundary rank calculation confirms the reduced Betti numbers 29 and 2 but does not replace the integral proof. The exact output is provided in `verification_output.txt` and ends with the Euler characteristic 28.

The result does not establish the equivariant homotopy type, higher-order projective-plane cases, a full distance filtration, or independent publication priority. No independent mathematical audit has been performed.
