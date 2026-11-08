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
The theorem combines a necessary-and-sufficient gap-count argument, the explicit floor construction, the cut-complex link identity, and the known seven-vertex \(S^1\) obstruction. The seed is independently tested by a complete 25-pair elementary-collapse certificate.

Run `python3 verify.py` in a directory containing this file and the verifier. It recomputes the seven disconnected triples, the face vector \((7,21,21,7)\), the complete elementary-collapse sequence and its terminal triangle boundary. It checks both directions by exhaustive seven-subset enumeration in 27 small parameter cases, and also checks 5,701 parameter cases for \(2\le p\le100\) and fourteen actual link-comparison cases for \(2\le p\le6\). The recorded stdout is in `verification_output.txt`; a final line `ALL_VERIFY_OK` indicates successful replay.

The finite tests do not establish the unrestricted theorem; the all-integer argument is contained in `RESULT.md`. Independent audit has not been performed.
