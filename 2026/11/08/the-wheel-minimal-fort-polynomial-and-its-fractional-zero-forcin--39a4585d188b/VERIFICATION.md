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

# Computational verification of the wheel minimal-fort theorem

Run from the artifact directory:

```
python3 verify_wheel_forts.py
```

The program uses only the Python 3 standard library. It independently builds every wheel \(W_{n+1}\) for \(3\le n\le12\), tests every nonempty selected vertex subset against the fort condition, and tests inclusion-minimality by examining every proper nonempty subset. The resulting complete cardinality counts and hub-containing counts are compared with exact integer-polynomial recurrences derived from the displayed denominators \(A\) and \(B\). The initial published thirteen-term hub sequence is checked separately. Recurrence consistency and positivity are checked through rim order 160. For the directly enumerated graph instances, the proposed uniform fractional transversal weights satisfy every minimal-fort inequality exactly, and two disjoint minimal forts are found in each instance.

A numerical LP optimization check using SciPy's HiGHS solver was separately executed on every enumerated minimal-fort hypergraph for rim orders three through twelve. Its optimum equalled the claimed rational value in all cases. This external numerical solver check is corroboration only; the exact fractional formula relies on the symmetrization proof in RESULT.md.

The exhaustive graph-level computation is finite, and the recurrence is a computational consequence of the same symbolic denominators. They are not independent mathematical certification and cannot exclude overlapping unpublished or unindexed prior results. Independent audit has not been performed.
