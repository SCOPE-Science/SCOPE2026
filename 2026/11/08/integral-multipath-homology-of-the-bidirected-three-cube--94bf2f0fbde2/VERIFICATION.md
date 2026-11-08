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

# Verification of integral multipath homology

The accompanying `verify_cube_multipath.py` is a standalone standard-library Python 3 program. It builds the graph and all face sets from their definitions; no signed matrices, face lists or claimed ranks are accepted as input.

The recursive source/outdegree path-extension enumerator and the combination-based indegree/outdegree plus cycle predicate generate **identical** face sets. Exhaustion is mathematical rather than heuristic: on eight graph vertices an acyclic disjoint directed-path union has at most seven arcs, and all \(536{,}155\) subsets of the 24 arcs with size at most seven are examined by the second enumerator.

Both opposite-coordinate discrete-Morse matchings undergo a full directed Hasse acyclicity test. Each selected pivot is checked to be \(\pm1\). Exact signed integer cancellations preserve augmented simplicial homology; the residual differentials square to zero. The integer diagonalization uses only elementary unimodular row/column operations and asserts that every residual nonzero pivot is a unit; it would fail rather than silently accept any nonunit Smith factor. The remaining matrices have rank two in degree four and rank four in degree five. Independent direct elimination of every original simplicial boundary over \(\mathbb F_2\) and \(\mathbb F_3\) agrees with these ranks and the derived integral Betti numbers. Hamiltonian cycle count supplies a further degree-six check.

The recorded output `verification_output.txt` is the stdout of an actual complete run; it ends with `INTEGRAL_CUBE_MULTIPATH_HOMOLOGY_VERIFIED`. These checks prove the complete fixed-object integral homology. They do **not** prove a wedge decomposition, classify any larger cube or constitute an independent external audit.
