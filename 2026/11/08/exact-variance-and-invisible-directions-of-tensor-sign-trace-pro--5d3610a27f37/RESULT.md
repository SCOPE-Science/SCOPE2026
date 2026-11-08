# Exact variance and invisible directions of tensor-sign trace probes

## Finding

Let \(k\geq1\) and \(d_1,\ldots,d_k\geq1\) be integers, \(D=\prod_{j=1}^{k}d_j\), and \(A\in\mathbb R^{D\times D}\) be symmetric. Draw independent Rademacher sign vectors \(s^{(j)}\in\{-1,1\}^{d_j}\) and use the rank-one tensor probe \(v=s^{(1)}\otimes\cdots\otimes s^{(k)}\) to estimate \(\operatorname{tr}A\) by \(Q_A=v^{\mathsf T}Av\).

For each coordinate pair \(\alpha\prec\beta\) in \(\prod_j\{1,\ldots,d_j\}\), define its *pair pattern* \(\pi(\alpha,\beta)\) as follows: the \(j\)-th component is empty if \(\alpha_j=\beta_j\), and otherwise is the unordered pair \(\{\alpha_j,\beta_j\}\). For each nonempty pattern \(P\), let \(G_P\) be the set of coordinate pairs with pattern \(P\), and define

\[
 c_P(A)=2\sum_{\{\alpha,\beta\}\in G_P} A_{\alpha\beta}.
\]

Here \(\alpha\prec\beta\) is merely a device to count each unordered coordinate pair once. Let \(J(P)\) be the set of nonempty components of the pattern. Then \(|G_P|=g_P=2^{|J(P)|-1}\prod_{j\notin J(P)}d_j\). The exact one-probe variance is

\[
\boxed{\operatorname{Var}(Q_A)=\sum_{P\ne\varnothing}c_P(A)^2.}
\]

The space \(\mathcal K\) of symmetric matrices for which **every** tensor-sign probe returns the exact trace is exactly the simultaneous kernel of the \(c_P\), with

\[
\boxed{\dim\mathcal K=\frac{D(D+1)}2-\left[\prod_{j=1}^k\left(1+\binom{d_j}{2}\right)-1\right].}
\]

This is a complete classification, not merely a sufficient criterion. Its coefficients are mutually independent linear functionals. Moreover, its Frobenius-distance refinement is exact:

\[
\boxed{\operatorname{dist}_F(A,\mathcal K)^2=\frac12\sum_{P\ne\varnothing}\frac{c_P(A)^2}{g_P}.}
\]

In particular, with \(g_{\min}\) and \(g_{\max}\) the minimum and maximum nonempty group sizes (for \(D\ge2\)),

\[
2g_{\min}\operatorname{dist}_F(A,\mathcal K)^2\le\operatorname{Var}(Q_A)\le2g_{\max}\operatorname{dist}_F(A,\mathcal K)^2,
\]

and both coefficients are attained, even after adding a sufficiently large positive multiple of the identity so that the witness matrices are positive definite. For exactly two factors with \(d_1=m\ge2\), \(d_2=n\ge2\), these optimal constants are \(4\) and \(2\max\{m,n\}\).

A consequence that distinguishes tensor-sign probes from independent-coordinate Hutchinson probes: non-diagonal *positive definite* matrices can have zero variance under tensor probes while having strictly positive variance under independent Rademacher probes. Conversely, tensor probes can double the variance of independent probes even in dimension four.

## Assumptions and scope

All matrices are real symmetric, all sign coordinates are independent and uniform on \(\{-1,1\}\), and all tensor factors are independently sampled. The statement concerns a **single** quadratic-form trace sample. For the average of \(N\ge1\) independent samples, every variance formula is divided by \(N\). The theorem imposes no positivity assumption on \(A\), although the explicit contrasts below can be chosen positive definite. Degenerate factor dimension \(d_j=1\) is permitted; when \(D=1\) there are no nonempty patterns, the variance is zero, and distance formulas with group extrema are omitted.

