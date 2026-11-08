# Rank–support enumeration and Gaussian laws for abelian subgroups of path graphical groups

## Finding

Fix a prime power \(q\), integers \(n\geq 1\) and \(r\geq 0\), and the path \(P_n\) on vertices \(1,\ldots,n\). For its graphical alternating matrix space \(\mathcal B_n\subseteq\mathrm{Alt}_n(\mathbb F_q)\), let \(A_{n,r}(q;w)\) count \(r\)-dimensional common totally isotropic subspaces, with each subspace weighted by \(w^k\), where \(k\) is the number of vertex coordinates on which at least one vector in the subspace is nonzero.

Write \(G_r(q)=\prod_{i=0}^{r-1}(q^r-q^i)\) (with \(G_0(q)=1\)); write \(\left[\begin{smallmatrix}r\\d\end{smallmatrix}\right]_q\) for the Gaussian binomial coefficient. Then the complete two-variable enumeration is the following **finite rational formula**, valid for every \(r\geq0\):

\[
\sum_{n\geq0} A_{n,r}(q;w)z^n
=\frac1{G_r(q)}\sum_{d=0}^r(-1)^{r-d}q^{\binom{r-d}{2}}
\left[\begin{smallmatrix}r\\d\end{smallmatrix}\right]_q
\frac{1+(q^d-q)wz}{1-(1+(q-1)w)z-(q^d-q)wz^2}.
\]

For \(r\geq1\) fixed and \(n\to\infty\), condition on a uniformly chosen \(r\)-dimensional totally isotropic subspace, and let \(K_{n,r}\) be its support size. Define

\[
\Delta_{q,r}=\sqrt{q^2+4(q^r-q)},\qquad
\lambda_{q,r}=\frac{q+\Delta_{q,r}}2,\qquad
\mu_{q,r}=\frac12+\frac{q-2}{2\Delta_{q,r}},\qquad
\sigma_{q,r}^2=\frac{q(q^r-1)}{\Delta_{q,r}^3}.
\]

Then \(\sigma_{q,r}^2>0\) and

\[
\frac{K_{n,r}-\mu_{q,r}n}{\sigma_{q,r}\sqrt n}\ \Longrightarrow\ N(0,1),\quad
\mathbb E K_{n,r}=\mu_{q,r}n+O_{q,r}(1),\quad
\mathrm{Var}(K_{n,r})=\sigma_{q,r}^2n+O_{q,r}(1).
\]

Moreover, for fixed \(q,r\geq1\), the total number of such subspaces is asymptotic to \(C_{q,r}\lambda_{q,r}^n\), where

\[
C_{q,r}=\frac{q^r-(q-\Delta_{q,r})/2}{\Delta_{q,r}G_r(q)}>0.
\]

In particular, **over \(\mathbb F_2\) the limiting support density is exactly \(1/2\) for every fixed positive rank**. For any odd prime \(p\), the same formulas count, by quotient rank and labeled-vertex support, the abelian subgroups containing the derived subgroup in the canonical path graphical group of class two and exponent \(p\). This is a group-theoretic interpretation, not a claim for characteristic-two exponent-four graphical groups.

For the natural first nontrivial rank \(r=2\), the rational generating function simplifies to

\[
\sum_{n\geq0}A_{n,2}(q;1)z^n=
\frac{z^3}{(1-z)(1-qz)(1-qz-(q^2-q)z^2)}.
\]

## Assumptions and scope

Let \(P_n\) have edges \(\{i,i+1\}\), \(1\leq i<n\). Let \(B_i=E_{i,i+1}-E_{i+1,i}\), and \(\mathcal B_n=\mathrm{span}_{\mathbb F_q}\{B_i:1\leq i<n\}\). A subspace \(U\leq\mathbb F_q^n\) is common totally isotropic when \(u^\top B_i v=0\) for every \(u,v\in U\) and every \(i\). Its support is \(\mathrm{supp}(U)=\{j:\exists u\in U,\ u_j\ne0\}\), a well-defined coordinate-invariant of this labeled presentation. When \(r>\lceil n/2\rceil\), \(A_{n,r}=0\). The formula includes \(n=0\) by convention: it has one rank-zero subspace and none of positive rank.

For odd prime \(p\) and \(n\geq2\), define the path graphical group \(G_n(p)\) as \(V\oplus W\) with \(V=\mathbb F_p^n\), \(W=\mathbb F_p^{n-1}\), and product

