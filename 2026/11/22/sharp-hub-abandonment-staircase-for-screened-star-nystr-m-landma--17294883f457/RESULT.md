# Sharp hub-abandonment staircase for screened-star Nyström landmarks

## Finding

Let \(K_{1,m}\) be the unweighted star with center \(o\), \(m\ge2\) leaves, and combinatorial Laplacian \(L\). At arbitrary \(\mu>0\), set \(G_\mu=(\mu I+L)^{-1}\). For a selected vertex set \(S\) of cardinality \(1\le k\le m\), define the **standard unrescaled Nyström approximation**
\[
\widehat G_{\mu,S}=G_{\mu,:,S}(G_{\mu,S,S})^{-1}G_{\mu,S,:},\qquad
\mathcal E_\mu(S)=\operatorname{tr}(G_\mu-\widehat G_{\mu,S}).
\]
Every size-\(k\) set containing the center has the same error \(E_H\); every size-\(k\) all-leaf set has error \(E_L\). Their exact formulas are
\[
E_H=\frac{m-k+1}{\mu+1},\qquad
E_L=\frac{m-k}{\mu+1}
 +\frac{(\mu+1)^2+m-k}{(\mu+1)[\mu(\mu+m+1)+k]},
\]
\[
\boxed{E_L-E_H=\frac{m+1-2k-(m-1)\mu}
{(\mu+1)[\mu(\mu+m+1)+k]}.}
\]
Consequently, with \(\mu_k=(m+1-2k)/(m-1)\) for \(1\le k\le\lfloor m/2\rfloor\), the center-containing sets are **exactly** the minimizers when \(0<\mu<\mu_k\); the all-leaf sets are **exactly** the minimizers when \(\mu>\mu_k\); and both types tie when \(\mu=\mu_k\). For \(\lfloor m/2\rfloor<k\le m\), only all-leaf sets minimize for every \(\mu>0\). The positive thresholds \(\mu_k\) are strictly decreasing in an arithmetic progression of spacing \(2/(m-1)\). At equality, the number of minimizers is \(\binom m{k-1}+\binom mk\); away from equality it is respectively \(\binom m{k-1}\) or \(\binom mk\). For \(k=m+1\), the unique full set has zero error.

The determinant criterion is persistently opposed to the low-screening trace criterion. For every \(1\le k\le m\) and \(\mu>0\), **only all-leaf sets maximize** \(\det(G_{\mu,S,S})\), because
\[
\frac{\det(G_{\mu,S,S})\ \text{for a center-containing }S}
 {\det(G_{\mu,S,S})\ \text{for an all-leaf }S}
=\frac{(\mu+1)^2}{\mu(\mu+m+1)+k}<1.
\]
In particular, when \(0<\mu<1\), the unique structural type of optimal singleton is the center, but every optimal size-\(m\) set consists of **all** leaves. Thus **no nested sequence can be globally trace-optimal at every budget**. Any append-only procedure that starts from the optimal singleton must, at budget \(m\), have residual \(1/(\mu+1)\), whereas the global optimum is \(1/(\mu+m)\). Its residual approximation ratio is exactly \((\mu+m)/(\mu+1)\), which diverges linearly with \(m\) at fixed positive \(\mu<1\).

## Assumptions and scope

The graph has exactly \(m+1\) vertices and unit, undirected center-to-leaf edges. The diagonal shift is uniform and strictly positive. Columns are selected without replacement; the selected principal block is inverted exactly without ridge modification. The loss is the **unnormalized trace residual**, not spectral norm, Frobenius norm, or inverse trace for a different matrix. The determinant comparison concerns the selected Green principal block, not a dynamical observability Gramian or a spanning-tree objective. All assertions quantify over all integers \(m\ge2\), budgets \(1\le k\le m\), and all real \(\mu>0\).

## Proof

**1. Residual/principal-inverse identity.** Write \(A=\mu I+L\), so \(G=A^{-1}\). Partition rows and columns into selected \(S\) and unselected \(U\). The block inversion identity says the Schur complement \(G_{U,U}-G_{U,S}G_{S,S}^{-1}G_{S,U}\) equals \((A_{U,U})^{-1}\). Since the other rows and columns of the Nyström residual vanish, \(\mathcal E_\mu(S)=\operatorname{tr}((A_{U,U})^{-1})\). Positivity of \(A\) makes all inverses legitimate.

**2. Sets including the center.** With the center in \(S\), the \(m-k+1\) unselected vertices are isolated leaves in the principal submatrix of \(A\), each with diagonal \(\mu+1\). Thus \(\mathcal E_\mu(S)=E_H=(m-k+1)/(\mu+1)\).

**3. Sets omitting the center.** With all selected vertices leaves, write \(r=m-k\). The unselected block comprises the center and \(r\) leaves:
\[
A_{U,U}=\begin{pmatrix}\mu+m&-\mathbf 1_r^{\mathsf T}\\-\mathbf 1_r&(\mu+1)I_r\end{pmatrix}.
\]
Its center Schur complement is \(s=\mu+m-r/(\mu+1)=[\mu(\mu+m+1)+k]/(\mu+1)>0\). Inverting the block and summing its diagonal gives \(r/(\mu+1)+s^{-1}[1+r/(\mu+1)^2]\), which is precisely \(E_L\). For \(r=0\), this reduces to \(1/(\mu+m)\); the same formula remains valid without any zero-dimensional inversion ambiguity.

