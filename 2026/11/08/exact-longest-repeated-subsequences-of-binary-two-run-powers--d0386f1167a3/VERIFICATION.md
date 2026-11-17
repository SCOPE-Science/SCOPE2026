---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: any mixed binary root U has cyclic zero and one run ceiling costs C0,C1; each of its e copies requires at least eC0 source zero runs and eC1 one runs, so C0,C1<=floor(k/e). Its length is at most floor(k/e)(a+b), attained by root (0^a1^b)^floor(k/e); unary roots yield e floor(ka/e), e floor(kb/e). These exhaust the binary alphabet, giving stated exact global optimum. Direct independent exhaustive root embedding on all small a,b,k/e instances corroborated boundary k<e and unary takeover.

## originality

PASS

PASS best-of-knowledge: algorithmic general periodic subsequence literature and longest-run subsequences do not yield an explicitly published same-invariant all-exponent two-run formula; related all-window patterns permit a freely chosen phase and are not logically identical.

## value

PASS

PASS: exact complete natural subfamily of a hard scattered periodic subsequence problem; explains sharp mixed versus pure-root phase transition with a structural capacity lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
