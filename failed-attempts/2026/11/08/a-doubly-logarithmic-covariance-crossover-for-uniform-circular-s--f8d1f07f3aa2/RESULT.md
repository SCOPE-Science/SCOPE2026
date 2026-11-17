# A doubly logarithmic covariance crossover for uniform circular spacings

## Finding

For every integer \(n\ge2\), let \((X_1,\ldots,X_n)\) be a uniformly distributed random vector on the simplex \(\{x_i\ge0,\ \sum_i x_i=1\}\), and set \(M_n=\max_i X_i\) and \(K_n(t)=\sum_{i=1}^{n}\mathbf1_{\{X_i>t\}}\). For sufficiently large \(n\) write
\[
a_n=\log\log n+\log\log\log n,\qquad t_n(z)=\frac{a_n+z}{n}.
\]
For **every fixed real \(z\)**,
\[
\boxed{\lim_{n\to\infty}n\operatorname{Cov}(M_n,K_n(t_n(z)))=1-e^{-z}.}
\]
For each \(n\ge2\), this covariance, as a function of \(t\in(0,1)\), has a unique zero \(\tau_n\), and
\[
\boxed{n\tau_n=\log\log n+\log\log\log n+o(1).}
\]
The two-term centering is significant: the covariance changes sign at scale \((\log\log n)/n\), far below the typical maximum-spacing scale \((\log n)/n\). The claim is a **scaled asymptotic transition**, not a new claim to the previously derivable finite covariance expression.

## Assumptions and scope

All logarithms are natural. The random vector has the Dirichlet distribution with all parameters equal to one. It is also the vector of cyclic gaps produced by \(n\) independent uniform points on a circle of circumference one (ordered cyclically from an arbitrary starting point). The inequality in \(K_n(t)\) is strict; probability-zero equality is immaterial. The limit is pointwise in fixed \(z\in\mathbb R\); neither a uniform-in-\(z\) statement nor a finite-sample rate for the root is asserted. The formula defining \(t_n(z)\) is used only for sufficiently large \(n\) that its logarithms exist and \(0<t_n(z)<1\).

## Proof

**1. One-coordinate decomposition.** Write \(Y_{n-1}\) for the maximum coordinate of an independent Dirichlet vector of dimension \(n-1\). For \(n=2\) the latter is the deterministic value one. Conditional on \(X_1=x\), the remaining coordinates equal \((1-x)\) times this Dirichlet vector. Put
\[
R_n=\bigl(X_1-(1-X_1)Y_{n-1}\bigr)_+.
\]
Then, pointwise,
\[
M_n=(1-X_1)Y_{n-1}+R_n.
\]
The standard spacing identity \(\mathbb EM_n=H_n/n\), where \(H_n=\sum_{j=1}^n1/j\), follows for example from the exponential representation or integration of the classical maximum-spacing distribution. Since \(\mathbb E Y_{n-1}=H_{n-1}/(n-1)\) and \(\mathbb E(1-X_1)=(n-1)/n\), the identity implies \(\mathbb ER_n=1/n^2\).

The coordinate \(X_1\) has density \((n-1)(1-x)^{n-2}\) on \((0,1)\). Hence for \(p=(1-t)^{n-1}\),
\[
\mathbb P(X_1>t)=p,\qquad
\mathbb E[(1-X_1)\mathbf1_{\{X_1>t\}}]=\frac{n-1}{n}(1-t)p.
\]
By exchangeability, \(\operatorname{Cov}(M_n,K_n(t))=n\operatorname{Cov}(M_n,\mathbf1_{\{X_1>t\}})\). Substitute the decomposition, and define
\[
\eta_n(t)=n^2\mathbb E\bigl[R_n\mathbf1_{\{X_1\le t\}}\bigr].
\]
An **exact identity for every** \(n\ge2\) and \(0<t<1\) is
\[
\boxed{n\operatorname{Cov}(M_n,K_n(t))
=1-\eta_n(t)-(1-t)^{n-1}(1+ntH_{n-1}).}\tag{1}
\]
Indeed, the first term contributes \(H_{n-1}(1-t)p\) to \(n\mathbb E[M_n\mathbf1_{\{X_1>t\}}]\); subtracting \(H_np\) gives \(-p(1/n+tH_{n-1})\). The remaining term is \(n\mathbb E[R_n\mathbf1_{\{X_1>t\}}]=(1-\eta_n(t))/n\). Multiplication by \(n\) yields (1).

**2. The error is negligible at the proposed crossover.** On \(\{R_n>0,\ X_1\le t\}\), the first coordinate is the largest, so \(M_n=X_1\le t\). Since \(0\le R_n\le1\),
\[
0\le\eta_n(t)\le n^2\mathbb P(M_n\le t).
\]
Let \(E_1,\ldots,E_n\) be independent unit-rate exponentials and \(S=\sum_i E_i\). The normalized vector \((E_i/S)\) has the required Dirichlet law. On \(S\le2n\), the event \(M_n\le t\) implies \(\max_iE_i\le2nt\). Thus by a Chernoff bound and independence,
\[
\eta_n(t)\le n^2\bigg[\left(\frac2e\right)^n+
\left(1-e^{-2nt}\right)^n\bigg]
\le n^2\bigg[\left(\frac2e\right)^n+
\exp\{-ne^{-2nt}\}\bigg].\tag{2}
\]
For \(t=t_n(z)\), put \(u=nt=a_n+z\). Then \(u=O(\log\log n)\) and \(ne^{-2u}=n e^{-2z}/[(\log n)^2(\log\log n)^2]\to\infty\) faster than \(\log n\). Therefore the right side of (2) is \(o(1)\).

