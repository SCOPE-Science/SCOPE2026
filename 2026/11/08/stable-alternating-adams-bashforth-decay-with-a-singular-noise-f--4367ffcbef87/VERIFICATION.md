---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Standard interpolatory variable-step AB2 on scalar decay has transfer T(h,p)=[[1−h−h²/(2p),h²/(2p)],[1,0]]. For H=T(a,b), L=T(b,a), M=LH, tr M=1−(a+b)+(a+b)²/2+ab/4 and det M=ab/4. Jury factorizations prove strict stability iff 0<a+b<2 (boundary a+b=2 is marginal). With independent fixed-variance additive scalar noise each step, long-phase covariance solves P=MPM^T+σ²[(Le1)(Le1)^T+e1e1^T]. As a↓0 at fixed b∈(0,2), M→[[c,0],[1,0]] with c=1−b+b²/2∈[1/2,1), and aLe1→(−b²/2,0). Continuity of the stable discrete Lyapunov inverse gives lim a²V_long=σ²b⁴/[4(1−c²)], positive and finite. Independently reconstructed SymPy transfer/Jury identities and exact b=1,a=1/10 variance 42631561/1200771, with scaled coefficient σ²/3; the universal result follows from the uniform local-in-a stability and limiting covariance proof.

## originality

PASS

The deterministic ratio-free stability boundary and unbounded phase-specific transient are decisively covered in complete earlier October 12 and November 2 AB2 results, and are not credited. Their theorems have no stochastic update forcing or stationary two-periodic Lyapunov covariance. The new positive exact a^(-2) noise-variance coefficient is not implied by a large deterministic operator norm alone. Early Nordsieck variable-step papers might contain similar analyses but available abstracts do not decide that; the authorized full-text attempt failed (VPN disconnected). Best-of-knowledge O is qualified rather than automatically rejected.

## value

PASS

A precise example where every fixed unequal-step deterministic recursion is strictly asymptotically stable while per-update perturbations have unbounded stationary variance is a useful distinction between Floquet stability and stochastic robustness. The sharp b-dependent coefficient, phase specification and additive-noise model make the mathematical limitation reproducible and informative, not merely an old stability rephrasing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