**4. Sign and counting.** Subtracting the preceding formulas yields the boxed rational difference, with strictly positive denominator. Its numerator is affine and strictly decreasing in \(\mu\), with a positive zero exactly when \(k\le\lfloor m/2\rfloor\). All leaf permutations preserve the loss and there are no other vertex-set types; hence all optimizer types, ties, counts, and the arithmetic threshold progression follow.

**5. Determinants.** By Jacobi's complementary principal-minor identity, \(\det G_{S,S}=\det A_{U,U}/\det A\). A direct center/leaf Schur calculation gives \(\det A=(\mu+1)^{m-1}\mu(\mu+m+1)\). Consequently,
\[
D_H=\frac{(\mu+1)^{2-k}}{\mu(\mu+m+1)},\qquad
D_L=\frac{\mu(\mu+m+1)+k}{(\mu+1)^k\mu(\mu+m+1)}.
\]
Their ratio is as stated. The strict inequality follows because \(\mu(\mu+m+1)+k-(\mu+1)^2=(m-1)\mu+k-1>0\).

**6. Append-only barrier.** At budget one, the difference is \((m-1)(1-\mu)/[(\mu+1)(\mu(\mu+m+1)+1)]\), so for \(0<\mu<1\) only the center wins. At budget \(m\), the only all-leaf set has error \(1/(\mu+m)\), while every center-containing set has error \(1/(\mu+1)\). Since an append-only sequence cannot delete its first center, the exact stated ratio follows. This quantifies an obstruction for any prefix-constrained method, not the particular decisions made by a named greedy implementation.

## Verification

The standalone `verify.py` uses exact rational and symbolic arithmetic. It algebraically checks the two residual and determinant identities, compares explicit Nyström matrices against their formulas for stars with \(2\) through \(12\) leaves at seven rational shifts and all budgets, enumerates every size-\(k\) vertex subset on stars with \(2\) through \(8\) leaves at three rational shifts, and tests the nonnesting and growing-ratio statements. The included checker ran successfully with **3557 exact assertions**. These finite checks are corroboration; the preceding block-inverse proof establishes the all-parameter claim.

As a concrete interior example, at \(m=10\) and \(\mu=1/2\), the center type has smaller trace residual at budget \(k=3\), with \(E_L-E_H=4/105\), while the leaf type has smaller residual at budget \(k=4\), with \(E_L-E_H=-4/39\). No size-three optimal set is contained in a size-four optimal set.

## Relationship to prior work

Classical Nyström approximation and greedy column-selection methods motivate exact landmark design and the nestedness issue [1,2]. A later nuclear-score analysis studies exact/greedy Laplacian rank reduction and even uses a star as a model, but its star experiment concerns the stationary-state/vanishing-regularization formulation, not this uniform positive screening theorem for every budget [3]. Published all-budget noise-free leader placement on weighted stars is a close analogue at zero uniform screening: it optimizes inverse grounded Laplacians for arbitrarily weighted stars but does not state or imply the complete \(\mu>0\) threshold sequence, all positive-screening principal determinants, or the exact finite-shift append-only ratio [4]. The specific result is separate from generic diagonal-plus-rank-one Nyström formulas because the star Green matrix has nonuniform common-factor loadings and a singular diagonal baseline under that representation.

## Limitations

The result is for **unweighted stars only** and **uniform positive killing/screening**. It does not classify general trees, unequal star conductances, noisy selected landmarks, approximate inverses, or spectral-norm-optimal columns. A search of accessible published statements found no dominating positive-screening all-budget classification, but does not prove historical novelty. The full text of the closest indexed noise-free weighted-star result was not accessible during comparison, so an unrecognized implication or equivalent formulation remains a publication-priority risk. No independent mathematical audit has been performed.

## References

[1] A. Gittens and M. W. Mahoney, *Revisiting the Nyström Method for Improved Large-Scale Machine Learning*, arXiv:1303.1849, initial submission March 7, 2013. https://arxiv.org/abs/1303.1849

[2] A. Farahat, A. Ghodsi, and M. Kamel, *A novel greedy algorithm for Nyström approximation*, AISTATS 2011, Proceedings of Machine Learning Research 15:269–277. https://proceedings.mlr.press/v15/farahat11a.html

[3] M. Fornace and M. Lindsey, *Column and row subset selection using nuclear scores: algorithms and theory for Nyström approximation, CUR decomposition, and graph Laplacian reduction*, arXiv:2407.01698, first posted July 1, 2024, especially Section 6.1.2. https://arxiv.org/abs/2407.01698

[4] *Optimal noise-free leaders on an arbitrarily weighted star: two candidate sets and a re-entrant hub*, publicly indexed mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-optimal-noise-free-leaders-on-an-arbitrarily-weighted-star-two-c--58eb0fc2195a
