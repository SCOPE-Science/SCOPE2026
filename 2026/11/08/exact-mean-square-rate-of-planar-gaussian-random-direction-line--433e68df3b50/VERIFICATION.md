---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Whiten the 2D quadratic and express a single exact line-search update as orthogonal rank-one projector ww^T. Reflection symmetry closes the diagonal covariance moments. Differentiating E[sin²(theta)/(a cos²(theta)+b sin²(theta))]=1/(sqrt(b)(sqrt(a)+sqrt(b))) yields B=1/[2(t+1)²]*[[t+2,t],[t,t(2t+1)]]. Its trace=(t²+t+1)/(t+1)² and determinant=t/[2(t+1)²], and its positive Perron left/right vectors give the same exact asymptotic expected-objective root for every nonzero deterministic initial state. The strict comparison with t/(t+1) follows the stated polynomial identity for t>1. Independently computed t=2 matrix [[2/9,1/9],[1/9,5/9]] and Perron root (7+sqrt(13))/18, confirming key normalization and the distinction from the 2/3 one-step bound.

## originality

PASS

The natural algorithm is already Gaussian random pursuit / one-column randomized subspace Newton. The inspected 2015 Gower–Richtárik full result computes expected projection / first-moment identities and one-step worst-case bounds; RSN 2019 Theorem 2 gives a general expected-error upper bound. Neither supplies the submitted exact fourth-projector-moment 2-state transfer nor its sharp all-start long-run Perron rate. Other published orthogonal-pair studies couple two directions and do not imply the iid result. Best-of-knowledge PASS with explicit possible older random projection-product formulations.

## value

PASS

It resolves a natural sharp asymptotic constant for a common 2D quadratic optimization algorithm and shows strict improvement over the sharp conditional one-step bound, with a 3/2 high-contrast leading-gap factor. Fourth angular moments and invariant covariance eigenstructure are substantive, not mere substitution of first-moment estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
