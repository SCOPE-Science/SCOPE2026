# Rare-event variance collapse in old-age power-weight recursive trees

## Finding

Let \(T_n^{(\alpha)}\) be the total root-to-vertex path length in a power-weight recursive tree, whose vertex \(j\ge2\) attaches independently to parent \(k<j\) with probability proportional to \(k^\alpha\). For each fixed \(\alpha<-1\), let
\[
Z_\alpha=\lim_{n\to\infty}\frac{T_n^{(\alpha)}-\mathbb ET_n^{(\alpha)}}{n}
\]
be its nondegenerate centered \(L^2\) limit, and put \(\sigma_\alpha^2=\operatorname{Var}(Z_\alpha)\).

**Theorem (extreme old-age variance and weak collapse).** As \(\alpha\to-\infty\),
\[
\boxed{\sigma_\alpha^2=18^\alpha+32^\alpha+o(32^\alpha).}
\]
Nevertheless,
\[
\boxed{Z_\alpha/\sigma_\alpha\longrightarrow0\quad\text{in probability},\qquad
\mathbb E(Z_\alpha/\sigma_\alpha)^2=1.}
\]
Thus the standardized fluctuations have no nondegenerate weak limit along this extreme-preference regime; their variance is carried by events of vanishing probability.

## Assumptions and scope

The tree starts with root vertex \(1\) of depth \(D_1=0\). Parent choices are mutually independent, and for every integer \(j\ge2\),
\[
\Pr(K_j=k)=\frac{k^\alpha}{\sum_{i=1}^{j-1}i^\alpha},\quad 1\le k<j,
\qquad D_j=D_{K_j}+1,
\qquad T_n^{(\alpha)}=\sum_{j=1}^nD_j.
\]
All limits in \(n\) are at a **fixed** exponent \(\alpha<-1\); subsequently the parameter \(\alpha\) tends to negative infinity. The theorem does not assert a joint \(n,\alpha\) limit with unrestricted relative speeds. The exact variance representation is a starting point established in the cited source, but the two-term exponent asymptotic and non-uniformly-integrable weak collapse are the claims proved below.

## Proof

For brevity write \(w_j=j^\alpha\), \(W_j=\sum_{k=1}^jw_k\), and \(p_j=w_j/W_j\). Define the weighted depth sum \(A_n=\sum_{j=1}^nw_jD_j\), the centered conditional innovation
\[
\xi_j=D_j-1-A_{j-1}/W_{j-1}\quad(j\ge2),
\]
and \(v_j=\mathbb E\xi_j^2\). The parent law gives \(\mathbb E(\xi_j\mid K_2,\ldots,K_{j-1})=0\), so the innovations are pairwise orthogonal. Centering the recursion for \(A_n\) and dividing by \(W_n\) gives
\[
\frac{A_n-\mathbb EA_n}{W_n}=\sum_{j=2}^np_j\xi_j.
\]
Also, for \(n\ge2\),
\[
\frac{T_n^{(\alpha)}-\mathbb ET_n^{(\alpha)}}n
=\sum_{j=2}^np_j\xi_j+\frac1n\sum_{j=2}^n(1-jp_j)\xi_j.
\]
For \(\alpha<-1\), \(p_j\le j^\alpha\), \(\sup_j jp_j<\infty\), and the innovation variances are bounded by \(\sum_{k=2}^\infty p_k<\infty\). The martingale series converges in \(L^2\), while the second sum tends to zero in \(L^2\) by orthogonality. Consequently
\[
Z_\alpha=\sum_{j=2}^\infty p_j\xi_j,
\qquad \sigma_\alpha^2=\sum_{j=3}^\infty p_j^2v_j.
\tag{1}
\]
Here \(\xi_2=0\), and the one-vertex Bernoulli depth representation, or equivalently total-variance decomposition, yields
\[
v_2=0,\qquad v_{j+1}=(1-p_j^2)v_j+p_j(1-p_j)\quad(j\ge2).
\tag{2}
\]
In particular, \(v_3=p_2(1-p_2)\).

