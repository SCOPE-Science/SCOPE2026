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

# Verification

From the directory containing `verify.py`, execute:

```sh
python3 verify.py
```

Observed output:

```text
PASS: 15810 parameter-length comparisons; two operator implementations agree.
```

One implementation deletes the first `1` and appends it to the end. The other implements the independent zero-gap transformation. The checker builds complete cyclic factor sets and compares their image sets and their cardinalities, not merely sample strings. It covers the one-step formula for each \(1\le a,b\le12\) and every \(1\le n\le4(a+b)+3\), and the singleton-one-run all-iteration formula for each \(1\le a\le12\), \(1\le k\le10\), and every \(1\le n\le(k+3)(a+1)+2\).

The infinite results rely on the zero-gap collision classification and the cyclic phase proof in `RESULT.md`. In particular, the statement that a length has no further collisions is proved symbolically, not inferred from an absence of counterexamples in a finite loop. Boundary values \(n=1\), \(n=a+1\), \(n=a+b\), exact period multiples, and the least stable length \((k+1)(a+1)-1\) are included. A different all-iterate formula for non-singleton 1-runs is not asserted. This verification is not an independent external mathematical audit.
