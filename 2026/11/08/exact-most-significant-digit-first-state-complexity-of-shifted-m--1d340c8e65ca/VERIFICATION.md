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

# Reproducibility and finite verification

Use Python 3 (standard library only) and run `python3 checker.py` in the directory containing the seven supplied files. Successful output is:

```
VERIFY_OK
parameter_cases 896
signature_witnesses 12136
direct_arithmetic_checks 107520
independent_automaton_minimizations 896
```

The checker independently computes the explicit finite valuation-signature formula, constructs integer representatives for every state candidate, checks direct valuation outputs, explores reachable prefixes in MSD-first order, and minimizes the resulting complete deterministic output automaton. Its parameter region is \(2\le b,m\le5\) and \(0\le c<56\). It is a finite stress test, not a proof for unbounded parameters.

The proof is in `RESULT.md`: (1) continuation equivalence is exactly equality of the \((K+1)\)-coordinate valuation vector, because every suffix is either nonexceptional or reduces to one of the named offsets; (2) the finite radix trie partitions all prefix values; (3) missing-child residues and marked-leaf power witnesses realize every claimed signature; and (4) all differing signatures are distinguishable by some suffix. The exact formula and the quadratic-logarithmic upper bound follow without infinite enumeration or external certificates.

Limits: no independent mathematical audit has been performed; historical priority is not certified; the formula concerns this particular MSD-first representation with leading-zero padding, and its upper bound is not asserted sharp.