**3. Compute the scaled profile.** As \(n\to\infty\), \(u=O(\log\log n)\), and
\[
(1-u/n)^{n-1}=e^{-u}(1+o(1)),\qquad
H_{n-1}=\log n+\gamma+o(1).
\]
Consequently,
\[
(1-t_n(z))^{n-1}(1+nt_n(z)H_{n-1})
=e^{-z}\frac{1+uH_{n-1}}{(\log n)(\log\log n)}(1+o(1))
\longrightarrow e^{-z},
\]
because \(u/(\log\log n)\to1\). Identity (1) and the negligible-error bound give \(n\operatorname{Cov}\to1-e^{-z}\) for each fixed \(z\).

**4. Unique zero and its position.** Let \(h_n(t)=\mathbb E[M_n\mid X_1>t]\). Conditional on \(X_1>t\), the coordinate can be represented as \(X_1=t+(1-t)B\) where \(B\) has the \(\operatorname{Beta}(1,n-1)\) law, independently of \(Y_{n-1}\). Therefore
\[
h_n(t)=\mathbb E\max\left\{t+(1-t)B,\ (1-t)(1-B)Y_{n-1}\right\}.
\]
For fixed \(B,Y_{n-1}\), this is the maximum of two affine functions of \(t\), so \(h_n\) is continuous and convex on \([0,1]\). Moreover \(h_n(0)=\mathbb EM_n\), \(h_n(1)=1>\mathbb EM_n\), and
\[
\operatorname{Cov}(M_n,K_n(t))=n(1-t)^{n-1}\bigl(h_n(t)-\mathbb EM_n\bigr).
\]
When \(0<t<1/n\), \(R_n>0\) forces \(X_1>1/n>t\), hence \(\eta_n(t)=0\). Differentiating (1) at \(t=0\) shows that the right derivative of \(n\operatorname{Cov}\) is \((n-1)-nH_{n-1}<0\). Thus the convex function \(h_n(t)-\mathbb EM_n\) is negative immediately to the right of zero and positive at one. Convexity makes its later zero unique: if \(s>0\) has negative value and \(t>s\) is a zero, every \(u>t\) satisfies a strictly positive lower secant bound. Hence there is exactly one zero \(\tau_n\in(0,1)\).

Finally, for any fixed \(\varepsilon>0\), the already established profile has strictly negative sign at \(z=-\varepsilon\) and strictly positive sign at \(z=+\varepsilon\), for all sufficiently large \(n\). Uniqueness yields
\[
\frac{a_n-\varepsilon}{n}<\tau_n<\frac{a_n+\varepsilon}{n}.
\]
Since \(\varepsilon>0\) was arbitrary, \(n\tau_n-a_n\to0\), proving the asserted two-term centering. \(\square\)

## Verification

The standalone `verify.py` evaluates finite-sample covariance coefficients with exact rational arithmetic, independently integrates the conditional Dirichlet maximum over the one-coordinate beta density for small dimensions, and tests rigorous explicit error bounds (2) in large finite dimensions. Its execution passed 101 exact, bounded and quadrature assertions. Those checks corroborate algebra and normalization but do not replace the all-dimensional proof above. Run `python verify.py` with Python 3; the optional mpmath dependency adds the independent quadrature comparisons.

## Relationship to prior work

The basic Dirichlet spacings and the maximum \(M_n\), including \(\mathbb EM_n=H_n/n\) and its \((\log n)/n\) extreme-value scale, are classical. Holst (1980) studies ordered broken-stick spacings, exponential representations and a related *sequential coverage time*, but does not state the covariance between a fixed-sample maximum and the number of gaps above a threshold. Schlemm (2014) computes maximum-spacing moments and its Gumbel limit, not this cross-statistic. An exact finite covariance formula and its one-crossing sign property can already be established by simplex identities; those are background and are not asserted to be new here. The assessed mathematical content is the sharp \(\log\log n+\log\log\log n\) location of that zero and the entire \(1-e^{-z}\) scaled crossover profile. General spacing literature may contain an implicit specialization; see the limitations.

## Limitations

The crossover is only pointwise for fixed real \(z\). It does not give a uniform finite-sample error, full joint limit law, or a result for nonuniform point locations or non-unit Dirichlet parameters. The root converges slowly because of iterated logarithms. A complete historical priority proof is impossible from an indexed search alone; the closest inspected primary texts have been compared by their actual theorems and observables. Independent specialist validation has not been performed.

## References

- Lars Holst, “On the lengths of the pieces of a stick broken at random,” *Journal of Applied Probability* **17** (1980), 623–634, DOI: `10.2307/3212956`; open full text: https://imprs-gw-lectures.aei.mpg.de/wp-content/uploads/2023/12/Holst_StickBreakingDistributions.pdf .
- Eckhard Schlemm, “Limiting distribution of the maximal distance between random points on a circle: A moments approach,” arXiv:1405.6114v1, first posted 2014-05-23, https://arxiv.org/abs/1405.6114 .
