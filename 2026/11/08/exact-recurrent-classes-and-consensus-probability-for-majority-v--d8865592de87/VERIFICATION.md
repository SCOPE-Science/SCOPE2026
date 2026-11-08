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

# Verification of the finite-state checks

Run `python3 verify.py` using a standard Python 3 interpreter; the script has no third-party dependencies. It independently enumerates all binary configurations for \(k=1,2,3,4,5\), generating state transitions by executing the three-vertex majority operation rather than using the theorem's class description. Its terminal strongly connected components are checked against the two unanimous states and all monochromatic-pair colorings with both hub opinions. A separate rational first-step system for the group-count process is compared against the theorem's conditional formula for every configuration. Finally, exact rational Bernoulli probabilities at \(q=1/5,1/3,1/2,2/3,4/5\) are summed over all initial states and checked against the closed expression.

The script yields `PASS: 2835 exact certificates, all reachable states through k=5, recurrent classes and iid formula verified`. It never approximates a finite probability. This is not an exhaustive computational proof for unbounded \(k\); the all-size class theorem, exponential-race argument and independent-exponential freezing-time distribution are proved analytically in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
