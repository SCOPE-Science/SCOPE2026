# A three-clock critical extinction hierarchy in a discrete food chain

## Finding

For the three-species discrete trophic map of Alsedà, Lázaro, Solé, Vidiella and Sardanyés at the critical basal growth parameter \(\mu=1\), every strictly positive forward orbit remaining in the biological simplex has three precisely distinguishable extinction clocks. With \(\beta,\gamma>0\), there are constants \(H\in\mathbb R\) and \(L>0\), depending on the orbit, such that

\[
\frac1{x_n}=n+\log n+H+O\!\left(\frac{\log n}{n}\right),\qquad
 y_n\sim\frac{L\beta^n}{\Gamma(n)n^H}\exp\!\left(-\frac{(\log n)^2}{2}\right).
\]

The top predator has the sharper, universal two-term logarithmic extinction law

\[
\log z_n=-\frac12n^2\log n+\left(\frac34+\frac12\log\beta\right)n^2+O\!\left(n(\log n)^2\right).
\]

In particular, \(x_n\sim1/n\), \(y_n\) is factorially small with a nontrivial squared-logarithm correction, and \(z_n\) has a superfactorial \(n^2\log n\) clock. All three conclusions hold simultaneously on an explicit nonempty open set of strictly positive initial data. The asymptotic top-level second coefficient is independent of the upper-predator conversion rate \(\gamma\).

## Assumptions and scope

Fix any \(\beta>0\) and \(\gamma>0\). Let \((x_n,y_n,z_n)_{n\ge0}\) obey

\[
 x_{n+1}=x_n(1-x_n-y_n-z_n),\quad
 y_{n+1}=\beta y_n(x_n-z_n),\quad
 z_{n+1}=\gamma y_nz_n.
\]

Assume that \(x_n,y_n,z_n>0\) and \(x_n+y_n+z_n\le1\) for *all* integers \(n\ge0\). This is a conditional theorem for strictly positive forward-surviving trajectories; it does not assert that every point in the simplex has a positive orbit. The hypothesis is not vacuous: each initial datum satisfying

\[
0<x_0<1,\quad 0<z_0<x_0/2,\quad y_0>0,\quad
x_0+y_0+z_0<1/2,\quad \beta x_0<1/2,\quad\gamma y_0<1/4
\]

belongs to the required set, as shown below. For \(n\ge1\), \(\Gamma(n)=(n-1)!\). Landau terms hold with constants depending on fixed parameters and the initial state.

## Proof

**1. A forward-invariant positive wedge.** On the displayed open set, suppose inductively that all coordinates are positive, decreasing, \(z_n<x_n/2\), and their sum is less than \(1/2\). Then \(x_{n+1}\in(0,x_n)\), \(0<y_{n+1}\le\beta x_0y_n<y_n/2\), and \(0<z_{n+1}\le\gamma y_0z_n<z_n/4\). Also

\[
 \frac{z_{n+1}}{x_{n+1}}=
 \frac{z_n}{x_n}\frac{\gamma y_n}{1-x_n-y_n-z_n}
 <\frac12\frac{z_n}{x_n}.
\]

The induction closes; positivity persists and the total abundance stays below \(1/2\). Strict initial inequalities give a nonempty open wedge for every positive \(\beta,\gamma\).

**2. Factorial control before asymptotics.** For any strictly positive simplex survivor, \(x_{n+1}\le x_n(1-x_n)\), hence with \(t_n=1/x_n\) we have \(t_{n+1}\ge t_n+1\) and

\[
 x_n\le\frac1{n+t_0},\quad
 y_n\le y_0\frac{\beta^n\Gamma(t_0)}{\Gamma(n+t_0)}.
\]

The latter follows by multiplying \(y_{n+1}\le\beta x_ny_n\). In particular, \(y_n\to0\) faster than every negative power, and since \(z_{n+1}=\gamma y_nz_n\), the sequence \(z_n\) has the same property (indeed, a still stronger one). Writing \(p_n=y_n+z_n\), we have \(\sum_{n\ge0}n^m p_n<\infty\) for every fixed integer \(m\ge0\).

**3. Exact reciprocal increment and its correction.** Algebra gives, with \(t_n=1/x_n\) and \(p_n=y_n+z_n\),

\[
 t_{n+1}-t_n=1+\frac1{t_n}+\epsilon_n,
\quad
\epsilon_n=\frac1{t_n(t_n-1)}+
\frac{t_np_n}{(1-1/t_n-p_n)(1-1/t_n)}.
\]

For sufficiently large \(n\), both denominators are bounded below by a positive constant. Moreover, from the same recurrence, \(t_{n+1}\le(t_n+2)(1+4p_n)\). Since \(\sum p_n<\infty\), a discrete Gronwall product gives \(t_n=O(n)\). Thus \(\epsilon_n=O(n^{-2}+np_n)\), \(\sum_n\epsilon_n<\infty\), and its tail is \(O(1/n)\). Together with \(t_n\ge n+t_0\), this first yields \(t_n=n+O(\log n)\). Hence

