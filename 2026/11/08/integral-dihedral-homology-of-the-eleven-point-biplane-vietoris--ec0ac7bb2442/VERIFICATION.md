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

# Finite exact verification

Run `python3 verify_biplane_dihedral.py` with Python 3 (standard library only). It reconstructs every incidence, all 22-by-22 shortest-path distances, and all 79 maximal radius-two cliques independently of the analytic classification. The exact zero-based list of 34 selected four-cycle columns is printed in `RESULT.md` and hard-coded as a reproducible minor certificate. The script computes the determinant via fraction-free integer Bareiss elimination and obtains \(-1\), thereby verifying the integral spanning condition; the topological deduction from it is spelled out in `RESULT.md`.

Independently, the program enumerates the complete face vector and calculates the mod-two chain boundary ranks, obtaining only ordinary \(\beta_0=1\) and \(\beta_3=21\). These mod-two checks corroborate but do not establish integral torsion-freeness, which is instead provided by the unimodular attaching minor.

For every element of the 22-member dihedral subgroup it verifies that the vertex action preserves all maximal simplices, calculates signed traces on all simplicial chain groups by explicit fixed-face enumeration, and converts Lefschetz numbers to degree-three homology traces. For nonidentity rotations the trace is \(-1\); for reflections it is \(+1\). The reflection has five fixed edges (chain sign \(-1\)) and five fixed tetrahedra (chain sign \(+1\)), giving Lefschetz number zero. The analytic pair count and the exact script result agree.

No machine output is used as a substitute for the proof of CW attaching-cell consequences or the finite-group rational character decomposition. No independent validation has been performed.
