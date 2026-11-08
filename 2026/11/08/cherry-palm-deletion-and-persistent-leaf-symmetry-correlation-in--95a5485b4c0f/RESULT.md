# Cherry-Palm deletion and persistent leaf–symmetry correlation in uniform Cayley trees

## Finding

Let \(T_n\) be uniformly distributed among the \(n^{n-2}\) trees on the labeled vertices \([n]\), for each integer \(n\ge4\). Let \(L_n\) count degree-one vertices (leaves). For each vertex \(v\), let \(d_v^{\mathrm{leaf}}\) count its leaf neighbors, and define the cherry-pair count
\[
C_n=\sum_{v=1}^{n}\binom{d_v^{\mathrm{leaf}}}{2}.
\]
A cherry is an *unordered pair* of distinct degree-one vertices with one common neighbor; a vertex with three leaf neighbors contributes three cherries. Define
\[
p_m=\left(1-\frac1m\right)^{m-2}\quad(m\ge2),\qquad
\mu_n=\frac{n(n-1)(n-2)}{2}\frac{(n-2)^{n-4}}{n^{n-2}}.
\]
For every real-valued function \(f\) on the attainable leaf counts, there is the **cherry-Palm deletion identity**
\[
\frac{\mathbb E[C_nf(L_n)]}{\mathbb E C_n}
=\mathbb E\left[f\left(2+L_{n-2}-I_{n-2}\right)\right],
\tag{1}
\]
where, on the right, \(T_{n-2}\) is an independent uniform labeled Cayley tree on \(n-2\) vertices and \(I_{n-2}\) indicates whether any one fixed vertex is a leaf of that smaller tree. In particular \(\mathbb EC_n=\mu_n\), and
\[
\boxed{\operatorname{Cov}(L_n,C_n)=
\mu_n\left[2+(n-3)p_{n-2}-np_n\right]>0\qquad(n\ge4).}
\tag{2}
\]
Furthermore,
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(L_n,C_n)}n
=\frac{2e-3}{2e^3},\qquad
\boxed{\lim_{n\to\infty}\operatorname{Corr}(L_n,C_n)
=\frac{2e-3}{\sqrt{2(e-2)(e^2+2e-2)}}\approx0.6178583783.}
\tag{3}
\]
Thus dependence between the global leaf population and the number of interchangeable leaf pairs remains substantial after standardization.

## Assumptions and scope

The trees are simple, unrooted, uniformly labeled spanning trees of the complete graph; there is no growth-process interpretation. All leaves have graph degree one, including the two vertices of the unique tree on two vertices. Cherries are pair-subsets of leaf neighbors, **without** the alternative convention that their center must have degree exactly three. Equations (1) and (2) hold for every integer \(n\ge4\), with no other randomization or asymptotic assumptions. Equation (3) is an ordinary integer-size limit.

## Proof

**1. A marked-cherry bijection.** Fix three distinct labels \(a,b,v\) in \([n]\). The event \(A_{a,b;v}\) says that \(a,b\) are degree-one vertices each adjacent to \(v\). Deleting \(a,b\) from any tree satisfying this event gives an arbitrary tree on the remaining \(n-2\) labels. Conversely any tree on those labels becomes one satisfying \(A_{a,b;v}\) by adding both edges \(av,bv\). This is a bijection; thus the conditional residual tree is uniform and
\[
\mathbb P(A_{a,b;v})=\frac{(n-2)^{n-4}}{n^{n-2}}.
\tag{4}
\]
After reattaching the two leaves, every residual vertex except \(v\) retains its leaf status; the chosen center \(v\) ceases to be a leaf even if it was one. Consequently \(L_n=2+L_{n-2}-I_{n-2}\) under this conditioning. Summing the indicator of \(A_{a,b;v}\) over \(v\) and the unordered pairs \(\{a,b\}\) counts \(C_n\). Every summand has the same conditional law, proving (1) and the expression for \(\mu_n\).

**2. Covariance and its strict sign.** By the Prüfer correspondence, a specified vertex of an \(m\)-vertex uniform Cayley tree is a leaf exactly when its label is absent from the uniform word of length \(m-2\); its probability is \(p_m\). Hence \(\mathbb EL_n=np_n\). Equation (1) with \(f(t)=t\) gives
\[
\frac{\mathbb E[C_nL_n]}{\mu_n}
=2+(n-2)p_{n-2}-p_{n-2}=2+(n-3)p_{n-2}.
\]
This proves (2). To verify the strict sign for all sizes, the function \(h(x)=(1-1/x)^{x-2}\), for \(x\ge2\), is strictly decreasing: its logarithmic derivative is
\[
\frac{d}{dx}\log h(x)=\log(1-1/x)+\frac{x-2}{x(x-1)}< -\frac1x+\frac1x=0\quad(x>2).
\]
Thus \(p_{n-2}>p_n\) and \(p_n< p_3=2/3\) for \(n\ge4\). The bracket in (2) equals
\[
2-3p_n+(n-3)(p_{n-2}-p_n)>0.
\]

