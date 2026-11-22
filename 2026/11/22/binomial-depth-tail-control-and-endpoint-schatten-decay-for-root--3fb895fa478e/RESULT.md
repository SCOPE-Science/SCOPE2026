# Binomial depth-tail control and endpoint Schatten decay for rooted-tree Aluthge iterates

## Finding

**Theorem (depth-tail endpoint principle).** Let \(\mathfrak T=(V,E)\) be any finite or countable directed tree with a distinguished root \(o\) and all edges directed away from \(o\). For any \(0<p<\infty\), \(0<t<1\), and any complex weighted forward shift \(W\in\mathcal S_p(\ell^2(V))\), write \(W_n=\Delta_t^n(W)\), where \(\Delta_t(T)=|T|^tU|T|^{1-t}\) for the polar decomposition \(T=U|T|\). Define \(\rho_v=\|We_v\|\), \(a_v=\rho_v^p\), and let \(d(v)\) be the finite depth of a vertex. If \(B_n\sim\operatorname{Binomial}(n,t)\), then for every integer \(n\ge0\),

\[
\boxed{\|W_n\|_{\mathcal S_p}^p\le\sum_{v\in V}a_v\,\mathbb P(B_n\le d(v)).}
\]

Consequently \(\|W_n\|_{\mathcal S_p}\to0\), **without** assuming membership of \(W\) in any smaller Schatten class. More quantitatively, for every integer \(K\ge1\),

\[
\|W_n\|_{\mathcal S_p}^p\le
\|W\|_{\mathcal S_p}^p\,\mathbb P(B_n<K)
+\sum_{d(v)\ge K}a_v.
\]

In particular, for \(n\ge1\),

\[
\boxed{\|W_n\|_{\mathcal S_p}^p\le e^{-nt/8}\|W\|_{\mathcal S_p}^p+\sum_{d(v)>nt/2}\rho_v^p.}
\]

The convergence has **no distribution-free rate** over the unit sphere of finite-rank tree shifts: for every fixed \(n\ge0\),

\[
\sup_{\substack{\|W\|_{\mathcal S_p}=1\\ W\text{ a finite-rank forward path shift}}}\|\Delta_t^n(W)\|_{\mathcal S_p}=1.
\]

## Assumptions and scope

The complex Hilbert space has standard orthonormal basis \((e_v)_{v\in V}\). A weighted forward tree shift is specified by coefficients \(\lambda_{vu}\in\mathbb C\) for children \(u\in\operatorname{Chi}(v)\), and

\[
We_v=\sum_{u\in\operatorname{Chi}(v)}\lambda_{vu}e_u,
\qquad
\rho_v^2=\sum_{u\in\operatorname{Chi}(v)}|\lambda_{vu}|^2.
\]

There is a *unique* parent for each nonroot vertex; child sets may be empty or infinite. Every vertex is at some finite distance from the root. No injectivity, positive-weight, locally finite branching, or lower bound on nonzero weights is assumed. The Schatten \(p\) quasi-norm is understood also for \(0<p<1\). Since distinct columns of \(W\) have disjoint supports, \(W^*W\) is diagonal with entries \(\rho_v^2\), and

\[
\|W\|_{\mathcal S_p}^p=\sum_v\rho_v^p<\infty.
\]

For a finite tree, append zero edge weights if desired; no infinite-dimensional limit is needed for the finite case.

## Proof

**Step 1: a pointwise energy inequality.** Let \(T\) be an arbitrary bounded weighted shift on the same tree and put \(r_v=\|Te_v\|\). Its polar factor sends \(e_v\) to \(Te_v/r_v\) if \(r_v>0\) and to zero otherwise. The diagonal modulus thus gives the exact new edge weights

\[
\lambda'_{vu}=\begin{cases}
\lambda_{vu}(r_u/r_v)^t,&r_v>0,\\
0,&r_v=0.
\end{cases}
\]

