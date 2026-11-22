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

The standalone Python 3 checker `verify.py` directly enumerates forbidden-factor-avoiding concepts and every possible coordinate support for each test domain, calculates all Boolean traces, checks the geometric window criterion, and separately computes the face-polynomial coefficient formulas. It covers linear lengths 0 through 10 and circular lengths from \(r+2\) through 10 for each \(1\le r\le4\).

Executed command: `python verify.py`. Outcome: `PASS direct trace tests: 70 cases, 16260 supports; all polynomial coefficients and VC ranks verified`. The reported path/cycle coefficient examples at lengths eight and ten are reproducible. These tests independently check the small instances; the universal theorem is justified by the terminating zero-gap splitting proof, not by finite tests.

The priority comparison used bibliographic and indexed statement searches. Johnson (2021) was inspected in accessible full HTML; the general s-extremal article was read in accessible HTML; the forbidden-substring algorithm paper was inspected through its abstract. The closest indexed two-trigram statement was available as a summary, not a verified full-document comparison. No external independent audit or formal proof assistant check is claimed.
