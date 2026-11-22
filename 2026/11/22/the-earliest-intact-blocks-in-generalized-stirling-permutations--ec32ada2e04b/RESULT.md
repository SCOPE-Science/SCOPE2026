# The earliest intact blocks in generalized Stirling permutations form a Poisson point process

## Finding

Fix an integer \(r\ge2\). Let \(\sigma_n\) be uniform among the \(r\)-Stirling permutations on the multiset containing exactly \(r\) copies of each label \(1,\ldots,n\). A label is **intact** if all its copies form one consecutive run. Write \(I_{n,i}\) for its intactness indicator and define
\[
\alpha_r=\frac{r-1}{r},\qquad
b_n=n^{\alpha_r/(1+\alpha_r)}=n^{(r-1)/(2r-1)},\qquad
\Xi_n=\sum_{i=1}^n I_{n,i}\,\delta_{i/b_n}.
\]
As \(n\to\infty\), with \(r\) fixed, \(\Xi_n\) converges vaguely in distribution on \([0,\infty)\) to a Poisson point process with intensity \(x^{\alpha_r}\,dx\). In particular, if \(M_n=\min\{i:I_{n,i}=1\}\), then for every \(t\ge0\),
\[
\boxed{\ \lim_{n\to\infty}\Pr\{M_n/b_n>t\}
=\exp\left(-\frac{t^{1+\alpha_r}}{1+\alpha_r}\right).\ }
\]
The same point-process limit determines all successive intact birth labels. For each fixed positive integer \(k\), if \(M_{n,k}\) denotes the \(k\)-th smallest intact label (with \(+\infty\) when necessary), then jointly for any fixed number of ranks,
\[
\frac{M_{n,k}}{b_n}\ \Rightarrow\
\bigl((1+\alpha_r)G_k\bigr)^{1/(1+\alpha_r)},
\]
where \(G_k\) are the successive arrival times of a unit-rate Poisson process, so \(G_k\sim\operatorname{Gamma}(k,1)\). The convergence is not asserted uniformly for growing ranks.

## Assumptions and scope

An \(r\)-Stirling permutation is a word containing \(r\) copies of each integer \(1,\ldots,n\), with each letter lying strictly between two consecutive copies of \(i\) larger than \(i\). All valid words have equal probability. The integer \(r\ge2\) remains fixed; only \(n\to\infty\). A label is intact precisely when *all* \(r\) copies remain consecutive, not when an arbitrary adjacent pair forms a plateau, and not when a maximal enclosing block has a specified size. The deterministic newest label is always intact. The first intact label exists for every \(n\ge1\).

The assertion concerns a rare early-label window of width \(n^{(r-1)/(2r-1)}\), distinct from a macroscopic birth-prefix window of width \(n\). It claims no total-variation bound or rate of convergence.

## Proof

**1. Growth representation and exact inclusion probabilities.** Start with the word consisting of \(r\) copies of \(1\). At stage \(k+1\), insert the contiguous run of \(r\) copies of the new largest letter \(k+1\) into one of \(rk+1\) word gaps, uniformly. Every word has a unique predecessor obtained by deleting its largest-letter run; thus the process is uniform on the valid words.

For a finite set \(S\subseteq\{1,\ldots,n\}\), let \(c_\ell(S)=|S\cap\{1,\ldots,\ell\}|\). Conditional on every marked label born by stage \(\ell\) still being intact, exactly \((r-1)c_\ell(S)\) gaps would break one of their intact runs. Such internal gaps are disjoint. Once a run has been broken it cannot become intact again, since later insertions never remove letters. Therefore
\[
\boxed{\ \Pr\{I_{n,i}=1\text{ for all }i\in S\}
=\prod_{\ell=1}^{n-1}\left(1-\frac{(r-1)c_\ell(S)}{r\ell+1}\right).\ }\tag{1}
\]
The empty set gives probability one; the final label contributes no survival factor. All factors are nonnegative, including when many labels are marked.

