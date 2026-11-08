# Exact pressure and Gaussian square counts on the first interacting domino–square strip

## Finding

Tile the open \(4\times N\) rectangle by axis-aligned \(1\times2\) and \(2\times1\) dominoes and \(3\times3\) squares, with all tiles on the integer grid, no overlap, and no protrusion. Let \(b_{N,k}\) be the number of tilings using exactly \(k\) squares, with \(b_{0,0}=1\). The complete bivariate generating function is

\[
\sum_{N\geq0}\sum_{k\geq0}b_{N,k}z^N u^k
=\frac{(1-z^2)(1-z-3z^2+z^3+z^4)}{Q(z,u)},
\]

where

\[
Q(z,u)=1-2z-7z^2+8z^3+17z^4-4z^5-9z^6+z^8-2u^2z^6(1-z^2)^2.
\]

In particular, every \(b_{N,k}\) with odd \(k\) is zero. Give all tilings of the \(4\times N\) rectangle equal probability, and let \(K_N\) count their \(3\times3\) squares. There are positive constants \(\mu\) and \(\sigma^2\), uniquely and explicitly specified below, such that

\[
\mathbb E K_N=\mu N+O(1),\qquad
\operatorname{Var}(K_N)=\sigma^2 N+O(1),\qquad
\frac{K_N-\mu N}{\sigma\sqrt N}\ \Rightarrow\ \mathcal N(0,1).
\]

Numerically, \(\mu\approx0.00976801009338\), \(\sigma^2\approx0.0181927432682\), and the exponential tiling growth per column is \(\lambda\approx2.85495052828335\).

## Assumptions and scope

All board widths are integers \(N\geq0\). The vertical dimension is exactly four cells; boundaries are open, not cylindrical or periodic. Rotations of a domino are the two separately listed available orientations; a square has a single orientation. Tilings are distinct when their occupied cell sets differ. The two-variable series is formal about \(z=0\), with \(u\) marking the number of square tiles. Statistical limits hold only under uniform measure on these finite tilings, for \(N\to\infty\).

This tile set is primitive in the rectangular-tiling sense: the horizontal domino forces any possible common horizontal divisor \(p>1\) to equal two, the vertical domino forces the analogous vertical divisor \(q>1\) to equal two, and the \(3\times3\) square obeys neither divisibility. Its full-plane tiling shift is therefore cohomologically trivial by Thorat's criterion [1]. The present result concerns a different invariant: quantitative pressure in a constrained strip. For height three each square spans the full strip and splits the tiling into renewal blocks; height four first allows other tiles to pass along the remaining row.

## Proof

**Exact finite transfer construction.** At the left boundary of the column to be filled, record three four-bit masks \((a,b,c)\). They encode occupied cells in the current and next two columns from tiles previously started. Begin at \((0,0,0)\). Fill the lowest vacant cell of the current column, recursively choosing exactly one of: a vertical two-cell domino inside this column; a horizontal domino occupying the same row in the next column; or a \(3\times3\) square occupying three consecutive rows in each of the current and next two columns. Exclude choices colliding with occupied masks or crossing the top/bottom edge. Each square choice receives weight \(u\); each completed current column receives weight \(z\). Once all four cells in the current column are filled, shift \((a,b,c)\mapsto(b,c,0)\), using the incremented masks after placing tiles. Recursive choices ending at the same next triple contribute their multiplicity.

Breadth-first exploration from the empty triple gives exactly 18 reachable states. In the deterministic exploration ordering, they are

```
(0,0,0), (15,0,0), (3,0,0), (9,0,0), (15,14,0),
(12,0,0), (15,7,0), (6,0,0), (14,0,0), (7,0,0),
(1,0,0), (8,0,0), (2,0,0), (14,14,0), (4,0,0),
(7,7,0), (13,0,0), (11,0,0).
```

Write \(T(u)\) for the 18-state adjacency matrix weighted by \(u\) per newly started square and including edge multiplicities. Every open rectangle tiling corresponds to exactly one length-\(N\) path from the empty state back to itself, hence

\[
\sum_{k\ge0}b_{N,k}u^k=(T(u)^N)_{00},\qquad
B(z,u)=\bigl[(I-zT(u))^{-1}\bigr]_{00}.
\]

Exact polynomial/rational elimination of this explicitly specified finite matrix yields the displayed numerator and denominator. The accompanying verification program generates every state/edge from first principles, performs the exact symbolic inversion, and tests the identity. The odd-square restriction also follows immediately from the area parity identity \(4N=2d+9k\), where \(d\) counts dominoes.

