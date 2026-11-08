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
# Verification record

Run `python3 verify_franklin_character.py` and `python3 verify_franklin_boundary.py` from this package. Both require only Python's standard library. Exact output is stored in `character_output.txt` and `boundary_output.txt`.

The character verifier enumerates all 1091 nonempty matching faces, checks 539 Morse pairs and an acyclic directed Hasse diagram of 3942 incidences, constructs all 48 graph automorphisms by exhaustive adjacency-preserving backtracking, and computes the reduced Lefschetz character both by signed fixed simplices and by independent compatible edge-orbit enumeration. All ten class representatives, sizes and traces are printed. The index-two complement to the central half-turn is verified to act faithfully on four order-three subgroups, and all five irreducible character identities are checked.

The second verifier independently enumerates every subset of the eighteen graph edges and performs mod-two Gaussian elimination on simplicial boundaries. Its reduced Betti numbers agree with the integral discrete-Morse proof; mod-two evidence alone is not used to infer integral homotopy.

The claims are restricted to ordinary matching complexes of the explicitly given Franklin graph, the full rational third-homology character, and its \(S_4\times C_2\) decomposition. No independent audit or formal mathematical certification has been performed.
