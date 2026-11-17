---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The two infective path frontiers each expose exactly one active edge at rates λ_A and λ_B until the gap is exhausted. Exponential memorylessness and time changes from peripheral infection events preserve the iid next-capture Bernoulli probability p=λ_A/(λ_A+λ_B). Hence X~Bin(m,p), and A territory Z_A=w_0+Σ_{j≤X}w_j, independent of off-path transition rates. In symmetric case, Var Z_A=m/4+2Σ b_j Cov(X,I_j)+Σ b_i b_j Cov(I_i,I_j). The covariances are positive; strict positive-definiteness of nested tail-indicator covariance implies maximizers concentrate B at one interior vertex, where central binomial and tail probability factors are largest. Minimum m/4 iff extras are seed-attached, maximum at center(s) with supplied formula. Independently exact evaluated m=3,B=4 gives maximum 31/4; m=2,B=2 gives both central maxima 9/4; boundary B=0 gives m/4. Finite CTMC checker was inspected but universal reasoning is analytical.

## originality

PASS

The path-interface memoryless reduction is an elementary underlying mechanism and is not counted as independent novelty. Full exact variance maximization/minimization with all equality cases over every fixed-(n,m) finite tree is a separate shape-optimization statement. Sun–Saad–Lokhov gives exact DMP for discrete-time mutually exclusive processes on trees and finite-horizon resource decisions, not the explicit continuous-time binomial weighted-prefix *variance extremizer*. Related first-passage competition and outbreak-variance studies have distinct observables. Best-of-knowledge O PASS with residual risk from broader, unindexed tree-competition classifications.

## value

PASS

Fixing seed distance and vertex count but allowing arbitrary branching naturally asks which tree geometry maximizes uncertainty in the final competing territory size. The sharp all-shapes central attachment theorem, both equality classes, and side-rate invariance provide a reusable exact benchmark, not an arbitrary tiny graph enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
