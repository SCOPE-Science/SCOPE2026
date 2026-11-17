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

The structural proof analyzes every integer \(n\ge3\). Its critical steps are: (i) exact geodesic-to-three-edge-path correspondence; (ii) the thin-column join \(A_n=D_1*\cdots*D_n\); (iii) the complete thick-column cover \(B_j\), with \(B_j\) contractible and all cross-intersections lying in \(A_n\); (iv) each \(L_j=B_j\cap A_n\simeq S^1\); (v) simple connectivity of \(A_n\), making every attaching circle nullhomotopic. Integral long exact sequences yield the inclusion and symmetry statements.

Run `python verify_rook_gp_homotopy.py` to reproduce `verification_output.txt` with standard Python 3. The program independently compares direct graph-geodesic faces, star-forest faces and the proposed cover for every subset on boards with \(n\in\{2,3,4,5\}\). It then calculates reduced homology over \(\mathbb F_2\) using exact bit-matrix elimination, and checks fifteen signed Lefschetz characters for row/column permutations against the derived integral-module characters.

The finite calculations do not prove the unrestricted homotopy theorem, torsion-freeness or the integral symmetry modules. Those claims rely on the explicit joins and homotopy pushouts above. No computer proof system, external certificate or independent mathematical audit is claimed.
