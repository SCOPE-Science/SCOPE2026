---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

FAIL

Conditioning on a fixed h-set being an H-component leaves the complement distributed as G(n−h,p) and rules out straddling copies because F is connected. Summing the conditional-mean differences over component indicators proves the general covariance identity, and the positive expectation factor and unimodality of p^e(1−p)^q give the general induced sign cases. But the P3 specialization in the Finding and Proof drops the complement term. Both conventions need B_n=3[binom(n,3)−binom(n−3,3)]=(9n²−45n+60)/2, not 3 binom(n,3). At n=6, p=1/2, direct exact enumeration yields induced covariance −735/8192, whereas the printed special formula gives −195/2048. The printed non-induced factor likewise has the wrong coefficient for n≥6. The induced root count (two iff n≥4) survives since B_3=3, B_4=12, B_n increases, and max p²(1−p)=4/27. The printed root scales do not survive: the correct scales are p_-∼(sqrt(2)/3)n^−1 and 1−p_+∼(2/9)n^−2, by B_np²(1−p)=1 and B_n∼(9/2)n². The n=4 example is unaffected.

## originality

FAIL

A distinct indexed record states the same general finite covariance factor for the same two counting conventions and the complete same sign classification, including the induced nonclique two-root case. The surviving P3 specialization is an immediate substitution into that result; its corrected leading scales only use the resulting cubic and the leading term of its coefficient. This is statement-level coverage, not a conclusion about historical priority or copying. The frozen large-n scales do not provide a distinct correct result.

## value

PASS

The covariance phase classification is a meaningful invariant of naturally coupled component and motif statistics. The exact finite-size threshold for a positive/negative/positive pattern distinguishes induced from non-induced counts. That scientific interest does not make the faulty asymptotic example correct, or rescue the proposal as a distinct result once the exact overlap is accounted for.

The dated certificate retains the supplied scientific assessment, sources and limitations.
