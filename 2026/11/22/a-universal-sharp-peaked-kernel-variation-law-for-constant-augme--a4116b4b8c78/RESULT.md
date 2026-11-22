# A universal sharp peaked-kernel variation law for constant-augmented interpolation

## Finding

For every integer \(n\ge 2\), every fixed strictly ordered set of real interpolation nodes \(X=(x_1,\ldots,x_n)\), and every continuous nonincreasing profile \(\phi:[0,\infty)\to[0,1]\) satisfying \(\phi(0)=1\), \(\lim_{t\to\infty}\phi(t)=0\), and strict positive definiteness of \(\phi(|u-v|)\) on every finite set of distinct real sites, define the constant-augmented radial interpolation operator \(S_{\varepsilon,X}\) below. Its sharp nodal-to-continuous total-variation norm obeys

\[
\lim_{\varepsilon\to\infty}\sup_{V_d(y)>0}
\frac{\operatorname{Var}_{[x_1,x_n]}(S_{\varepsilon,X}y)}{V_d(y)}
=\frac{4\lfloor n^2/4\rfloor}{n}-1
=\begin{cases}n-1,&n\text{ even},\\ n-1-1/n,&n\text{ odd}.\end{cases}
\]

In fact, with \(h=\min_{1\le i<n}(x_{i+1}-x_i)>0\), there is a constant \(C_n\) such that for all sufficiently large \(\varepsilon\), the absolute difference between this sharp norm and its stated limit is at most \(C_n[\phi(\varepsilon h/2)+\phi(\varepsilon h)]\). Thus Gaussian profiles have an exponentially small error in \(\varepsilon^2h^2\), while exponential profiles have an exponentially small error in \(\varepsilon h\).

The limit is independent of the profile and all fixed positive gaps. For every finite \(\varepsilon>0\), a nodal single-step sequence attains the exact induced norm. For all sufficiently large \(\varepsilon\) (depending on \(X,n,\phi\)), some central step attains that finite-parameter norm, and no noncentral step does. When \(n\) is even, the unique eligible step index is \(j=n/2\); when \(n\) is odd, the two eligible indices are \(j=(n-1)/2\) and \(j=(n+1)/2\). Uniqueness of arbitrary extremizing data vectors is not asserted.

For every fixed input \(y\), the limiting variation itself is

\[
\lim_{\varepsilon\to\infty}\operatorname{Var}_{[x_1,x_n]}(S_{\varepsilon,X}y)
=|y_1-\bar y|+2\sum_{i=2}^{n-1}|y_i-\bar y|+|y_n-\bar y|,
\qquad \bar y=\frac1n\sum_{i=1}^ny_i.
\]

## Assumptions and scope

The data vector \(y=(y_1,\ldots,y_n)\) is real, \(V_d(y)=\sum_{i=1}^{n-1}|y_{i+1}-y_i|\), and \(\operatorname{Var}_{[x_1,x_n]}\) is the usual supremum-over-partitions variation of a continuous real function on the closed node interval. Set \(K_\varepsilon=(\phi(\varepsilon|x_i-x_j|))_{i,j=1}^n\). For every \(\varepsilon>0\), solve the unique saddle-point system

\[
K_\varepsilon c+a\mathbf1=y,\qquad\mathbf1^{\mathsf T}c=0,
\]

and define

\[
(S_{\varepsilon,X}y)(x)=a+\sum_{i=1}^nc_i\phi(\varepsilon|x-x_i|),
\quad x_1\le x\le x_n.
\]

The scalar constant term and side constraint reproduce constant data exactly. Gaussian \(\phi(t)=e^{-t^2}\), exponential \(\phi(t)=e^{-t}\), and other strictly positive definite monotone decaying kernels satisfy the hypotheses. Neither differentiability nor equal spacing is assumed. The limit takes the peak-narrowing scale \(\varepsilon\to\infty\) **after fixing** \(n\) and \(X\); it is not uniform over collapsing grids or increasing node counts.

## Proof

