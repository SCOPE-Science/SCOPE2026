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

# Exact verification

The attached `verify.py` uses Python 3.9+ and the standard library only. Run `python3 verify.py`. Its recorded output is in `verification_output.txt`.

The program exhaustively tests the \(2^{16}\) vertex subsets by their induced degrees; independently builds all faces using component-size checks; confirms the full face vector, the 96 and 120 maximal faces in dimensions six and seven respectively, and the 3,405 augmented matching pairs; then verifies all 35,104 ordinary directed Hasse incidences by a topological ordering of all 6,812 nonempty faces. The surviving ordinary critical cells are one vertex and three dimension-six cells. Exact mod-two simplicial chain-rank calculations give unreduced Betti numbers \((1,0,0,0,0,0,3,0)\).

All eight graph rotations are checked as automorphisms, and their signed fixed-face Lefschetz traces give the character \((3,-1,-1,-1,3,-1,-1,-1)\), which exactly equals the sum of the sign and rational fourth-root characters. The invariant rank is zero by averaging. A finite certificate does not prove a general family theorem or independently establish novelty, and no independent audit has been performed.
