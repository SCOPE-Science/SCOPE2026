---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For L=f″−U′f′, let q=Aαx^(α−1) and H=cx^b with H′=1/q. Choosing the immaterial additive constant log(Aα) gives e^U=q e^H. At 0 both scale and speed are locally integrable for 0<α<2, and scale diverges at infinity. Taking the upper boundary to infinity in the killed interval Green kernel gives the positive occupation integrals of the record; the divergent scale excludes escape to infinity before hitting 0. Since ∫_x^∞e^(−U)=e^(−H(x)), the mean derivative is q and the mean is Ax^α, with almost-sure absorption. The second-moment integral is finite for every finite x (stretched exponential at infinity and integrable scale at 0). Integrating its inner integral by parts against −d(e^(−H)) cancels the derivative of M_1² and yields V′=2q(x)e^(H(x))∫_x^∞q(z)e^(−H(z))dz. The substitution u=c z^b gives the displayed Gamma formula and V′∼2(Aα)^3x^(3α−3); integrating yields the plateau tail, logarithm and power with the stated signs and constants. In the plateau integral set u=sv in the positive region 0<u<v; the v integral is Γ(2p)(1−s)^(−2p), giving the Beta factor, including the α=1/2 check. Strong Markov gives compatible independent downward passage increments for ordered starting levels. Construct the increasing process on rational levels and extend by right limits (the mean level function is continuous, giving stochastic continuity). Its centered square-integrable martingale has bounded second moment in the subcritical case; convergence in L² and almost surely follows, and the limiting variance is the positive plateau.

## originality

PASS

Credit is confined to the evaluated finite-start variance, sharp α=2/3 large-distance transition and Gamma–Beta plateau, and the resulting centered limit. The prescribed mean/potential, general moment recursions and the use of passage increments are prior techniques. The verified prior statements have different objectives or do not meet the hypotheses needed to imply this result as stated.

## value

PASS

For a natural inverse-design family with the same exact power-law mean mechanism, variance distinguishes three different absolute noise regimes as the initial distance grows. A nondegenerate centered limit despite divergent mean has a concrete stochastic interpretation; the exact plateau and tail separate this claim from a generic moment recursion or an isolated constant-force special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