**Pressure and distribution.** The directed 18-state graph is strongly connected; the empty state has a one-column self-loop (two vertical dominoes), so the graph is primitive. This is established by finite graph reachability and recorded in the verifier. For every real \(t\), \(T(e^t)\) has a simple dominant positive eigenvalue \(\lambda(e^t)\), analytic in \(t\), with a spectral gap. Thus \(p(t)=\log\lambda(e^t)\) is analytic. Let \(r(u)=1/\lambda(u)\), so \(r(u)\) is the smallest positive zero in \(z\) of \(Q(z,u)\) for \(u\) near one. Put \(r=r(1)\), \(Q_z=\partial_z Q(r,1)\), and use analogous derivative notation. Then

\[
\mu=p'(0)=\frac{Q_u(r,1)}{rQ_z(r,1)},\qquad
r_t=-\frac{Q_u(r,1)}{Q_z(r,1)},
\]

\[
 r_{tt}=-\frac{Q_{zz}(r,1)r_t^2+2Q_{zu}(r,1)r_t+Q_u(r,1)+Q_{uu}(r,1)}{Q_z(r,1)},
\qquad
\sigma^2=p''(0)=\left(\frac{r_t}{r}\right)^2-\frac{r_{tt}}r.
\]

Here the first and second \(t\)-derivatives are evaluated at \(t=0\) after substituting \(u=e^t\). Exact differentiation and the positive Perron root produce the numerical values in the Finding.

The variance is **strictly positive**: if the asymptotic variance of a finite irreducible Markov additive edge weight were zero, the square-count weight would be cohomologous to a constant, forcing equal square-count-per-column averages along all cycles. The one-column empty-state self-loop has square count zero, whereas the six-column return formed by two horizontally adjacent \(3\times3\) squares in the top three rows (with the remaining row tiled by three dominoes) has square count two. Their cycle averages differ. Standard finite-matrix perturbation (equivalently, the quasi-powers argument) now gives

\[
\mathbb E e^{tK_N}=
\frac{c(t)}{c(0)}\exp\bigl(N[p(t)-p(0)]\bigr)
\bigl(1+O(\rho^N)\bigr)
\]

uniformly for \(t\) in a neighborhood of zero, where \(c(t)>0\) is analytic and \(0<\rho<1\). Differentiation proves the mean and variance asymptotics; Taylor expansion at \(t=0\) and characteristic functions prove the asserted central limit theorem. These arguments are infinite-length proofs rather than extrapolations from small boards.

## Verification

Run `python verify.py` with Python 3 and SymPy installed. It reconstructs the 18-state graph, verifies strong connectivity and the zero-square self-loop, derives the exact rational function by symbolic matrix inversion, and independently enumerates individual cell placements on each \(4\times N\) board for \(1\leq N\leq9\). It checks the two methods agree on the **entire square-count histogram**, not just total counts. The first nontrivial square counts are \(b_{6,2}=2\), \(b_{7,2}=6\), \(b_{8,2}=32\), \(b_{9,2}=108\). The total counts for \(N=0,\ldots,9\) are \(1,1,5,11,36,95,283,787,2277,6444\). It also evaluates the Perron-root derivatives for the stated numerical approximations.

## Relationship to prior work

Thorat [1] proves a decidable criterion for triviality of rectangular-tiling cocycles and associated mixing properties, not a finite-width weighted transfer function or a square-count limit theorem. Propp [2] establishes recurrence and reciprocity for domino-only rectangular tilings; it does not include squares. The standard weighted finite-transfer-matrix and Perron–Frobenius mechanisms are not claimed as new. The assessed specific contribution is the exact two-variable rational pressure function for this first interacting mixed strip, together with the resulting strictly positive square-frequency variance and Gaussian law. The literature search did not locate an exact prior table or a stronger theorem that specializes to this statement; this is not a proof of historical uniqueness.

## Limitations

The full planar pressure/entropy is not computed. Neither arbitrary strip heights nor periodic vertical boundaries are covered. No statement is made about dynamical systems outside this tiling shift. Numerical constants are approximations to the exact implicit Perron-root expressions, and the central limit theorem applies to the uniform finite-board ensemble. The independent scientific audit and comprehensive historical-priority confirmation have not been performed.

## References

[1] Aditya Thorat, *Cocycles on Tiling Spaces*, arXiv:2610.39907v1, October 29, 2026, sections 2.3–2.5 and 3, https://arxiv.org/html/2610.39907v1.

[2] James Propp, *A Reciprocity Theorem for Domino Tilings*, *Electronic Journal of Combinatorics* 8(1), R18 (2001), https://doi.org/10.37236/1562.

[3] J. Cohn, R. Kenyon and J. Propp, *A Variational Principle for Domino Tilings*, *Journal of the American Mathematical Society* 14 (2001), 297–346, https://arxiv.org/abs/math/0008220.
