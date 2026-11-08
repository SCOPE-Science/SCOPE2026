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

Use Python 3.9 or newer, standard library only: `python3 verify.py`. The deterministic program prints three PASS lines. It implements inverse Prüfer sequences, exact breadth-first-search tree distances, integer coefficient comparison, and an independently constructed subset-state CTMC Laplace recurrence. It uses no network requests, random tests or unlisted dependencies.

The exhaustive finite domain consists of one tree at order one and \(n^{n-2}\) labeled trees at each order \(2\le n\le6\): counts \(1,1,3,16,125,1296\). On every such labeled tree, the program verifies that every nonmedian is strictly coefficientwise dominated by some distance median. This is an exhaustive finite certificate because each labeled tree is represented by exactly one Prüfer sequence. Its conclusion is not extrapolated to higher orders.

For the explicit seven-vertex tree, the program checks integer distance sums, all distance-tail polynomial coefficients, and the exact polynomial relation \(P_0(t)-P_1(t)=t(t^2+3t-6)/6\). Its analytic sign establishes the complete positive-deadline phase diagram. A separately derived continuous-time SI subset-state recurrence tests exactly 21 rational Laplace identities (three positive rates and seven sentinels). Those 21 checks corroborate the setup, but are not a substitute for the analytic all-real-time proof.

The claims exclude recovery, heterogeneous rates, cyclic networks, multiple sentinels and imperfect monitoring. The source and historical-priority comparison has not been independently audited.
