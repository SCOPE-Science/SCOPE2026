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

# Reproduction

Use Python 3 with only the standard library. In this directory execute:

```
python3 verify_literal.py
python3 verify_shuffle.py
```

The first program independently enumerates all position masks for each length \(0\le n\le18\) and filters by the exact deleted pattern. It checks 190 source/deletion parameter pairs, 1,850 positive residual entries and a total of 17,709 counted positional embeddings against the exact fiber formula and distinct-set count. The second program independently computes literal interleavings using a two-index recursion, and checks 20,427 block-type cases over \(0\le n\le22\), 550 nonempty histogram bins and 500 seeded longer random parameter/word checks through length 100. The outputs are saved as `verify_literal.stdout.txt` and `verify_shuffle.stdout.txt`.

The all-length proof is the phase-gap bijection in `RESULT.md`: every pair of retained symbols is consecutive in the source, all deletions occur in \(\ell+1\) gaps, and every admissible embedding is represented uniquely by a weak composition with prescribed gap parities. Thus finite tests are regression checks, not the scientific basis for unbounded quantifiers. An independent algebraic normalization check compared the sum of all fiber multiplicities to \(\binom{\lfloor(n+d)/2\rfloor}{d}\) for all \(0\le d\le n\le34\); it agreed everywhere. There is no mechanized proof certificate or independent audit.