When \(r_v>0\), introduce the probability coefficients \(\pi_{vu}=|\lambda_{vu}|^2/r_v^2\). With \(b_v=r_v^p\) and \(\mathcal Q b(v)=\sum_{u\in\operatorname{Chi}(v)}b_u\),

\[
\begin{aligned}
\|\Delta_t(T)e_v\|^p
&=r_v^{p(1-t)}\left(\sum_u\pi_{vu}r_u^{2t}\right)^{p/2}\\
&\le b_v^{1-t}\left(\sum_u b_u\right)^t\\
&\le(1-t)b_v+t\mathcal Q b(v).
\end{aligned}
\]

The first inequality uses \(r_u^p\le\sum_w r_w^p\) for each child and \(\sum_u\pi_{vu}=1\). The second is scalar weighted arithmetic-geometric mean, valid for any positive exponent \(p\). When \(r_v=0\), the new outgoing column is zero and the same inequality holds. The argument remains valid for countably many children by nonnegative-series convergence.

**Step 2: propagate the inequality.** Let \(a^{(n)}_v=\|W_ne_v\|^p\), with \(a^{(0)}_v=a_v\). Every \(W_n\) remains a tree shift by Step 1. The positive operator \(\mathcal Q:\ell^1(V)\to\ell^1(V)\) is contractive because every nonroot vertex has exactly one parent:

\[
\sum_v\mathcal Q b(v)=\sum_{u\ne o}b_u\le\sum_ub_u
\qquad (b\ge0).
\]

Writing \(P=(1-t)I+t\mathcal Q\), Step 1 yields \(a^{(n+1)}\le Pa^{(n)}\) coordinatewise; hence \(a^{(n)}\le P^na\). Because \(I\) and \(\mathcal Q\) commute,

\[
P^n=\sum_{k=0}^n\binom nk(1-t)^{n-k}t^k\mathcal Q^k.
\]

Unique parent chains give, with Tonelli's theorem for the nonnegative sums,

\[
\sum_v\mathcal Q^k a(v)=\sum_{d(u)\ge k}a_u.
\]

Sum the coordinatewise comparison and interchange the finite binomial sum with the nonnegative vertex sum. This proves the boxed inequality. In particular every iterate is in \(\mathcal S_p\) and its \(p\)-energy is nonincreasing.

**Step 3: the limit and quantitative tail.** For each fixed vertex \(v\), \(\mathbb P(B_n\le d(v))\to0\) since \(0<t<1\). Since each term is at most one and \(\sum_va_v<\infty\), dominated convergence for series proves \(\|W_n\|_{\mathcal S_p}^p\to0\). Split the vertex sum into depths below and at least \(K\) for the stated second bound. With \(K=\lfloor nt/2\rfloor+1\), the standard multiplicative Chernoff inequality gives \(\mathbb P(B_n<K)\le e^{-nt/8}\); \(d(v)\ge K\) is equivalent to \(d(v)>nt/2\). This proves the explicit exponential-plus-tail estimate.

**Step 4: sharp absence of a common rate.** On a path of \(L\) edges, give each of the \(L\) edges the constant positive weight \(L^{-1/p}\), and every later edge weight zero. The initial \(p\)-energy equals one. The formula in Step 1 shows that for each \(n<L\) exactly the last \(n\) formerly positive edges have vanished while the first \(L-n\) retain that weight. Thus

\[
\|\Delta_t^n(W)\|_{\mathcal S_p}^p=\frac{L-n}{L}.
\]

Letting \(L\to\infty\) at fixed \(n\), and using the general nonincrease of the \(p\)-energy, gives the asserted supremum.

## Verification

The companion standalone file `tree_aluthge_verifier.py` deterministically tests finite rooted trees with random complex and zero weights across \(p\in\{1/2,1,2,4\}\), \(t\in\{0.17,0.5,0.83\}\), and fourteen iteration counts. It compares the exact edge rule against the diagonal-modulus polar calculation, the numerical Schatten energy against the binomial-depth bound, and the path example against its exact formula. The script uses only the Python standard library and reports `ROOTED_ALUTHGE_DEPTH_DIAGNOSTICS_OK 30516`. This is a finite diagnostic, not a proof of the universal theorem; Steps 1–4 supply the infinite-dimensional proof.