**2. Single-label asymptotics and the unique rare-event scale.** With \(\alpha=\alpha_r\), (1) gives
\[
\begin{aligned}
p_{n,i}:=\Pr\{I_{n,i}=1\}
&=\prod_{\ell=i}^{n-1}\frac{r\ell-r+2}{r\ell+1}\\
&=\frac{\Gamma(n-1+2/r)\,\Gamma(i+1/r)}
{\Gamma(i-1+2/r)\,\Gamma(n+1/r)}.
\end{aligned}\tag{2}
\]
By standard fixed-shift Gamma-ratio estimates, uniformly as \(i\to\infty\) with \(i\le n\),
\[
p_{n,i}=(i/n)^\alpha\bigl(1+O_r(i^{-1}+n^{-1})\bigr).
\tag{3}
\]
The same estimates, with finitely many small indices absorbed into the constant, imply \(p_{n,i}\le C_r(i/n)^\alpha\) for every \(n\ge i\ge1\).

Consequently for each fixed \(t\ge0\), using the proposed \(b_n\),
\[
\sum_{i\le t b_n}p_{n,i}\longrightarrow
\int_0^t x^\alpha\,dx=\frac{t^{\alpha+1}}{\alpha+1},
\tag{4}
\]
where \(b_n^{1+\alpha}/n^\alpha=1\). No other polynomial scale gives a finite, nonzero count of first intact labels: its expectation is of order \(m^{1+\alpha}/n^\alpha\) for an early prefix of length \(m\to\infty\), \(m=o(n)\).

**3. Joint rare events factorize.** For distinct ordered \(i_1<\cdots<i_s\), set \(h_\ell=(r-1)/(r\ell+1)\). Formula (1) is \(\prod_{\ell=1}^{n-1}(1-c_\ell(S)h_\ell)\), whereas \(\prod_{j=1}^s p_{n,i_j}\) equals \(\prod_{\ell=1}^{n-1}(1-h_\ell)^{c_\ell(S)}\). Fix \(0<\varepsilon<T<\infty\) and \(s\). If every \(i_j\in[\varepsilon b_n,Tb_n]\), then, for large \(n\), Taylor expansion of the logarithm with \(0\le c_\ell(S)\le s\) gives
\[
\left|\log\frac{\Pr\{I_{n,i_j}=1\text{ for all }j\}}
{\prod_{j=1}^s p_{n,i_j}}\right|
\le C_{r,s}\sum_{\ell\ge\varepsilon b_n}\ell^{-2}
=O_{r,s,\varepsilon}(b_n^{-1})=o(1).
\tag{5}
\]
The approximation is uniform over all distinct labels in that window; their separation need not grow.

There is also an all-index domination bound. Bernoulli's inequality yields \(1-ch\le(1-h)^c\) for integer \(c\ge0\), whenever \(ch\le1\). Every factor in (1) satisfies this condition, so
\[
\Pr\{I_{n,i}=1\text{ for all }i\in S\}
\le\prod_{i\in S}p_{n,i}.\tag{6}
\]
This inequality controls every order of the rare-event expansion and the small-label boundary, without an independence assumption.

**4. Laplace functional.** Let \(f\) be any continuous, nonnegative function with compact support in \([0,T]\). Put \(u_{n,i}=1-e^{-f(i/b_n)}\) and \(A_n=\sum_i u_{n,i}p_{n,i}\). By (3) and a Riemann-sum argument, \(A_n\to A:=\int_0^T(1-e^{-f(x)})x^\alpha\,dx\).

Expand \(\mathbb E\exp(-\langle f,\Xi_n\rangle)\) by multiplying \(\prod_i(1-u_{n,i}I_{n,i})\). The term with \(s\) distinct specified labels, divided by \(s!\), is nonnegative in magnitude and by (6) bounded by \(A_n^s/s!\). For each fixed \(s\), (5) shows that the portion with all scaled labels at least \(\varepsilon\) is asymptotic to its independent-Bernoulli counterpart. Terms containing an index below \(\varepsilon b_n\) contribute at most \((\sum_{i<\varepsilon b_n}p_{n,i})A_n^{s-1}/(s-1)!\), which tends by (4) to at most \(\varepsilon^{1+\alpha}A^{s-1}/((1+\alpha)(s-1)!)\). Letting \(\varepsilon\downarrow0\) proves that the full order-\(s\) coefficient converges to \(A^s/s!\); repeated indices in the independent counterpart contribute \(o(1)\), as \(\max_{i\le Tb_n}p_{n,i}\to0\). The uniform summable majorant \(C^s/s!\) permits exchanging the limit and alternating sum. Hence
\[
\lim_{n\to\infty}\mathbb E e^{-\langle f,\Xi_n\rangle}
=e^{-A}
=\exp\left(-\int_0^\infty(1-e^{-f(x)})x^\alpha\,dx\right),
\]
which is the Laplace functional of the stated Poisson point process. Thus \(\Xi_n\) converges vaguely in distribution.

