# Brownian maximum–area coupling for matching deficiency and edge count in random threshold graphs

## Finding

Let \(n\ge2\) be even. Sample \(n\) independent \(\operatorname{Uniform}[0,1]\) weights and join distinct vertices precisely when their weights sum to more than \(1\). Write \(E_n\) for its number of edges, \(\nu_n\) for its maximum-matching size, and \(D_n=n-2\nu_n\) for the number of vertices unpaired by a maximum matching. For standard Brownian motion \(B\) on \([0,1]\), let \(M=\max_{0\le t\le1}B(t)\) and \(A=\int_0^1 B(t)\,dt\). Then, along even \(n\to\infty\),

\[
\left(\frac{D_n}{\sqrt n},\frac{E_n-n(n-1)/4}{n^{3/2}}\right)
\xrightarrow{\ d\ } \left(M,-\frac12 A\right).
\]

The dependence is nontrivial: moment convergence yields

\[
\lim_{\substack{n\to\infty\\n\,\mathrm{even}}}
\frac{\operatorname{Cov}(D_n,E_n)}{n^2}=-\frac5{32},
\qquad
\lim_{\substack{n\to\infty\\n\,\mathrm{even}}}
\operatorname{Corr}(D_n,E_n)
=-\frac{5}{32\sqrt{(1-2/\pi)/12}}
\approx-0.897904199418.
\]

Also \(\operatorname{Cov}(D_n,E_n)<0\) strictly for every even \(n\ge2\). In particular, the limiting matching deficiency is half-normal and the centered edge count is Gaussian, but they are not asymptotically independent.

## Assumptions and scope

This is the independent, *symmetric* uniform-weight threshold-graph model, not an Erdős–Rényi graph or a reinforced graph. The vertex labels are immaterial to the two statistics. There is no conditioning on a matching or on the edge count. All joint weak limits and moment assertions here are along even graph orders; no assertion concerns other threshold distributions. The covariance normalization uses \(n^2\), not \(n^{3/2}\). The status of historical priority is qualified in the literature discussion below.

## Proof

**1. Exact binary encoding.** The known uniform binary creation-sequence representation of this graph model (Reilly–Scheinerman; Diaconis–Holmes–Janson) gives independent fair bits \(b_1,\ldots,b_{n-1}\). Starting with one vertex, bit \(b_j=0\) adds an isolated vertex; bit \(b_j=1\) adds a vertex adjacent to all \(j\) earlier vertices. Thus the edge count is exactly

\[
E_n=\sum_{j=1}^{n-1}j b_j,\qquad
\mathbb E E_n=\frac{n(n-1)}4,\qquad
\operatorname{Var}(E_n)=\frac{n(n-1)(2n-1)}{24}.
\]

Reverse the creation bits and set \(X_k=1-2b_{n-k}\) for \(1\le k\le n-1\); these are independent symmetric signs. Define \(S_0=0\), \(S_k=\sum_{i=1}^k X_i\), and \(H_n=\max_{0\le k\le n-1}S_k\). The random-walk maximum is the maximum excess of zeros over ones in any suffix of the original creation sequence. Ross's deterministic maximum-matching theorem for threshold graphs (2011, Proposition 4.3) gives

\[
\nu_n=\left\lfloor\frac{n-H_n}{2}\right\rfloor,
\quad\text{hence, for even }n,\quad
D_n=2\left\lceil\frac{H_n}{2}\right\rceil,
\qquad 0\le D_n-H_n\le1.
\]

Separately, substitute \(b_{n-k}=(1-X_k)/2\) into the exact edge formula and rearrange the double sum:

\[
E_n-\frac{n(n-1)}4
=-\frac12\sum_{k=1}^{n-1}(n-k)X_k
=-\frac12\sum_{k=1}^{n-1}S_k.
\]

This gives an **exact coupling of the two graph invariants by the same random walk**. It is the key ingredient beyond their separately known marginal descriptions.

**2. Joint weak limit.** By the functional Donsker invariance principle, the piecewise-linear interpolation of \(S_k/\sqrt n\) on grid \(k/n\) converges weakly in \(C[0,1]\) to standard Brownian motion. Complete its final interval by holding at \(S_{n-1}\), a modification of length \(1/n\). The supremum and time-integral are continuous under the supremum norm, while the latter integral differs from \(n^{-3/2}\sum_{k=1}^{n-1}S_k\) by a term vanishing in probability. The matching rounding error is bounded by \(1/\sqrt n\). The continuous-mapping theorem proves the displayed joint limit.

**3. Moment convergence.** The maximum satisfies \(0\le H_n\le\max_{k\le n-1}|S_k|\). Doob's \(L^4\) maximal inequality for the martingale \(S_k\), together with the fourth-moment formula for independent symmetric signs, gives \(\mathbb E H_n^4=O(n^2)\); the bounded rounding perturbation gives \(\mathbb E D_n^4=O(n^2)\). The centered edge sum is a weighted sum of independent symmetric signs, with \(\mathbb E(E_n-\mathbb E E_n)^4=O(n^6)\). The two normalized variables therefore have bounded fourth moments, and their products are uniformly integrable. Their means, second moments and covariance converge, as claimed.

