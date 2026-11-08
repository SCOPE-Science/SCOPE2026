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

# Reproducible certificate verification

Keep `CERTIFICATE.txt` and `verify.py` in the same directory. Run `python3 verify.py` using the Python 3 standard library. The supplied verification produced:

```text
CERTIFICATE_VALIDATED classes=108 even=56 odd=52 path=105 edges=104
OMITTED 0001101001,0011110101,0110111111
```

The verifier independently enumerates all 1024 words, takes every cyclic rotation, forms all 108 necklace classes, checks parity class sizes, checks each path element is the least rotation, tests all 104 consecutive graph edges, verifies that all 105 classes are distinct, and checks that only the specified three even classes are omitted. Those tests constitute a complete finite witness check, not a randomized or bounded search. The graph-theoretic upper bound follows from bipartiteness and the verified class census.

The calculation neither proves general even-order sharpness nor establishes historical priority. This is a reproducible self-review; independent mathematical audit is not performed.