**1. Existence and constant reproduction.** Strict positive definiteness makes \(K_\varepsilon\) positive definite. The saddle-point matrix is invertible: a null-vector satisfies \(K_\varepsilon c+a\mathbf1=0\) and \(\mathbf1^{\mathsf T}c=0\), whence \(c^{\mathsf T}K_\varepsilon c=0\), so \(c=0\) and \(a=0\). For constant input \(y=b\mathbf1\), the unique solution is \((c,a)=(0,b)\). Every basis translate is monotone on either side of its center, hence has finite variation on \([x_1,x_n]\). The finite sum does too.

**2. Exact finite-parameter step reduction.** For \(1\le j<n\), write \(s^{(j)}_i=\mathbf1_{\{i>j\}}\). Every data vector decomposes as

\[
y=y_1\mathbf1+\sum_{j=1}^{n-1}(y_{j+1}-y_j)s^{(j)}.
\]

Linearity and exact constant reproduction, followed by the triangle inequality for total variation, give

\[
\operatorname{Var}(S_{\varepsilon,X}y)
\le\sum_{j=1}^{n-1}|y_{j+1}-y_j|\operatorname{Var}(S_{\varepsilon,X}s^{(j)}).
\]

Since \(V_d(s^{(j)})=1\), the sharp norm is exactly

\[
K_{\varepsilon,X}=\max_{1\le j<n}\operatorname{Var}(S_{\varepsilon,X}s^{(j)}),
\]

and this maximum is attained by a step for every \(\varepsilon>0\). This is an exact identity, not a discrete-grid approximation to continuous variation.

**3. Concentration of the coefficients.** Put \(h=\min_{1\le i<n}(x_{i+1}-x_i)>0\). Since \(\phi\) is nonincreasing and vanishes at infinity, \(K_\varepsilon\to I\) entrywise and in matrix norm. Solving the limiting saddle-point equations gives

\[
a_\varepsilon\to\bar y,\qquad c_{i,\varepsilon}\to y_i-\bar y.
\]

The convergence is uniform on the normalized compact set \(y_1=0\), \(V_d(y)\le1\). Indeed, \(\|K_\varepsilon-I\|_\infty\le(n-1)\phi(\varepsilon h)\), so a Neumann-series inverse and the explicit Schur complement \(a_\varepsilon=(\mathbf1^{\mathsf T}K_\varepsilon^{-1}y)/(\mathbf1^{\mathsf T}K_\varepsilon^{-1}\mathbf1)\) yield uniform \(O_n(\phi(\varepsilon h))\) errors.

**4. Localization of total variation.** Define Voronoi breakpoints \(m_i=(x_i+x_{i+1})/2\), with \(m_0=x_1\) and \(m_n=x_n\), and closed cells \(J_i=[m_{i-1},m_i]\). The \(i\)-th translate \(g_i(x)=\phi(\varepsilon|x-x_i|)\) has variation on its own cell tending to \(w_i\), where \(w_1=w_n=1\) and \(w_i=2\) for \(2\le i\le n-1\): each interior peak has one ascent and one descent, while each endpoint peak has just one flank. More precisely, its own-cell variation differs from \(w_i\) by at most \(2\phi(\varepsilon h/2)\).

For \(j\ne i\), the center \(x_j\) lies outside the interior of \(J_i\) and \(|x-x_j|\ge h/2\) throughout that cell. Monotonicity makes \(g_j\) monotone on \(J_i\), so \(\operatorname{Var}_{J_i}(g_j)\le\phi(\varepsilon h/2)\). The reverse triangle inequality for variation, applied separately on the cells, then gives

\[
\left|\operatorname{Var}_{[x_1,x_n]}(S_{\varepsilon,X}y)
-\sum_{i=1}^nw_i|c_{i,\varepsilon}|\right|
\le C_n\phi(\varepsilon h/2)\sum_{i=1}^n|c_{i,\varepsilon}|.
\]

The constant baseline contributes no variation. Since a continuous function's variation is additive over consecutive subintervals, the cell estimates sum exactly; no omitted interface jumps occur. Combining this bound with step 3 proves the stated fixed-data limiting formula, uniformly over the normalized data set.

**5. Sharp optimization.** For the step \(s^{(j)}\), its mean is \((n-j)/n\). There are \(j\) centered entries of value \(-(n-j)/n\) and \(n-j\) of value \(j/n\). The weighted endpoint/interior counts are respectively \(2j-1\) and \(2(n-j)-1\), so its limiting variation is

