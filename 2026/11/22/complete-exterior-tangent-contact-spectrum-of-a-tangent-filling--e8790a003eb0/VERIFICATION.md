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
# Verification of exterior tangent-contact spectrum

The proof in `RESULT.md` is valid for every prime power of characteristic greater than three. It uses a nonsingular conic for each exterior boundary point, a nodal cubic for the singular exterior point, and the exact quadratic-character sum for a separable quadratic. No sample computation is used to assert an infinite-field identity.

Run `python3 verify_tangent.py`. This program creates the finite fields with prime orders \(5,7,11,13,17,19,23,29,31\) and quadratic orders \(25,49,121\), enumerates every rational projective point and every smooth rational contact, computes tangent gradients directly, then compares each exterior contact count with the symbolic formula and aggregate histogram. Its success sentinel is `ALL_EXTERIOR_TANGENT_CONTACT_TESTS_PASSED`. The code requires only the Python standard library.

The experiment does not assess priority, does not cover infinitely many fields computationally, and does not compute distinct tangent-line multiplicities. The non-computational proof is explicit in the result document.
