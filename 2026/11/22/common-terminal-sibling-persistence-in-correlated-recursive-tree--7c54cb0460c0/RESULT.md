# Common terminal-sibling persistence in correlated recursive trees

## Finding

**Theorem (exact concordance kernel and square-root alignment crossover).** Let \(n\ge3\) and \(0\le r\le1\). Form two rooted uniform recursive trees on birth labels \(1,\ldots,n\). At the birth of each \(k\ge2\), independently across \(k\), the two trees copy one common uniformly chosen parent with probability \(r\); with probability \(1-r\), they choose their parents independently and uniformly among labels \(1,\ldots,k-1\). A *terminal sibling pair* is an unordered pair of distinct vertices with no children and with a common parent. Let \(H_n(r)\) count label pairs that are terminal siblings in **both** trees (the two parent labels need not match). Let \(B_n(r)\) count such shared terminal sibling pairs whose parent labels **differ** between the trees.

For \(2\le i<j\le n\), put \(a=i-1\), \(b=j-1\), and
\[
\begin{aligned}
T_{ij}(r)&=\frac{r^2}{b}+\frac{r(1-r)}{ab}+\frac{1-r}{b^2},\\
U_{ij}(r)&=\prod_{d=i}^{j-2}\left(1-\frac{2-r}{d}+\frac{1-r}{d^2}\right),\\
V_j(r)&=\prod_{d=j}^{n-1}\left(1-\frac{4-2r}{d}+\frac{4(1-r)}{d^2}\right).
\end{aligned}
\]
Empty products equal one. The exact finite-size expectations are
\[
\boxed{\begin{aligned}
\mathbb E H_n(r)&=\sum_{2\le i<j\le n}T_{ij}(r)U_{ij}(r)V_j(r),\\
\mathbb E B_n(r)&=(1-r)^2\sum_{2\le i<j\le n}\frac{i-2}{(i-1)(j-1)^2}U_{ij}(r)V_j(r).
\end{aligned}}
\]
In particular,
\[
\boxed{\mathbb E H_n(0)=\frac{n}{12(n-2)},\qquad \mathbb E H_n(1)=\frac n6.}
\]
For every fixed \(r\in(0,1]\),
\[
\boxed{\lim_{n\to\infty}\frac{\mathbb E H_n(r)}n=\frac{r^2}{(3-r)(5-2r)}.}
\]
For fixed \(r\in[0,1]\), the mismatched-parent expectation stays bounded and in fact
\[
\boxed{\lim_{n\to\infty}\mathbb E B_n(r)=\frac{(1-r)^2}{(3-r)(4-2r)}.}
\]
Finally, for **every** sequence \(r_n\to0\), the following two-term expansion, with two separate error terms, holds:
\[
\boxed{\mathbb E H_n(r_n)=n r_n^2\left(\frac1{15}+o(1)\right)+\frac1{12}+o(1).}
\]
Hence if \(\sqrt n\,r_n\to\lambda\in[0,\infty)\), then \(\mathbb E H_n(r_n)\to1/12+\lambda^2/15\), whereas if \(\sqrt n\,r_n\to\infty\) and \(r_n\to0\), then \(\mathbb E H_n(r_n)\sim nr_n^2/15\). These are **expectation** statements; no concentration, Poisson limit, or statistical detection threshold is asserted.

## Assumptions and scope

The trees have the same birth labels and a deterministic root \(1\), and their parent-choice vectors are coupled independently at each birth. Every marginal parent choice is uniform and independent across birth times. The parameter \(r\) is the actual mixing probability for sharing a parent draw, not the marginal probability of equality of two parent labels (the latter also includes chance agreement under independent draws). A terminal vertex has outdegree zero in the rooted tree; the root is not treated as an undirected degree-one leaf. The common-pair statistic counts a pair at most once, even if its parent has three or more terminal children. The parameter \(r\) may depend on \(n\) only in the displayed vanishing-alignment asymptotics.

## Proof

