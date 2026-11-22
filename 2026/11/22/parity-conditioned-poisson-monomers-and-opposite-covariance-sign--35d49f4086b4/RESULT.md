# Parity-conditioned Poisson monomers and opposite covariance signs in tripartite dimer gases

## Finding

Let \(K_{n,n,n}\) be the complete tripartite graph with three labelled parts, each containing \(n\ge2\) vertices. Every matching \(M\) receives weight \(\lambda_n^{|M|}\), where \(\lambda_n=n/c\) and \(c>0\) is fixed. Write \(U_{n,i}\) for the number of uncovered vertices (monomers) in part \(i\in\{1,2,3\}\), and \(R_n=U_{n,1}+U_{n,2}+U_{n,3}\). Put
\[
 x=3\sqrt{c/2},\qquad \varepsilon_n\equiv n\pmod 2.
\]
Let \(Q_{\varepsilon_n}\) be the law of three independent Poisson variables, each of mean \(x/3\), conditioned on their sum having parity \(\varepsilon_n\). Then
\[
 d_{\mathrm{TV}}\bigl(\mathcal L(U_{n,1},U_{n,2},U_{n,3}),Q_{\varepsilon_n}\bigr)=O_c(n^{-1}).
\]
The following nonasymptotic bounds hold. For even \(n\),
\[
 d_{\mathrm{TV}}\le\frac{3\bigl(x^2+3x\tanh x\bigr)}{4n}.
\]
For odd \(n=2m+1\ge3\),
\[
 d_{\mathrm{TV}}\le \frac{\sinh x}{x}\left[\frac1m+\frac{x\coth x-1}{2(2m+1)}+\frac{3\bigl(x^2+5x\coth x+3\bigr)}{8m}\right].
\]
In particular, for distinct parts \(i\ne j\),
\[
 \lim_{\substack{n\to\infty\\ n\,\mathrm{even}}}\operatorname{Cov}(U_{n,i},U_{n,j})=\frac{x^2}{9\cosh^2 x}>0,
\qquad
 \lim_{\substack{n\to\infty\\ n\,\mathrm{odd}}}\operatorname{Cov}(U_{n,i},U_{n,j})=-\frac{x^2}{9\sinh^2 x}<0.
\]
The same limits hold for \(n^2\operatorname{Cov}(\mathbf1_{v\text{ monomer}},\mathbf1_{w\text{ monomer}})\), for **any two distinct vertices** \(v,w\), whether in the same part or in different parts. Thus the critical near-perfect-matching window has a genuine parity reversal of its leading two-site dependence.

## Assumptions and scope

The graph is simple and finite, with all edges between different parts present and no within-part edges. Matchings are sets of pairwise vertex-disjoint edges. All edge activities are the same \(n/c\); uncovered vertices have unit activity. No limits are taken in \(c\): each statement holds for every fixed \(c>0\). Convergence and covariance limits are taken separately through even and odd integers \(n\), with all labelled sites fixed in their respective parts as \(n\) grows. The total-variation bounds can exceed one for small \(n\) or large \(c\), but remain correct inequalities. The result is an equilibrium finite-size scaling theorem, not a thermodynamic phase transition.

## Proof

**Exact finite matching count.** For \(u=(u_1,u_2,u_3)\) with \(0\le u_i\le n\), set
\[
 a_{12}=\frac{n-u_1-u_2+u_3}{2},\quad
 a_{23}=\frac{n+u_1-u_2-u_3}{2},\quad
 a_{31}=\frac{n-u_1+u_2-u_3}{2}.
\]
If all \(a_{ij}\) are nonnegative integers, the number of labelled matchings with monomer count vector \(u\) is exactly
\[
 C_n(u)=\frac{(n!)^3}{u_1!u_2!u_3!\,a_{12}!a_{23}!a_{31}!};
\]
otherwise the count is zero. To obtain this formula, choose uncovered vertices in each part, partition the remaining vertices by partner part, then bijectively pair each of the three partner classes. Every matching has one unique construction.

Write \(\epsilon=n\bmod2\). A nonzero count has \(\sum_i u_i=2j+\epsilon\) for an integer \(j\ge0\) (the number of dimers missing relative to a maximum matching). If \(n=2m\) then \(a_{12}=m+u_3-j\), cyclically, and the number of maximum matchings equals \(C_n(0,0,0)=(n!)^3/(m!)^3\). If \(n=2m+1\) then the same expression \(a_{12}=m+u_3-j\) holds and the total maximum-matching count equals \(3(n!)^3/[(m!)^2(m+1)!]\). These maximum matching formulas agree with the known complete-tripartite maximum-matching sequence, but the near-perfect law below is not inferred from the maximum count alone.

