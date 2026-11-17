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

# Verification and limitations

The infinite-dimensional correctness argument is written in `RESULT.md`, including the only new nonstandard lemma: the endpoint positive radial rescaling in the equality case. It needs only the triangle inequality, a Hahn–Banach norming functional, continuity and two published median-location results. No formal proof assistant or independently certified proof is claimed.

The supplemental exact-rational checker was run with `python CHECK.py` and reported:

```text
PASS {'strict': 6300, 'saturated': 36} total 6336 and exact exceptional witness t=1/12
```

The checker exhaustively covers only the stated bounded integer grid in three explicit two-dimensional polygonal norms. This is not an exhaustive classification of all norms, triangles or infinite-dimensional spaces. The main theorem follows from the human-readable analytical proof and cited established theorems, not this finite enumeration. Originality is based on inspected statements and proof sections of published sources and actual semantic literature comparisons; absence of a search match is not proof of mathematical novelty.
