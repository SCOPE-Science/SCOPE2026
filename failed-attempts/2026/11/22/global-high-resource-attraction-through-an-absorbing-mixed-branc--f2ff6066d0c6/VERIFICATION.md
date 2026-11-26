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

The two unfolded odds are A=r(1+b)/alpha and B=(1+rb)/(alpha*r), where 0<r<1 and 0<b<=1 for the ordered half-domain. A<1; while B<1 the order is preserved and r decreases by a factor at most 2r0/(1+r0)<1, contradicting B<1 once r<1/alpha. At the first B>=1, including equality, (r',b')=(AB,1/B), which lands in [0,4/alpha^2] x [0,1] and strictly preserves the physical ordering. The closed rectangle is an auxiliary continuous extension at zero odds, not an enlargement of the physical initial data. It is invariant and lands in the smaller rectangle with r<=min(5/32,4/alpha^2). In max{2alpha|dr|,|db|} the two Jacobian row bounds there are 55/64 and 3/4; the mean-value inequality and Banach give geometric convergence. Substitution gives the stated fixed point in the trap (r_*<=2/alpha^2<=1/8), with the announced physical coordinates. Swap symmetry handles the other half-domain. Independent bounded replay: python /workspace/review_replay.py 1 passed the symbolic branch and fixed-point checks, norm constants and a tie at alpha=4; the universal assertions use the inequalities above, not sampled trajectories.

## originality

FAIL

The central global basin and permanent mixed-branch theorem is already covered by a distinct published catalogue theorem for every alpha>2. The same-day label is not evidence of which proof came first. The closed lower endpoint is a short entry argument, and the exact one-step weighted-norm estimate is a different certificate rather than a new global selection phenomenon.

## value

FAIL

Global branch absorption is substantive as mathematics, but it is already supplied over a wider parameter range. The remaining edge-of-square start reduces to the broader theorem, and the one-step constant in a different metric, though correct and useful in this proof, is not shown to answer a separate substantive rate, sharpness or robustness question. No genuinely valuable independent remainder was established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
