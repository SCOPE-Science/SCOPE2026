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

# Verification record

The analytical proof is in `RESULT.md`, with the four independently checkable steps: circular overlap, exact necklace equivalence, prime-period ambiguity classification, and the Bernoulli observation information bounds. The converse uses the standard relative-entropy-to-testing-risk inequality whose proof is explicitly supplied.

Execute the standalone checker with `python check.py` using Python 3.10 or later. Its finite exact checks cover 139774 rotational-word parameter triples, 464 full necklace-class parameter pairs, and 1300 rational Bernoulli-channel identities; all passed. The counts are test cases, not exhaustive coverage of all possible periods, and no numerical or finite evidence is substituted for the universal proof.

The research result has received only self-review. No independent scientific audit or third-party verification has been conducted. The literature comparison is bounded and cannot establish worldwide publication priority.
