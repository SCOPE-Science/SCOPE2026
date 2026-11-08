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

# Reproducibility checks

Execute the following standard-library programs from the same directory, using Python 3:

```sh
python exact_coefficients.py
python direct_trajectories.py
python replay_checks.py
```

The matching captured outputs are `exact_coefficients.out`, `direct_trajectories.out`, and `replay_checks.out`. `exact_coefficients.py` computes trinomial coefficients, exact activity counts for both equal and unequal path lengths, and the edge-form identity. `direct_trajectories.py` independently enumerates full state spaces and measures periodic root-excitation rates using a functional-graph reduction, without invoking the path-sum formula. `replay_checks.py` compares those independent answers class by class, checks their factor-three relation, and checks zero-activity counts.

The tested parameter tuples include nine instances, with full exhaustive state spaces ranging from \(243\) to \(177147\) labeled configurations per rule, for a total of \(318087\) states across those nine graphs **per update rule**. This is finite verification, not an infinite-family proof. The local central limit asymptotics follow from the proof in `RESULT.md`; the numerical limit checks in the output logs are illustrations only. The existing general circulation theorem is a cited published premise rather than a computation to certify independently.
