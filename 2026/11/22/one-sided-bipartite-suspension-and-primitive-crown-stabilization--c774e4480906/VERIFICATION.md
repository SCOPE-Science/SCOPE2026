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

# Reproducibility and scope

Run `python3 verify.py` using standard Python 3. The companion `check_output.txt` records the actual result; it is not a substitute for the proof.

The verifier generates adjacency for rectangular matched-defect bipartite graphs, expands every closed-neighborhood simplex, checks that the two shore-generated hemispheres intersect in the original graph, and computes mod-two simplicial Betti numbers by exact binary elimination. It calculates signed fixed-face Lefschetz numbers and compares them with the predicted automorphism character for all listed permutations. Its output covers nine rectangular cases, 270 individual character checks, and three balanced controls.

The general suspension and primitive integral augmentation exact sequence follow from the explicit combinatorial collapses, homotopy pushout, Mayer–Vietoris sequence and graph-pair relative homology proved in `RESULT.md`; they are **not** inferred from these finite checks. The rational quotient conclusion uses finite-group invariants over characteristic zero. The verifier does not decide integral torsion in geometric quotients, global equivariant homotopy types, or bibliographic priority. Independent mathematical validation has not been performed.
