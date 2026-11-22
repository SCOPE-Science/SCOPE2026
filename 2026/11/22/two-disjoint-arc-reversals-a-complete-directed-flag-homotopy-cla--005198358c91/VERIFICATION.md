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

Run `python verify.py` from the directory containing this file and `verification_output.txt` with Python 3 (standard library only). The executable enumerates every choice of four distinct vertices and all three pairings for \(n=4,\ldots,9\), evaluates transitive subtournaments from the forbidden-triple criterion, and compares mod-two reduced homology with the exact classification. It also validates the claimed ten elementary free-face pairs for the central five-vertex crossing core. Expected stdout is stored verbatim in `verification_output.txt`.

Actual checks: 756 full configurations, classifications distributed as 689 contractible-predicted, 52 circle, 10 three-sphere, and five \(S^1\vee S^2\). Each crossing free face is present and has exactly one proper containing coface at its removal step; the final complex is one vertex. All assertions passed.

The arithmetic checks are finite and over \(\mathbf F_2\); they do not independently establish integer homotopy types or universal quantification. The general proof in `RESULT.md` establishes those by explicit cone, join, suspension and simplicial-collapse arguments. No external audit or independent validation has been performed.
