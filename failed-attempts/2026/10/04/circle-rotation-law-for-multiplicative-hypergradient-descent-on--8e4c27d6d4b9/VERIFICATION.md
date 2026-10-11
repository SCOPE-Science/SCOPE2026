---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

With \(q_t=\lambda\alpha_t\), the sign of consecutive scalar gradients gives exactly the multiplicative factors \(1+\beta\) for \(q_t<1\) and \(1-\beta\) for \(q_t>1\), matching the primary quadratic analysis after the normalization \(\lambda=2a\). Repeated multiplication enters \([1-\beta,1+\beta]\); there \(|1-q_t|\le\beta\), so \(|x_{t+1}|\le\beta|x_t|\). Put \(A=\log(1+\beta)\), \(C=-\log(1-\beta)\), and reduce \(\log q+C\) modulo \(A+C\); both branches become addition by \(A\). Standard circle-rotation dynamics then gives exact period equal to the denominator of rational \(A/(A+C)\), and dense orbits when it is irrational. The bundled verifier checks band entry, the conjugacy identity, a period-three example, dense-bin behavior, and contraction; these are corroborative of the exact proof.

## originality

FAIL

The 2017 Oxford thesis already derives the same multiplicative rule on one-dimensional quadratics, gives the three learning-rate regimes, proves eventual trapping in the identical \((1-\beta,1+\beta)\)-scaled interval, and notes geometric contraction there. After that published analysis, passing to logarithms turns the two multiplicative branches into a translation modulo \(\log((1+\beta)/(1-\beta))\); rational-periodic versus irrational-dense behavior is the standard circle-rotation classification. The final claim is therefore an implication-level dynamical corollary of the thesis rather than an uncovered scalar-quadratic theorem.

## value

PASS

The rotation viewpoint gives a clean explanation of why the optimization variable can converge while the adaptive learning rate is periodic or dense, and it yields exact phase behavior for every \(\beta\). This is a useful structural interpretation, but it cannot pass acceptance because the underlying theorem is already implication-level covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
