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

# Reproduction of the exact finite reduction

Run `python3 verify.py --check certificate.json` with Python 3.9 or newer in the extracted artifact directory. No nonstandard library is required. The checker recomputes all matching-face lists, checks the seven-cycle action on every face, reconstructs the finite quotient cell incidences with orientation signs, verifies fifteen chosen elementary collapses and the spanning tree, and replays the ordered twenty-six generator-relator eliminations. It checks that the final nineteen two-cell attachments have degrees listed in the certificate, all divisible by seven, with at least one of absolute degree seven. The recorded standard output is in `verification_output.txt`.

The checker verifies a finite CW calculation, not a general theorem about all matching complexes. The passage from the reduced attaching words to the Moore-space wedge is a separate, explicit argument in RESULT.md. The supplied files give no independent external mathematical audit and make no homeomorphism or global-literature-priority claim.
