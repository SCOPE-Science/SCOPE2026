# A sharp Gaussian-to-factorial predator-extinction crossover at the Ricker prey threshold

## Finding

In the normalized Ricker predator–prey map
\[
 x_{n+1}=R x_n e^{-x_n}-x_n y_n,\qquad
 y_{n+1}=\alpha x_n y_n,
\]
where \(R=e r\in(0,1]\) and \(\alpha>0\), the neutral prey-extinction boundary separates two *different clocks for predator clearance*. This is a theorem about trajectories that stay strictly positive, because the map's whole positive quadrant is not forward invariant.

**Subcritical case.** For every such orbit with \(0<R<1\), there are \(C,D>0\), depending on its initial condition, for which
\[
 x_n=C R^n(1+o(1)),\qquad
 y_n=D(\alpha C)^n R^{n(n-1)/2}(1+o(1)).
\]
In particular,
\[
 \lim_{n\to\infty}\frac{-\log y_n}{n^2}=-\frac12\log R>0.
\]

**Critical case.** For every such orbit with \(R=1\), a finite number \(H\in\mathbb R\) and a positive constant \(D\) exist such that
\[
 \frac1{x_n}=n+\frac12\log n+H+O\!\left(\frac{\log n}{n}\right),
\]
and
\[
 y_n=\frac{D\alpha^n}{\Gamma(n)}\,n^{-H}
       \exp\!\left[-\frac14(\log n)^2\right](1+o(1)).
\]
Consequently,
\[
 \lim_{n\to\infty}\frac{-\log y_n}{n\log n}=1.
\]
The universal stretched-lognormal factor \(\exp[-(\log n)^2/4]\), not just the factorial exponent, is a necessary part of the exact critical asymptotic.

## Assumptions and scope

The parameters are \(0<R\le1\), \(\alpha>0\), with \(x_0>0\), \(y_0>0\); the orbit is assumed to satisfy \(x_n,y_n>0\) for every integer \(n\ge0\). This hypothesis is substantive: the prey update can be negative when \(y_n\ge R e^{-x_n}\). The open set
\[
 0<x_0<\min\{1,1/\alpha\},\qquad 0<y_0<R e^{-x_0}
\]
ensures positivity for all iterations. Indeed, in this set both coordinates decrease strictly, whereas the threshold \(R e^{-x_n}\) increases. More general positive orbits are covered without assuming they begin in this set.

The constants have exact definitions. In the subcritical case,
\[
 C=\lim_{n\to\infty}x_n R^{-n}>0,\qquad
 D=\lim_{n\to\infty}\frac{y_n}{(\alpha C)^nR^{n(n-1)/2}}>0.
\]
In the critical case,
\[
 H=\lim_{n\to\infty}\left(x_n^{-1}-n-\tfrac12\log n\right),
\]
and
\[
 D=\lim_{n\to\infty}\frac{y_n\Gamma(n)}{\alpha^n}
    n^H\exp\!\left[\tfrac14(\log n)^2\right]>0.
\]
The limits are proved below; these formulas use ordinary natural logarithms and \(\Gamma(n)=(n-1)!\).

## Proof

**1. Global extinction on positive orbits.** Since
\(0<x_{n+1}<R x_n e^{-x_n}\le x_n\), the prey sequence decreases. Its limit must be zero: a positive limit \(\ell\) would force the one-step ratio to be bounded above by \(e^{-\ell}<1\). The predator ratio is \(y_{n+1}/y_n=\alpha x_n\to0\), so \(y_n\to0\) faster than every fixed geometric rate.

**2. Strictly subcritical clock.** For \(R<1\),
\[
 x_n\le x_0R^n,\qquad
 0<y_n\le y_0(\alpha x_0)^nR^{n(n-1)/2}.
\]
Write
\[
 \frac{x_{n+1}}{Rx_n}=e^{-x_n}\left(1-\frac{y_n e^{x_n}}R\right).
\]
The parenthesis is positive by the orbit hypothesis. The sums \(\sum_n x_n\) and \(\sum_n y_n\) converge, so the product of these ratios converges to a strictly positive limit. Therefore \(C=\lim x_nR^{-n}\) exists and belongs to \((0,\infty)\). The tails of those sums are \(O(R^n)\), giving \(x_n/(CR^n)=1+O(R^n)\). Iterating the predator equation yields
\[
 y_n=y_0\alpha^n\prod_{k=0}^{n-1}x_k
 =y_0(\alpha C)^nR^{n(n-1)/2}
  \prod_{k=0}^{n-1}\frac{x_k}{CR^k}.
\]
The last infinite product converges to a strictly positive number, proving the claimed \(D\) and exact Gaussian-in-generation law.

