# Sharp continuum-to-lattice settling-time transition for hypercube farthest-vertex contractions

## Finding

Let \(d\geq3\) and \(0<\lambda<1\). Start the Euclidean farthest-vertex contraction on the cube \(Q_d=[-1,1]^d\), moving a fraction \(1-\lambda\) toward a farthest corner on each step. On the null sets where one coordinate vanishes, resolve the tied corner sign by choosing \(-1\) in that coordinate. Write \(\delta=-\log\lambda\).

There are precisely \(2^{d-1}\) attracting primitive two-cycles, each of the form
\[
\mathcal O_\sigma=\{a\sigma,-a\sigma\},\qquad
 a=\frac{1-\lambda}{1+\lambda},\qquad \sigma\in\{-1,1\}^d,
\]
with \(\sigma\) and \(-\sigma\) identifying the same orbit. Every point of \(Q_d\) converges geometrically to one of them, and their Lebesgue-normalized basins all have volume \(2^{1-d}\).

For a Lebesgue-uniform initial point \(X\in Q_d\), almost surely each nonzero coordinate changes sign for the first time at a finite positive integer \(\tau_i\), after which its sign alternates at every step. Let \(H_d=\max_i\tau_i\), the last first-sign-change time among the coordinates. **For every positive integer \(n\)** the exact distribution is
\[
\Pr(H_d\le n)=\left[\min\{1,e^{n\delta}-1\}\right]^d.
\]

This finite-dimensional identity has two distinct sharp singular regimes as \(d\to\infty\), with contraction parameters \(\lambda_d=e^{-\delta_d}\) and \(\delta_d\to0\):

1. **Continuum regime:** if \(d\delta_d\to0\), then
\[
 2d\bigl(\log2-\delta_d H_d\bigr)\ \Longrightarrow\ E,
 \qquad \Pr(E>t)=e^{-t}\ \ (t\ge0).
\]
2. **Lattice regime:** if \(d\delta_d\to\gamma\in(0,\infty)\) and the fractional part \(r_d=\{(\log2)/\delta_d\}\) tends to \(r\in[0,1]\), then
\[
 H_d-\left\lfloor\frac{\log2}{\delta_d}\right\rfloor\ \Longrightarrow\ J_{\gamma,r},
 \qquad \Pr(J_{\gamma,r}\le k)=\exp\bigl(-2\gamma(r-k)_+\bigr)
 \quad(k\in\mathbb Z).
\]
The \(r=1\) expression is a legitimate endpoint subsequential law, while \(r=0\) is the opposite endpoint; their distinction describes a genuine arithmetic phase dependence. As a further boundary case, when \(d\delta_d\to\infty\) and \(r_d\to r\in(0,1]\), the displayed centered hitting time tends to \(1\) in probability.

## Assumptions and scope

All norms used in the farthest-corner rule are Euclidean. For \(x\in[-1,1]^d\), the chosen corner has \(i\)-th coordinate \(-1\) when \(x_i\ge0\), and \(+1\) when \(x_i<0\). This convention defines a single-valued map everywhere; any other deterministic tie rule consistent off the coordinate hyperplanes gives the same almost-everywhere hitting-time statistics. The statement about **all initial points** is made for this explicit convention. The two singular limits concern independent random initial coordinates, uniformly distributed on \([-1,1]\), and refer to convergence in law; no central-limit scaling is claimed. The \(r\in[0,1]\) endpoint allowance describes subsequences of fractional parts, which themselves lie in \([0,1)\).

## Proof

**Coordinate reduction.** Maximizing the squared distance \(\sum_i(x_i-v_i)^2\) over \(v_i\in\{-1,1\}\) selects each sign separately. Therefore \(F_\lambda\) is the Cartesian product of
\[
 f_\lambda(t)=\begin{cases}\lambda t-(1-\lambda),&t\ge0,\\
 \lambda t+(1-\lambda),&t<0.\end{cases}
\]
Put \(c=1-\lambda\). While a positive coordinate has not changed sign, its value after \(j\) steps is \(\lambda^j(1+t)-1\). Its first passage to the nonpositive half-line is finite, and the arrival value lies in \([-c,0]\). The next value lies in \([c(1-\lambda),c]\). Every point of that positive interval maps into \([-c,0)\), and conversely every point of \([-c,0)\) maps into \((0,c]\). Thus the scalar signs alternate forever after the first change. Negative starting coordinates follow by odd symmetry away from the tie; a starting zero maps first to \(-c\) and subsequently enters the same alternating regime.

