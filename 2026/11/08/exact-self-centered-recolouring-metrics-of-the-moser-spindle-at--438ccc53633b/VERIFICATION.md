---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Graph is explicitly the 7-vertex 11-edge H4 Hajós/Moser spindle. Proper named k-colorings form vertices and legal one-vertex changes form edges. Exhaustive enumeration of ALL k^7 functions and ALL legal moves followed by BFS from EACH proper coloring is an exhaustive finite proof, not sample evidence. Independently implemented C++ BFS (not relying on submitted logs) obtained k=4:384 states,528 edges, all eccentricities13 and exact unordered distance histogram (528,960,1584,2496,4080,6624,9456,10896,11232,11472,10896,2832,480); k=5:5040 states,22560 edges, all eccentricities10 and histogram (22560,110400,382680,1019520,2102160,3196920,3290400,2005200,534600,33840). Correct palette labeling, unused colors, connectedness, degree histograms and N choose 2 sums checked. All graph states/pairs enumerated exactly.

## originality

PASS

Cereceda–van den Heuvel–Johnson 2005 Property 7 proves H4 is k-mixing for k>=4, so connectedness is prior. It does not determine the exact two graph diameters, self-centered eccentricity for every named coloring, or all pair-distance histograms. Resultary searches for the exact Moser spindle metric found this record and metric studies of different graphs (Petersen, Wagner, Grötzsch), not a previous same-object table. This is a natural finite exact refinement, not a claim of new connectivity or a general family theorem.

## value

PASS

The Moser spindle is a canonical smallest-form unit-distance 4-chromatic obstruction; its critical-palette 4/5 color reconfiguration graphs are natural finite objects. Exact sharp worst-case recoloring distances and all-vertex self-centeredness provide explicit benchmarks and demonstrate an uncommon nonregular self-centered metric phenomenon; complete pair histogram is independently reproducible and not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
