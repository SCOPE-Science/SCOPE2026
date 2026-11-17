# Two sharp least-variance transitions in three-level order polytopes

## Finding
For integers \(p\ge2\) and \(q\ge1\), consider the order polytope of the maximal ranked three-level poset with rank sizes \((p,q,p)\). Let \(X\) be uniform with respect to ordinary \((2p+q)\)-dimensional Euclidean volume. The covariance \(\Sigma=\operatorname{Cov}(X)\) has an explicitly diagonalizable spectrum. As the middle rank grows, its **least-variance eigenspace changes exactly twice**: first from contrasts within the middle rank to a block-constant mode, then to contrasts within the outer ranks. At the second transition, a genuine high-multiplicity eigenvalue tie occurs.

Write \(N=2p+q\), \(D=(N+1)(N+2)\), and
\[
 c_p=\frac{(p+1)(p+2)}{12D},\qquad
 c_q=\frac{(q+1)(q+2)}{12D}.
\]
Define
\[
 S=\frac{(p+1)(2p+1)}{6D},\quad
 T=\frac{6pq+q^2+3q+2}{12D},\quad
 B=\frac{\sqrt{pq}(p+1)}{4D},
\]
and
\[
 \lambda_\pm=\frac{S+T\pm\sqrt{(S-T)^2+8B^2}}{2},\qquad
 \lambda_A=\frac{(p+1)(p^2+2pq+p+q+1)}{6(N+1)D}.
\]
Then the full multiset of eigenvalues of \(\Sigma\), including multiplicities, is:
\[
 \begin{array}{c|c}
 \text{eigenvalue}&\text{multiplicity}\\\hline
 c_p&2p-2\\ c_q&q-1\\ \lambda_A&1\\ \lambda_-&1\\ \lambda_+&1
 \end{array}
\]
(the \(c_q\) row is absent at \(q=1\)); coincident eigenvalues must have their multiplicities added.

The largest eigenvalue is always \(\lambda_+\), simple. The exact smallest-eigenspace law is
\[
 \begin{array}{c|c|c}
 \text{parameters}&\lambda_{\min}&\dim E_{\min}\\\hline
 q=1&\lambda_-&1\\
 2\le q\le p-2&c_q&q-1\\
 q\ge2,\;p-1\le q\le p+2&\lambda_-&1\\
 q=p+3&c_p=\lambda_-&2p-1\\
 q\ge p+4&c_p&2p-2
 \end{array}
\]
An empty parameter range contributes no cases. In the first transition, the minimum changes between \(q=p-2\) and \(q=p-1\), whenever \(p\ge4\). In the second, equality occurs **exactly at \(q=p+3\)** for every \(p\ge2\). This is a classification of all integer parameters, not an asymptotic statement.

## Assumptions and scope
For \(p\ge2\) and \(q\ge1\), let \(L,M,U\) be disjoint coordinate sets of sizes \(p,q,p\), and set
\[
 P_{p,q}=\{(x_i)_{i\in L\cup M\cup U}\in[0,1]^{2p+q}:x_\ell\le x_m\le x_u\ \forall \ell\in L,m\in M,u\in U\}.
\]
This is the standard order polytope for the ordinal sum of antichains \(A_p\oplus A_q\oplus A_p\), with the usual unweighted Euclidean metric. Uniform means normalized Lebesgue measure on this full-dimensional polytope; it does **not** mean the uniform distribution on its finite vertex set. The eigenspaces are taken in the ambient Euclidean coordinate space. Since \(P_{p,q}\) is full-dimensional, all covariance eigenvalues are positive.

The two coordinate zero-sum spaces supported on \(L\) and \(U\) carry eigenvalue \(c_p\); these are not necessarily the *entire* eigenspace when there is a tie. When \(q\ge2\), the zero-sum space supported on \(M\) carries eigenvalue \(c_q\). The \(\lambda_A\)-eigenvector is proportional to \(\mathbf1_L-\mathbf1_U\); the \(\lambda_\pm\) modes lie in the two-dimensional space spanned by \((\mathbf1_L+\mathbf1_U)/\sqrt{2p}\) and \(\mathbf1_M/\sqrt q\).