For two factors, the coefficient formula is particularly transparent. Write \(A_{ia,jb}\) for the matrix indexed by \((i,a)\) and \((j,b)\). Orthogonality of Walsh characters gives

\[
\begin{aligned}
\operatorname{Var}(Q_A)/4={}&\sum_{i<j}\left(\sum_a A_{ia,ja}\right)^2
+\sum_{a<b}\left(\sum_i A_{ia,ib}\right)^2\\
&+\sum_{i<j}\sum_{a<b}\left(A_{ia,jb}+A_{ib,ja}\right)^2.
\end{aligned}
\]

For the ordered coordinates \((1,1),(1,2),(2,1),(2,2)\), set

\[
K_{\pm}=\begin{pmatrix}0&0&0&1\\0&0&\pm1&0\\0&\pm1&0&0\\1&0&0&0\end{pmatrix},
\quad A_{\pm}(t)=I_4+tK_{\pm},\quad 0<t<1.
\]

Both are strictly positive definite because \(K_{\pm}^2=I_4\). Under tensor-sign probes, the \(-\) case satisfies \(Q_{A_{-}(t)}\equiv4\) and \(\operatorname{Var}(Q_{A_{-}(t)})=0\), whereas the \(+\) case has \(\operatorname{Var}(Q_{A_{+}(t)})=16t^2\). Under a fully independent four-coordinate Rademacher probe either matrix has variance \(8t^2\). This is a fixed-basis comparison of two valid trace estimators, not a comparison of their computational costs.

## Proof

**Step 1: exact orthogonal Fourier modes.** For each pattern \(P\), let \(\chi_P\) denote the product of the two sign coordinates in every factor where \(P\) specifies an unordered pair; its contribution is one in factors where \(P\) is empty. Expanding a symmetric quadratic form gives

\[
Q_A=\sum_\alpha A_{\alpha\alpha}+2\sum_{\alpha\prec\beta}A_{\alpha\beta}v_\alpha v_\beta
=\operatorname{tr}A+\sum_{P\ne\varnothing}c_P(A)\chi_P.
\]

The identity uses \((s^{(j)}_a)^2=1\). Each distinct nonempty \(\chi_P\) is a distinct Walsh character on the product of all sign cubes. Consequently it has mean zero, its square equals one, and it is orthogonal in expectation to every other character. This proves unbiasedness and the exact variance formula without moment inequalities.

**Step 2: linear independence of all coefficient constraints.** To realize any nonempty pattern, choose opposite endpoints in each active factor, and choose any common coordinate in every inactive factor. Hence the patterns are all present. For a fixed pattern with \(r=|J(P)|\ge1\), the active factors admit \(2^r\) ordered choices of opposite endpoints, and division by two accounts for interchange of the two full multi-indices; each inactive factor contributes \(d_j\) common-index choices. Thus \(|G_P|=2^{r-1}\prod_{j\notin J(P)}d_j\). Distinct patterns partition the off-diagonal matrix entries, and each \(c_P\) has a nonzero coefficient on its own disjoint group. They are linearly independent, giving codimension \(\prod_j(1+\binom{d_j}{2})-1\) and the stated kernel dimension. Vanishing variance is equivalent to the vanishing of every nonconstant Walsh coefficient, which is equivalent to an exactly constant estimator on all sign assignments.

**Step 3: exact Frobenius projection.** On a fixed off-diagonal group \(G_P\), the kernel constraint is that the corresponding upper-triangular entries sum to zero. The unique Euclidean projection of those \(g_P\) entries onto that hyperplane subtracts their mean. The squared loss in the *symmetric matrix Frobenius norm* is twice the sum of squared changes to upper-triangular entries, namely \(2(\sum_{G_P}A_{\alpha\beta})^2/g_P=c_P(A)^2/(2g_P)\). All groups and diagonals are mutually orthogonal. Summing gives the exact distance identity and sharp bounds. For any single pattern, take a symmetric matrix supported on that pattern to attain its group-size constant. Adding a sufficiently large scalar identity preserves variance and distance while making the matrix positive definite.

