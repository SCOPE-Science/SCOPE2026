# Variance-gamma median thresholds and Wishart small-correlation corollaries — provenance-corrected presentation

## Status and provenance

The five-regime large-scale variance-gamma median asymptotics below are correct, but they were already established in the earlier SCOPE record
`2026/09/18/variance-gamma-median-large-noise-phase-transitions--2d5865f4207e`,
first committed at 2026-09-18T17:10:12Z.

This record was first committed later, at 2026-09-19T04:05:38Z. It is therefore not a separate discovery of the \(r=1\) and \(r=3\) thresholds or their constants. It is retained as an alternate Bessel-density derivation and for its explicit Wishart small-correlation specialization.

## The variance-gamma asymptotics

Let
\[
V_{r,\theta,\sigma}\sim\mathrm{VG}(r,\theta,\sigma,0),
\qquad r>0,\quad\theta>0,\quad\sigma>0.
\]
As \(\sigma/\theta\to\infty\):

For \(0<r<1\),
\[
\operatorname{Med}(V_{r,\theta,\sigma})
\sim
\left[
r\,2^r\frac{\Gamma((r+1)/2)}{\Gamma((1-r)/2)}
\right]^{1/r}
\theta^{1/r}\sigma^{-(1-r)/r}.
\]

For \(r=1\),
\[
\operatorname{Med}(V_{1,\theta,\sigma})
=
\frac{\theta}{
\log(\sigma/\theta)+\log(2\log(\sigma/\theta))+1-\gamma+o(1)}.
\]

For \(1<r<3\),
\[
\operatorname{Med}(V_{r,\theta,\sigma})
=
(r-1)\theta+
\frac{
2((r-1)/2)^{r-1}\Gamma((3-r)/2)
}{
r\,\Gamma((r-1)/2)
}
\theta^r\sigma^{-(r-1)}
+o(\theta^r\sigma^{-(r-1)}).
\]

For \(r=3\),
\[
\operatorname{Med}(V_{3,\theta,\sigma})
=
2\theta+
\frac43\frac{\theta^3}{\sigma^2}\log(\sigma/\theta)
+o\!\left(\frac{\theta^3}{\sigma^2}\log(\sigma/\theta)\right).
\]

For \(r>3\),
\[
\operatorname{Med}(V_{r,\theta,\sigma})
=
(r-1)\theta+
\frac{2(r-1)}{3(r-3)}
\frac{\theta^3}{\sigma^2}
+o(\theta^3/\sigma^2).
\]

These are algebraically identical to the formulas in the earlier SCOPE record.

## Alternate derivation

Set \(\theta=1\), \(\kappa=\sigma^2\), and \(s=r/2\). The gamma-difference representation gives an exact symmetric-beta expression for \(F_\kappa(0)\), whose expansion is
\[
\frac12-F_\kappa(0)
=
\frac{\Gamma((r+1)/2)}{\sqrt\pi\,\Gamma(r/2)}
\kappa^{-1/2}
\left(1-\frac{r+1}{6\kappa}+O(\kappa^{-2})\right).
\]
The positive-side density is a Bessel-\(K\) density. Its small-argument expansion changes form at
\[
\nu=\frac{r-1}{2}=0
\quad\text{and}\quad
\nu=1,
\]
which are exactly \(r=1\) and \(r=3\). Matching the positive mass needed to move the CDF from \(F_\kappa(0)\) to \(1/2\) yields the five regimes above. At \(r=2\), the coefficient reduces to \(1/2\), agreeing with the exact asymmetric-Laplace median expansion.

This is an alternate derivation/reproducibility route, not a new theorem relative to the earlier SCOPE result.

## Wishart small-correlation corollary

If \(X\sim W_p(V,n)\), write
\[
V_{ii}=\sigma_i^2,\qquad V_{jj}=\sigma_j^2,\qquad
V_{ij}=\rho\sigma_i\sigma_j,\qquad S=\sigma_i\sigma_j,
\]
with \(\rho>0\). The off-diagonal marginal is
\[
X_{ij}\sim\mathrm{VG}\!\left(n,\rho S,S\sqrt{1-\rho^2},0\right).
\]
Therefore, as \(\rho\downarrow0\),
\[
\operatorname{Med}(X_{ij})
=
\frac{S\rho}{
\log(1/\rho)+\log(2\log(1/\rho))+1-\gamma+o(1)}
\qquad(n=1),
\]
\[
\operatorname{Med}(X_{ij})
=
S\left(\rho+\frac12\rho^2+o(\rho^2)\right)
\qquad(n=2),
\]
\[
\operatorname{Med}(X_{ij})
=
S\left(2\rho+\frac43\rho^3\log(1/\rho)
+o(\rho^3\log(1/\rho))\right)
\qquad(n=3),
\]
and for fixed integer \(n>3\),
\[
\operatorname{Med}(X_{ij})
=
S\left((n-1)\rho+
\frac{2(n-1)}{3(n-3)}\rho^3+o(\rho^3)\right).
\]
These follow directly by substituting
\(\theta=\rho S\) and \(\sigma=S\sqrt{1-\rho^2}\) into the earlier five-regime theorem.

## Scientific value

The main asymptotic theorem is retained for reproducibility rather than priority. The useful additional presentation here is the direct statistical interpretation of the two critical shapes in Wishart off-diagonal medians.

## Literature note and limitations

Gaunt--Ouimet prove monotonicity, bounds, and the limiting median but do not state these rates in their public arXiv description. The older generalized-Laplace monograph by Kotz--Kozubowski--Podgórski was not available as lawful open full text during this audit; an authorized institutional retrieval was queued and later timed out, so no claim is made to have read it in full. That issue no longer controls the provenance conclusion because the earlier SCOPE record is already decisive.

The asymptotics are pointwise for fixed \(r\) and fixed positive \(\theta\); they are not uniform through \(r=1\) or \(r=3\), and no finite-scale remainder bound is supplied.

## References

1. R. E. Gaunt and F. Ouimet, *Bounds for the median of the generalized hyperbolic and related distributions*, arXiv:2609.20212 (2026).
2. A. Fischer, R. E. Gaunt, A. Sarantsev, *The Variance-Gamma Distribution: A Review*, Statistical Science 40 (2025).
3. SCOPE record `2026/09/18/variance-gamma-median-large-noise-phase-transitions--2d5865f4207e`, first committed 2026-09-18T17:10:12Z.
