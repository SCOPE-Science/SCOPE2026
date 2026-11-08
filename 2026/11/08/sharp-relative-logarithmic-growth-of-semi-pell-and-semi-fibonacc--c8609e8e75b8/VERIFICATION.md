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

# Verification and reproducibility

`CHECKER.py` (Python 3, standard library only) computes both recurrences for positive indices less than \(2^{18}\). It independently counts the binary partitions with odd multiplicities by occupied-level number for every \(1\le N<130\), and compares the unweighted total with the semi-Fibonacci recurrence and the weighted total with the semi-Pell recurrence. All comparisons pass. It also prints the numerical ratio-exponent trend at \(N=2^m-1\) for \(5\le m\le17\) and checks elementary lower-bound construction inequalities at representative values of \(m\). The actual recorded standard output is `CHECKER_OUTPUT.txt`.

The proof in `RESULT.md` is self-contained: it does not infer an asymptotic limit from these finite tests. Its essential unbounded estimates are (1)–(7), all with quantified ranges and explicit construction. No independent scientific audit or external certification has been performed.