**1. Paired-parent equality.** Let \(P_k^{(1)},P_k^{(2)}\) denote the two parents selected for birth label \(k\). For any \(x,y<k\) and \(d=k-1\), their law is
\[
\Pr(P_k^{(1)}=x,P_k^{(2)}=y)=\frac{r\mathbf1_{\{x=y\}}}{d}+\frac{1-r}{d^2}.
\]
Since the paired choices at births \(i\) and \(j\) are independent, summing over the possible ordered pair of shared parent values \((x,y)\in\{1,\ldots,i-1\}^2\) yields
\[
\begin{aligned}
&\Pr(P_i^{(1)}=P_j^{(1)},P_i^{(2)}=P_j^{(2)})\\
&=a\left(\frac r a+\frac{1-r}{a^2}\right)\left(\frac r b+\frac{1-r}{b^2}\right)+a(a-1)\frac{(1-r)^2}{a^2b^2}\\
&=T_{ij}(r).
\end{aligned}
\]
The contribution from \(x\ne y\), namely \((a-1)(1-r)^2/(ab^2)\), is exactly the probability that the two sibling pairs have *different* parents. Both parents at birth \(j\) must be earlier than \(i\), so the sibling event cannot itself make \(i\) nonterminal.

**2. Persistence of terminality.** Every birth strictly between \(i\) and \(j\) must avoid \(i\) as parent in both trees. With \(d=k-1\) eligible parents, this occurs with probability
\[
u_d(r)=r\left(1-\frac1d\right)+(1-r)\left(1-\frac1d\right)^2
=1-\frac{2-r}{d}+\frac{1-r}{d^2}.
\]
Every birth after \(j\) must avoid both \(i\) and \(j\) in both trees; its probability is
\[
v_d(r)=r\left(1-\frac2d\right)+(1-r)\left(1-\frac2d\right)^2
=1-\frac{4-2r}{d}+\frac{4(1-r)}{d^2}.
\]
All these avoidance events are independent across births and independent of the paired-parent event at \(i,j\). Multiplying their probabilities establishes the exact pair probabilities \(T_{ij}U_{ij}V_j\) and \(\frac{(a-1)(1-r)^2}{ab^2}U_{ij}V_j\). Summation over labels proves the two finite formulas.

**3. Exact endpoints.** At \(r=1\), all parent choices coincide, so \(H_n(1)\) is the ordinary one-tree sibling-pair count, with
\[
\Pr(i,j\text{ terminal siblings})=\frac{i-1}{(n-1)(n-2)}.
\]
Summing gives \(\mathbb E H_n(1)=n/6\). At \(r=0\), the two trees are independent; squaring this pair probability and summing gives
\[
\mathbb E H_n(0)=\frac{\sum_{i=2}^{n-1}(n-i)(i-1)^2}{(n-1)^2(n-2)^2}
=\frac{n}{12(n-2)}.
\]

**4. Uniform asymptotic bounds.** For every \(r\in[0,1]\), the avoidance factors obey \(u_d(r)\le1-1/d\) and \(v_d(r)\le1-2/d\). Their telescoping products therefore obey the simple common bound
\[
0\le U_{ij}(r)V_j(r)\le\frac{(i-1)(j-1)}{(n-1)(n-2)}.
\tag{1}
\]
On any region with \(i/n\to x\), \(j/n\to y\), and \(0<x<y<1\), if \(r_n\to r\), the logarithmic products have uniform first-order expansions, giving
\[
U_{ij}(r_n)V_j(r_n)\longrightarrow
\left(\frac xy\right)^{2-r}y^{4-2r}=x^{2-r}y^{2-r}.
\tag{2}
\]
The inequality (1) dominates the scaled summands and permits passage to the corresponding triangular-region Riemann integrals. For the leading \(r^2/b\) term, the integral is
\[
\int_0^1\!\int_0^y\frac{x^{2-r}y^{2-r}}y\,dx\,dy
=\frac1{(3-r)(5-2r)}.
\]
The contributions from \(r(1-r)/(ab)\) and \((1-r)/b^2\) to the expectation are each uniformly bounded: by (1), the former contributes at most \(r/2\) and the latter at most \(1/2\). Their ratio to \(n\) therefore vanishes. This proves the fixed-\(r>0\) density formula.

For the different-parent count, its summands have an integrable uniform majorant from (1), while (2) gives the limit
\[
(1-r)^2\int_0^1\!\int_0^y x^{2-r}y^{-r}\,dx\,dy
=\frac{(1-r)^2}{(3-r)(4-2r)}.
\]
This also holds at either endpoint.

