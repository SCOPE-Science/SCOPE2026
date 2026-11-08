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

Run `python3 checker.py` with Python 3 standard library. It explicitly enumerates all subsequences of the host, derives the minimal absent set via all single-symbol deletions, and checks both the closed-form count and the complete run criterion. The recorded replay passed 55 positive parameter triples with \(1\le a,b,r\le4\), total host length at most 20, 693 MAS words and 683,530 candidate comparisons. It also checks recurrence values through \(r=10\) in all three regimes.

Separately, direct greedy subsequence decisions and the analytic block-cost identity agreed for all 64 triples with \(1\le a,b,r\le4\), across binary candidates of length at most 13. This second check was not included as a second executable file, and is not needed for proof reproduction.

The proof in RESULT.md covers all \(a,b,r\ge1\) through a greedy matching lemma, deletion-case classification and formal-series enumeration. Neither finite enumeration nor a run log constitutes an infinite certificate. Independent mathematical audit has not been performed; historical-priority risk remains.