## Relationship to prior work

Stanković [1, Proposition 5.8] proves endpoint Schatten convergence for classical **one-path unilateral** weighted shifts, with a binomial formula for successive scalar weights; [1, Corollary 5.9] also treats orthogonal sums of finite-dimensional blocks and such shifts. The present estimate replaces scalar path products with a noncommutative branching-column inequality and sums energy by unique-parent depth. It applies to rooted-tree shifts that are not unitarily equivalent to the direct-sum class.

To see that even the *equal-ideal endpoint* is a genuine extension, fix an exponent \(p>0\), and take a root with two children, each followed by an infinite ray. Give the root's two edges weight \(1/4\). At depth \(k\ge1\) on the left ray use the outgoing weight \(\alpha_k=(k+2)^{-1/p}(\log(k+3))^{-2/p}\), and on the right ray use \(2\alpha_k\). The resulting shift is injective and in \(\mathcal S_p\) because \(\sum_k\alpha_k^p<\infty\), but in no \(\mathcal S_q\) with \(0<q<p\), since \(\sum_k\alpha_k^q=\infty\). Its spectrum is \(\{0\}\), since a nonzero eigenvector would be zero first at the root and inductively at every vertex. However, \(W^*W\) and \(WW^*\) do not commute: the latter has a nonzero off-diagonal entry between the two children while the former has distinct diagonal entries there. Every orthogonal sum of classical unilateral weighted shifts has commuting \(W^*W\) and \(WW^*\); since this injective quasinilpotent operator cannot have a nonzero finite-dimensional reducing summand, it is not covered by [1, Corollary 5.9]. It also fails the smaller-class hypothesis of [1, Theorem 5.5].

Trepkowski [2, Theorem 4.1] establishes the one-step Aluthge edge-weight formula for directed trees, also in an unbounded setting, but does not give the iterated endpoint Schatten-depth estimate. Bala [3, Theorem 2.4] proves convergence in the operator norm for compact operators for the usual Aluthge transform; operator-norm convergence alone does not imply convergence in the same Schatten class. Altwaijry–Conde–Feki–Stanković [4] treats Schatten inequalities and equality cases for operator transforms, without the quantitative iterated rooted-tree depth law.

## Limitations

The theorem concerns **rooted, forward** directed trees, where every vertex has finite depth and a unique parent, and fixes \(0<t<1\). It does not assert the same result for rootless graphs, directed cycles, backward tree shifts, general weighted graphs with multiple parents, or the Duggal endpoint \(t=1\). The bound need not be attained on every branching tree and does not give a rate depending only on \(p\), \(t\), and the initial Schatten norm. No statement is made about arbitrary compact operators outside this shift class. Finite diagnostics have no logical role in proving the countable-tree limit.

## References

1. H. Stanković, *Singular values of iterated Aluthge transforms of compact operators*, arXiv:2611.07728v1, first posted 5 November 2026; especially Theorem 5.5, Remark 5.7, Proposition 5.8 and Corollary 5.9. https://arxiv.org/abs/2611.07728
2. J. Trepkowski, *Aluthge transforms of weighted shifts on directed trees*, arXiv:1401.4415v1, first posted 17 January 2014; especially Theorem 4.1. https://arxiv.org/abs/1401.4415
3. N. Bala, *The iterated Aluthge Transforms of compact operators*, arXiv:2602.07916v1, first posted 8 February 2026; Theorem 2.4. https://arxiv.org/abs/2602.07916
4. N. Altwaijry, C. Conde, K. Feki and H. Stanković, *Schatten \(p\)-norm related to some transforms of operators*, Communications on Pure and Applied Analysis 23 (2024), 1990–2004, DOI:10.3934/cpaa.2024078. https://doi.org/10.3934/cpaa.2024078
