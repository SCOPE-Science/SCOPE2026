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

The accompanying `verify.py` runs with the Python 3 standard library only. From the extracted package directory, run:

```bash
python3 verify.py
```

Observed output:

```text
PASS: exact exchangeable-cardinality comparison cases: 446363
PASS: direct finite one-approval core profiles: 6678
PASS: sharp TV-boundary rational tests: 14
NOTE: tail asymptotics require the analytical proof.
```

The first check independently enumerates all committee and proposal combinations, all candidate-permutation orbit classes of ballots, and the strict quota gaps for candidate counts from two through eight. The second directly checks the core definition against the count-threshold characterization for one-approval electorates with up to three seats and six voters. The third evaluates the sharp contamination identity using exact fractions.

These checks establish the finite enumerated identities and rule out several normalization mistakes. They do not by themselves certify the all-size exchangeability lemma, the heterogeneous Chernoff bound, the central limit theorem or the binomial large-deviation limit; those are proved analytically in `RESULT.md` using the specified hypotheses. No external certificate or independent audit was performed.