**Dominated factorial ratios.** For \(m\ge1\), define \(f_m(d)=[m!/(m-d)!]/m^d\) for integers \(d\le m\), using factorials at nonnegative arguments, and set \(f_m(d)=0\) when \(d>m\). For nonnegative \(d\le m\), \(f_m(d)=\prod_{r=0}^{d-1}(1-r/m)\); for \(d=-v<0\), \(f_m(-v)=\prod_{r=1}^v(1+r/m)^{-1}\). In every case \(0\le f_m(d)\le1\), and
\[
 1-f_m(d)\le\begin{cases}d(d-1)/(2m),&d\ge0,\\v(v+1)/(2m),&d=-v<0.\end{cases}
\]
(The first bound also holds when \(d>m\), by its right side being at least one.) Extend every inadmissible finite count by zero.

Let \(B_n(u)\) be the weight \(C_n(u)\lambda_n^{-j}\) divided by the **total number** of maximum matchings. If \(n=2m\), define \(b(u)=(c/2)^j/(u_1!u_2!u_3!)\) for total monomer count \(2j\), and zero otherwise. Then
\[
 B_n(u)=b(u)\prod_{i=1}^3 f_m(j-u_i),\qquad 0\le B_n(u)\le b(u).
\]
If \(n=2m+1\), define \(b(u)=(c/2)^j/[3u_1!u_2!u_3!]\) for total monomer count \(2j+1\), and zero otherwise. Then
\[
 B_n(u)=b(u)\left(1+\frac1m\right)\left(\frac{2m}{2m+1}\right)^j\prod_{i=1}^3 f_m(j-u_i).
\]
For admissible vectors these are exact algebraic identities; when an edge count is negative, the corresponding \(f_m\) factor vanishes, as required by the zero-count convention. An admissible vector can have \(j>m\). In both cases the sum of \(B_n\) over the \(j=0\) sector is one, so \(S_n=\sum_u B_n(u)\ge1\). Moreover, for each fixed \(u\) of the required parity, \(B_n(u)\to b(u)\) along the corresponding parity subsequence.

**Explicit total variation.** In the even case \(d_i=j-u_i\) lies between \(-j\) and \(j\). The elementary product bound and \(1-\prod_i f_i\le\sum_i(1-f_i)\) give
\[
 0\le b(u)-B_n(u)\le\frac{3j(j+1)}{2m}\,b(u),
\]
including excluded vectors with \(j>m\). Set \(T=\sum_u b(u)=\cosh x\). Since \(B_n\le b\), the normalized laws obey \(d_{\mathrm{TV}}\le(T-S_n)/T\). The sum \(\sum_{j\ge0}j(j+1)x^{2j}/(2j)!=(x^2\cosh x+3x\sinh x)/4\) gives the advertised bound.

In the odd case \(d_i\in[-j-1,j]\), and the factor \((2m/(2m+1))^j\) differs from one by at most \(j/(2m+1)\). It follows that
\[
 |B_n(u)-b(u)|\le b(u)\left[\frac1m+\frac{j}{2m+1}+\frac{3(j+1)(j+2)}{2m}\right].
\]
Again this includes excluded vectors. Here \(T=\sum b(u)=\sinh x/x\). For the odd-conditioned Poisson sum \(R\), \(\mathbb ER=x\coth x\) and \(\mathbb E[R(R-1)]=x^2\). Consequently the \(b\)-normalized means of \(j\) and \((j+1)(j+2)\) are \((x\coth x-1)/2\) and \((x^2+5x\coth x+3)/4\), respectively. For nonnegative unnormalized weights \(B_n,b\) and \(S_n\ge1\), \(d_{\mathrm{TV}}(B_n/S_n,b/T)\le\sum_u|B_n-b|\). Summing proves the odd bound. Finally, normalization of \(b\) gives exactly the three independent Poisson variables conditioned on the required total parity.

