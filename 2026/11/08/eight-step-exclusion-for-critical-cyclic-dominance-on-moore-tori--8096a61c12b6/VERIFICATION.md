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

# Reproduction and limits

Run `python3 verification/check_period_gap.py` with Python 3 standard library. The program performs 36 exhaustive local configurations, including 9 strictly slack cases, then checks every compatible-signature edge and all four-cliques across nine graphs for periods 3 through 8, finding none. Its separate period-nine probe returns a compatible four-clique: this demonstrates that the certificate does not simply assert global exclusion for all periods.

Expected final line:

```
VERIFY_OK local_cases=36 strict_cases=9 ruled_out_signature_graphs=9
```

All arithmetic is exact integer/Boolean arithmetic. No floating-point approximation, random sampling, external data, or untrusted services enter this finite certificate. The source establishes its logical relevance to periodic trajectories; program output alone would not prove that reduction. The theorem does not establish global fixation or the existence of long periodic orbits. Independent scientific validation has not been performed.
