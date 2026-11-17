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

# Verification

The supplied `verify.py` is executable with Python 3 and the standard library only: `python3 verify.py`. It enumerates actual cyclic actions on uniform matroid vertices and compares the invariant orbit-support faces with the proposed skeleton, checks reduced homology ranks over \(\mathbb F_2\), and checks all small label-permutation signed Lefschetz traces directly on faces. It also checks a primitive coefficient divisibility pattern. Output from the included script was reproduced:

`UNIFORM_MATROID_ORBIT_EXTERIOR_CHECKS_PASS cases=45 symmetric_actions=12498 signed_trace_checks=12498`

These 45 parameter instances, 12,498 symmetry actions, and 12,498 trace comparisons are **finite corroboration only**. They do not prove an exact Ext order for every parameter. The proof of the general theorem rests on the literal orbit-coordinate PL correspondence, a stable contractible subcomplex, exterior contraction, uniqueness of a rational equivariant lift between nonisomorphic hook modules, and an explicit primitive coefficient test. The last three steps prove the exact integer order independently of any finite test.

Scientific limitation: the exact order concerns one canonical integral module extension; it is not ordinary homology torsion or a classification of all equivariant homotopy types. Historical literature could contain an equivalent formulation not found during the searches.
