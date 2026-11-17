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

# Reproducible finite proof checks

Run `python3 verify.py` in a clean Python 3 environment; no third-party packages are required. The program enumerates the twelve lines, the seventy-two matroid bases and fifty-four four-point caps in lexicographic order; constructs all boundaries; verifies a unimodular rank-28 boundary section and the integral rank-44 kernel lattice; verifies a unimodular rank-43 minor for the cap cycles; and checks the area functional on each kernel basis vector. It also enumerates all 432 affine automorphisms and verifies the orientation sign rule and cap transitivity.

The included `verification_output.txt` is actual output of this program. These exhaustive finite checks certify the exact integer calculations for the explicitly enumerated nine-point object, assuming faithful execution of the included source. The logical steps from the two minors and the primitive functional to the homology quotient, and the minimum-support argument, appear in `RESULT.md`.

No independent audit has been performed. The result does not extend by finite enumeration to arbitrary affine planes.
