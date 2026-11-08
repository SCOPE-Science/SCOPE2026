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
# Verification evidence and limits

Run `python3 verify_packet.py` with Python 3. The program depends only on the standard library. It constructs all candidate lattice vectors of squared norm at most \(4\) for FCC and at most \(5\) for doubled BCC, then evaluates the necessary subset-sum constraints for all independent unordered triples. It checks the exact Gram-matrix patterns, all integer determinants, the candidate counts, and every permutation tetrahedron's ball center with rational arithmetic.

Expected successful checks: `FCC_PASS 24 unordered optimal frames; 144 ordered frames; 96 radius^2=1 and 48 radius^2=3/4 packet simplices` and `BCC_PASS 8 unordered optimal frames; 48 ordered frames; all 48 doubled-coordinate packet simplices have radius^2=5/4`.

The proof, not finite computation alone, establishes why the finite list contains **every** possible optimum: any candidate frame with no larger packet radius must satisfy the subset-sum diameter inequality, so its lattice vectors are already in the enumerated bounded set. The exact squared radii are proved by explicit centers and matching lower bounds. No general statement about other lattices or higher dimensions is established, and independent audit has not been performed.
