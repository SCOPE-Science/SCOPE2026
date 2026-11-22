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

# Reproducibility
Execute the following with Python 3 and the standard library in a directory containing the supplied files:

```
python3 checks/direct_ternary.py
python3 checks/independent_family_census.py
```

The first enumerates all \(3^{10}=59049\) ternary assignments and checks the two independent color classes and both neighbor-color requirements directly; it also partitions the \(110\) solutions into five automorphism orbits by all \(120\) ground permutations. The second enumerates the \(75\) nonempty intersecting edge families of \(K_5\), checks ordered disjoint family pairs against an explicit zero-edge obstruction condition, and tabulates the five possible types. The two algorithms were run successfully; the exact membership bitstrings both had SHA-256 `9b0ed36c88e965202e95769ae99bad5673ac9d9bd0b3ecb0e1910e9aa8648087`.

The programs test all feasible labelled functions (not just minima) and use different primary representations. Their agreement is a finite computational verification; the proof in RESULT.md supplies a separate structural classification. The check does not establish novelty, validate unrestricted graph families, or constitute an independent external audit.
