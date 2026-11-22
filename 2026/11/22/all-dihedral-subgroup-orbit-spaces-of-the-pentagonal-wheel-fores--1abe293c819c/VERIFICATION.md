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

# Verification of the finite integral computation
Run `python3 verify_wheel_quotients.py` using Python 3.9 or later. It regenerates all forest faces, canonicalizes each flag under the specified graph-automorphism action, builds integral flag-orbit cellular boundaries, checks consecutive boundary compositions, and performs unimodular chain reductions on the resulting matrices. It asserts the exact orbit cell counts and final ranks, and prints `VERIFY_OK` on completion.

The expected quotient-cell vectors (degrees zero through four) are \((93,1358,4992,6624,2904)\) for the rotations, \((244,3432,12504,16560,7260)\) for a reflection, and \((60,716,2520,3312,1452)\) for full dihedral symmetry. Reduced chain ranks after all integer unit cancellations are, respectively, \((1,0,0,0,6)\), \((1,0,0,0,15)\), and \((1,0,0,0,3)\). The labeled complex has \((10,45,115,170,121)\) nonempty faces by cardinality and a thirty-element edge-rooted forest basis index set. The independent index-set test verifies three free dihedral orbits.

The program proves the integer chain calculation only for the precisely described finite simplicial complex. It does not by itself prove the external theorems invoked for the simply connected labeled forest complex, the fundamental group of the orbit space, or the Whitehead–Hurewicz conclusion; those hypotheses and deductions are written separately in RESULT.md. No independent audit has been performed.
