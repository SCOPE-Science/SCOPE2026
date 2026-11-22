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
Run `python3 VERIFY.py` with Python 3.9+; the file has no external dependencies. The program reconstructs the cyclic-power graph and flag simplices directly, checks common-neighbor interval identities and dominated-vertex reductions, replays each proposed relative elementary collapse with a free-coface test in 29 nonexceptional finite fault instances, plus three exceptional face checks, checks intact cyclic flag collapses for five powers, and verifies that the exceptional squared-cycle fault collapses to a connected rank-two graph.

The actual program exited successfully and printed four PASS lines. Its complete output can be regenerated from the embedded code. These finite checks are supplementary to the all-integer mathematical argument. They do not certify unpublished prior art, minimality of the graph-order bound, or independent validation.
