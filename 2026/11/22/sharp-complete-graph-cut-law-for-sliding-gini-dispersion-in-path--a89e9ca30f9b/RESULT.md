# Sharp complete-graph cut law for sliding Gini dispersion in path variation

## Finding

Let \(m\ge2\) and \(n\ge 2m\). For a real sequence \(x=(x_1,\ldots,x_n)\), define the **full-window moving Gini mean difference** by
\[
(\mathcal G_mx)_i=\binom{m}{2}^{-1}\sum_{i\le p<q\le i+m-1}|x_q-x_p|,
\qquad 1\le i\le n-m+1.
\]
For any finite real sequence \(z\), write \(V(z)=\sum_j|z_{j+1}-z_j|\), with \(V\) of a one-point sequence equal to zero. The sharp two-input seminorm coefficient is
\[
\boxed{\sup_{V(x-y)>0}\frac{V(\mathcal G_mx-\mathcal G_my)}{V(x-y)}
=K_m=\frac{2\lfloor m^2/4\rfloor}{\binom{m}{2}}
=\begin{cases}\frac{m}{m-1},&m\text{ even},\\[2pt]
\frac{m+1}{m},&m\text{ odd}.
\end{cases}}
\]
The value is **attained by finite, strictly increasing inputs** for every \(m\ge2\) and every \(n\ge2m\). In particular, the values at window widths \(2,3,4,5,6\) are \(2,4/3,4/3,6/5,6/5\), and \(K_m\downarrow1\) along each parity subsequence.

More generally, for every **even, globally one-Lipschitz** function \(\phi:\mathbb R\to\mathbb R\), define
\[
(\mathcal F_{m,\phi}x)_i=\binom{m}{2}^{-1}
\sum_{i\le p<q\le i+m-1}\phi(x_q-x_p).
\]
For **all** \(n\ge m\), including short sequences, the universal estimate
\[
V(\mathcal F_{m,\phi}x-\mathcal F_{m,\phi}y)\le K_m V(x-y)
\]
holds. This is a uniform envelope over the family of pairwise-difference statistics, **not** a claim that each \(\phi\) individually has sharp coefficient \(K_m\). Absolute value saturates the envelope.

## Assumptions and scope

All signals are finite real open paths, windows are consecutive and complete without padding or wraparound, and both domain and codomain use **unweighted adjacent total variation**. The dispersion normalization is the mean over the \(\binom{m}{2}\) unordered pairs; dividing by \(m^2\) instead would change the coefficient. No stochastic assumptions, tie-breaking conventions, bounded input range, or differentiability of \(\phi\) are required. The only dimension restriction for the *upper bound* is \(n\ge m\); the attainment statement uses \(n\ge2m\).

## Proof

**1. Reduction to a single step.** Let \(H^{(j)}\in\mathbb R^n\) be zero on sites \(1,\ldots,j\) and one on sites \(j+1,\ldots,n\), for \(1\le j<n\). The maps \(\mathcal F_{m,\phi}\) are invariant under addition of constants. Every difference \(x-y\) decomposes as a constant plus
\[
\sum_{j=1}^{n-1}\delta_j H^{(j)},\qquad
\delta_j=(x_{j+1}-y_{j+1})-(x_j-y_j),\qquad
\sum_j|\delta_j|=V(x-y).
\]
Hence telescoping successive steps and the triangle inequality for \(V\) reduce the full two-input bound to proving
\(V(\mathcal F_{m,\phi}(z+tH^{(j)})-\mathcal F_{m,\phi}z)\le K_m|t|\) for every \(z,j,t\). When \(t=0\), this is immediate.

**2. A finite crossing-pair representation.** For \(t\ne0\), only pairs of indices that straddle the cut \(j\) change. Label the left observations in reverse spatial order \(L_a=z_{j-a+1}\) and the right observations \(R_b=z_{j+b}\), where these sites exist. For a crossing pair put
\[
\epsilon_{ab}=
\frac{\phi(R_b+t-L_a)-\phi(R_b-L_a)}{t},
\qquad |\epsilon_{ab}|\le1.
\]
Set \(\epsilon_{ab}=0\) if a labeled site is absent. A full window with \(\ell\) sites left of the cut and \(m-\ell\) right has output change \(tS_\ell/\binom{m}{2}\), where
\[
S_\ell=\sum_{\substack{a,b\ge1\\a\le\ell,\ b\le m-\ell}}\epsilon_{ab},
\qquad 0\le\ell\le m,
\qquad S_0=S_m=0.
\]
The actual sequence of output changes is a contiguous part of the canonical sequence \((S_m,S_{m-1},\ldots,S_0)\), padded by zeros whenever windows lie wholly on one side. Consequently its variation is bounded by \(|t|V(S_0,\ldots,S_m)/\binom{m}{2}\), even when the cut is near a signal endpoint.

