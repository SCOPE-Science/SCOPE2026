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

The included `verify.py` is a standalone exact-rational reference implementation. To check:

```sh
python3 verify.py
```

Observed result:

```text
PASS: 864 exact parameter/network cases, 96768 exhaustive binary-action profiles; three sharp-boundary cases.
```

The checker constructs \(W\), inverts \(I-cW\) using rational Gauss–Jordan elimination, solves the unique stationary opinion for every action vector, and evaluates each player's optimized unilateral payoff difference. It compares the computed set of all tie-broken fixed points with the derived formula; the three explicit boundary checks distinguish exact ties from strict cooperation.

The exact cases use community sizes \(m=2,3,4\), influence shares \(a\in\{0,1/4,1/2,3/4,4/5,5/6,9/10,1\}\), multiple positive parameter triples, and several admissible public-goods multipliers.

The general theorem is proved analytically by a within-community comparison lemma and two-by-two linear elimination. No finite checker proves all real parameters or unbounded population sizes. This file records a self-review only; independent audit has not been performed.
