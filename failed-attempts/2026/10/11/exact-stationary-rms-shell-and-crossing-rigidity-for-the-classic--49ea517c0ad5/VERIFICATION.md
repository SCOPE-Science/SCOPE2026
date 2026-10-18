---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For xdot=yz, ydot=x-y, zdot=1-xy, arbitrary one-coordinate stationarity tests give E[x-y|y]=0 and E[1-xy|z]=0. Hence E[xy]=E[y^2]=1; expanding (x-y)^2 yields E[x^2]-1=E[ydot^2]. Equality implies the invariant support has x=y, whence tangency and compactness force only (+1,+1,0), (-1,-1,0); otherwise E[y^2]=1 forces positive measure of both |y|<1 and |y|>1, and periodic measures cross at least twice. Independently reconstructed generator algebra and checked it against the exact same-flow previously published proof. No dependence on numerical trajectories.

## originality

FAIL

The previously published 2026-10-4 Resultary RESULT.md for the EXACT same classical Sprott B vector field already proves the state-independent E[y^2]=1, the same equality rigidity, both-sided amplitude crossing, and nonconstant-orbit crossing. Its proof explicitly derives E[(x-y)^2]=E[x^2]-1 (the current activity defect) and additionally proves E[y^2 z]=-E[(x-y)^2]<0, forcing z<0. The current conditional E[x|y]=y, E[xy|z]=1 are routine generator-test reformulations that do not constitute a separately motivated new theorem after the stronger original. Thus the whole submitted final finding is scientifically covered; it cannot pass O through relabeling the conditionals.

## value

FAIL

With the exact RMS=1, defect formula, equality case and both-side crossing already in the earlier same-object theorem, the current package is a redundant restatement. The additional unweighted conditional expressions are routine antiderivative identities with no separate demonstrated use that would warrant independent publication. This rejection does not contradict the source calculations, which are correct.

The dated certificate retains the supplied scientific assessment, sources and limitations.
