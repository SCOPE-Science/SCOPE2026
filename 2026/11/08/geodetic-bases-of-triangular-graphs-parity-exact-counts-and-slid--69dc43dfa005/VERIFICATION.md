---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In L(K_n) an omitted ab must be the middle of a length-two shortest path between disjoint selected ax and by, so the endpoint neighbor sets must allow different x and y. Failure is precisely an isolated endpoint somewhere or two leaves attached to the same vertex. At the edge-cover bound even n gives a matching; odd n gives one P3 and matching edges, and P3 is forbidden. With n=2k+1 and k+2 edges the component count is k or k−1 by cycle rank. The former forces a triangle and the latter a forest with total excess three over two vertices per component. No 3-vertex tree is allowed, so the unique larger tree has five vertices; any nonpath tree of that size has two leaves with a common neighbor. Matching counts and the 5!/2 path factor then give the census. A matched-edge deletion cannot be repaired. In a triangle, deleting one of three edges allows four attachments per external pair, all slides. In a P5 labeled 1 through 5, each terminal deletion allows only reconnection 15; deleting 23 leaves 12 and 3–4–5, so internally the allowed inserts are 13,15,25,35, with only 15 a jump-only move. Reflecting gives the symmetric internal deletion, and each internal deletion adds four moves per external pair, two slides. This gives all stated degrees. The explicit three-slide sequence swaps one triangle label with one matching label, and using the current triangle label as a buffer for three such exchanges swaps two exterior labels while restoring the triangle. Path states slide to triangle states, yielding odd-order connectivity including the singleton n=3; even states have no moves.

## originality

PASS

The closest read treatment of the ordinary geodetic number on this exact graph obtains an upper bound, not the sharp parity classification, the minimum-state census, or the slide/jump structure. The cited non-split problem and a nearby distance-equalizer census are different invariants.

## value

PASS

The complete minimum-state classification for the natural triangular family explains an exact parity effect and also fully resolves local mobility. In particular it distinguishes an entirely frozen even family from a connected odd family even for the more restrictive slide rule; neither the upper bound nor recording a few counts explains this.

The dated certificate retains the supplied scientific assessment, sources and limitations.