\[
\frac{(2j-1)(n-j)+(2(n-j)-1)j}{n}
=\frac{4j(n-j)}n-1.
\]

Maximizing the integer concave quadratic \(j(n-j)\) over \(1\le j<n\) yields \(\lfloor n^2/4\rfloor\), attained precisely at the central index or the two neighboring central indices. The finite step set and uniform coefficient convergence allow the maximum to pass through the limit. Strict separation from all other limiting step values proves the eventual-central-step assertion. This completes the proof for every allowed profile and grid.

## Verification

The standalone `checker.py` in this package computes the augmented interpolation system by partial-pivoting elimination and estimates continuous variation by fine sampling. It checks exact constant reproduction and nodal interpolation, the step-response maximum principle against random data, and convergence toward the formula at irregular fixed nodes with sizes \(2\) through \(8\), for both Gaussian and exponential kernels. Running `python3 checker.py` requires only the Python standard library and prints `ALL_LOCALIZED_KERNEL_VARIATION_CHECKS_PASS` when these finite tests pass. Sampling is expressly not a proof of continuous variation or of the infinite-parameter limit; the proof above supplies both.

## Relationship to prior work

Classical radial-basis-function interpolation and its conditioning, flat-kernel limits, and peak-concentration behavior motivate the question. Platte and Driscoll's 2004 technical report and 2005 article develop Gaussian interpolants, polynomial transformations, potential-theoretic convergence and Lebesgue constants, rather than the constant-augmented, narrow-kernel variation norm. Yarotsky (2012) gives Gaussian interpolation error formulas and convergence for analytic inputs and arbitrary nodes, not a discontinuous-step bounded-variation stability norm. These differences concern objects and implications, not mere terminology: neither the \(L^\infty\) Lebesgue coefficient nor analytic error estimates determine the present exactly sharp TV coefficient for constant-reproducing peaked interpolants. Ordinary-kriging/constant-trend interpolation is a known construction; only its specified asymptotic variation law is claimed here.

The familiar qualitative 'bed-of-nails' picture predicts localized peaks but does not itself specify their shared baseline, their endpoint/interior variation weights, nor the central-step maximization yielding \(4\lfloor n^2/4\rfloor/n-1\). A definitive claim of global historical priority is not made: relevant specialized kriging or BV literature could contain this exact law under a different name.

## Limitations

This is an asymptotic in the peak-narrowing scale for each fixed finite one-dimensional knot configuration. No finite-scale closed formula, uniform simultaneous large-\(n\)/large-\(\varepsilon\) theorem, multidimensional BV analogue, or nonmonotone/oscillatory profile extension is proved. Strict positive definiteness and monotone profile decay are hypotheses, not conclusions for arbitrary named radial families. The result does not assert a norm bound for the unaugmented Gaussian RBF map on variation seminorms; without constant reproduction that ratio need not be finite. The scientific priority assessment remains subject to examination of additional historical interpolation and geostatistical sources.

## References

1. R. B. Platte and T. A. Driscoll, *Polynomials and their Potential Theory for Gaussian Radial Basis Function Interpolation*, Technical Report 2004-01, University of Delaware, publicly available 2004-12-21: https://udspace.udel.edu/items/e069ffca-870f-437b-85ca-c0494e4117aa/full ; journal version *SIAM Journal on Numerical Analysis* 43 (2005), 750–766, https://doi.org/10.1137/040610143 . Author-hosted full text: https://tobydriscoll.net/_docs/platte-polynomials-potential-theory-2005-a.pdf .
2. D. Yarotsky, *Univariate interpolation by exponential functions and Gaussian RBFs for generic sets of nodes*, first arXiv version 2012-05-27, https://arxiv.org/abs/1205.5961 ; full text https://arxiv.org/pdf/1205.5961 .
3. O. Davydov and D. T. Oanh, *On the optimal shape parameter for Gaussian radial basis function finite difference approximation of the Poisson equation*, *Computers & Mathematics with Applications* 62 (2011), 2143–2161, open preprint at https://strathprints.strath.ac.uk/36480/ .
