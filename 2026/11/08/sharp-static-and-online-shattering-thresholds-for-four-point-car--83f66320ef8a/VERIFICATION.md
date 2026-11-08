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
The exact mathematical proof establishes all \(m,n\ge2\). Run `python3 checker.py` in the same directory. It reconstructs all fixed-two-row, fixed-two-column concepts for six finite parameter pairs, computes every support trace through size three, and evaluates the exact mistake-tree minimax recurrence. It verifies a concrete eight-leaf depth-three tree on the \(3\times3\) grid, including distinct witnesses at every leaf. `checker_output.txt` stores the independently reproduced stdout. Experiments are evidence only for finite cases; they do not replace the all-parameter proof. Independent audit is not performed.
