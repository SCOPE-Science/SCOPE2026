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

# Reproducibility and scope

Run `python verify_rule73.py` for the complete exact-integer finite-state certificate. It constructs \(735\) states of a deterministic Boolean-relation automaton and checks \(a_n=b_n\) for \(1\le n\le39\), then \(735\) recurrence evaluations for \(40\le n\le774\). Cayley–Hamilton makes the latter checks logically sufficient for every larger index. The expected terminal line is `VERIFY_OK`.

Run `python check_small.py` for a separate direct-exhaustive input-to-output calculation at every ring length \(1\le n\le16\). The expected terminal line is `BRUTE_OK`.

The arithmetic is exact integer computation, with no randomization or external libraries. The proof does not rely on finite extrapolation. An independent mathematical audit has not been performed. These scripts verify the stated one-step cyclic image formula, not multi-step behavior or historical priority.
