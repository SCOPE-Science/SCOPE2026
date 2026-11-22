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

# Reproducibility and limits

Use Python 3 with its standard library and execute `python3 verify_direct.py` and `python3 verify_run.py` from a directory containing these standalone files. Each prints PASS for its finite tests and terminates with a nonzero exit code on a failed assertion.

`verify_direct.py` enumerates all binary received words of lengths two through eight. For each possible length-two-deletion predecessor it computes subsequence embedding multiplicities using a dynamic program and compares \(\prod_x e(y,x)^{e(y,x)}\) exactly, with no floating-point threshold. It verifies both the two alternating global maxima and every word at the next distinct entropy level.

`verify_run.py` implements the exact run functional as a product of integer powers. It enumerates all binary received words of lengths two through fifteen and verifies the exact second-level product, the alternating level, and all equality cases. Its computations check the algebraic formula over finite lengths and do not establish the infinite quantifier.

The all-length proof is mathematical: run identity (1), strict cost inequality (3), balanced endpoint minimization (4), Jensen comparison (5), and real derivative and Taylor bounds (6)--(7). The nonstandard run identity and cost inequality originate from the cited primary paper; they are not independently reproved here beyond the stated critical comparison steps. The claim does not depend on logs, third-party software downloads, or machine-generated infinity certificates. No independent validation is asserted.
