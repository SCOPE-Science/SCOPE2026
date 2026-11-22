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

Execute `python3 verify_heawood_matching_collapse.py` with Python 3 standard library in the same extracted directory. The code constructs every graph adjacency, every simplicial face, every graph automorphism and every matching from their definitions. It verifies the complete \(8{,}850\)-nonempty-face directed Hasse acyclicity of the intact Morse matching and checks all \(121\) orbit-representative relative elementary collapse sequences. It also checks that the full \(30\)-orbit partition covers all \(3{,}462\) matchings, with no reliance on an external orbit table. An elementary collapse is certified by the exact remaining codimension-one cofaces of the free face, with every target face preserved. The Python output is embedded in `verification_output.txt`, but the output alone is not a proof.

The proof uses exact integers and finite sets, not approximate linear algebra. The use of the standard discrete-Morse theorem to infer the intact \(S^6\) homotopy type is the only substantive general topological result beyond elementary collapses. The possible risks are ordinary implementation mistakes despite the exhaustive checks and unindexed equivalent prior publications. The scientific claim has undergone a self-review; no external or independent audit has been performed.
