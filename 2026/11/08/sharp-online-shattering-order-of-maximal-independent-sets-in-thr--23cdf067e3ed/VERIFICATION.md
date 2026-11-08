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

The mathematical proof of the all-order statement is given in `RESULT.md`; its critical steps are the threshold-graph maximal-independent-set normal form, the one-hot/prefix split classification, the rank recurrence, and the distinct-cut counting argument. None of these unrestricted claims follows solely from finite testing.

Execute `python3 verify_threshold.py` using Python 3. The script uses only the standard library and was executed from its own path. It enumerates all 2,047 creation words with lengths one through eleven and checks: (1) direct maximal-independent-set enumeration from graph edges for words through length eight, (2) a separate definition-based recursion for Littlestone dimension, (3) the interval recurrence, and (4) VC dimension from every finite query support. The first orders attaining ranks one, two, and three are two, five, and eleven, respectively.

Observed final output: `THRESHOLD_ONLINE_PASS 2047 minimum_ranks [(0, 1), (1, 2), (2, 5), (3, 11)]`.

Independent mathematical validation has not been performed. Exhaustive finite checking is not an infinite proof and does not exclude an earlier equivalent result under different terminology.
