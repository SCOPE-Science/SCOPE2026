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

Reproduction: execute `python3 verify.py` with a standard Python 3 interpreter. The file builds finite prefixes large enough to contain the complete factor language for each tested length; this cutoff is justified by adjacent power gaps and the occurrence of all zero/single-marker factors. It enumerates all factor words, forms their full cyclic-rotation orbits, tests orbit inclusion, and counts distinct Hamming weights.

Observed output:

```
VERIFY_OK base_length_pairs=1600 bases=2..11 lengths=1..160
```

The check is finite, does not cover all integer bases or lengths, and is not an independent or formal proof. The theorem for all \(B\ge2\) and all \(n\ge1\) follows from the explicit combinatorial argument in `RESULT.md`.
