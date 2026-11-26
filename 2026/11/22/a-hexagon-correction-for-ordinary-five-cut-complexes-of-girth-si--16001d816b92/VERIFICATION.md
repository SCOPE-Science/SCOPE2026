---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification

The accompanying `verify.py` enumerates connected five-sets, hexagons, the dual's possible six- and seven-vertex faces, disconnected four-set extensions, and the proposed free faces on eight finite graphs. Its recorded output is `verification_output.txt`. The companion `independent_mod2.py` constructs the ordinary cut complexes for five small examples and reduces the boundary matrices over \(\mathbb F_2\); its recorded output is `mod2_output.txt`.

A bounded reproduction independently checked the live cofaces of each proposed collapse at the moment of deletion, including a theta graph with three hexagons sharing three-edge paths. With \(H=c_5-h_6\) the number of removed three-faces, the checked \((c_5,h_6,B;H)\) are:

| Graph | Counts |
|---|---:|
| 10-cycle | (10, 0, 116; 10) |
| 11-cycle | (11, 0, 199; 11) |
| Hexagon plus isolates | (6, 1, 121; 5) |
| Two disjoint hexagons | (12, 2, 320; 10) |
| Three-branch theta graph | (24, 3, 105; 21) |
| Heawood | (252, 28, 491; 224) |
| Möbius–Kantor | (288, 24, 1101; 264) |
| Pappus | (324, 18, 2074; 306) |

In the first five rows a separate mod-two chain calculation also reproduced the stated top Betti numbers. This does not certify integral torsion-freeness or exhaust the family. The connector lemma and elementary collapses give the general integral result; the subsequent homotopy argument is not validated by mod-two ranks alone.
