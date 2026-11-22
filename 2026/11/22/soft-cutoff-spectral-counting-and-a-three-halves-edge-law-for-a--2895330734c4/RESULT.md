# Soft-cutoff spectral counting and a three-halves edge law for a power-tapered Hilbert matrix

## Finding

For the positive, trace-class matrix
\[
H_\varepsilon(m,n)=\frac{(mn)^{-\varepsilon/2}}{m+n},\qquad m,n\in\mathbb N,\quad\varepsilon>0,
\]
let \(N_\varepsilon(s)=\#\{j:\lambda_j(H_\varepsilon)>s\}\), where eigenvalues are counted with multiplicity. For every fixed \(0<s<\pi\), put \(L=\log(\pi/s)\). Then
\[
\lim_{\varepsilon\downarrow0}\varepsilon N_\varepsilon(s)
=\mathcal F(L):=\frac{1}{\pi^2}\int_0^L\operatorname{arcosh}(e^v)\,dv.
\]
This profile has the two sharp asymptotic regimes
\[
\mathcal F(L)=\frac{2\sqrt2}{3\pi^2}L^{3/2}(1+O(L))\quad(L\downarrow0),
\qquad
\mathcal F(L)=\frac{L^2}{2\pi^2}+\frac{\log2}{\pi^2}L+O(1)\quad(L\to\infty).
\]
Thus smooth power tapering changes the threshold-edge exponent from the square-root profile of hard Hilbert sections to a three-halves power. These are **sequential** limiting statements: first \(\varepsilon\downarrow0\) for fixed \(s\), then investigate the resulting profile as \(s\) varies.

The same argument proves, for every integer \(r\ge1\),
\[
\lim_{\varepsilon\downarrow0}\varepsilon\operatorname{Tr}(H_\varepsilon^r)
=\frac{1}{2\pi r}\int_{\mathbb R}\left(\frac{\pi}{\cosh(\pi\xi)}\right)^r\,d\xi.
\]
In particular the first three limits are \(1/2\), \(1/2\), and \(\pi^2/12\).

## Assumptions and scope

The ambient space is \(\ell^2(\mathbb N)\) with \(\mathbb N=\{1,2,\ldots\}\). The matrix is an entrywise power-tapered version of the Hilbert matrix with denominator \(m+n\), not \(m+n-1\). All parameters \(\varepsilon\) are strictly positive; no finite-section cutoff is applied to the operator in the theorem. The norm bound \(\|H_\varepsilon\|\le\pi\) follows from Hilbert's inequality because \(H_\varepsilon=D_\varepsilon H_0D_\varepsilon\) with \(D_\varepsilon=\operatorname{diag}(n^{-\varepsilon/2})\). Positivity follows from
\[
\frac1{m+n}=\int_0^1 t^{m+n-1}\,dt,
\]
and trace class follows from positivity and the finite diagonal trace
\[
\operatorname{Tr}(H_\varepsilon)=\frac12\sum_{n\ge1}n^{-1-\varepsilon}=\frac12\zeta(1+\varepsilon).
\]
In particular \(H_\varepsilon\) is compact, so \(N_\varepsilon(s)\) is finite for every \(s>0\).

## Proof

**1. Continuous comparison with a uniform Hilbert–Schmidt error.** Let \(C_\varepsilon\) on \(L^2([1,\infty),dx)\) have the positive kernel
\[
f_\varepsilon(x,y)=\frac{(xy)^{-\varepsilon/2}}{x+y}.
\]
As with the discrete matrix, the Laplace representation makes \(C_\varepsilon\) positive. Its diagonal trace is \(\operatorname{Tr}C_\varepsilon=1/(2\varepsilon)\), so it is trace class. The Carleman norm inequality gives \(\|C_\varepsilon\|\le\pi\). Restrict henceforth to \(0<\varepsilon\le1\).

Let \(P\) denote orthogonal projection onto functions constant on each interval \([n,n+1)\), \(n\ge1\). Identify that range with \(\ell^2(\mathbb N)\), and extend \(H_\varepsilon\) by zero on its orthogonal complement, calling the extension \(\widetilde H_\varepsilon\). We claim
\[
\sup_{0<\varepsilon\le1}\|C_\varepsilon-\widetilde H_\varepsilon\|_{\mathcal S_2}<\infty.\tag{1}
\]
Indeed, \(\partial_x f_\varepsilon=-(\varepsilon/(2x)+1/(x+y))f_\varepsilon\), and similarly for \(y\). Since \((xy)^{-\varepsilon/2}\le1\),
\[
|\partial_x f_\varepsilon|\le\frac1{2x(x+y)}+\frac1{(x+y)^2},\qquad
|\partial_y f_\varepsilon|\le\frac1{2y(x+y)}+\frac1{(x+y)^2}.
\]
The squared right-hand sides are integrable over \([1,\infty)^2\). The unit-cell Poincaré inequality, applied independently in both variables, bounds \(\|C_\varepsilon-PC_\varepsilon P\|_{\mathcal S_2}\) by a constant times the \(L^2\)-norms of these derivatives, uniformly in \(\varepsilon\). The matrix of \(PC_\varepsilon P\) is the unit-square average of \(f_\varepsilon\). Comparing that average with \(f_\varepsilon(m,n)\), monotonicity in both variables and the displayed derivative estimates at the lower cell corners bound the squared entrywise differences by a constant times
\[
\sum_{m,n\ge1}\left(\frac1{m(m+n)}+\frac1{n(m+n)}+\frac1{(m+n)^2}\right)^2<\infty.
\]
This proves (1).

Both operators have norm at most \(\pi\) and Hilbert–Schmidt norm \(O(\varepsilon^{-1/2})\): for positive operators, \(\|T\|_{\mathcal S_2}^2\le\|T\|\operatorname{Tr}T\), and the displayed traces have that order. For every fixed integer \(r\ge2\), telescope the difference of their \(r\)-th powers. In each summand use the uniform Hilbert–Schmidt bound (1) for one factor, an \(O(\varepsilon^{-1/2})\) Hilbert–Schmidt bound for another, and operator-norm bounds \(\le\pi\) for the remaining factors. Hölder's trace-ideal inequality gives
\[
|\operatorname{Tr}(H_\varepsilon^r)-\operatorname{Tr}(C_\varepsilon^r)|=O_r(\varepsilon^{-1/2}).\tag{2}
\]
For \(r=1\), the exact trace formulas give directly
\(\varepsilon\operatorname{Tr}(H_\varepsilon)\to1/2=\varepsilon\operatorname{Tr}(C_\varepsilon)\). Thus all fixed positive moments agree to leading order after multiplication by \(\varepsilon\).

**2. Exact continuum moment limit.** The unitary logarithmic coordinate change \((Uf)(t)=e^{t/2}f(e^t)\), \(t\ge0\), transforms \(C_\varepsilon\) into the positive operator with kernel
\[
 e^{-\varepsilon(t+s)/2}k(t-s),\qquad k(v)=\frac1{2\cosh(v/2)}.
\]
Under the Fourier convention \(\widehat k(\xi)=\int_{\mathbb R}k(v)e^{-i\xi v}\,dv\),
\[
\widehat k(\xi)=\frac\pi{\cosh(\pi\xi)}.
\]
For \(r\ge2\) the cyclic trace integral, with \(t_1=t\), \(t_j=t+v_j\) and \(v_1=v_{r+1}=0\), becomes
\[
\varepsilon\operatorname{Tr}(C_\varepsilon^r)
=\frac1r\int_{\mathbb R^{r-1}}
 \exp\!\left[-\varepsilon\sum_{j=1}^r(v_j+M(v))\right]
 \prod_{j=1}^r k(v_j-v_{j+1})\,dv_2\cdots dv_r,
\]
where \(M(v)=\max(0,-v_2,\ldots,-v_r)\). The exponent is nonpositive, and the cyclic product is integrable because its integral is \(k^{*r}(0)<\infty\). Dominated convergence and Fourier inversion yield
\[
\lim_{\varepsilon\downarrow0}\varepsilon\operatorname{Tr}(C_\varepsilon^r)
=\frac1r k^{*r}(0)
=\frac1{2\pi r}\int_{\mathbb R}\widehat k(\xi)^r\,d\xi.
\]
The \(r=1\) case is the previously evaluated diagonal trace. Together with (2), this proves the full moment assertion.

**3. From moments to counting.** Define the finite measure on \([0,\pi]\)
\[
\mu_\varepsilon=\varepsilon\sum_j\lambda_j(H_\varepsilon)\,\delta_{\lambda_j(H_\varepsilon)}.
\]
Its \(q\)-th ordinary moment, for integer \(q\ge0\), is \(\varepsilon\operatorname{Tr}(H_\varepsilon^{q+1})\). Step 2 identifies every limit with the corresponding moment of the finite measure
\[
\mu=\frac1{2\pi}\int_0^\infty\int_{\mathbb R}
 e^{-u}\widehat k(\xi)\,
 \delta_{e^{-u}\widehat k(\xi)}\,d\xi\,du.
\]
Since all measures are supported in the compact interval \([0,\pi]\) and moments determine finite measures there, polynomial approximation gives \(\mu_\varepsilon\Rightarrow\mu\). For every \(s>0\), \(\mu\) has no atom at \(s\), because for any fixed \(\xi\) there is at most one \(u\ge0\) with \(e^{-u}\widehat k(\xi)=s\). Testing the bounded function \(\mathbf1_{(s,\pi]}(x)/x\) proves
\[
\lim_{\varepsilon\downarrow0}\varepsilon N_\varepsilon(s)
=\frac1{2\pi}\int_0^\infty\int_{\mathbb R}
 \mathbf1_{\{e^{-u}\pi\operatorname{sech}(\pi\xi)>s\}}\,d\xi\,du.
\]
For \(s=\pi e^{-L}\), integration over \(u\) gives \(\frac1{2\pi}\int (L-\log\cosh(\pi\xi))_+\,d\xi\). Its derivative with respect to \(L\) is \(\pi^{-2}\operatorname{arcosh}(e^L)\), and its value at \(L=0\) is zero, giving \(\mathcal F(L)\) exactly. Finally
\(\operatorname{arcosh}(e^L)=\sqrt{2L}(1+O(L))\) as \(L\downarrow0\) and \(=L+\log2+O(e^{-2L})\) as \(L\to\infty\). Integrating proves both asymptotics.

## Verification

The argument identifies the operator domain, trace-ideal bounds, uniform discretization error, exact continuum moment limit, compact-interval moment determinacy, absence of positive limit atoms, and the two sequential endpoint expansions. The accompanying `check.py` independently evaluates the Fourier-normalization integrals and the counting-profile derivative and edge ratios numerically, and checks elementary finite-section matrix properties. These numerical calculations are supplementary and do not certify infinite-dimensional statements.

## Relationship to prior work

The unweighted Hilbert matrix and its Mellin/Carleman spectral multiplier are classical. Otte's arXiv:2207.11029 treats hard finite-dimensional Hilbert sections and determinant Szegő asymptotics. Fedele's DOI:10.1007/s00020-019-2556-9 studies hard and scale-regularized Hankel spectral densities, including a cutoff \(e^{-(j+k)/N}\); the family here instead has the singular slow taper \((mn)^{-\varepsilon/2}\), for which infinitely many scales \(\varepsilon\log n\) contribute differently. Guo and Tang's arXiv:2607.28221 motivates renewed study of generalized Hilbert operators but its accessible abstract concerns symbol-dependent Hardy-space boundedness rather than this symmetric spectral limit. The theorem here supplies an explicit non-hard profile and its characteristic three-halves edge, not a new diagonalization of the classical Carleman operator.

## Limitations

This is a first-order fixed-threshold spectral law, not a uniform error bound in \(s\) or a double-scaling theorem near \(s=\pi\) or \(s=0\). It does not give eigenvalue-by-eigenvalue asymptotics for fixed \(\varepsilon\). The manuscript arXiv:2607.28221 was available by abstract only during the comparison, and an abstract general semiclassical weighted Wiener–Hopf theorem might encompass the operator class. The claimed formulas require no such theorem, but this broader bibliographic possibility is a residual originality risk.

## References

1. Y. Guo and P. Tang, *Generalized Hilbert operators on Hardy spaces*, arXiv:2607.28221 (first posted 30 July 2026), https://arxiv.org/abs/2607.28221.
2. P. Otte, *A Szegő Limit Theorem Related to the Hilbert Matrix*, arXiv:2207.11029 (first posted 22 July 2022), https://arxiv.org/abs/2207.11029.
3. E. Fedele, *The Spectral Density of Hankel Operators with Piecewise Continuous Symbols*, Integral Equations and Operator Theory 92 (2020), article 1, https://doi.org/10.1007/s00020-019-2556-9.
4. E. Preissmann and O. Lévêque, *On Generalized Weighted Hilbert Matrices*, arXiv:1303.1085 (2013), https://arxiv.org/abs/1303.1085.