**3. The complete-graph cut identity.** Pair \((a,b)\) is active precisely for \(a\le\ell\le m-b\), possible only when \(a+b\le m\). By the \(\ell_1\)-sign duality,
\[
\begin{aligned}
V(S_0,\ldots,S_m)
&=\max_{\sigma_0,\ldots,\sigma_{m-1}\in\{-1,1\}}
\sum_{\ell=0}^{m-1}\sigma_\ell(S_{\ell+1}-S_\ell)\\
&=\max_{\sigma}\sum_{a+b\le m}
\epsilon_{ab}(\sigma_{a-1}-\sigma_{m-b})\\
&\le\max_\sigma\sum_{a+b\le m}|\sigma_{a-1}-\sigma_{m-b}|.
\end{aligned}
\]
The index correspondence \((a,b)\mapsto(a-1,m-b)\) is a bijection between eligible crossing pairs and the edges \(0\le u<v\le m-1\) of the complete graph on \(m\) vertices. Each edge contributes two if its endpoints have opposite signs and zero otherwise. The sum is twice the cardinality of a cut, whose maximum is \(2\lfloor m^2/4\rfloor\), attained by a balanced cut. Thus \(V(S)\le2\lfloor m^2/4\rfloor\), proving the universal one-step and full two-input upper bounds without any ordering or differentiability hypothesis.

**4. Finite sharpness.** Take any \(n\ge2m\), \(x_k=k\) at every site, and \(y_k=k+1\) for \(k>m\), \(y_k=k\) otherwise. Then \(V(y-x)=1\). For every crossing pair, the right value exceeds the left value, so increasing the right half by one raises its absolute pairwise difference by exactly one. The window-change profile runs through
\[
\frac{1}{\binom{m}{2}}\bigl(0,\ (m-1),\ 2(m-2),\ \ldots,\
\ell(m-\ell),\ \ldots,\ (m-1),\ 0\bigr),
\]
with any additional output entries equal to zero. This nonnegative profile rises to \(\lfloor m^2/4\rfloor/\binom{m}{2}\) and then falls to zero. Therefore its variation is exactly \(K_m\); finite inputs attain the upper bound. The parity formulas follow by simplifying \(\lfloor m^2/4\rfloor\).

## Verification

The standalone pure-Python script `check_gini_window.py` checks: (i) all sign assignments to all crossing pairs for widths \(2\) through \(6\), a stronger finite test than checking feasible sample orderings; (ii) exact rational sharpness witnesses for widths \(2\) through \(32\) at two signal lengths each; (iii) 1200 seeded rational random two-input tests for Gini dispersion, 300 for a clipped-pair kernel, and 200 single-step tests. Run using `python3 check_gini_window.py` from the directory containing the extracted files. These finite checks are corroborative: the complete-graph argument proves the result for arbitrary dimensions.

## Relationship to prior work

Gini's mean difference is the classical mean absolute pairwise distance. Gerstenberger and Vogel (2014 preprint; later 2015 journal article) analyze statistical efficiency and robustness of the same normalized sample statistic. Gerstenberger, Vogel, and Wendler (2016) use it in change-point tests for dependent time series, including its pair-kernel Lipschitz property. Neither the examined finite-sample efficiency theory nor the time-series asymptotic tests provide the sharp adjacent-variation sensitivity of **overlapping local windows**. The present argument makes this additional combinatorial effect precise by reducing the sensitivity calculation to the maximum cut of a complete graph. Related local MAD, variance, median, and cyclic-output Gini-stability results concern different statistics or different variation metrics and do not imply the stated formula.

## Limitations

The sharpness construction requires at least \(2m\) input sites. For \(m\le n<2m\) the bound holds, but its exact optimal coefficient is not determined here. No analogous sharp formula is established for weighted pair contributions, irregularly spaced windows, cyclic windows, higher-dimensional image neighborhoods, or observation-mass weights. Even one-Lipschitz pair kernels may have strictly smaller optimal constants than \(K_m\). The source comparisons address accessible and indexed literature; historical equivalents in unindexed works cannot be categorically excluded.

## References

1. C. Gerstenberger and D. Vogel, *On the efficiency of Gini's mean difference*, arXiv:1405.5027, first submitted 20 May 2014, https://arxiv.org/abs/1405.5027 ; journal DOI https://doi.org/10.1007/s10260-015-0315-x .
2. C. Gerstenberger, D. Vogel, and M. Wendler, *Tests for scale changes based on pairwise differences*, arXiv:1611.04158, first submitted 13 November 2016, https://arxiv.org/abs/1611.04158 .
3. M. Zenga, M. Polisicchio, and F. Greselin, *The variance of Gini's mean difference and its estimators*, *Statistica* 64 (2004), 455–475, https://doi.org/10.6092/issn.1973-2201/50 .
