---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Reconstructed the spectral branch: the killed Dirichlet resolvent applied to 1 is a strictly decreasing positive Laplace transform at the reset site, with a positive first-mode pole at s=-r and limit zero at +infinity. The resulting eigenvalue is the spectral bound (the complex transform is bounded by its real-part transform). At r<1 the chord bound for sine and the endpoint integral yield F≥r(1-r)(1/2-bδ); r=1 is directly subcritical. For r>1, the two elementary upper bounds on the hyperbolic log ratio cover 0<k≤10 and 10≤k≤3/δ; the derivative bound is strictly positive thereafter, and H tends to +infinity. With y=kδ/2, the omitted hyperbolic logarithms are exponentially small and log(1+k²)=2 log k+o(1); y-log y=L+log 2+o(1) first gives y/L→1 and then the stated additive error. Independent 80-digit bisection of the tail equation gave y=6.472776535862423 at δ=.02 and y=62.39119872476099 at δ=10^-25, with corresponding excesses after subtracting L+log L+log 2 of .5035517169858867 and .08051594923374374. These are finite corroborations, not a proof; replay by bisecting 2y−log(1+(2y/δ)²)+log(1+exp(−4yb/δ))−log(1+exp(−4y(b−δ)/δ)) on [1.5,200]. Only linear mean-population growth is established. The repair clarifies prior coverage without altering any mathematical hypothesis or result.

## originality

PASS

The distinct supported claim is the explicit near-edge singular expansion with additive log L and log 2, not discovery of the crossover or its exact equation. The repaired comparison credits the prior broader qualitative crossover; the quantified analytic uniqueness argument anchors the identification of the asymptotic root.

## value

PASS

The previously plotted threshold becomes singular at the absorbing edge. An explicit additive-accuracy estimate of its scaled root quantifies that divergence, while leading-order scaling alone leaves an unbounded log L error. Identifying the relevant branch, including the actual sign of mean growth, makes the rate law usable without confusing it with a survival probability. The proof cutoff .02 is not claimed optimal or valuable on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
