# Fixed-rank signed-rook fourth moments: a one-third transition and additive minimizers

## Finding
For integers \(n\ge2\) and \(1\le k\le n\), choose a uniformly random placement of \(k\) nonattacking rooks on an \(n\times n\) board, independently giving each rook a fair sign. Let \(W\) be the resulting real matrix, with the signs in the occupied cells and zeros elsewhere. For every nonzero real coefficient matrix \(A\), define
\[
 F_A(W)=\operatorname{tr}(A^{\mathsf T}W),\qquad
 K_{n,k}(A)=\frac{\mathbb E F_A^4}{(\mathbb E F_A^2)^2}.
\]
The **complete sharp range**, attained at both ends and throughout the interval, is
\[
 \boxed{\min\left\{3-\frac2k,\frac nk\right\}
 \le K_{n,k}(A)\le
 \max\left\{\frac{n^2}{k},4\right\}.}
\]
The **lower extremizers** change exactly when \(n=3k-2\):

- If \(n>3k-2\), they are precisely the matrices with all \(n^2\) entries of equal nonzero absolute value.
- If \(n<3k-2\), they are precisely the matrices supported on one complete row or column, every entry there having the same nonzero absolute value.
- If \(n=3k-2\), put \(S=\sum_{ij}A_{ij}^2\), \(x_{ij}=A_{ij}^2/S\), \(r_i=\sum_jx_{ij}\) and \(c_j=\sum_i x_{ij}\). Equality holds exactly when
\[
 \boxed{x_{ij}=\frac{r_i+c_j}{n}-\frac1{n^2}\quad\text{for every }i,j.}
\]
The coefficients' signs are arbitrary. The critical equality set is a positive slice of an additive row-column affine space, containing both the flat and complete-row families.

The **upper extremizers** are exactly single-entry matrices except in three cases: for \((n,k)=(2,2)\) and \((3,3)\), they have equal nonzero absolute entries on a complete permutation matching; for \((n,k)=(4,4)\), they have arbitrary nonzero magnitudes on any nonempty partial matching. In all cases signs are free.

For the real \(n^2\)-dimensional space \(X_{n,k}=\{F_A:A\in\mathbb R^{n\times n}\}\) with its \(L^4\) norm, the exact real-linear Banach--Mazur distance is
\[
 \boxed{d_{\mathrm{BM}}\!\left(X_{n,k},\ell_2^{n^2}(\mathbb R)\right)^4
 =\frac{\max\{n^2/k,4\}}{\min\{3-2/k,n/k\}}.}
\]

## Assumptions and scope
All expectations use the uniform distribution over fixed-size matchings, independent uniform signs, and the counting probability measure. Each of the \(\binom nk^2 k!\) matchings is equally likely; each has \(2^k\) equally likely signings. \(A\) is real, \(n\ge2\), \(1\le k\le n\), and \(A\ne0\). All statements describe the full matrix-coefficient space, without restrictions on rank or signs of \(A\).

## Proof
**Exact moments.** Let \(S=\sum_{ij}A_{ij}^2\), \(U=\sum_{ij}A_{ij}^4\), and let \(D_A\) denote the sum of \(A_{ij}^2 A_{i'j'}^2\) over unordered pairs of distinct cells in different rows *and* different columns. A cell is occupied with probability \(k/n^2\), and a fixed disjoint pair is occupied with probability \(k(k-1)/[n^2(n-1)^2]\). Independence of the rook signs gives
\[
 \mathbb EF_A^2=\frac{kS}{n^2},\qquad
 \mathbb EF_A^4=\frac{kU}{n^2}
 +\frac{6k(k-1)}{n^2(n-1)^2}D_A.
\]
Set \(x_{ij}=A_{ij}^2/S\), \(T=\sum_{ij}x_{ij}^2\), \(D=D_A/S^2\) and \(q=3(k-1)/(n-1)^2\). Then
\[
 \boxed{K_{n,k}(A)=\frac{n^2}{k}H_q(x),\qquad H_q(x)=T+2qD.}
\]
Let \(P\) sum \(x_{ij}x_{i'j'}\) over unordered distinct pairs sharing a row or a column. Since \(T+2P+2D=1\),
\[
 H_q=1-2P+2(q-1)D.
\]

**Upper bound.** For \(q<1\), the last identity gives \(H_q\le1\), with equality only if \(P=D=0\), i.e. precisely one positive \(x_{ij}\). For \(q=1\), it gives equality exactly when \(P=0\), i.e. positive masses on a partial matching. Since \(q\le3/(n-1)\), the remaining cases \(q>1\) occur only for \((n,k)=(2,2)\) and \((3,3)\). To maximize \(H_q\), whenever two positive masses share a row or column, redistribute their fixed sum. The contribution of those two coordinates has strictly positive quadratic coefficient (their mutual pair is not in \(D\)), so the maximum moves to an endpoint. Thus every maximizer is supported on a matching of size \(m\le n\). On that support \(D=(1-T)/2\), hence \(H_q=q+(1-q)T\); for \(q>1\) this is largest when \(m=n\) and the \(n\) masses are equal, giving \(H_q=q+(1-q)/n\). Substitution yields \(K_{n,k}=4\) in these two exceptional cases. Together this proves the upper constant and every equality case.

