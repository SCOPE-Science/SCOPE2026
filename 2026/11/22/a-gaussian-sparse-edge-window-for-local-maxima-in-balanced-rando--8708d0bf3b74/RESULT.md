# A Gaussian sparse-edge window for local maxima in balanced random bipartite graphs

## Finding

Let \(G_{n,n}(p)\) be the random bipartite graph with two labeled classes of \(n\) vertices, each cross-edge present independently with probability \(p\). Assign the \(2n\) vertices an independent uniformly random total ordering, and let \(S_{n,p}\) be the number of vertices that have no *earlier* neighbor in the ordering (equivalently, local maxima if the earlier positions carry larger labels). If \(p=p_n\) satisfies

\[
p_n\longrightarrow 0,\qquad
\frac{n p_n^2}{\log^2(1/p_n)}\longrightarrow\infty,
\]

then

\[
\boxed{\sqrt{p_n}\bigl(S_{n,p_n}-\mathbb E S_{n,p_n}\bigr)
\ \xrightarrow{\ d\ }\ \mathcal N(0,1).}
\]

For all \(n\ge1\) and \(0<p\le1\), the exact mean is

\[
\mathbb E S_{n,p}=\frac{2n}{(n+1)p}\bigl(1-(1-p)^{n+1}\bigr).
\]

The normal law also governs the number \(T_{n,p}=2n-S_{n,p}\) of vertex recolorings in the random-central-daemon, initially monochrome, proper-coloring process with at least \(n+1\) available colors. Indeed, \(\sqrt{p_n}(T_{n,p_n}-\mathbb E T_{n,p_n})\) has the same standard Gaussian limit. The proof discovers an exact cancellation: in an infinite balanced side-interleaving model, the variance of the conditional mean of the peak count is \(2/(2-p)\), bounded as \(p\downarrow0\), although the conditional Bernoulli noise has variance asymptotic to \(1/p\).

## Assumptions and scope

All graphs are simple, undirected and labeled. Conditional on the two vertex classes, the \(n^2\) potential edges are mutually independent Bernoulli variables. The vertex ordering is uniform and independent of the edges. A peak is a vertex with no adjacent vertex placed earlier, so isolated vertices are peaks. The result is *annealed*: the graph and the ordering are both random. The parameter \(p_n\) is deterministic; no claim is made for arbitrary \(np_n\to\infty\), fixed positive \(p\), an unbalanced bipartition, nonmonochrome initial colors, or a different activation rule. The condition entails \(n p_n\to\infty\).

## Proof

**Step 1 (conditional independent peaks).** Expose the ordered sequence of bipartition sides, coded by a word \(W\) in letters \(A,B\), with exactly \(n\) of each. Let \(H_j\) count the letters of the *opposite* side strictly before position \(j\), and write \(q=1-p\). Conditional on \(W\), the peak indicators \(X_j\) are independent Bernoulli random variables with parameters \(q^{H_j}\): the edge sets connecting each vertex to its earlier, opposite-side vertices are pairwise disjoint, even though they concern one random graph. Thus \(S_{n,p}=\sum_{j=1}^{2n}X_j\). This is also the conditional product law in Proposition 9 of de Panafieu et al. The finite mean follows alternatively because the degree of a vertex is binomial \(\operatorname{Bin}(n,p)\), and its chance to be a local maximum among itself and its neighbors is \(\mathbb E[1/(D+1)]=(1-q^{n+1})/((n+1)p)\).

