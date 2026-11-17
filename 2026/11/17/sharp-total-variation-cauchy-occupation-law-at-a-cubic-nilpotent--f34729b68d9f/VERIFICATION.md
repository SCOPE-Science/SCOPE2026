---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

The analytic proof in `RESULT.md` is the basis of all infinite-parameter and asymptotic statements. The exact conserved-energy derivative follows from \(V'(x)=x^3/P(x)\), and the change of variables \(dv=V'(x)\,dx\) separately on the two monotone branches produces the shell weight \(W(v)\). The critical algebraic cancellation is explicitly integrated: the Abel transform of the leading tail \(c v^{-3/2}\mathbf1_{v\ge1}\) equals \(2c\sqrt{1-E^{-1}}\), whereas its full integral is \(2c\). Bounds on the remainder yield \(O(\log E/E)\). An exact density-normalization comparison then relates the total-variation discrepancy to the Cauchy tail beyond the energy turning points.

Run `python CHECK.py` from a directory containing this file and `CHECK.py`, using Python 3 and the standard library. The program checks the rational identity for the example \(P(x)=1+x+x^2\), computes energy turning points with bisection, smooths the square-root singularities by an angular substitution, and reports the rescaled outer Cauchy mass and the period-integral residual at energies 100, 500 and 3000. The completed run printed:

```
E=100, sqrt(E) * Cauchy outside mass=0.3909077177, J-C=-0.0070916673
E=500, sqrt(E) * Cauchy outside mass=0.3901329133, J-C=-0.0013258438
E=3000, sqrt(E) * Cauchy outside mass=0.3899020845, J-C=-0.0002158943
NILPOTENT_CAUCHY_TV_DIAGNOSTICS_OK
```

The predicted exact limiting value at those parameters is \(\sqrt3/(\sqrt2\pi)\approx0.3898484006\). Computed samples cannot certify an infinite limit or an all-parameter claim; those follow solely from the displayed derivation. Floating-point quadrature does not constitute an interval enclosure. No independent mathematical audit has been performed.