**Lower bound and a nonnegative decomposition.** Define the row and column masses \(r_i=\sum_jx_{ij}\), \(c_j=\sum_i x_{ij}\), and the interaction residual
\[
 z_{ij}=x_{ij}-\frac{r_i+c_j}{n}+\frac1{n^2}.
\]
Both row and column sums of \(z\) vanish. As the total mass of \(x\) is one, disjoint-pair counting gives \(2D=1-\sum_i r_i^2-\sum_jc_j^2+T\). Orthogonal decomposition into constant, row, column and interaction components yields the **exact identity**
\[
 \boxed{
 H_q(x)-\left(\frac1{n^2}+q\frac{(n-1)^2}{n^2}\right)
 =\frac{1-q(n-1)}{n}
 \left[\sum_i\left(r_i-\frac1n\right)^2+
 \sum_j\left(c_j-\frac1n\right)^2\right]
 +(1+q)\sum_{ij}z_{ij}^2.}
\]
When \(q<1/(n-1)\), both coefficients are positive and the unique minimizing \(x\) is the uniform matrix. This gives \(K_{n,k}=3-2/k\). At \(q=1/(n-1)\), the row/column coefficient is zero, while the interaction term stays positive, so equality holds **exactly** for \(z=0\). This is the stated additive equality family and it occurs exactly when \(n=3k-2\).

For larger \(q\), an independent endpoint argument gives an exact positive decomposition. Put \(q_0=1/(n-1)\), \(q_1=3/(n-1)\), and \(\theta=(q-q_0)/(q_1-q_0)=[q(n-1)-1]/2\in(0,1]\). For a uniform permutation \(\pi\in S_n\), let \(Y_\pi=\sum_i x_{i,\pi(i)}\). Direct summation shows
\[
 \operatorname{Var}_\pi Y_\pi
 =\frac{T}{n}+\frac{2D}{n(n-1)}-\frac1{n^2}\ge0,
\]
so that
\[
 \boxed{H_q(x)-\frac1n
 =(1-\theta)\frac{n}{n-1}\sum_{ij}z_{ij}^2
 +\theta\left[n\operatorname{Var}_\pi(Y_\pi)+\frac{4D}{n-1}\right].}
\]
All terms are nonnegative. When \(q>q_0\), equality requires \(D=0\) and \(\operatorname{Var}_\pi Y_\pi=0\). The condition \(D=0\) means the positive support is pairwise intersecting as edges of a complete bipartite graph, hence lies in one row or one column. The zero permutation variance then requires all \(n\) magnitudes in that row/column to agree and be positive. Conversely these matrices attain equality. This gives \(K_{n,k}=n/k\) above the threshold, including the full-rank endpoint. The two deficits supply exact stability identities on both sides of the critical parameter.

**Connected range.** \(A\mapsto F_A\) is injective because \(\mathbb EF_A^2=kS/n^2>0\). On the connected unit sphere of \(\mathbb R^{n^2}\), \(K_{n,k}(A)\) is continuous and achieves the extrema above. Therefore every intermediate value occurs.

**Optimal Euclidean distortion.** The two sharp endpoints compare \(\|F_A\|_4\) and \(\|F_A\|_2\). To show no other Euclidean norm improves their ratio, average any admissible positive-definite comparison quadratic form over independent signed row and signed column permutations of \(A\). These operations preserve the law of \(F_A\). Sign changes eliminate off-diagonal terms in the average; row and column permutations equate all diagonal terms. Thus every averaged comparison form is a scalar multiple of \(\sum_{ij}A_{ij}^2\). The attained sharp endpoints force distortion at least the fourth root of their ratio, which the natural \(L^2\) structure realizes.

## Verification
Execute `python rook_rank_checker.py` using Python 3. The checker uses exact rational arithmetic. It independently enumerates fixed-rank signed rook matrices for 72 coefficient-and-rank cases in dimensions two through four, checks moment identities directly, tests sharp endpoint witnesses through dimension 26, and verifies both exact nonnegative-deficit decompositions on 2,380 normalized rational coefficient matrices. It also checks nonuniform critical additive equality witnesses in five dimensions. These finite tests corroborate formulas; they do not replace the preceding analytical proof.

## Relationship to prior work
Malandro's 2011 work develops spectral analysis of partial bijections organized by rook rank, domain, and range, making fixed-rank matrix-coefficient questions natural. Pass and Spektor's 2014 work studies sharp fourth-moment behavior of dependent Rademacher vectors under *pairwise independence and exchangeability* assumptions. Neither inspected work treats independent random signs conditional on a uniformly chosen partial matching, nor gives the rank-dependent sharp interval, the critical additive equality set, or the exact Euclidean distortion above. The full signed-permutation endpoint \(k=n\) is one boundary case; it does not imply the sharp behavior or equality structure of all smaller ranks.

## Limitations
The result concerns **real** coefficients, independent fair rook signs, exactly fixed rook cardinality, fourth moments, and square boards. It does not classify complex coefficient phases, biased signs, nonuniform matchings, rectangular boards, or sixth and higher moments. Bibliographic searches do not establish absolute novelty; earlier formulations in unindexed literature remain possible. No independent mathematical audit has been conducted.

## References
1. M. E. Malandro, *Inverse semigroup spectral analysis for partially ranked data*, arXiv:1110.5679, first submitted 2011-10-25, https://arxiv.org/abs/1110.5679.
2. B. Everitt and J. Fountain, *Partial symmetry, reflection monoids and Coxeter groups*, arXiv:0812.2789, first submitted 2008-12-15, https://arxiv.org/abs/0812.2789.
3. B. Pass and S. Spektor, *On Khinchine type inequalities for pairwise independent Rademacher random variables*, arXiv:1412.7859, first submitted 2014-12-25, https://arxiv.org/abs/1412.7859.
