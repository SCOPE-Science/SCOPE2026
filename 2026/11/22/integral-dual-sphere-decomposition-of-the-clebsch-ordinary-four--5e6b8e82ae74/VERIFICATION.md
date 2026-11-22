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

The included Python 3 program `verify_clebsch_4cut_dual.py` requires no third-party packages. Run it directly in a shell. Its recorded output `verification_output.txt` ends with `VERIFY_OK`.

The program exhaustively reconstructs all graph edges, all 680 connected four-subsets, all 192 five-faces and the absence of six-faces; it checks the 40-edge \((16,5,0,2)\) graph parameters. It verifies signed \(\partial_3\partial_4=0\), independently computes 455 unit pivots for the three-boundary relative to the natural 2-cycle basis, and 191 unit pivots for the four-boundary. Every pivot is \(\pm1\), all residual columns are exactly zero, and the operations are unimodular over \(\mathbb Z\), proving primitive image and excluding hidden torsion. The script prints deterministic pivot-order SHA-256 digests as additional reproduction fingerprints.

The homotopy conclusion uses the full two-skeleton, Hurewicz, the integral homotopy classification of a two-connected three-dimensional CW complex, and primitive four-cell attachments. The cut-complex homology then follows by integral combinatorial Alexander duality. The computation alone does not prove the original cut complex has a particular homotopy type. No independent audit has been performed.
