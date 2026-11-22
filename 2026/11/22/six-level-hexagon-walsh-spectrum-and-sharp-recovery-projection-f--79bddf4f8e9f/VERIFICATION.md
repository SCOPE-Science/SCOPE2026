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

# Verification scope

Use `python3 verify.py`, with only the Python 3 standard library. The script fully reconstructs the graph from the Fano plane, enumerates its hexagons independently in two ways, computes a spanning-tree reduction and reconstructs the corresponding Eulerian cycles, tests the exact 256-character signed sums by both direct evaluation and a butterfly transform, and evaluates the Walsh projection kernel.

Exact expected values: twenty-eight six-cycles, cycle-space dimension eight, reduced multiplier histogram `{-8:28,-4:56,0:108,4:42,12:21,28:1}`, projection-kernel histogram `{-12:56,-4:42,0:28,4:21,8:108,148:1}`, rank `1212416`, nullity `884736`, smallest positive multiplier magnitude `4`, and endpoint norm `121/16`. The script asserts these identities and prints `PASS` only if all checks hold. The finite check covers all 256 reduced characters, not a sample; a separate full 2,097,152-character transform yielded the same enlarged multiplier table.

The exact numeric certificate is finite and is paired in `RESULT.md` with the general character-restriction and translation-averaging proofs. The code does not independently certify novelty or peer review.
