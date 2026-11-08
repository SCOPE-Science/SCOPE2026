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

# Verification and its limitations
The companion `verify_line_hex.py` is self-contained and uses only the Python standard library. It constructs the original graph, its line graph and square, enumerates every Rips face and every closed-neighborhood-core face, enumerates all simple six-cycles and both alternating triangles, checks the exact set difference, performs every claimed elementary collapse with a complete remaining-face coface check, and compares binary Betti numbers with the two-cell predictions. Its emitted output is included as `verification_output.txt`.

The checks cover seven source graph families: cycles \(C_6,C_7,C_8\); two theta graphs with respectively three and four length-three arms; three once-subdivided complete graphs with four through six original vertices; and the Heawood incidence graph. The most overlapping case, subdivision of \(K_6\), has twenty distinct hexagons, forty exceptional triangles and 450 directly checked elementary-collapse pairs. The Heawood graph has twenty-eight hexagons, fifty-six exceptional triangles and mod-two second Betti number forty-eight. Checks report the full graph counts and face counts.

The argument for arbitrary graph order is the explicit combinatorial proof in `RESULT.md`. Finite homology checks are over \(\mathbb F_2\), not an integral Smith-normal-form computation. The integral result is instead established by the two-dimensional CW model and its exact integer boundary map; the only possible torsion mentioned is in first homology. No test of finitely many graphs could by itself prove the universal claim. Independent validation has not been performed.