On an alternating branch, \(f_\lambda^2(t)=\lambda^2t+c^2\) for the positive phase and \(f_\lambda^2(t)=\lambda^2t-c^2\) for the negative phase. Each has the unique appropriate fixed point \(\pm c/(1+\lambda)\). Hence every scalar coordinate converges geometrically to the appropriate two-cycle. Their Cartesian products yield the indicated \(2^{d-1}\) primitive cycles and exhaust all periodic points. Away from the countable union of coordinate switching preimages, sign reflections commute with the dynamics; they transitively permute the \(2^{d-1}\) attractors. Since these reflections preserve cube volume, every attracting basin has normalized volume \(2^{1-d}\).

**Exact hitting-time law.** For a positive initial coordinate \(t\in(0,1)\), outside the countable set of exact-zero crossings,
\[
 \tau(t)=\left\lceil\frac{\log(1+t)}{\delta}\right\rceil.
\]
The same holds with \(|t|\) for a negative initial coordinate. If \(U\sim\mathrm{Unif}(0,1)\), then \(\Pr(\tau\le n)=\Pr(U\le e^{n\delta}-1)=\min\{1,e^{n\delta}-1\}\) for every \(n\ge1\). The \(d\) coordinates are independent, so raising this probability to the \(d\)-th power gives the displayed exact law.

**Singular limits.** Write \(M_d=\max_{1\le i\le d}|X_i|\). Almost surely,
\[
 H_d=\left\lceil\frac{\log(1+M_d)}{\delta_d}\right\rceil.
\]
The elementary exact identity \(\Pr(d(1-M_d)>t)=(1-t/d)^d\) for \(0\le t\le d\) shows \(d(1-M_d)\Longrightarrow E\), where \(E\) is unit exponential. Taylor expansion near \(M_d=1\) gives
\[
 d\bigl(\log2-\log(1+M_d)\bigr)=\frac{d(1-M_d)}2+o_{\Pr}(1).
\]
The ceiling introduces an error smaller than \(\delta_d\) after rescaling by \(\delta_d\). If \(d\delta_d\to0\), multiplying the last display by two proves the continuum regime.

When \(d\delta_d\to\gamma\in(0,\infty)\), set \(b_d=\lfloor(\log2)/\delta_d\rfloor\). Then
\[
 \frac{\log(1+M_d)}{\delta_d}-b_d
 =r_d-\frac{d(1-M_d)}{2d\delta_d}+o_{\Pr}(1)
 \Longrightarrow r-\frac E{2\gamma}.
\]
Since the limiting variable has a continuous distribution and therefore gives zero mass to the integer discontinuities of the ceiling, the continuous-mapping theorem yields \(J_{\gamma,r}=\lceil r-E/(2\gamma)\rceil\). Its distribution is exactly \(\Pr(J_{\gamma,r}\le k)=\Pr(E\ge2\gamma(r-k))=e^{-2\gamma(r-k)_+}\). Finally, if \(d\delta_d\to\infty\) and \(r_d\to r>0\), the exact CDF implies \(\Pr(H_d\le b_d)\to0\), while \(H_d\le b_d+1\) almost surely; this proves the stated frozen endpoint.

## Verification

The accompanying standalone `check.py` performs exact-rational checks of the scalar and product two-cycles, two-step contraction identities, eventual sign alternation, and finite-grid threshold counts at several contraction ratios and dimensions. It passed 7,030 supporting assertions. The unbounded-dimension and infinite-time conclusions are proved in the preceding argument; the finite checks do not certify those limits.

## Relationship to prior work

Abdulaziz (2024) studies the farthest-vertex game on planar regular polygons and identifies two-point attracting orbits when the number of polygon vertices is even. In particular, the square shares the present map's elementary two-cycle mechanism. The product construction supplies a high-dimensional hypercube setting, but that prior planar result does not state the exact distribution of the last first-sign-change time or its joint high-dimensional/weak-contraction limits. The new quantitative object is the exact settling-time law and its continuum/lattice crossover, **not** a claim that coordinatewise affine contraction or elementary uniform maxima are new techniques. Other piecewise-contraction and sign-feedback results have different state spaces, selection rules, or target statistics.

## Limitations

This is a result for Euclidean farthest corners of the axis-aligned hypercube, not for arbitrary centrally symmetric polytopes. The exact time law is for Lebesgue-uniform independent starting coordinates; other initial laws yield different order statistics. Its normalized basins have equal measure, but their geometric boundaries are not classified here. No publication-priority claim is made beyond the inspected sources; general extreme-value theory supplies the classical order-statistic step. The result has not received independent mathematical audit.

## References

1. Abdulrahman Abdulaziz, *The Chaos Game Versus Uniform Rotation: From Sierpinski Gaskets to Periodic Orbits*, arXiv:2407.02506, first public preprint 2024-06-17, especially Section 5.
2. Standard elementary order-statistic identity for maxima of independent uniform random variables (derived explicitly above; no external theorem needed).
