# Conditional leaf erasure and the depth–leaf covariance profile of recursive trees

## Finding

**Theorem (fixed-leaf erasure).** Let \(n\ge2\), and form a *uniform random recursive tree* on birth labels \(1,\ldots,n\): the root is label \(1\), and for each \(t=2,\ldots,n\) the parent \(P_t\) is independently uniform on \(\{1,\ldots,t-1\}\). Let \(X_i\) indicate that vertex \(i\) has no children in the final tree. For every fixed \(S\subseteq\{2,\ldots,n\}\), condition on \(X_i=1\) simultaneously for all \(i\in S\). Delete these vertices and relabel the surviving vertices in increasing birth order. **The entire remaining tree is exactly a uniform random recursive tree on \(n-|S|\) vertices.**

More explicitly, writing \(r_j=|S\cap\{2,\ldots,j-1\}|\) for a surviving vertex \(j\notin S\), and denoting its edge-depth by \(D_j\),
\[
\mathcal L(D_j\mid X_i=1\ (i\in S))
=\mathcal L(D_{j-r_j}^{\mathrm{RRT}}),
\qquad
\mathbb E\left[z^{D_j}\prod_{i\in S}X_i\right]
=q_{n,S}\prod_{k=1}^{j-r_j-1}\left(1+\frac{z-1}{k}\right),
\]
for every complex \(z\), where the empty product is \(1\), and
\[
q_{n,S}=\Pr(X_i=1\text{ for all }i\in S)
=\prod_{t=2}^{n}\left(1-\frac{|S\cap\{2,\ldots,t-1\}|}{t-1}\right)>0.
\]
For fixed \(j\), conditioning on any nonempty set of earlier surviving leaves strictly lowers the depth in stochastic order relative to its unconditional law.

**Exact mixed-moment consequence.** For all integers \(n\ge3\), \(2\le j\le n\), and \(2\le i\le n\), the covariance with one fixed leaf indicator is
\[
\operatorname{Cov}(D_j,X_i)=
\begin{cases}
-\dfrac{i-1}{(n-1)(j-1)}, & i<j,\\[3pt]
0, & i\ge j.
\end{cases}
\]
Consequently, with \(L_n=\sum_{i=2}^{n}X_i\), the total number of leaves,
\[
\boxed{\operatorname{Cov}(D_j,L_n)=-\frac{j-2}{2(n-1)}.}
\]
It vanishes for the deterministic-depth vertex \(j=2\), and is strictly negative for all \(j\ge3\). At the final arrival \(j=n\), this covariance tends to \(-1/2\), while the correlation is asymptotic to \(-\sqrt{3/(n\log n)}\).

## Assumptions and scope

The model is **uniform attachment**, not the preferential-attachment, uniform Cayley-tree, or plane-oriented recursive-tree model. Parents \(P_t\) are mutually independent. All leaves are vertices with **outdegree zero**; the root is not a leaf for \(n\ge2\). Each set \(S\) is fixed before drawing the tree and excludes the root. The conditioning event has positive probability. The covariance identities require \(n\ge3\), and the correlation assertion concerns \(j=n\to\infty\).

## Proof

**1. Conditional product law and deletion.** The event \(E_S=\{X_i=1\text{ for every }i\in S\}\) says exactly that, for each arrival \(t\), its chosen parent \(P_t\) avoids already born members of \(S\). Write \(S_{<t}=S\cap\{2,\ldots,t-1\}\). Since the original parent choices are independent and \(E_S\) intersects one restriction on each \(P_t\), the conditioned parents remain independent, each uniform on \(\{1,\ldots,t-1\}\setminus S_{<t}\). Their restriction probabilities multiply, proving the formula for \(q_{n,S}\).

No vertex in \(S\) can be a parent under \(E_S\); each is therefore terminal, so its deletion leaves the parent of every surviving nonroot vertex unchanged. If that vertex has rank \(a\) among survivors, it originally had exactly \(a-1\) possible surviving parents, all equally likely and independent of the choices at the other surviving births. Thus its relabelled parent is independent and uniform on \(\{1,\ldots,a-1\}\). This proves the **entire-tree law**, including its hypotheses and all quantifiers.

**2. Exact depth law.** Let \(F_m(z)=\mathbb E[z^{D_m^{\mathrm{RRT}}}]\) in a uniform recursive tree on \(m\) labels. The recursion \(D_m=1+D_{P_m}\), together with \(F_1(z)=1\), gives
\[
F_m(z)=\frac{z}{m-1}\sum_{a=1}^{m-1}F_a(z)
=\prod_{k=1}^{m-1}\left(1+\frac{z-1}{k}\right).
\]
For the last equality, use \(F_{m+1}/F_m=(m-1+z)/m\) for \(m\ge2\), and \(F_2=z\). Equivalently \(D_m\) is distributed as a sum of independent Bernoulli random variables of success probabilities \(1/k\), \(k=1,\ldots,m-1\). The erasure theorem maps surviving vertex \(j\) to birth rank \(j-r_j\), proving the conditional generating function, the strict stochastic ordering for \(r_j>0\), and
\[
\mathbb E[D_j\mid E_S]=H_{j-r_j-1},\qquad
\mathbb E[D_j]=H_{j-1},\quad H_m=\sum_{k=1}^{m}k^{-1},\ H_0=0.
\]

