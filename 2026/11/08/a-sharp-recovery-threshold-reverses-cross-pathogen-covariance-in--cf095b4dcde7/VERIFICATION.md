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

# Verification of the exact covariance identity

The algebraic derivation is in `RESULT.md` under *Proof*. The standalone `verify.py` uses the standard library's `fractions.Fraction`, enumerates all independent first-round events for the source and three other vertices, applies the actual synchronous second-round per-pathogen survival/acquisition probability, and checks the two marginal probabilities and joint probability against the claimed expressions. The tested hypergraph has distinct triangles \(\{0,1,2\}\) and \(\{0,1,3\}\); it has a positive activated-overlap term when all three external vertices carry the pathogen.

Run from the extracted package directory:

```sh
python3 verify.py
```

Actual verification output:

```
overlapping-triangle exact case: 319/512 25215/32768 -639847670625/70368744177664
PASS: 97 exact rational full-transition tests
```

The script covers combinations of four survival probabilities, two pairwise transmission survival probabilities, two higher-order transmission survival probabilities, two overlap-transmission survival probabilities and three positive integer secondary susceptibility multipliers, plus the named baseline. Exact rational arithmetic avoids float tolerance issues. Mathematical quantifiers over all hypergraphs and real parameters are proved, not tested exhaustively. The time-two and synchronized-event assumptions cannot be dropped from the theorem. Independent audit was not performed.
