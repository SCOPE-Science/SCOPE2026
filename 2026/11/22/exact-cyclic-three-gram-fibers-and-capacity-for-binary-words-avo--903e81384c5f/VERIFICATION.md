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

Run `python3 check.py` using Python 3 and no third-party modules. The program independently generates every binary circular source through circumference 15, discards cyclic `11`, canonicalizes rotations, measures all eight oriented length-three factors, groups exact inverse fibers, and compares them to the totient/Burnside formula. For each circumference it separately checks the distinguishable-profile count, the singleton-profile count, and the first ambiguity boundary. All tests passed. The checks do not establish novelty or substitute for the algebraic all-length proof.
