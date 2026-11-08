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

# Verification of the finite checks

Run `python3 verify_penultimate_fixed.py` in a directory containing this file and the script. Only the Python standard library is required. `verification_output.txt` contains the checked program output, whose final line is `PENULTIMATE_COORDINATE_FIXED_SPHERES_OK`.

The script constructs every binary vector and compares every weight-orbit pair directly (without substituting the closed-form distance formula) for dimensions \(2\) through \(10\). It independently checks the predicted admissible weight classes and all their pair compatibilities. On \(B_m\), it verifies every neighborhood inclusion at the exact point it is used, plus the final residual graph, for \(1\le m\le30\). It also constructs independent sets and mod-two boundary matrices for \(1\le m\le6\) and confirms the expected homology ranks. The complement checks verify the lack of admissible paired orbit vertices for \(1\le m\le20\).

The unbounded theorem follows from the orbit model and neighborhood-collapse proof in `RESULT.md`; numerical ranges are only corroborative. Mod-two calculations do not independently prove torsion-freeness, which is supplied by the explicit integral homotopy collapse. The homology sign uses the integral Lefschetz trace argument, not a finite numerical inference. No independent external audit or validation has been carried out.