**4. Exact Brownian covariance.** The standard reflection principle implies \(M\overset d=|N(0,1)|\), hence \(\operatorname{Var}(M)=1-2/\pi\); direct integration gives \(\operatorname{Var}(A)=1/3\). Put \(h(t)=\operatorname{Cov}(B(t),A)=t-t^2/2\). Cameron–Martin/Gaussian integration by parts gives

\[
\operatorname{Cov}(M,A)
=\mathbb E\left[\left.\frac{d}{d\epsilon}\right|_{\epsilon=0}
\sup_{t\in[0,1]}\{B(t)+\epsilon h(t)\}\right].
\]

Brownian motion has an almost surely unique maximizing time \(T\). The continuous deterministic perturbation has directional derivative \(h(T)\), bounded by \(\|h\|_\infty\), so differentiation under expectation is legitimate. The classical arcsine law says \(T\sim\operatorname{Beta}(1/2,1/2)\), with \(\mathbb ET=1/2\) and \(\mathbb ET^2=3/8\). Therefore

\[
\operatorname{Cov}(M,A)=\mathbb E(T-T^2/2)=\frac12-\frac3{16}=\frac5{16}.
\]

Multiplication by the edge component's factor \(-1/2\) gives \(-5/32\). Combining the nonzero covariance with the limiting variances \(1-2/\pi\) and \(1/12\) proves the correlation formula.

**5. Strict finite-order sign.** On any fixed creation word, replacing one bit \(0\) by \(1\) only adds edges. Thus \(D_n\), the deficiency of a maximum matching, is nonincreasing in each bit, while \(E_n=\sum j b_j\) is strictly increasing in each bit. For each independent bit, conditional monotonicity gives \(\operatorname{Cov}(D_n,b_j)\le0\). The last bit has strictly negative covariance: if every preceding bit is \(1\), changing that last bit from \(0\) to \(1\) changes a clique-plus-isolate into a clique, so for even \(n\) the deficiency falls from \(2\) to \(0\). Because this event has positive probability,
\[
\operatorname{Cov}(D_n,E_n)=\sum_{j=1}^{n-1}j\operatorname{Cov}(D_n,b_j)<0.
\]

## Verification

The standalone \(\texttt{verify.py}\) (Python standard library only; run with `python3 verify.py`) recomputes graph edges directly from every creation sequence through ten vertices and compares maximum matching sizes against an exhaustive dynamic-programming matching solver, rather than trusting the walk formula. It also checks finite exact edge/matching covariance signs through sixteen vertices and the known Ross matching-number distribution through fourteen vertices. Its completed run passed **46,820 exact assertions**. The Brownian integration identity is checked rationally; **finite enumeration is not a proof of the weak limit**, whose proof is in the preceding section.

## Relationship to prior work

Reilly and Scheinerman (2009) establish the uniform creation-sequence representation and perfect-matching event, together with edge statistics. Diaconis, Holmes and Janson (public arXiv version 2009) study the model and its graph limits. Ross (2011, Section 4) gives the exact marginal matching-number law and the deterministic maximum-tail-excess characterization; these are expressly **not** claimed as original here. The present statement concerns their **joint** fluctuations under one graph draw and the resulting explicitly negative, nonzero \(n^2\)-scale covariance. The inspected baseline results do not state or imply this numerical covariance without an additional joint coupling and Brownian maximum–area calculation.

Other work on strengthened Pólya threshold-graph matching probabilities or on greedy matchings of split graphs treats different dynamics or marginal events; it does not imply this statement for independent uniform vertex weights. A prior result about Hamiltonicity-conditioned random threshold graphs concerns a different rare conditional law, not this unconditional joint coupling. Related historical results outside the inspected sources could still subsume part of the statement; database-search absence is not a proof of novelty.

## Limitations

This theorem addresses only the symmetric uniform-weight threshold model and even-order limit. It does not establish a finite-size closed form for the covariance, an explicit finite joint probability mass function, an error rate for joint convergence, or any result for arbitrary weight distributions. The classical individual limits and the random-walk representation of matching deficiency are credited to existing work. The result has undergone a self-review only, not an independent external audit; priority against all historical literature is not exhaustively certified.

## References

1. E. Perez Reilly and E. R. Scheinerman, *Random Threshold Graphs*, Electronic Journal of Combinatorics 16(1), R130 (2009). https://doi.org/10.37236/219 . Public journal date 2009-10-31.
2. P. Diaconis, S. Holmes and S. Janson, *Threshold Graph Limits and Random Threshold Graphs*, Internet Mathematics 5 (2008), 267–320; public arXiv version 2009-08-17, https://arxiv.org/abs/0908.2448 .
3. C. Ross, *Further Properties of Random Threshold Graphs* (2011), especially Section 4, https://arxiv.org/abs/1111.7157 ; public arXiv date 2011-11-30.
4. Standard functional invariance principle, Brownian reflection principle, arcsine law and Cameron–Martin Gaussian integration by parts, used in their usual one-dimensional forms.