**3. Covariance profile.** For \(2\le i<j\), take \(S=\{i\}\). The product probability simplifies by telescoping to \(\Pr(X_i=1)=(i-1)/(n-1)\), and the conditional mean depth decreases by \(H_{j-1}-H_{j-2}=1/(j-1)\). Hence
\[
\operatorname{Cov}(D_j,X_i)=\Pr(X_i=1)\big(\mathbb E[D_j\mid X_i=1]-\mathbb E[D_j]\big)
=-\frac{i-1}{(n-1)(j-1)}.
\]
For \(i\ge j\), the event that vertex \(i\) is a final leaf depends only on parent variables \(P_t\) with \(t>i\), all independent of the variables \(P_t\) with \(t\le j\) that determine \(D_j\); therefore its covariance is zero. Summing \(\sum_{i=2}^{j-1}(i-1)=(j-2)(j-1)/2\) proves the claimed formula for \(\operatorname{Cov}(D_j,L_n)\).

**4. Correlation limit.** The Bernoulli representation yields \(\operatorname{Var}(D_n)=H_{n-1}-H_{n-1}^{(2)}=\log n+O(1)\). The leaf-count variance is \(\operatorname{Var}(L_n)=n/12\) for \(n\ge3\): if \(B_n\) indicates whether the parent of arrival \(n+1\) was a leaf, then \(L_{n+1}=L_n+1-B_n\) and \(\Pr(B_n=1\mid L_n)=L_n/n\). Consequently \(\mathbb E L_n=n/2\) for \(n\ge2\), \(V_{n+1}=(1-2/n)V_n+1/4\), \(V_3=1/4\), and induction gives \(V_n=n/12\) for \(n\ge3\). Inserting \(j=n\) in the exact covariance and dividing by the standard deviations proves the displayed correlation asymptotic.

## Verification

The included `verify.py` independently enumerates every recursive tree through eight vertices and checks the **complete conditioned reduced-tree distribution for every set of removed leaves**, all relevant conditional vertex-depth laws, each indexed covariance, the total covariance, and leaf-count variance by exact integers and rational arithmetic. Running `python3 verify.py` returns 17,014 successful assertions. These finite checks corroborate, but do not replace, the general proof above.

## Relationship to prior work

Panholzer and Prodinger (2005 preprint, eventually published 2007) provide the unconditional fixed-label depth law and its generating function (Section 5, notably their formula (37)); Janson (first publicly verified online November 16, 2004) treats the complete global degree-count fluctuation profile, including the limiting leaf variance. Those results do **not** specify the conditional uniformity of the entire tree after simultaneously forcing selected original labels to remain leaves. Saunders (arXiv submitted June 6, 2019) studies a *different* deletion mechanism whose transition rules maintain an equiprobable size-conditioned tree, rather than conditioning on a fixed set of surviving terminal vertices. A previously published exact covariance between the *sum of all depths* and a *single leaf indicator* does not determine the full conditional distribution or complete reduced-tree law here; similarly, node-degree/leaf-count covariances describe outdegrees, not these conditional depth laws. Search and accessible-text comparisons found no explicit implication proving the fixed-leaf conditional erasure theorem.

## Limitations

Historical priority has not been independently adjudicated. Full text of Mahmoud–Smythe (1991) on the *number of leaves in rooted subtrees*, and some earlier books and surveys, was not fully accessible; their titles and available abstracts concern different observables, but implicit coverage remains a risk. The result applies only to uniform recursive trees and conditioning on a predetermined set of terminal birth labels; it does not claim the same erasure property for arbitrary tree models or data-dependent choices of which leaves to delete. No independence or external certification is claimed. The exact covariance alone is a consequence of the stronger conditional distribution theorem, not a separate claimed result.

## References

1. S. Janson, *Asymptotic degree distribution in random recursive trees*, *Random Structures & Algorithms* 26 (2005), 69–83, DOI: https://doi.org/10.1002/rsa.20046; first published online **2004-11-16**. Author-accessible manuscript: https://www2.math.uu.se/~svantejs/papers/sj155.pdf.
2. A. Panholzer and H. Prodinger, *The level of nodes in increasing trees revisited*, author manuscript posted April 2005, https://www.finanz.math.tugraz.at/~prodinger/levelinc3.pdf; *Random Structures & Algorithms* 31 (2007), 203–226, DOI: https://doi.org/10.1002/rsa.20161.
3. A. Saunders, *A Class of Random Recursive Tree Algorithms with Deletion*, arXiv:1906.02720, https://arxiv.org/abs/1906.02720; originally submitted 2019-06-06.
4. H. M. Mahmoud and R. T. Smythe, *On the Distribution of Leaves in Rooted Subtrees of Recursive Trees*, *Annals of Applied Probability* 1 (1991), 406–418, DOI: https://doi.org/10.1214/aoap/1177005874 (abstract/bibliographic comparison only).
