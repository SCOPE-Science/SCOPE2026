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

The proof in `RESULT.md` is self-contained. Its decisive nonstandard step is an exhaustive rational reduction: four possible first-two-prime pairs and twelve possible third-prime prefixes. No claim that a finite brute-force scan exhausts an infinite domain is needed; strict monotonicity supplies the bounds.

Run `python3 verify.py` in the same directory. The program checks all displayed rational inequalities, exhaustively enumerates prime third coordinates inside the **proved** bounds, solves for the forced fourth prime as a rational number, tests primality exactly, and confirms each product identity.

The program uses no external dependencies or data. Successful output is:

```
VERIFY_OK complete_prefix_cases=4 candidate_prime_triples=12 solutions=8
numbers=24871,29029,50065,58435,64285,87685,137885,140335
```

The algorithmic replay is a reproducibility check, not an independent mathematical audit. Limits: the classification excludes prime powers and all other values of the number of distinct prime factors; absence of an earlier published global classification is not mathematically provable from these searches.