**Step 2 (infinite balanced interleaving and its exact environmental variance).** Replace the finite balanced word by an infinite word of independent fair letters \(W_1,W_2,\dots\). Set \(H_j=\#\{i<j:W_i\ne W_j\}\), \(Q_j=q^{H_j}\), \(M(q)=\sum_{j\ge1}Q_j\), and \(V(q)=\sum_{j\ge1}Q_j(1-Q_j)=M(q)-M(q^2)\). For \(0<q<1\), define \(r=(1+q)/2\), \(s=(1+q^2)/2\). Direct conditioning on the sides at positions \(i<j\) gives

\[
\begin{aligned}
\mathbb E Q_i&=r^{i-1}, & \mathbb E Q_i^2&=s^{i-1},\\
\mathbb E(Q_iQ_j)&=\tfrac12(s^{i-1}+q^i)r^{j-i-1} &&(i<j).
\end{aligned}
\]

The diagonal and off-diagonal geometric series therefore yield, exactly,

\[
\mathbb E M(q)=\frac2{1-q},\qquad
\operatorname{Var}M(q)=\frac2{1+q}.
\]

The same identities hold for \(M(q^2)\) after substituting \(q^2\) for \(q\). Consequently, with \(p=1-q\downarrow0\),

\[
 p M(q)\xrightarrow{L^2}2,\qquad
 p M(q^2)\xrightarrow{L^2}1,\qquad
 pV(q)\xrightarrow{L^2}1,
\]

and \(\sqrt p(M(q)-2/p)\xrightarrow{L^2}0\). In particular, fluctuations from side interleaving itself are negligible on the \(p^{-1/2}\) scale, despite strongly fluctuating individual side counts.

**Step 3 (conditional central limit theorem).** Conditional on the infinite word, draw independent Bernoulli indicators \(X_j\) of parameters \(Q_j\). Their sum \(S_p^{\infty}\) is finite almost surely because \(\mathbb E S_p^{\infty}=2/p\). The centered summands are bounded by one, with total conditional variance \(V(q)\). The Berry--Esseen bound for independent (not necessarily identically distributed) Bernoulli variables is at most \(C V(q)^{-1/2}\), since the sum of absolute centered third moments does not exceed \(V(q)\). This applies to the countable sum by finite truncation, which converges almost surely and in \(L^2\) at fixed \(p\). As \(p V(q)\to1\) in probability, the conditional Gaussian approximation and Slutsky's theorem imply

\[
\sqrt p\bigl(S_p^{\infty}-2/p\bigr)\xrightarrow{d}\mathcal N(0,1).
\]

**Step 4 (transferring to the finite balanced graph).** Let \(K=\lceil 20\log(1/p)/p\rceil\). The condition in the theorem guarantees \(K\le n\) eventually and \(K^2/n\to0\). Sequentially coupling the first \(K\) letters of a uniformly shuffled balanced word to \(K\) independent fair letters fails with probability at most \(O(K^2/n)\): at step \(j\), the discrepancy of the conditional probability of an \(A\) from \(1/2\) is at most \((j-1)/(2(2n-j+1))\). Conditional on a successful word coupling, use the same independent uniform random coins for their Bernoulli peak indicators.

It remains to control peaks past \(K\). Conditional on the side at position \(j\) of the finite word, the weights assigned to the remaining \(2n-1\) vertices are \(n\) copies of \(q\) (the opposite side) and \(n-1\) copies of \(1\). The probability of a peak is the expectation of the product of \(j-1\) weights sampled without replacement. Maclaurin's elementary-symmetric-mean inequality bounds it by the \((j-1)\)-st power of the population mean, which is at most \(r^{j-1}\), where \(r=1-p/2\). In the infinite fair word, \(\mathbb E X_j=r^{j-1}\) exactly. Therefore both expected tail counts are bounded by

\[
\sum_{j>K}r^{j-1}\le\frac{2r^K}{p}
\le\frac{2}{p}e^{-pK/2}=O(p^9).
\]

The coupling error and both tail probabilities tend to zero, so the finite and infinite peak counts can be coupled to agree with probability tending to one. Finally,

\[
\left|\mathbb E S_{n,p}-\frac2p\right|
\le \frac{2}{(n+1)p}+\frac{2}{p}q^{n+1}
=o(p^{-1/2})
\]

under the stated condition. Replacing the centering in Step 3 by the exact finite mean proves the asserted limit.

**Step 5 (recolorings).** The random-order reduction for the specified monochrome self-stabilizing coloring process states \(T_{n,p}=2n-S_{n,p}\) in distribution. Negating a standard normal does not change its distribution; hence the recoloring assertion.

## Verification

Run `python3 verify_balanced_peaks.py` with Python 3 and its standard library. For both bipartition sizes \(n=1,2,3\), and each \(p\in\{1/3,1/2,2/3\}\), the verifier separately enumerates every binary side-interleaving word and every possible bipartite edge set, then compares the exact rational distribution of the number of peaks to the independent-indicator product law. It verifies the exact finite mean independently and checks the exact formulas \(\mathbb EM(q)=2/(1-q)\) and \(\operatorname{Var}M(q)=2/(1+q)\) at five rational arguments. These finite checks corroborate the proof but cannot establish a central limit theorem by themselves; the analytical steps above provide the unrestricted argument.

## Relationship to prior work

De Panafieu, Mathieu, Gradinariu Potop-Butucaru, and Tixeuil (2026, arXiv:2611.17989v1, first posted 2026-11-13) give the random-order reduction and the exact conditional product structure for bipartite Erdős--Rényi graphs, prove a limiting law for fixed positive edge probability, and explicitly leave the vanishing-edge-probability Gaussian question open (Section 5.4, Proposition 9 and Section 6). The present result concerns a genuine varying-probability range \(p\to0\), proves normal convergence in the balanced case, and identifies a cancellation of the random-interleaving variance that is absent from the general fixed-density limiting statement. Baldi, Rinott, and Stein (1989) study normal approximation for local maxima of random functions on deterministic graphs by dependency methods; that broader historical context does not by itself establish the particular sparse balanced random-graph scaling or the exact interleaving cancellation used here.

## Limitations

Only the stated window \(np^2/\log^2(1/p)\to\infty\) is proved. The more delicate window \(np\to\infty\) with \(np^2\) bounded remains outside this result, as do asymmetric shores, multiple initial colors, and quenched limits conditional on the random graph. The theorem does not claim an optimal Berry--Esseen rate for the finite model, nor exact variance asymptotics for all finite sizes. Historical novelty is subject to independent literature verification; the 1988 Stanford technical-report full text of Baldi--Rinott--Stein was not accessible during the comparison.

## References

1. É. de Panafieu, F. Mathieu, M. Gradinariu Potop-Butucaru, and S. Tixeuil, *The Exact Stabilization Time of Self-Stabilizing Coloring: Mean, Variance, and Distribution*, arXiv:2611.17989v1 (2026-11-13), https://arxiv.org/abs/2611.17989v1, especially Lemma 1 and Proposition 9.
2. P. Baldi, Y. Rinott, and C. Stein, *A Normal Approximation for the Number of Local Maxima of a Random Function on a Graph*, in *Probability, Statistics, and Mathematics* (1989), pp. 59--81, DOI:10.1016/B978-0-12-058470-3.50012-4; earlier Stanford technical report EFS NSF 306 (November 1988).
3. W. Hoeffding, *Probability inequalities for sums of bounded random variables*, Journal of the American Statistical Association 58 (1963), pp. 13--30 (sampling-without-replacement concentration background; the proof here uses only the classical Maclaurin inequality).
