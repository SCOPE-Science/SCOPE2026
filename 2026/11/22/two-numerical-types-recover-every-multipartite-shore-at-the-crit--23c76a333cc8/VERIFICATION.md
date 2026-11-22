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

# Verification and reproducibility

The complete statement and unbounded proof are in `RESULT.md`. Run the standalone standard-library program with:

```sh
python3 verification/check_counts.py
```

The actual console output of a completed execution is included in `verification/output.txt`. The script independently builds each named complete multipartite graph, creates all labelled adjacency diagrams with two distinct fresh vertices, and tests every candidate forbidden clique directly. It checks 64 cases with forbidden clique order 5, 6 or 7. Another routine enumerates integer partitions of each total size through 36, for 3 through 12 parts where permitted, verifying that no two distinct critical partitions share the predicted pair count (74,481 candidate profiles); boundary examples are asserted separately.

These checks do not prove an infinite statement. The analytic proof uses Henson's universal homogeneous extension theorem, elementary clique counting, and the classical Bang–Zsigmondy primitive-prime-divisor theorem. The exceptional cases of that theorem are addressed explicitly in `RESULT.md`. The theorem establishes uniqueness, not a polynomial-time reconstruction bound.

Independent mathematical audit has not been performed.