**5. Vanishing-alignment crossover.** Let \(r_n\to0\). Divide the exact sum into contributions of the three terms of \(T_{ij}\). Equation (1) bounds the middle contribution by \(r_n/2=o(1)\). The last contribution converges by (1)–(2) to
\[
\int_0^1\!\int_0^y x^2\,dx\,dy=\frac1{12},
\]
including the factor \(1-r_n\to1\). The first contribution equals \(n r_n^2\) multiplied by a normalized Riemann sum that converges to
\[
\int_0^1\!\int_0^y x^2y\,dx\,dy=\frac1{15}.
\]
No relation between the rates of \(n\to\infty\) and \(r_n\to0\) was imposed. This proves the separate-error expansion and its stated limiting and supercritical consequences. \(\square\)

## Verification

The standalone standard-library Python program `verify.py` computes the exact formula using rational arithmetic and independently enumerates every pair of parent-choice histories for \(3\le n\le6\) at four rational coupling probabilities. It separately checks total and mismatched-parent pair counts, the two exact endpoints through \(n=19\), and numerical approach to both Riemann-integral limits. Executing `python3 verify.py` outputs `PASS 57 grouped exact and asymptotic assertions` and `PASS 21 extra mismatch checks`. Computation supplements, but does not replace, the proof for arbitrary \(n\) or asymptotic sequences.

## Relationship to prior work

Janson's random recursive tree degree-profile central limit theorems (2004 online; 2005 journal) describe single-tree counts by outdegree and their growth fluctuations, not pair-matched terminal siblings between two correlated parent arrays. The 2013 motif-count analysis of Gopaladesikan, Mahmoud and Ward treats single-tree fringe motifs. Bäumler, Rácz, Ross and Sridhar's 2026 paper introduces independently sprinkled parent agreement and analyzes correlation detection and early-vertex labels; the present claim concerns an explicit *label-pair motif-overlap expectation* in that model, not a new model or a detection theorem. The public degree-profile cross-covariance result and the public exact one-tree terminal-sibling mean and covariance results provide useful antecedents but do not determine the cross-tree, same-label **parent incidence** events required for this calculation. In particular the \(r=0\) and \(r=1\) endpoints follow from the already-known one-tree sibling-pair law; the exact intermediate-coupling kernel, bounded mismatched-parent law and vanishing-coupling crossover are the assessed contributions.

## Limitations

The theorem concerns expectations, not the distribution or concentration of motif overlap. A mean crossover at \(r\asymp n^{-1/2}\) must not be confused with an established statistical detection threshold. It needs the explicit birth-label alignment and the independent stepwise parent-coupling law; it does not automatically extend to unlabeled trees, initial-prefix sharing, preferential attachment or other cherry definitions. More general unpublished or inaccessible motif-overlap results could imply some formulas; historical priority remains conditional on further independent literature review. Independent mathematical audit has not been performed.

## References

1. S. Janson, *Asymptotic degree distribution in random recursive trees*, *Random Structures & Algorithms* 26 (2005), 69–83, first online 2004-11-16. https://doi.org/10.1002/rsa.20046 ; author preprint https://www2.math.uu.se/~svantejs/papers/sj155.pdf .
2. M. Gopaladesikan, H. Mahmoud, M. D. Ward, *Asymptotic joint normality of counts of uncorrelated motifs in recursive trees*, *Methodology and Computing in Applied Probability* 16 (2014), 863–884, first online 2013-03-29. https://doi.org/10.1007/s11009-013-9333-z .
3. J. Bäumler, M. Z. Rácz, N. Ross, A. Sridhar, *Correlated uniform attachment trees*, arXiv:2606.02472, first posted 2026-06-01. https://arxiv.org/abs/2606.02472 .
4. *Exact terminal-sibling covariance and a constant regression slope in random recursive trees*, public finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-terminal-sibling-covariance-and-a-constant-regression-slop--261fc92cae7c .
5. *Exact terminal-sibling clustering covariance in uniform recursive trees*, public finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-terminal-sibling-clustering-covariance-in-uniform-recursiv--d3480f1053f7 .
6. *A rational cross-tree covariance kernel for correlated uniform-attachment degree profiles*, public finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-rational-cross-tree-covariance-kernel-for-correlated-uniform-a--3469578c4e97 .
