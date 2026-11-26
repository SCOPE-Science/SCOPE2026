---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Contracting the open paths formed by two prescribed images gives a bijection from completions to permutations on n−2 objects, adding only the already forced cycles. Among inverted ordered image pairs the two possible fixed points and the two-cycle contribute (a−1)+(n−b)+1=n−(b−a). Hence E[C_n I_{a,b}]=H_{n−2}/2+(n−(b−a))/(n(n−1)), and subtracting H_n/2 verifies the local covariance, including n=2 with H_0=0. Dividing by P(I=1)=1/2 gives the conditional mean. The weighted sum over distances yields −(2n−1)/12, and finite differentiation of the normalized Mallows weight gives q^{-1} Cov_q(C_n,Inv_n). The beta expansion follows at fixed n by the chain rule with q=e^{−beta}.

## originality

FAIL

A distinct indexed result states the same positional formula and aggregate covariance, and its Mallows derivative is equivalent. The conditional mean and inverse-temperature expansion in the frozen result are immediate consequences, not a surviving distinct result. This is demonstrated catalogue coverage; no external publication-priority claim is needed or made.

## value

PASS

The gap profile is a meaningful finite-n dependence invariant: it distinguishes the effect of nearby and distant positional inversions and its sum gives the susceptibility to the Mallows tilt. This is scientific interest in the identity, not new value added by the frozen duplicate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