**5. Ordered labels.** The limiting point process has a continuous intensity and cumulative intensity \(\Lambda(t)=t^{\alpha+1}/(\alpha+1)\), with \(\Lambda(t)\to\infty\) as \(t\to\infty\). Its count on \([0,t]\) is Poisson with mean \(\Lambda(t)\), and it almost surely has no atom at any fixed endpoint. Convergence of such counts gives the survival law for the first label and for every fixed subsequent rank. Applying the monotone map \(t\mapsto\Lambda(t)\) transforms the limiting points into a rate-one Poisson process, proving the Gamma arrival-time description.

## Verification

`CHECK.py` uses only the Python standard library. It enumerates all valid words via their unique insertion histories for several small multiplicities and sizes. It checks the event that each selected subset of labels remains intact against the exact rational product (1), checks the full word counts, and numerically checks the early-prefix expectation scale derived from (2). A completed run passed 288 exact or numerical assertions. The point-process convergence is established by Steps 1–5, **not** by finite enumeration, numerical checks, or simulations.

## Relationship to prior work

Janson, Kuba and Panholzer (2008) establish uniform insertion and increasing-tree representations for generalized Stirling permutations, and study aggregate permutation statistics. Kuba and Panholzer (2010) study specified-block sizes and distances between repeated copies, including one-label distributions and related tree statistics. Haglund and Visontai (2012) establish label-indexed multivariate generating polynomials and stability for plateaux and descents; these already encode much of the finite distributional dependence. A more recent birth-label covariance-kernel result also gives the exact joint inclusion product (1), together with a macroscopic \(\Theta(n)\) age-prefix covariance law. **The inclusion identity and finite multivariate encoding are therefore not claimed as original.** Their stated results do not determine the Poisson rare-event process at the smaller \(n^{(r-1)/(2r-1)}\) scale or the extreme-label Weibull law. Results about earliest surviving leaves of uniform recursive trees concern a different attachment model and a square-root, rather than this multiplicity-dependent, scale.

## Limitations

This is a fixed-\(r\) result. No assertion concerns growing multiplicity, quantitative error rates, total-variation convergence of an unbounded vector, or a central limit theorem for global plateau counts. The derivation uses a known exact inclusion formula; the contribution is the rare-age Poisson process and its scale. Earlier general rare-event or increasing-tree theorems may contain an equivalent specialization; mathematical priority requires independent confirmation. The review is not an independent audit.

## References

1. S. Janson, M. Kuba, and A. Panholzer, *Generalized Stirling permutations, families of increasing trees and urn models*, first public arXiv posting 2008-05-27, https://arxiv.org/abs/0805.4084 .
2. M. Kuba and A. Panholzer, *Analysis of Statistics for Generalized Stirling Permutations*, public author manuscript dated 2010-06-04, https://www.dmg.tuwien.ac.at/kuba/preprintStirblock.pdf .
3. J. Haglund and M. Visontai, *Stable multivariate Eulerian polynomials and generalized Stirling permutations*, European Journal of Combinatorics 33 (2012), 477–487, https://doi.org/10.1016/j.ejc.2011.10.007 ; author-accessible copy https://sites.math.washington.edu/~billey/classes/561.fall.2021/past.articles/haglund.vis.2012.pdf .
4. *Age-resolved covariance kernel for intact blocks in random Stirling permutations*, publicly available mathematical research record (2026), with a complete exact joint-survival formula and a macroscopic covariance-kernel theorem. Its finite formula is acknowledged rather than asserted to be new.