**3. Negligibility of predation at the critical parabolic scale.** Let \(R=1\). As \(x_n,y_n\to0\), for sufficiently large \(n\), the multiplier \(e^{-x_n}-y_n\) is at least \(1/2\). Thus \(x_n\ge c2^{-n}\) for a fixed \(c>0\). For each \(q\in(0,1)\), eventually \(\alpha x_n<q\), so \(y_n=O(q^n)\). Choosing \(q<2^{-m}\) proves \(y_n/x_n^m\to0\) exponentially for every fixed integer \(m\ge1\). In particular, \(x_n^{-1}y_n=O(\rho^n)\) for some \(\rho<1\).

**4. Universal prey shift.** Set \(u_n=1/x_n\). The exact identity
\[
 u_{n+1}=\frac{u_n e^{1/u_n}}{1-y_n e^{1/u_n}}
\]
and Step 3 give
\[
 u_{n+1}-u_n=1+\frac1{2u_n}+O(u_n^{-2})+O(\rho^n).
\]
Since \(u_n\to\infty\), the increments approach one; hence \(u_n/n\to1\), and summation first yields \(u_n=n+O(\log n)\). Put
\(h_n=u_n-n-\frac12\log n\). Then
\[
 h_{n+1}-h_n=O\!\left(\frac{\log n}{n^2}\right)+O(\rho^n).
\]
The increments are absolutely summable; \(h_n\to H\in\mathbb R\), and its tail is \(O((\log n)/n)\), as asserted.

**5. Full critical predator prefactor.** For \(n\ge1\), define
\[
 V_n=\log\!\left(\frac{y_n\Gamma(n)}{\alpha^n}\right)
    +\frac14(\log n)^2+H\log n.
\]
The multiplicative predator recurrence and \(\Gamma(n+1)=n\Gamma(n)\) show
\[
 V_{n+1}-V_n=\log(nx_n)
 +\frac14[\log^2(n+1)-\log^2n]+H\log(1+1/n).
\]
By Step 4,
\[
 \log(nx_n)=-\frac{\frac12\log n+H}{n}
   +O\!\left(\frac{(\log n)^2}{n^2}\right).
\]
Expanding the two remaining differences cancels both the \((\log n)/n\) and \(H/n\) terms; hence \(V_{n+1}-V_n=O((\log n)^2/n^2)\). This is absolutely summable. Thus \(V_n\to\log D\) for some \(D\in(0,\infty)\), proving the full asymptotic. Stirling's formula then implies the stated \(n\log n\) limit.

## Verification

The self-contained Python 3 file `check.py` reproduces a high-precision subcritical case and verifies numerical convergence of the critical \(H\) and \(\log D\) normalizations at four cutoffs. Its observed subcritical constants for \(R=0.7\), \(\alpha=1.5\), \((x_0,y_0)=(0.2,0.07)\) are \(C\approx0.103474455821465\) and \(D\approx0.344805387716297\); for the critical case with \((x_0,y_0)=(0.2,0.08)\), \(H\approx5.1133764\). The checker verifies only finite diagnostics; the proof above, not the computations, establishes the infinite conclusions. The open positivity set is verified by the elementary monotonicity argument.

## Relationship to prior work

Hamada, El-Azab and El-Metwally (2022) introduced the normalized map, proved local nonhyperbolicity at \(r=e^{-1}\), and established global extinction for \(r<e^{-1}\). Those facts are prior work, not new claims. Their Proposition 3 does not cover equality and does not state the two-term critical reciprocal-prey law or the factorial, stretched-lognormal predator prefactor. Other published asymptotic investigations of predator–prey maps concern different models or strictly hyperbolic extinction; no implied statement covering the critical prefactor was identified among the inspected sources. Publication priority beyond these comparisons is not independently certified.

## Limitations

The positive quadrant is not invariant for arbitrary initial conditions; this theorem is explicitly restricted to forward-positive orbits and provides a concrete nonempty open sufficient subset. No above-threshold attractor classification is asserted. The constants \(C,D,H\) are trajectory dependent, while the Gaussian and log-squared coefficients are universal. The asymptotics apply to the exact deterministic map and do not imply a stochastic extinction-time law. No independent mathematical audit has been performed.

## References

1. M. Y. Hamada, T. El-Azab, H. El-Metwally, *Bifurcations and dynamics of a discrete predator–prey model of ricker type*, Journal of Applied Mathematics and Computing 69 (2023), 113–135, first public online 27 April 2022, DOI: [10.1007/s12190-022-01737-8](https://doi.org/10.1007/s12190-022-01737-8).
2. Published open-access full text: [Springer Nature](https://link.springer.com/article/10.1007/s12190-022-01737-8). The model and relevant Proposition 2–3 appear in Sections 2–3.
