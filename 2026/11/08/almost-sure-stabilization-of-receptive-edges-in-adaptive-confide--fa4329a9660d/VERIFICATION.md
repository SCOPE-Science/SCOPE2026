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

# Verification and scope of the evidence

The proof is exact and does not depend on a numerical experiment. Its nonstandard sampling obligation is explicitly discharged by conditioning on the filtration immediately **before** each independent uniform edge draw. A possible pitfall is treating infinitely many receptive times as a deterministic subsequence; the argument instead works with predictable selection opportunities and bounds the failure probability after \(k\) opportunities by \((1-1/m)^k\). A union over all deterministic times handles an arbitrary finite last receptive selection.

The confidence jump inequality is \(c_e(t+1)\ge\gamma\) whenever the pair is selected while receptive, and it is incompatible with an eventual confidence limit \(0\). When the confidence tends to \(1\), the previously established zero–one confidence and opinion-limit theorems imply the endpoints' opinion limits coincide, and their distance becomes strictly less than confidence. The finite graph makes the simultaneous maximum of the per-edge stabilization times finite almost surely.

A standalone script \(\texttt{verify.py}\) checks the exact rational sampling upper bound for prescribed finite predictable opportunity rules, the upward-jump inequality, and finite synchronous replays of the two-node recurrence. These checks are finite diagnostics only; the infinite-time theorem follows from the written proof and the cited convergence results.

No independent external audit or independent validation has been performed. No numerical experiment can establish that the random stabilization time is almost surely finite; this is a theoretical conclusion.