## Proof
**1. Exact uniform sampling and order-statistic moments.** Put \(N=2p+q\). The hyperplanes imposing a total order on coordinates partition \(P_{p,q}\), up to measure-zero boundaries, into \(p!q!p!\) congruent standard order simplices. A uniform point can therefore be realized by sampling the ordered values \(Y_{(1)}<\cdots<Y_{(N)}\) of \(N\) independent uniform \([0,1]\) variables and independently assigning the first \(p\), next \(q\), and last \(p\) values uniformly to the coordinates in \(L,M,U\). The classical exact order-statistic covariance is
\[
 \operatorname{Cov}(Y_{(r)},Y_{(s)})=
 \frac{\min(r,s)[N+1-\max(r,s)]}{(N+1)^2(N+2)}.
\]
Also \(\mathbb E(Y_{(s)}-Y_{(r)})^2=(s-r)(s-r+1)/D\) for \(s>r\), by the Dirichlet spacing law.

**2. Permutation-equivariant decomposition.** Permutation invariance separately within \(L,M,U\) implies that the three coordinate-zero-sum subspaces are invariant and scalar, and their orthogonal complement is the three-dimensional block-constant subspace. For two distinct randomly assigned values from a block of \(a\) consecutive order statistics,
\[
 \frac12\mathbb E(X_i-X_j)^2=
 \frac{1}{2a(a-1)D}\sum_{r\ne s}|r-s|(|r-s|+1)
 =\frac{(a+1)(a+2)}{12D}.
\]
This is the contrast eigenvalue on that block, giving \(c_p,c_q\) and the stated multiplicities (the middle contrast space has dimension zero when \(q=1\)).

Let \(e_L=\mathbf1_L/\sqrt p\), \(e_M=\mathbf1_M/\sqrt q\), \(e_U=\mathbf1_U/\sqrt p\). Summing the order-statistic covariance in step 1 over pairs of ranks gives the exact block matrix
\[
 K=\begin{pmatrix}A&B&C\\B&T&B\\C&B&A\end{pmatrix},\qquad
 A=\frac{(p+1)(5p^2+4pq+5p+2q+2)}{12(N+1)D},
 \quad C=\frac{p(p+1)^2}{4(N+1)D}.
\]
Here \(T,B\) are precisely those in the Finding. Reversal symmetry interchanges \(L\) and \(U\). The antisymmetric vector \((e_L-e_U)/\sqrt2\) has eigenvalue \(A-C=\lambda_A\). On its symmetric orthogonal complement, \(K\) becomes
\[
 H=\begin{pmatrix}S&\sqrt2B\\\sqrt2B&T\end{pmatrix},
 \qquad S=A+C=\frac{(p+1)(2p+1)}{6D},
\]
whose eigenvalues are \(\lambda_-\) and \(\lambda_+\). This proves the entire eigenvalue multiset and invariant eigenspaces.

**3. Ordering and exact crossing factors.** Define the quadratic characteristic function
\[
 F(z)=(S-z)(T-z)-2B^2=(\lambda_--z)(\lambda_+-z).
\]
Since \(B>0\), \(\lambda_+>\max(S,T)\). Direct subtraction gives \(S>c_p\), \(T>c_q\), and \(S>\lambda_A\). A direct factorization yields
\[
 F(\lambda_A)=
 -\frac{p(p+1)^2(p+q)(p^2+pq+2p+q^2+q)}{12(N+1)^4(N+2)^2}<0.
\]
Consequently \(\lambda_-<\lambda_A<\lambda_+\), and \(\lambda_+\) is strictly above all other eigenvalues.

