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

Removing graph edges shrinks the dominance complex: a face contains no closed neighborhood. In a one-edge deletion, the relative set is upward closed in the source complex. A remaining relative simplex with exactly one immediate coface has no larger coface (such a coface would give at least two immediate ones) and no coface in the target. Its removal with that immediate coface is therefore a legal elementary collapse. An independent direct enumeration, without any graph symmetry, exhausted all 14,595 marked matching deletions (including nonextendible matchings), removing all relative faces in every case with 3,542,784 elementary pairs. It reproduced the full matching histogram (1,21,168,644,1218,1050,336,24) and the 1,260 nonextendible matchings. For the intact complex it independently checked 8,850 nonempty faces, 52,304 incidences, and acyclicity by DFS for a reverse-coordinate Morse pairing with just a critical 0-cell and 6-cell. The resulting CW model has the 6-cell attached to the point, so is S^6 up to homotopy. Concatenating collapses gives the canonical inclusion result and hence integral homology isomorphisms, not merely field Betti-number agreement. The recorded orbit method is sound: use the actual line-neighborhood triples, all shore-preserving collineations and the verified swapping polarity, and check every marked edge of each representative. The 121 checks are representative transitions, not asserted to be a minimal list of marked orbits.

## originality

PASS

The distinct claim is the relative elementary collapse for every matching fault, not the previously established intact sphere. No equivalent or mechanically covering result was identified in the bounded statement-level comparisons.

## value

PASS

The Heawood graph is the canonical Fano incidence graph and the closed-neighborhood complex tracks domination under deletion. Independent incidence faults can remove one third of the edges; there are many nonextendible fault sets, so it is substantive that every permitted deletion path retains not just a homology rank but its canonical integral class by relative elementary collapses. This is an exact stability property and a replayable benchmark for other incidence complexes, not a recomputation of the intact sphere.

The dated certificate retains the supplied scientific assessment, sources and limitations.