Put \(t=-\alpha\), and let \(t\to\infty\). The elementary integral comparison
\[
\sum_{k=2}^\infty k^{-t}\le 2^{-t}+\int_2^\infty x^{-t}\,dx=O(2^{-t})
\]
shows uniformly over \(j\ge2\) that
\[
p_j=j^{-t}(1+O(2^{-t})),
\qquad 0\le v_j\le\sum_{k=2}^{j-1}p_k=O(2^{-t}).
\tag{3}
\]
For \(j=3\), equation (2) gives \(v_3=2^{-t}(1+O(2^{-t}))\). Therefore
\[
p_3^2v_3=18^{-t}(1+O(2^{-t}))
=18^{-t}+o(32^{-t}),
\tag{4}
\]
because \(36^{-t}=o(32^{-t})\). For \(j=4\), using (2) again,
\[
v_4=(1-p_3^2)v_3+p_3(1-p_3)
=2^{-t}(1+o(1)),
\]
since \(p_3/p_2\to0\). It follows that
\[
p_4^2v_4=32^{-t}(1+o(1)).
\tag{5}
\]
For the remaining indices, (3) and another integral comparison imply
\[
0\le\sum_{j=5}^\infty p_j^2v_j
\le C2^{-t}\sum_{j=5}^\infty j^{-2t}
=O(50^{-t})=o(32^{-t}).
\tag{6}
\]
Adding (4)--(6) to (1), and returning to \(\alpha=-t\), proves the claimed two-term expansion.

To establish the weak collapse, write
\[
Z_\alpha=p_3(B_\alpha-p_2)+R_\alpha,
\qquad B_\alpha=\mathbf1_{\{K_3=2\}}\sim\operatorname{Bernoulli}(p_2),
\qquad R_\alpha=\sum_{j=4}^\infty p_j\xi_j.
\]
Orthogonality and (5)--(6) give
\[
\mathbb ER_\alpha^2=32^\alpha+o(32^\alpha)
=o(\sigma_\alpha^2).
\]
Hence \(R_\alpha/\sigma_\alpha\to0\) in \(L^2\). The event \(B_\alpha=1\) has probability \(p_2\to0\). On its complement, the absolute value of \(p_3(B_\alpha-p_2)/\sigma_\alpha\) is asymptotic to \(\sqrt{p_2}\to0\). This proves convergence in probability to zero. Finally \(\mathbb EZ_\alpha=0\) and \(\mathbb EZ_\alpha^2=\sigma_\alpha^2>0\) for each fixed \(\alpha<-1\), proving the stated unit-variance identity and the failure of uniform integrability of squared standardized fluctuations. \(\square\)

## Verification

The accompanying `checker.py` independently enumerates all weighted parent vectors through seven vertices at three negative integer exponents, compares the resulting exact-rational total-path-length variances with the innovation formula, and evaluates the asymptotic ratio at four more-negative exponents using high-precision decimal arithmetic. The actual execution passed 49 assertions. These finite checks do not establish either infinite-limit statement, which rests on the bounds and orthogonality arguments above. Reproduce with `python3 checker.py` using the Python standard library.

## Relationship to prior work

Gałązka and Wdowicka (2026, arXiv:2610.00614v1) establish the \(n\)-scale martingale limit and exact variance representation for every fixed power exponent. Their Section 10 expressly lists the behavior of the variance coefficient as a function of the exponent, including its asymptotics, among open directions. The present theorem keeps that representation as known input and resolves the **extreme old-age** parameter asymptotic with the first two exponential terms. It also identifies a weak-limit pathology of the standardized global correction that the fixed-parameter variance statement alone does not describe.

Lyon and Mahmoud (2022) treat the marginal insertion-depth law of power-weight trees. A one-vertex depth distribution does not determine the cross-vertex covariance of total path length. Related weighted-tree profile results for growing cumulative weights do not directly cover the summable extreme-old-age regime \(\alpha<-1\). The present proof does not assert priority against unlocated broader distributional results.

## Limitations

The parameter asymptotic does not imply a central limit theorem in any triangular regime where \(\alpha\) changes with the tree size. The result concerns the centered total-path-length \(L^2\) limit, not the Wiener index or all vertex-level statistics. The numerical checks are finite. The comparison with earlier insertion-depth literature is supported by accessible abstracts and citations, not a complete new examination of every older full text; definitive historical priority remains subject to independent checking.

## References

1. M. Gałązka and H. Wdowicka, *Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations*, arXiv:2610.00614v1, first posted 2026-09-30, https://arxiv.org/html/2610.00614v1.
2. M. R. Lyon and H. M. Mahmoud, *Insertion depth in power-weight trees*, Information Processing Letters 176 (2022), 106227, https://doi.org/10.1016/j.ipl.2021.106227.
3. C. Sénizergues, *Geometry of weighted recursive trees*, 2021 (referenced for weighted-profile context in Gałązka--Wdowicka); no claim from this source is needed for the proof.