**Step 4: two-factor constants and witnesses.** With two nontrivial factors, a nonempty pattern is active in either first factor, second factor or both. The group sizes are respectively \(n\), \(m\), and \(2\), proving the stated extrema. Direct multiplication gives \(K_{\pm}^2=I_4\), and the two possible off-diagonal cross contributions have coefficients \(2(t\pm t)\). Therefore their tensor variances are \(0\) and \(16t^2\). For independent signs \(z\in\{-1,1\}^4\), the classical quadratic-form identity \(\operatorname{Var}(z^{\mathsf T}Az)=4\sum_{i<j}A_{ij}^2\) gives \(8t^2\) for each witness.

## Verification

Run `python3 verify.py` from the same directory as this file. The standard-library-only checker uses exact integer and rational arithmetic. It enumerates every sign assignment for tensor dimensions \((2,2)\), \((2,3)\), \((3,2)\), \((2,2,2)\), and \((2,3,2)\), compares sample variances against the pattern formula, reconstructs the orthogonal projection and its Frobenius distance, checks group multiplicities and coefficient independence, and verifies both four-coordinate positive-definite witnesses. The recorded run passed 247 assertions.

These finite checks verify examples and implementation; the proof above establishes all integer dimensions and all real symmetric matrices, independent of computation. The code does not attempt numerical certification of a statement over infinitely many dimensions.

## Relationship to prior work

Bujanović and Kressner (arXiv:2004.06433, first submitted 2020-04-14) introduce trace estimators with rank-one Rademacher and Gaussian probes and prove unbiasedness and probability inequalities; their sections 2.4 and 3 do not give the exact Walsh variance kernel or its dimension. Meyer and Avron (arXiv:2309.04952, first submitted 2023-09-10) prove an exact *Gaussian* Kronecker-probe variance identity based on partial traces/transposes, and explicitly provide an *upper bound* for Rademacher probes, not an equality with its full zero-variance space. Ahle and collaborators (arXiv:1909.01410, 2019) study tensor sketch embeddings and moment bounds rather than the matrix-specific zero-variance classification. The classical Hutchinson variance law applies to independent-coordinate signs, which the tensor coordinates do not satisfy.

The present result determines the exact Rademacher tensor variance, all matrices invisible to its stochastic component, the rank of that measurement, and its Frobenius conditioning. It is not a new trace estimator, and the Gaussian exact variance, tensor-probe unbiasedness, general worst-case concentration estimates and classical independent-sign variance are established prior results.

## Limitations

The variance and kernel depend on the factorization and coordinate basis. They are not determined by the eigenvalues of the matrix and do not imply that tensor probes outperform independent probes for arbitrary operators. The operator-relative cost of Kronecker-vector multiplication is problem-dependent. The theorem concerns real sign probes only; Gaussian/complex probes and arbitrary non-product distributions have different fourth moments. It provides neither a distribution-free high-probability optimality statement nor an independent novelty certification. Related tensor-chaos and partial-transpose formulations could yield previously unnoticed equivalent special cases; that is an outstanding literature-precedence risk.

## References

1. Z. Bujanović and D. Kressner, *Norm and trace estimation with random rank-one vectors*, arXiv:2004.06433 (v1 2020-04-14; v2 2020-08-09), https://arxiv.org/html/2004.06433v2.
2. R. A. Meyer and H. Avron, *Hutchinson's Estimator is Bad at Kronecker-Trace-Estimation*, arXiv:2309.04952 (2023-09-10), https://arxiv.org/abs/2309.04952.
3. T. D. Ahle et al., *Oblivious Sketching of High-Degree Polynomial Kernels*, arXiv:1909.01410 (2019-09-03), https://arxiv.org/abs/1909.01410.
4. H. Avron and S. Toledo, *Randomized algorithms for estimating the trace of an implicit symmetric positive semi-definite matrix*, J. ACM 58(2), 2011. (Classical independent-sign variance comparison.)
