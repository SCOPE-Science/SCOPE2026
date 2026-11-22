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

# Reproduction record

Extract `check.py` and `collapses.json` side by side and run `python check.py` using Python 3.9 or later. No third-party modules are required. The script independently builds all-pairs graph distances by BFS and Floyd–Warshall, checks 336 forbidden triples, enumerates all \(2^{16}\) subsets, reconstructs the \((16,120,224,220,80)\) face vector, replays the 227 actual free-face collapses, validates the remaining \((16,85,77,28)\) complex, verifies signed compositions of differentials are zero, and uses integer unimodular row and column elimination for ranks \((15,46,27)\), with all nonzero Smith factors one. The resulting reduced integral Betti ranks are \((0,24,4,1)\) in degrees zero to three.

These are exact finite computations with a replayable face-collapse certificate; they do not independently establish novelty or larger-family results. No external independent audit has been performed.
