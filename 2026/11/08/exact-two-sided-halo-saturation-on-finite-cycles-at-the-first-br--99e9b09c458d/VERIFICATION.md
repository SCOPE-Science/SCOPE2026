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

PASS: Correct strict halo criterion 3|I∩E|>2|I| iff e(I)>2z(I). A deletion-minimal circular arc subcover of all unmarked vertices is at most a two-cover by the common-point triple-arc redundancy lemma. Consequently 2k>=sum e_j>=2sum z_j+m>=2z+m, excluding k<=z. At N=4q+3, k=2q+2 and z odd, equality forces exactly two arcs each including every marked vertex and exactly half the z unmarked vertices, contradiction. k=floor(N/2)+1+1_{N≡3 mod4} consecutive markers works: for each site in gap choose a side to traverse all k markers plus at most ceil(z/2) missing markers, yielding k>2ceil(z/2). For even N checkerboard markers give 2/3 three-site averages but not strictly above threshold. Independent exact bitmask enumeration checked N=3..12 minima and constructions and verified arc triple-cover property in bounded cases. Infinite N follows from combinatorial argument.

## originality

PASS

Best-of-knowledge independent originality qualified: exact strict two-sided finite-cycle saturation and mod-four penalty are not supplied by identified one-sided or Solyanik results; inaccessible directly relevant full article remains explicit risk.

## value

PASS

The first local two-sided bridging threshold 2/3 is geometrically natural for an uncentered maximal operator. Its exact all-N full-halo saturation cardinality and exceptional N≡3 mod4 penalty are motivated finite-cycle extremal facts, not routine threshold renaming. A competing one-sided formula cannot substitute for the two-sided sharp placement obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
