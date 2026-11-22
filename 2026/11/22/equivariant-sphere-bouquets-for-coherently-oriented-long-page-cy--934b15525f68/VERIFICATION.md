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

# Verification and reproducibility

Run `python3 verify.py` using Python 3 standard library. The included `verification_output.txt` records a completed run of the same code.

The program independently builds each finite digraph, tests every arc subset for degree and directed-cycle conditions, and compares the result to the stated face rule in 36 cases. It also constructs actual mod-two simplicial boundaries and checks Betti ranks and exact face counts in 24 bounded cases. Finally it forms genuine simplicial-cell orbit quotients and subgroup fixed supports for 15 finite subgroup examples. All tests passed. The all-parameter integral proof does **not** rely on those finite calculations: its key certificates are the exact missing-facet bijection, the explicit relative integral chain complex, and the fixed-space characterization.

The included program checks only finite graph instances and mod-two homology, not an independent proof of the infinite equivariant homotopy theorem. Its quotient calculation is over the field with two elements; the integral quotient assertions follow from the equivariant homotopy argument in the proof. Independent scientific auditing has not been performed.