**3. Exact second moments for the correlation limit.** For \(n\ge5\), define
\[
a_{n,j}=\frac{(n-j)^{n-j-2}}{n^{n-2}}\quad(j=3,4).
\]
The factor with \(n-j=1\) is interpreted as one (the unique single-vertex residual tree). Two *ordered* distinct cherries with one shared leaf must share their center and specify three leaves. There are \(n(n-1)(n-2)(n-3)\) such ordered pairs, and each occurs with probability \(a_{n,3}\). Two distinct cherries with disjoint leaf pairs (their centers equal or different) are counted by
\[
\frac{n(n-1)(n-2)(n-3)(n-4)^2}{4}
\]
ordered pairs, each occurring with probability \(a_{n,4}\). The diagonal contributes \(\mu_n\). Hence
\[
\mathbb EC_n^2=\mu_n+n(n-1)(n-2)(n-3)a_{n,3}
+\frac{n(n-1)(n-2)(n-3)(n-4)^2}{4}a_{n,4}.
\tag{5}
\]
At \(n=4\), direct enumeration yields \(\mathbb EC_4^2=9/4\), consistent with the three-leaf overlap count. Two specified vertices both have degree one exactly when both are absent from the Prüfer word. Consequently, for all \(n\ge4\),
\[
\mathbb EL_n^2=np_n+n(n-1)\left(1-\frac2n\right)^{n-2}.
\tag{6}
\]
Elementary expansions give
\[
\begin{aligned}
\mu_n&=e^{-2}\left(\frac n2+\frac32+O(n^{-1})\right),\\
\frac1n\operatorname{Var}(L_n)&\longrightarrow e^{-1}-2e^{-2},\\
\frac1n\operatorname{Var}(C_n)&\longrightarrow \frac12e^{-2}+e^{-3}-e^{-4},\\
2+(n-3)p_{n-2}-np_n&\longrightarrow2-3e^{-1}.
\end{aligned}
\]
For the cherry variance, these follow by using, for fixed \(j\),
\[
\left(1-\frac jn\right)^{n-j-2}
=e^{-j}\left(1+\frac{j(j+4)}{2n}+O(n^{-2})\right)
\]
in (5), for \(j=2,3,4\), and retaining the linear term after cancellation of the quadratic terms. Both limiting variance coefficients are positive. Substituting these results into (2) proves the covariance and correlation limits in (3).

## Verification

The reproducible Python program `check.py` reconstructs every tree from its Prüfer word for sizes \(n=4,5,6,7,8\) (a total of \(16+125+1296+16807+262144=280388\) trees). Using exact rational arithmetic, it checks leaf and cherry means, second moments, the mixed covariance, and the complete cherry-size-biased leaf-count distribution against deletion in a smaller uniform tree. It also checks positivity and moment inequalities in the formulas for each integer \(9\le n\le200\). The program reports 631 exact assertions passed. These finite checks supplement, but do not replace, the analytic all-size proof.

## Relationship to prior work

Erdős and Rényi, *Asymmetric graphs* (1963), §5, introduce the same unrestricted cherry notion and calculate marked-cherry probabilities to prove that almost every uniform labeled tree has a cherry. The marked-cherry counting mechanism is classical and is not claimed as new. The contribution here is the **full cherry-size-biased leaf-count deletion law**, its globally positive mixed covariance, and its explicit nonzero limiting correlation. They are not stated in that §5 treatment. Junk, Schmidt, and Weber, *Almost all trees have quantum symmetry* (original preprint 2019), §3, study cherries subject to the *additional center-degree-three restriction* and the probability of multiple such motifs; that differently normalized motif is not the statistic in (1). Disanto and Wiehe, *Exact enumeration of cherries and pitchforks in ranked trees under the coalescent model* (first public preprint 2011-12-06), concern a rooted binary ranked coalescent model rather than the unrooted uniform Cayley law; their joint enumeration is for cherries and pitchforks, not degree-one leaves and unrestricted sibling-leaf pairs. The relevant comparison is with actual mixed statements, not the shared word “cherry.”

## Limitations

The result concerns the uniform labeled Cayley model only, not recursive trees, unlabeled random tree shapes, nor binary phylogenetic tree models. The correlation is an ordinary second-moment quantity and does not establish a joint central limit theorem, stochastic monotonicity, or causal dependence. Earlier general forest-enumeration techniques may allow an implicit derivation; the review does not certify historical priority or independent validation. The original 1963 article predates the dated 2011 preprint anchor but its exact first-publication day could not be established: its publisher specifies only an issue month, while a secondary bibliographic index gives a possibly imputed first-of-month date. Therefore 2011-12-06 is the earliest day-verified preprint date among the inspected explicitly dated electronic sources, not a claim that no pertinent literature existed before 2011.

## References

1. P. Erdős and A. Rényi, “Asymmetric graphs,” *Acta Mathematica Academiae Scientiarum Hungaricae* **14** (1963), 295–315. DOI: https://doi.org/10.1007/BF01895716 . Author-hosted manuscript: https://www.renyi.hu/~p_erdos/1963-04.pdf . Relevant material: §5, pp. 312–313.
2. L. Junk, S. Schmidt, and M. Weber, “Almost all trees have quantum symmetry,” arXiv:1911.02952, initial public preprint 2019. https://arxiv.org/abs/1911.02952 . Relevant material: §3, definition and counting of center-degree-three cherries.
3. F. Disanto and T. Wiehe, “Exact enumeration of cherries and pitchforks in ranked trees under the coalescent model,” arXiv:1112.1295, first public preprint **2011-12-06** (UTC), https://arxiv.org/abs/1112.1295 . The ranked binary tree model differs from the uniform unrooted Cayley model.
4. Publisher record for Erdős–Rényi (1963), https://link.springer.com/article/10.1007/BF01895716 , indicates September 1963 without a verified release day; a secondary record https://bishtref.com/articles/10.1007/bf01895716 gives 1963-09-01 but this day may be a bibliographic placeholder.
