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

The mathematical statement is sound. On any macroscopic window bounded away from zero, independent Bernoulli products give Poisson arrivals: the first sum converges to c log(b/a) and the squared-probability sum vanishes, which yields the Laplace functional on compact windows. At the left endpoint the sign mixes since its bias is multiplied by ∏(1−2p_k)→0, including deterministic starting sign and arbitrary finite early edits. The left-end sign is independent of future flips. After logarithmic time change this is a stationary fair rate-c flip chain; integrating the finite-jump approximations gives displacement convergence on truncated windows. The discarded interval contributes at most its length plus a grid error, and all interpolations are deterministically 1-Lipschitz, proving C([0,T]) convergence. The stationary filter invariant density is verified by the identity ((1−z²)f_c)'=−2cz f_c and zero endpoint flux; sign coupling and filter contraction give uniqueness even for endpoint-singular c<1. The sign correlation (min/max)^{2c} gives the covariance by explicit integration; at c=1/2 it really gives a logarithm, with the long lag taken after the functional limit. Compact boundedness permits raw moment convergence despite initial sign bias, and the beta moments give Binder 2/(2c+3). Replayed python3 /workspace/audit_checks.py, check 1: exact finite histories with deterministic initial velocity and two deterministic early flips agreed with a separate two-state recursion and centered correlation product. This does not certify the functional limit; the frozen checker was inspected, not executed.

## originality

FAIL

The central functional universality claim is directly covered by Engländer–Volkov–Wang's Theorem 4(3), §6.1 and especially Remark 15. The remark explicitly says that convergence of np_n to c suffices for the same zigzag limit, and covers a broader stable-block class. Their zigzag is the same integrated log-time Poisson sign process. An arbitrary independent initial sign, rather than their initial fairness convention, is removed by a tail mixing argument and does not constitute a distinct scaling theorem. The claimed remaining covariance, trichotomy and Binder curve are direct elementary corollaries of this earlier process and marginal. The covariance need not appear verbatim in the earlier paper for that assessment.

## value

FAIL

The critical process and observables are scientifically useful, but the only candidate additions here are direct integrations of the known zigzag correlation, beta-moment substitution, and removal of an initial-sign convention by mixing. No nonroutine independent remainder is demonstrated, such as a controlled original-walk growing-lag regime, which is expressly excluded. A repaired novelty claim restricted to these corollaries would not meet the value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
