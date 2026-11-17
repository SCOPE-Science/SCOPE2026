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

# Reproducible verification

Run in the directory containing the attached standalone Python files:

```bash
python3 verify_mixed_theta.py
python3 verify_five_arm.py
```

Both programs use only the Python standard library. They reconstruct the graph metric by breadth-first search and enumerate **every nonempty Rips face** in the tested instances. `verify_mixed_theta.py` verifies all proposed radius-two free-face collapses for 63 path attachments, comprising 2,510 elementary pairs, and independently calculates mod-two homology for 28 mixed-theta graphs. Its inputs include base graphs with triangles and terminal distances exceeding three, as well as multiple successive ear attachments.

`verify_five_arm.py` verifies complete radius-three face enumerations for nine three/five-arm theta graphs with \(p\in\{2,3,4\}\) and \(q\in\{1,2,3\}\). It checks identical closed neighborhoods for removable short-arm vertices, independently replays all associated dominated-vertex free-face collapses, exhaustively constructs the long-arm factors, checks their four disjoint antipodal nonedges, and replays every cross-arm free-face collapse. It also computes complete mod-two boundary ranks and verifies the radius-four cone condition. Across its nine runs, it classifies 768 external cross-arm faces. The exact program outputs are in `verification_output.txt`.

**Limits:** Verified finite cases do not prove the all-parameter theorem and mod-two calculations alone do not establish integral torsion-freeness. The explicit, uniform elementary-collapse argument in `RESULT.md` establishes the integral homotopy type and the complete persistence barcode for arbitrary allowed parameters. This verification does not constitute an independent mathematical audit.