\[
 \frac1{t_n}=\frac1n+O\!\left(\frac{\log n}{n^2}\right)
\]

and the error is absolutely summable. Summing the increment and comparing with harmonic numbers now proves existence of a real \(H\) satisfying

\[
 t_n=n+\log n+H+O\!\left(\frac{\log n}{n}\right).
\]

**4. Middle-predator sharp clock.** Positivity of \(y_{n+1}\) implies \(x_n>z_n\), and exactly

\[
 \log y_n=\log y_0+n\log\beta+\sum_{k=0}^{n-1}\log x_k
       +\sum_{k=0}^{n-1}\log(1-z_k/x_k).
\]

Because \(t_n=O(n)\) and \(z_n\) decreases faster than any power, \(\sum_k z_k/x_k<\infty\); all its log factors are defined and their log sum converges to a finite real number (finitely many initial terms do not matter). The reciprocal expansion gives

\[
 \log(kx_k)=-\frac{\log k+H}{k}
      +O\!\left(\frac{(\log k)^2}{k^2}\right).
\]

The error series converges, while \(\sum_{k<n}1/k-\log n\) and \(\sum_{k<n}(\log k)/k-(\log n)^2/2\) both have finite limits. Since \(\sum_{k=1}^{n-1}\log k=\log\Gamma(n)\), there is a finite \(\log L\) such that

\[
 \log y_n=n\log\beta-\log\Gamma(n)
       -H\log n-\frac12(\log n)^2+\log L+o(1).
\]

Exponentiating proves the displayed positive-prefactor asymptotic.

**5. Apex-predator two-term clock.** Iterating its exact recurrence,

\[
\log z_n=\log z_0+n\log\gamma+\sum_{k=0}^{n-1}\log y_k.
\]

Step 4, Stirling's formula, and elementary summation give

\[
\sum_{k=1}^{n-1}\log\Gamma(k)
=\frac12n^2\log n-\frac34n^2+O(n\log n),
\quad \sum_{k=1}^{n-1}k=\frac12n^2+O(n).
\]

The \(-H\log k\) and \(-\tfrac12(\log k)^2\) corrections sum to at most \(O(n(\log n)^2)\), as do the other subleading terms. This yields the asserted apex formula. Neither the coefficient of \(n^2\log n\) nor that of \(n^2\) contains \(\gamma\), completing the proof.

## Verification

The standalone `CHECKER.py` implements the exact recurrence, using log coordinates for the two rapidly vanishing species to avoid numerical underflow. It checks the reciprocal increment identity, positivity, and long-range convergence diagnostics for three positive parameter sets in the explicit invariant wedge. Run it using `python3 CHECKER.py`; its terminal marker is `FINITE_DIAGNOSTICS_PASS`. Its finite tests only diagnose the identities and approach to the asymptotics; the proof above establishes the infinite-time conclusions.

## Relationship to prior work

Alsedà et al., *Dynamics in a time-discrete food-chain model with strong pressure on preys* (2019 preprint, 2020 publication), supply the same three-species map, biological simplex, equilibrium bifurcations, and qualitative regions. Their work identifies the neutral origin at \(\mu=1\) but does not state or derive these simultaneous critical extinction scales or the two-term apex logarithmic clock.

Two-species discrete predator–prey analyses have obtained factorial-logarithmic decay at a neutral prey multiplier, but such statements do not imply the present three-dimensional, extra-predator \(n^2\log n\) law. A separate continuous delayed food-chain result reports algebraic predator and exponential top-predator extinction; it concerns a different system. Standard gamma/Barnes-function asymptotics are used solely as analytic tools, not proposed as new discoveries.

## Limitations

The result is conditional on perpetual positivity inside the simplex; some physically admissible initial points may instead hit an escape or sign-changing regime. The explicit wedge proves the condition is nonvacuous, not that it describes the whole positive-survival basin. The parameters \(\beta,\gamma\) are fixed as \(n\to\infty\). The constants \(H,L\) retain initial-state dependence. The top-predator error term is not optimized. The literature comparison is based on inspected accessible texts and indexed searches, not a guarantee against unindexed equivalent results. No independent mathematical audit has been performed.

## References

1. L. Alsedà, J. T. Lázaro, R. Solé, B. Vidiella and J. Sardanyés, “Dynamics in a time-discrete food-chain model with strong pressure on preys,” first public preprint 2019-09-27, [arXiv:1909.12501](https://arxiv.org/abs/1909.12501); *Communications in Nonlinear Science and Numerical Simulation* **84** (2020), 105187, [doi:10.1016/j.cnsns.2020.105187](https://doi.org/10.1016/j.cnsns.2020.105187).
2. “On Dynamics and Invariant Sets in Predator–Prey Maps,” accessible two-species background, https://www.intechopen.com/chapters/70218.
3. Standard Stirling formula and summation for \(\log\Gamma\); no novel special-function identity is claimed.
