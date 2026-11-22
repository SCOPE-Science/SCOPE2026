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

## Actual checks

- Checked the exact identity by direct enumeration of graph incidence traces in `CHECKER.py`.
- Compared all graph edge sets on at most four original vertices, all nonempty choices of marked original vertices and marked edge subsets, plus 40,000 deterministic randomized cases (50,260 total checked marked configurations).
- Classified 93,025 distinct finite marked-edge skeletons through seven vertices and six selected edges; found 4,402 maximal cases and verified the predicted component types.
- Verified explicit sharp constructions for every marked split with each side size at most ten, excluding the empty split (120 constructions), and verified marked-edge constructions through 34 marked edges.
- Independent review and formal proof assistant validation were not performed. Finite enumeration is corroborative only; the all-size Euler argument is the mathematical proof.

## Replay

From the extracted artifact directory run `python CHECKER.py`. The emitted output is reproduced verbatim in `CHECKER_OUTPUT.txt`.
