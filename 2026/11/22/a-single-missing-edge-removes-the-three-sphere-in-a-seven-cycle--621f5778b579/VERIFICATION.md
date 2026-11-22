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

The standalone `verify.py` was executed with Python 3. It generated all 5,282 independent faces of the intact graph, all 5,647 faces after one edge deletion, and all 365 faces of the closed-neighborhood deletion link, including the empty face in each count. A separate complete enumeration of the 2,097,152 vertex masks corroborated both full face sets.

The checker built disjoint codimension-one acyclic Morse matchings with 2,638, 2,821, and 181 pairs, respectively. Complete directed-Hasse topological sorts passed over 5,281, 5,646, and 364 nonempty faces. The signed integral Morse differential from the three critical degree-four cells to the single critical degree-three cell of the intact complex was exactly zero in each column. The entire 42-edge automorphism orbit and the exact relative-face pushout were verified.

The interpretation of these finite certificates requires standard discrete Morse theory, simplicial cofibration, and integral homotopy reasoning. No independent external audit has been conducted. The finding does not concern multiple-edge faults or other graph orders.
