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

# Reproducibility and verification

Run `python3 verify_cayley_lattice.py` and `python3 verify_cayley_graph.py` from the directory containing the files. Both programs require only Python 3's standard library. The first reconstructs the geometric intersection matrix from thirteen explicit divisor vectors, checks the self-intersections and off-diagonal incidences, and uses fraction-free exact determinants on the principal submatrices to test all \(8192\) subsets. It checks every permutation of the four node labels and all five fixed-support coefficient vectors.

The second program independently enumerates the allowable support sets from the proven four-vertex graph criterion rather than from determinants; then it checks Frobenius-invariance for all 24 permutations and computes the global orbits both directly and with Burnside's formula. The exact outputs are recorded in `verification_output.txt`. Every number in the displayed five-case classification is checked by each algorithm, and the two descriptions agree on 726 admissible geometric supports.

These are exhaustive finite computations because the geometry proves that the complete negative-curve list consists of precisely thirteen curves. The computations do not establish historical priority, do not prove additional claims about other cubic surfaces, and do not constitute an independent mathematical audit.
