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

# Reproduction and boundaries

With Python 3, run `python3 verify.py` in the directory containing the standalone verifier. The script uses the standard library only and exact integers and rational fractions, and prints the counts of checks performed.

The checks run are (i) a full comparison of the rational-exchange criterion to unrestricted Pareto improvements on all aggregate integer copy-count vectors for 5,292 parameter/horizon combinations, (ii) 34 explicit horizon families, and (iii) complete enumeration of 109,220 ordered round-by-round allocations in five test profiles across horizons 1–7. Every one-round allocation pattern is also tested against EF1 for the tested positive valuation pairs.

The unrestricted allocation space permits both recurring goods to be assigned to the same agent in a given round. Imposing a one-per-agent constraint on Pareto competitors would change the theorem, and must not be done.

The general claim for arbitrary positive real values and arbitrarily many rounds follows from the exact algebraic proof in RESULT.md. The finite verifier does not by itself prove infinite quantifiers, real-valued ratio cases, unindexed literature priority, or independent validation. No independent audit has been performed.
