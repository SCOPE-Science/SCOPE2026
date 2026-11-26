---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The dot-product model gives a 3-regular bipartite graph and exactly 14*3*2=84 oriented move triples. The first-move decomposition is exact since a legal move consumes one peg, and a separate sequence is allowed for each target. Monotonicity follows by simulating the moves of a smaller set in a larger one, skipping a move if its landing vertex is already occupied: after that step the larger position still contains the smaller successor. Hence deletion of one peg at a time suffices to test inclusion-minimality. The full automorphism group consists of the Fano collineations GL(3,2) and their compositions with duality: the bipartition is unique and a point map preserving collinear triples preserves addition of distinct nonzero vectors. The frozen recurrence, C++ scan and forward search were inspected, not executed. An independent target-by-target boolean DP over all 16384 masks verified the complete size vector 0,0,0,0,336,1862,2989,3430,3003,2002,1001,364,91,14,1. It checked all four-set patterns and five-set failures, the 336 and 434 inclusion-minimal counts, and all four stated five-set orbits and representatives. Among four-sets the three winning patterns occur 168,84,84 times; for an unordered line pair the point pool has a single common incident point, two incident only to each respective line and two incident to neither, giving 8,4,4 choices per line pair. The failures at sizes six and seven are exactly the independent sets, so the optimum for some distribution is 4 and the threshold for every distribution is 8. Replay: `python3 /workspace/branches/2eb17ad4-ac1c-4d66-b74a-9ce7fe46fa42/heawood_check.py`; `run.txt` there also records target-specific jump sequences for one optimum.

## originality

PASS

The labelled census, Fano incidence iff for optimal starts and minimal-orbit classification are distinct in the checked evidence. The guarantee that some four-set reaches everything is already covered by the original pegging paper's vertex-edge diameter bound and is not credited as new in isolation.

## value

PASS

Heawood is the natural small cubic incidence graph of the Fano plane. The result does more than find an optimum already bounded by a general theorem: the three local incidence patterns classify every optimum, and the four irredundant five-set orbits show that not all minimal solutions are supersets of an optimum. The failure geometry and separation between the some-start and every-start thresholds give a reusable exact benchmark for nonreversible pegging, without implying a result for larger planes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
