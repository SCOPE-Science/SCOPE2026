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

# Executable verification and limits

Run `python3 verify_hexprism.py` from the directory containing the provided program; no third-party packages are required. The script reconstructs the eighteen graph edges, enumerates all 1,104 matching faces including the empty face, builds a 544-pair acyclic ordinary-cell discrete-Morse matching, and checks acyclicity by a complete topological sort of all 4,002 Hasse covers among the 1,103 nonempty faces. The resulting critical-cell dimensions are one zero-cell, thirteen three-cells, one four-cell.

Exact recursive **integer** elimination of matched-cell boundary relations produces the complete critical four-to-three differential, with column \((1,1,1,0,0,0,0,0,0,0,0,0,0)^\mathsf T\). Direct mod-two simplicial elimination provides an independent sanity check of the homology ranks. The same program enumerates all 24 dihedral-layer symmetries and signed fixed-chain traces and computes their rational irreducible multiplicities by integral character inner products. Recorded output in `VERIFY_OUTPUT.txt` was produced by executing that exact code.

This finite exhaustive proof does not extend to larger prism graphs without a new argument. Although the computation checks the discrete-Morse hypotheses and the exact attaching degrees, it is not a substitute for independent human assessment of literature priority or of the proof explanation.
