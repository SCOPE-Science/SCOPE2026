---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility of the height-24 equality classification

With Python 3 and NumPy, run `python3 verify_equality.py 1 24`. The program
uses integer arithmetic on 90 closed intervals from a common refinement.
It discards a tuple only on finding a clipped interval minimum strictly
below 8/17, then computes the exact minimum for each survivor. It asserts
each height's combinatorial count and the expected exact survivors:

```text
height=11 tuples=  19448 survivors=[((1, 2, 3, 4, 5, 7, 9, 11), '8/17')]
height=22 tuples=1184040 survivors=[((2, 4, 6, 8, 10, 14, 18, 22), '8/17')]
cells=90 total=7888725
```

The full output has an empty survivor list at each of the other 22 heights.
One can also run inclusive chunks `1 14`, `15 19`, `20 22`, `23 24`; together
they cover the same vectors. The proof and the replay cover only the equality
classification in the specified box. They do not independently prove any
assertion at unbounded height. The unrestricted optimum value is prior
work of Tan and Zhang, arXiv:2611.10782v1, Theorem 1.1.
