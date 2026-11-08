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

The proof in `RESULT.md` uses a marked-block EPPF cancellation, exact expectations from the Chinese restaurant recurrence, and gamma-ratio asymptotics. None of its infinitely many parameter instances is inferred from finite experiments alone.

Run the standalone Python standard-library checker by executing `python3 check.py` in the extracted artifact directory. It independently enumerates complete exchangeable partitions via Chinese restaurant transitions for five rational parameter pairs, checks all per-size means and mixed covariances for \(2\le n\le8\), tests the strict sign ordering, and compares four large-sample sign cutoffs with their analytic limits. The observed checker output was `PASS: 706 independent exact/analytic assertions; n up to 8, 5 parameter sets; asymptotic cutoff tests`.

No external software dependency or other artifact is necessary to replay the checks. The checker does not establish literature priority, verify inaccessible manuscripts, or constitute independent mathematical audit. Self-review only; independent audit not performed.
