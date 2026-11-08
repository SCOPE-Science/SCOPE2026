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

# Verification of the trophic-coherence optimization

`verify.py` uses only the Python standard library, specifically exact rational arithmetic (`fractions.Fraction`). Run `python3 verify.py` in the directory containing it. For each graph with \(n=4,5,\dots,32\), it constructs the original chain and apex feeding edge, enumerates all missing forward edges, evaluates every trophic level from the actual prey average, computes \(q^2\) by summing edge deviations, and tests the exact optimum set and closed formulas.

On the inspected package the execution returned:

```text
PASS: 4930 admissible link configurations over n=4..32
PASS: 29 sizes with complete optimum-and-improvement checks
PASS: 278 winning links checked without the formula
n=4 baseline: 1/2
n=4 chosen: 13/40
n=9 optimum: 157/80
```

The algebraic proof for arbitrary \(n\) is in `RESULT.md`, not delegated to code. This verifier does not establish empirical stability, cover arbitrary food webs, or assert that every prior publication was inspected.
