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

PASS

The theorem is mathematically correct, with two sign-wording errors in its written proof. In line 23 weak stability requires nondecreasing, not nonincreasing, energy under a flip. In line 27 after the even-n neutral leaf flip it is the hub parallel to the resulting leaf majority that flips downhill, not the antiparallel hub. Independently, H=J(st+(s+t)L) for hub spins s,t and leaf sum L; for opposite hubs the two costs are 2J(1-sL), 2J(1+sL). This gives the weak census, its central-binomial asymptotics, and the excited energy -J. Aligned hubs require every leaf opposite for weak stability; the two resulting states are strict at energy J(1-2n), including n=2. For even n a neutral leaf flip from L=0 gives |L|=2, and the correct parallel hub costs -2J. For odd n>=3, the hub parallel to L at |L|=1 is neutral; after flipping it there is an aligned leaf that can flip for -4J. No nonground state can belong to a closed class: a nonweak state has a downhill exit and an excited weak state has the verified neutral/downhill path. Finite-state time-homogeneous rates positive on those edges imply almost-sure absorption. Submitted checker was inspected, not executed; the result follows by direct algebra and the allowed-move graph.

## originality

FAIL

The census is an exact specialization of an existing fixed-point theorem on complete split graphs. The absorption claim is a specialization of an existing maximum-cut attractor theorem for the same allowed-move graph. The energy values and the at-most-two-flip escape follow directly from the exact cut formula and update inequalities in the latter proof. Arbitrary positive rates preserve the same closed classes. There is no sufficiently distinct remainder to repair.

## value

FAIL

The contrast between exponentially many weak minima and two absorbing states is meaningful, but is already present when the exact complete-split census and attraction results are combined at a=2. The energy translation and one check of the published update thresholds leave no independently valuable new theorem in this record. Fixing the sign error in the proof would not change that conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