\[
(v,c)(v',c')=(v+v',c+c'+\tfrac12\beta(v,v')),
\qquad \beta(v,v')_i=v_i v'_{i+1}-v_{i+1}v'_i.
\]

Its derived subgroup is \(W\), its order is \(p^{2n-1}\), and it has nilpotency class two and exponent \(p\). Subgroups containing \(W\) are in bijection with linear subspaces of \(V\); abelianness is exactly common isotropy. The coordinate-support statistic is relative to the distinguished path presentation; it is not claimed to be invariant under arbitrary abstract group isomorphisms.

## Proof

**1. Column formulation.** Choose an ordered basis for an \(r\)-dimensional subspace \(U\) and form its \(r\times n\) matrix \(M\) of basis rows. Let \(c_i\in\mathbb F_q^r\) be column \(i\). For the bilinear form \(B_i\), common isotropy means every two-by-two minor of \([c_i\ c_{i+1}]\) vanishes. Thus consecutive columns are linearly dependent. Conversely, this condition implies all isotropy equations. The matrix has rank \(r\) exactly when the columns span \(\mathbb F_q^r\). Its support consists exactly of nonzero columns. Each subspace corresponds to precisely \(G_r(q)\) ordered row bases. This proves the reduction to dependent-adjacent-column sequences with full span. In a reduced-row-echelon basis, two consecutive pivot columns cannot both occur, since their adjacent minor would be nonzero. Thus the pivot set is an independent set of the path, giving \(r\leq\lceil n/2\rceil\); conversely, coordinate subspaces on independent sets attain every allowed rank.

**2. Transfer for sequences in dimension \(d\).** Let \(T_{n,d}(q;w)\) be the weighted number of \(n\)-term column sequences in \(\mathbb F_q^d\) with adjacent dependence, including sequences of lower span. For \(d\geq1\), put \(m_d=(q^d-1)/(q-1)\). Let \(a_n\) be the weight of sequences ending at zero, and \(b_n\) the weight of sequences ending at a nonzero vector on one specified projective line, summed over that line's \(q-1\) nonzero vectors. Then

\[
a_{n+1}=a_n+m_db_n,\qquad
b_{n+1}=(q-1)w(a_n+b_n).
\]

The transition matrix has trace \(1+(q-1)w\) and determinant \((q-q^d)w\). With \(T_{0,d}=1\) and \(T_{1,d}=1+(q^d-1)w\), the weighted count obeys

\[
T_{n+2,d}=(1+(q-1)w)T_{n+1,d}+(q^d-q)wT_{n,d}.
\]

For \(d=0\) the all-zero sequence is the only possibility, and the same recurrence and initial conditions hold. Taking ordinary generating functions gives

\[
\sum_{n\geq0}T_{n,d}(q;w)z^n=
\frac{1+(q^d-q)wz}{1-(1+(q-1)w)z-(q^d-q)wz^2}.
\]

**3. Gaussian-lattice inversion.** For a fixed \(r\)-space \(V\), the number of column sequences with span contained in a particular \(d\)-subspace is \(T_{n,d}\). Möbius inversion in the lattice of subspaces uses \(\mu(D,V)=(-1)^{r-d}q^{\binom{r-d}{2}}\) for \(\dim D=d\). There are \(\left[\begin{smallmatrix}r\\d\end{smallmatrix}\right]_q\) such subspaces. Therefore the number of sequences spanning all of \(V\) is

\[
\sum_{d=0}^r(-1)^{r-d}q^{\binom{r-d}{2}}
\left[\begin{smallmatrix}r\\d\end{smallmatrix}\right]_q T_{n,d}(q;w).
\]

Division by the free action of \(\mathrm{GL}_r(q)\) on ordered row bases gives the stated generating function, including the zero-rank and empty-path boundaries. At \(r=2\), algebraic cancellation of the three rational terms yields the displayed simple four-factor formula.

**4. Fixed-rank asymptotics.** Set \(w=e^t\) with complex \(t\) near zero. The transfer for dimension \(r\) has eigenvalues

\[
\lambda_\pm(t)=\frac{1+(q-1)e^t\pm\sqrt{(1+(q-1)e^t)^2+4(q^r-q)e^t}}2.
\]

At \(t=0\), \(\lambda_+(0)=\lambda_{q,r}>0\). For every \(d<r\) the dominant transfer eigenvalue is strictly smaller, and \(|\lambda_-(0)|<\lambda_+(0)\). This remains true uniformly for complex \(t\) in a sufficiently small neighborhood of zero. The coefficient of \(\lambda_+(t)^n\) in \(T_{n,r}\) is analytic and positive at zero; explicitly at zero it equals \((q^r-\lambda_-(0))/\Delta_{q,r}\). Hence, for some \(0<\rho<1\), uniformly near \(t=0\),

\[
\mathbb E[e^{tK_{n,r}}]=
\frac{a(t)}{a(0)}\left(\frac{\lambda_+(t)}{\lambda_+(0)}\right)^n
(1+O_{q,r}(\rho^n)),\qquad a(0)>0.
\]

Analytic differentiation yields the displayed expectation and variance. Differentiation of the quadratic equation for \(\lambda_+(t)\) gives

\[
\left.\frac{d}{dt}\log\lambda_+(t)\right|_{t=0}
=\frac12+\frac{q-2}{2\Delta_{q,r}},\qquad
\left.\frac{d^2}{dt^2}\log\lambda_+(t)\right|_{t=0}
=\frac{q(q^r-1)}{\Delta_{q,r}^3}>0.
\]

Expand the logarithm to second order at \(t=is/(\sigma_{q,r}\sqrt n)\); the characteristic functions of the centered, scaled variables tend to \(e^{-s^2/2}\) for every real \(s\). Lévy's continuity theorem proves the central limit theorem. At \(w=1\), retaining the unique dominant term also yields the stated \(C_{q,r}\lambda_{q,r}^n\) count.

**5. Group interpretation.** In \(G_n(p)\), the commutator of \((v,c)\) and \((v',c')\) is \((0,\beta(v,v'))\). Thus a subgroup containing \(W\) is abelian exactly when its image in \(V\) is common isotropic for \(B_1,\ldots,B_{n-1}\). Every \(r\)-space lifts to one such subgroup (its full preimage); quotient rank and support coincide. The group claims follow without importing any claim about exponent-four groups.

## Verification

Run `python3 verify.py` from the accompanying package. It compares the transfer-plus-Möbius coefficient polynomial against independent enumeration of reduced-row-echelon subspaces. It exhaustively checks \(86\) cases over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\), including all support sizes, and separately verifies the rank-two rational-series coefficients at several field orders. The verifier uses explicit \(\mathbb F_4\) multiplication with the irreducible polynomial \(u^2+u+1\).

Examples: for \((q,n,r)=(2,6,2)\), the weighted support polynomial is \(10w^2+28w^3+21w^4+4w^5\); for \((q,n,r)=(3,5,2)\), it is \(6w^2+22w^3+12w^4\). These are finite checks; no finite enumeration alone proves the universal formulas or limiting law.

## Relationship to prior work

Youming Qiao, *A q-analogue of graph independence polynomials with a group-theoretic interpretation*, arXiv:2408.09963 (first public August 19, 2024), establishes graph-uniform polynomiality of totally isotropic subspace counts and the odd-prime graphical-group interpretation. Neither these general existence statements nor their illustrative computations state the path-specific **bivariate support law in every rank**, its two-state recursive computation, or its explicit fixed-rank Gaussian limit. The work explicitly identifies more efficient recursive methods as an avenue for further research. The foundational graph-to-isotropy correspondence and group interpretation are prior facts, not new claims here.

Tobias Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564 (2021), identifies the graphical groups of paths as maximal class-two quotients of upper unitriangular groups and gives path conjugacy-class polynomials. These count conjugacy classes and their sizes, not central-containing abelian subgroups by quotient rank and coordinate support.

Bei, Chen, Guan, Qiao, and Sun, *From independent sets and vertex colorings to isotropic spaces and isotropic decompositions*, arXiv:1904.03950 (2019), establishes the maximum-isotropic-dimension correspondence and general graph/alternating-space foundations. Those results are credited, including the known bound \(r\leq\lceil n/2\rceil\).

General induced-subgraph component methods can already produce the **unweighted** isotropic rank counts by specialization, so unweighted path-rank counting alone is not claimed as new. The assessed contribution is the simultaneously support-refined all-rank law, its efficient bivariate transfer and exact Gaussian support density and variance. Full publication-priority verification remains provisional.

## Limitations

The full rank–support generating function concerns a **labeled path** and common isotropic vector subspaces of its graphical alternating matrix space. The group interpretation applies only over odd prime fields for exponent-prime graphical groups and counts only abelian subgroups containing the derived subgroup. It does not enumerate every abelian subgroup, and support depends on the canonical vertex coordinates. The limit takes path length to infinity with field order and quotient rank fixed; it is not a joint high-rank/high-length limit. The asymptotic theorem is proved from a spectral gap, not from the finite tests. A broader published weighted enumeration might subsume the result, so novelty remains conditional on the inspected literature.

## References

1. Y. Qiao, *A q-analogue of graph independence polynomials with a group-theoretic interpretation*, arXiv:2408.09963, first posted August 19, 2024, https://arxiv.org/html/2408.09963.
2. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564, first posted July 12, 2021; *Bull. London Math. Soc.* **54** (2022), 1923–1943, https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12665.
3. X. Bei, S. Chen, J. Guan, Y. Qiao, and X. Sun, *From independent sets and vertex colorings to isotropic spaces and isotropic decompositions*, arXiv:1904.03950, first posted April 8, 2019, https://arxiv.org/abs/1904.03950.
