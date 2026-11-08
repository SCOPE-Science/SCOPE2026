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

Run `python3 verify.py` with Python 3.9 or later. The program requires only the standard library and ends with `VERIFY_OK` if all assertions hold.

The checker constructs the Lie brackets from seven independent structure constants and verifies the alternating law and all basis-triple Jacobi identities in three fields. It independently checks the central derivation rule on all ordered basis pairs, enumerates every possible central map, and checks pointwise commutator membership for every generator direction. Over \(\mathbb F_2\), it additionally tests all \(256\) elements of the algebra against the noninner example and checks all \(16\) central maps against all elements. Direct enumeration of inner linear maps yields \(32\) different maps, agreeing with the center dimension.

Observed counts: over \(\mathbb F_2\), eight central almost-inner maps versus four central inner maps; over \(\mathbb F_3\), nine versus nine; over \(\mathbb F_4\), sixteen versus sixteen.

This is a finite computational check, not a universal proof. The universal statement rests on the structural reduction and determinant calculation in `RESULT.md`. The count of all almost-inner maps also uses that the class-three quotient has only inner almost-inner derivations, proved there. An independent mathematical audit has not been performed.