Because \(\lambda_+>c_p,c_q\), the sign of \(F(c_a)\) is exactly the sign of \(\lambda_--c_a\). Exact algebraic cancellation gives
\[
 F(c_p)=-\frac{p(p+1)(p+q)(p-q+3)}{48D^2},
 \qquad
 F(c_q)=\frac{pq(p^2-q^2-3q-3)}{24D^2}.
\]
For integers \(p\ge2,q\ge1\), the first changes from negative to positive across \(q=p+3\), with equality exactly at \(q=p+3\). For the second, write \(G=p^2-q^2-3q-3\). When \(q\le p-2\), \(G\ge p^2-(p-2)^2-3(p-2)-3=p-1>0\); when \(q\ge p-1\), \(G\le p^2-(p-1)^2-3(p-1)-3=-p-1<0\). Hence \(\lambda_->c_q\) exactly when \(q\le p-2\), whereas \(\lambda_-<c_q\) for \(q\ge p-1\). Finally, \(c_q<c_p\) precisely when \(q<p\). These comparisons, together with the absence of middle contrasts at \(q=1\), exhaust all possibilities and establish the table in the Finding. At \(q=p+3\), the \(2p-2\) outer contrasts and the single \(\lambda_-\) mode coincide, giving multiplicity \(2p-1\), with no additional tie because \(c_q>c_p\) and \(\lambda_A>\lambda_-\).

## Verification
The standalone standard-library checker `check_covariance.py` reconstructs the covariance matrix from **separate exact-rational sums of uniform order-statistic covariance terms**, independent of the closed formulas used in the proof. It compares all three block-constant covariance entries, the contrast eigenvalues, and the factorized characteristic signs. It tests \(p=2,\ldots,17\) and \(q=1,\ldots,2p+11\), covering 480 distinct parameter pairs and 850,040 rank-pair covariance summands. Run with `python3 check_covariance.py`. Expected result:

```
THREE_LEVEL_ORDER_COVARIANCE_EXACT_PASS profiles=480 order_statistic_pairs=850040
```

This finite check is corroboration only; the identities and strict inequalities in step 3 constitute the proof for every permitted parameter pair.

## Relationship to prior work
Ahmad, Fourier and Joswig introduce and study maximal ranked posets and their order/chain polytopes, including rank profiles of the form \((p,q,p)\), with emphasis on face-number inequalities and chains of geometric interpolations [1]. Freij-Hollanti and Lundström study ordinal sums and their order- and chain-polytope face vectors [2]. Classical covariance identities for uniform order statistics, and their asymptotic spectra, are previously known [3]; step 1 credits these ingredients rather than asserting they are new.

The present claim concerns the **uniform Euclidean volume distribution on the order polytope**, and extracts exact finite-dimensional covariance eigenvectors, all eigenvalues, and the integer two-transition least-eigenvalue classification including a high-multiplicity tie. Neither the face-number questions in [1,2] nor the covariance of the *fully sorted* vector in [3] is the statement or directly implies this three-block randomized-coordinate eigenspace classification without the additional calculation. An equivalent prior reformulation could nevertheless exist.

## Limitations
The theorem is restricted to three ranks whose first and third cardinalities agree, with \(p\ge2\). It does not determine spectra for arbitrary rank profiles, nonuniform volume densities, or the discrete uniform distribution on vertices. The novelty search is not a proof of historical priority. Numerical or finite-rational verification is not the source of the universal quantifiers. 

## References
[1] Ibrahim Ahmad, Ghislain Fourier, Michael Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626, first public version September 4, 2023. https://arxiv.org/abs/2309.01626

[2] Ragnar Freij-Hollanti, Teemu Lundström, *\(f\)-vector inequalities for order and chain polytopes*, arXiv:2312.13890, first public version December 21, 2023. https://arxiv.org/abs/2312.13890

[3] M. A. Stephens, *Asymptotic properties for covariance matrices of order statistics*, Biometrika **62** (1975), 23–28. https://doi.org/10.1093/biomet/62.1.23
