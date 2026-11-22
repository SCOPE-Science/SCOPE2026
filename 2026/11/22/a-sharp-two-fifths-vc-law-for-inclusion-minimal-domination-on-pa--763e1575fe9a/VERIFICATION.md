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

# Reproducing the exact finite-state proof

Extract `verify.py` and run `python3 verify.py` from the directory containing it. It has no third-party dependencies, network access or precomputed data. The expected final marker is `ALL_CHECKS_PASS`.

The script derives all 206 reachable deterministic support-language states from a 64-state local five-bit verifier, obtains exactly 140 terminal accepting states and 79 rejecting transitions, and checks the canonical ordered transition-pair digest `745e40a73b2b4c98aa3dee965bd42ffe216cefd75c1ccb361d3d905f7650bd1d`. It verifies every component of the max-plus vectors, including the 78 unreachable-at-that-length components assigned minus infinity, not just the maxima, for \(w_{n+5}=w_n+2\) at each length \(n=16,17,18,19,20\); the recurrence propagates these to all larger lengths. It verifies base dimensions for 0 through 20 and enumerates every shattered support using independent neighborhood domination and literal selected-vertex deletion for lengths 0 through 13.

`verification_output.txt` contains the captured successful run and prints sample entire polynomial coefficients at lengths 11 and 13. The exhaustive direct enumeration is a finite cross-check, not itself an all-length proof; the all-length result relies on the complete finite-state graph and max-plus induction. The experiment does not establish independent scientific validation, publication priority or the Littlestone dimension for general connected paths.