**Covariance limits.** The estimates above also bound every finite normalized probability by a constant depending only on \(c\) times a factorially decaying \(b(u)\). Therefore convergence extends to all polynomial moments, not just bounded tests. The conditioned total \(R\) satisfies
\[
 \mathbb ER=\begin{cases}x\tanh x,&\text{even},\\x\coth x,&\text{odd},\end{cases}
 \qquad\mathbb E[R(R-1)]=x^2.
\]
Conditional on \(R\), the limiting species-count vector is multinomial with equal probabilities \(1/3\); hence for distinct species \(i,j\), \(\mathbb EU_i=\mathbb ER/3\), \(\mathbb E[U_iU_j]=x^2/9\). This gives \((x^2-(\mathbb ER)^2)/9\), the two strictly opposite covariance limits.

For distinct labelled vertices in different parts, exchangeability gives \(\mathbb E[I_vI_w]=\mathbb E[U_iU_j]/n^2\); for two vertices of one part it gives \(\mathbb E[I_vI_w]=\mathbb E[U_i(U_i-1)]/[n(n-1)]\). Under the limiting multinomial law, \(\mathbb E[U_i(U_i-1)]=x^2/9\). In both geometries, multiplying the connected covariance by \(n^2\) yields the same limit. This finishes the proof.

## Verification

A standalone pure-Python script, `verify_tripartite.py`, verifies the exact labelled matching formula against independent graph-state recursion for \(1\le n\le5\), checks the known perfect/near-perfect matching counts, and evaluates the stated finite total-variation inequalities over several activities and sizes. It also checks the predicted eventual signs numerically at \(n=80,81\) for \(c=2\). These finite tests are supplementary; the preceding factorial-ratio argument proves the assertions for every permitted \(n\) and \(c\).

Run with `python3 verify_tripartite.py` (standard library only). The expected last status begins with `TRIPARTITE_CHECKS_PASSED`.

## Relationship to prior work

The original Heilmann–Lieb monomer-dimer framework and its matching recursions establish the equilibrium setting and absence of positive-fugacity phase transitions in thermodynamic models. Subsequent mean-field work proves laws of large numbers and central limit theorems for models on complete graphs at different density scales, including imitative interactions; those theorems neither state the balanced complete-tripartite parity-conditioned near-perfect law nor its two-point sign reversal. The published maximum-matching sequence for \(K_{n,n,n}\) gives precisely the \(j=0\) counts used above, but not the joint near-perfect monomer distribution. A 2025 study concerns path-trees of \(K_{1,s,t}\), which are different from balanced \(K_{n,n,n}\) and their Gibbs monomer counts. Relevant previously recorded results on complete **bipartite** monomer–dimer models have an exact shore-difference constraint; no such constraint holds in this three-part setting, and the present proof uses genuinely three-variable factorial sums. Related results on **irreversible** tripartite dimer parking describe non-equilibrium jamming rather than the Gibbs distribution. These comparisons support a provisional originality assessment, not an independent historical-priority guarantee.

## Limitations

The theorem concerns fixed \(c>0\) and uniform activities on exactly balanced three-part graphs. It does not give uniform error estimates as \(c\) varies with \(n\), characterize arbitrary unbalanced multipartite graphs, or establish finite-size covariance signs for every \(n\). The even and odd asymptotic regimes must not be conflated. General matching-polynomial identities and unexamined historical sources may contain equivalent specializations; the literature comparison is bounded and no independent validation has been performed.

## References

1. O. J. Heilmann and E. H. Lieb, “Monomers and Dimers,” *Physical Review Letters* **24**, 1412–1414 (publicly published 1970-06-22), DOI: https://doi.org/10.1103/PhysRevLett.24.1412.
2. D. Alberici, P. Contucci, M. Fedele and E. Mingione, “Limit theorems for monomer-dimer mean-field models with attractive potential,” arXiv:1506.04241 (publicly posted 2015-06-13), https://arxiv.org/abs/1506.04241.
3. D. Alberici, P. Contucci and E. Mingione, “Mean-Field Monomer-Dimer models. A review,” arXiv:1612.09181 (2016-12-29), lawful full-text review https://www.dm.unibo.it/~contucci/public_html/Research/acmr.pdf.
4. OEIS A297527, “Number of maximum matchings in the complete tripartite graph \(K_{n,n,n}\),” https://oeis.org/A297527 (initial entry 2017-12-31; subsequent formulas dated 2018-01-01).
5. Y. Ma, “The Matching Polynomial of the Path-Tree of the Complete Tripartite Graph \(K_{1,s,t}\),” *Applied Mathematics* **16** (2025), 526–534, https://doi.org/10.4236/am.2025.167030.
