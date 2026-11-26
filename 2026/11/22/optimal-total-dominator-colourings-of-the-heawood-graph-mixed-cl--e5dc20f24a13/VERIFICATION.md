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

An independent complete reproduction, python3 /workspace/evidence/heawood_replay.py, returned HEAWOOD_REPLAY_OK. It catalogues all nonempty independent subsets and all vertices each can witness by open-neighbourhood inclusion, then enumerates exact covers with at most eight blocks by always covering the least remaining vertex. This canonically selects one block of each possible partition at a time. A branch can be pruned if an unmet vertex has no neighbour left, since a future witness block must be nonempty and entirely contained in its remaining neighbourhood. This yields no valid partitions below eight and 2,751 at eight. On each side it also independently counts witnesses down to one block (the uploaded side checker instead filters for at least four), obtaining 49, 140, 21, 1 at 4–7 and the asserted collinear/pencil and (1,1,2,3) profiles at four. In a mixed class there is no common neighbour at all. Pair counts were recovered directly from the eight-block states by restricting to the two sides; (4,4), (4,5), (5,4), (5,5) give 2401,161,161,28 respectively. Every valid edge is equivalent to equal eight-block restrictions after deleting its moved vertex, and conversely two distinct partitions with the same such restriction differ by exactly that move. This independently yields 11,662 edges, degrees 0:21, 2:56, 5:224, 6:476, 7:168, 10:1806, components 21 singletons and orders 966 and 1764, the dual profiles at 1764, and the 616/322/28 split at 966. The isolate set equals that constructed directly from all 21 incident flags. Multiplying by 8! gives 110,920,320. The uploaded code was inspected, not run. In the side-pairing prose, witness coverage must be tested after all merges jointly (as the code does). The prior-work paragraph's shorthand '350 mixed optimum classes' should read '350 optimum partitions with mixed classes'; the Finding already has the correct wording and counts.

## originality

PASS

The scalar minimum is known and not an original contribution. The full census of optimal unlabelled partitions, mixed cases, and the associated one-vertex recolouring graph goes beyond the inspected scalar theorem and neighbouring Heawood classifications. One close flag indexing genuinely recurs, but for a different state space and constraint.

## value

PASS

The Fano incidence graph is a canonical test case rather than an arbitrary finite slice. Class counts answer whether an optimal colouring can violate the class-first domination condition while still giving every vertex a witness. The exact move graph answers which optimal states can be reconfigured without raising the palette: a whole dual block-profile sector is inaccessible from any mixed state, and the incident flags are precisely the isolates. Neither feature follows just from the known scalar optimum. This is a finite benchmark and structure classification, not a formula for larger planes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
