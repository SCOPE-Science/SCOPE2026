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

## Exact certificates

`CERTIFICATE.json` contains complete deterministic transition tables, representative predecessor masks, start states, Perron-component vertex sets, two integer 99-power witness vectors, and rigorous rational enclosures. `rule22_verify.py` reproduces all data directly from Rule 22's Boolean truth table, checks the canonical minimization, checks all components and Perron-vector inequalities using arbitrary-precision integers, and cross-checks length-one through length-eighteen admissible-word counts.

## Independent finite-word check

`rule22_independent.py` independently applies the exact one-count update rule to every binary predecessor block of length \(n+2t\) for \(1\le n\le12\) and \(t=1,2\). It confirms both word-count sequences and inclusion of the second image in the first. This independent finite calculation is corroboration only; the infinite entropy assertion follows from the deterministic finite automaton and exact Perron bound.

## Reproduction

From a directory containing the three supplied scientific files, run:

```bash
python3 rule22_verify.py CERTIFICATE.json
python3 rule22_independent.py
```

The two commands return `PASS` on the embedded certificate. The exact rational inequalities \(191716/100000<\lambda_1<191718/100000\) and \(186746/100000<\lambda_2<186748/100000\) rely only on integer arithmetic, while the displayed decimal entropy approximations are illustrative.

## Boundaries

No assertion about larger times, a limiting image language, uniqueness in the global literature, or independent mathematical certification is verified here.
