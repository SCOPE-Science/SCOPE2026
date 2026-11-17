# The finite-rank truncated Toeplitz near-invariance bound is sharp in every rank

## Finding

For every integer \(n\geq1\), there is a scalar truncated Toeplitz operator on a finite-dimensional monomial model space and a perturbation of **rank exactly \(n\)** whose kernel has minimum nearly \(S^*\)-invariance defect **exactly \(2n+1\)**. Therefore the general \(2n+1\) upper bound of Chattopadhyay and Khan [1, Theorem 5.4] cannot be decreased at any perturbation rank, even for bounded analytic monomial symbols and finite-dimensional model spaces.

More precisely, put
\[
 k=2n+2,\qquad r=3n+4,\qquad N=k+r=5n+6,\qquad \theta(z)=z^N.
\]
Let \(e_t(z)=z^t\) for \(0\leq t<N\), viewed as the orthonormal monomial basis of \(K_\theta=H^2\ominus\theta H^2\). Let \(A=A_{z^k}^{\theta}\) and for \(1\leq j\leq n\) define
\[
 u_j=e_{3j},\qquad q_j=e_{r+2j},\qquad p_j=A u_j=e_{k+3j}.
\]
Set
\[
 B_n=A-\sum_{j=1}^{n}p_j\otimes q_j,
\]
where \((p\otimes q)f=\langle f,q\rangle p\). Then the perturbation has rank \(n\). Its kernel is the explicit graph
\[
 \mathcal M_n:=\ker B_n
 =\left\{\,g+\sum_{j=1}^{n}g_{r+2j}e_{3j}:
 g=\sum_{t=r}^{N-1}g_t e_t\,\right\}.
\]
Every member of \(\mathcal M_n\) vanishes at the origin, and
\[
 \boxed{\dim\frac{\mathcal M_n+S^*\mathcal M_n}{\mathcal M_n}=2n+1.}
\]
The displayed quotient dimension is precisely the smallest dimension of a nearly \(S^*\)-invariance defect space for \(\mathcal M_n\).

## Assumptions and scope

Work over the complex Hardy space \(H^2(\mathbb D)\). The compressed multiplication operator \(A_{z^k}^{\theta}\) acts on \(K_\theta\) by
\[
 A e_t=\begin{cases}e_{t+k},&t+k<N,\\0,&t+k\geq N.\end{cases}
\]
For a closed subspace \(\mathcal M\subset H^2\), its minimum near-invariance defect is the least integer \(d\) such that there exists a \(d\)-dimensional \(D\subset H^2\) satisfying \(f\in\mathcal M\) and \(f(0)=0\Rightarrow S^*f\in\mathcal M+D\). In the present construction \(\mathcal M_n\subset zH^2\); hence the least possible \(d\) equals \(\dim((\mathcal M_n+S^*\mathcal M_n)/\mathcal M_n)\).

All parameters and matrices are explicitly specified for every \(n\geq1\). No infinite-dimensional approximation is used to establish the lower bound.

## Proof

**Step 1: the finite-rank perturbation and its kernel.** Let \(U:\mathbb C^n\to K_\theta\) send its \(j\)-th coordinate vector to \(u_j\), and let \(Q:K_\theta\to\mathbb C^n\) be \((Qf)_j=\langle f,q_j\rangle\). The monomials \(u_j\) and \(q_\ell\) lie in disjoint coordinate blocks, so \(QU=0\). Consequently,
\[
 B_n=A(I-UQ),\qquad (I-UQ)^{-1}=I+UQ.
\]
Since the \(p_j=A u_j\) are distinct nonzero basis vectors and \(Q\) has full row rank, \(\operatorname{rank}(AUQ)=n\). The kernel of \(A\) is
\[
 G=\operatorname{span}\{e_r,e_{r+1},\dots,e_{N-1}\},
\]
so \(\ker B_n=(I+UQ)G\). This gives the displayed graph formula and shows \(\dim\mathcal M_n=k\). Its smallest occurring monomial degree is at least three, so \(\mathcal M_n\subset zH^2\).

**Step 2: exact quotient formula.** For \(g\in G\), set \(f=(I+UQ)g\). Removing the bottom monomial after applying the backward shift gives
\[
 h=S^*g-g_re_{r-1}\in G,
\qquad (Qh)_j=g_{r+2j+1}.
\]
Therefore
\[
 S^*f-(I+UQ)h
 =g_re_{r-1}
  +\sum_{j=1}^{n}g_{r+2j}e_{3j-1}
  -\sum_{j=1}^{n}g_{r+2j+1}e_{3j}.
\tag{1}
\]
Define
\[
 W=\operatorname{span}\{e_{r-1},e_{3j-1},e_{3j}:1\leq j\leq n\}.
\]
The \(2n+1\) displayed monomials are pairwise different, all have degree less than \(r\), and are linearly independent. Hence \(\dim W=2n+1\). Because projection of \(\mathcal M_n=(I+UQ)G\) onto the high-degree block \(G\) is the identity on \(G\), every vector of \(\mathcal M_n\cap W\) is zero.

The \(2n+1\) coefficients \(g_r\), \(g_{r+2j}\), and \(g_{r+2j+1}\) appearing in (1) are coordinate evaluations at pairwise distinct indices of \(\{r,\ldots,N-1\}\). Their values can therefore be prescribed independently. Equation (1) consequently shows that the image of \(S^*\mathcal M_n\) in \((\mathcal M_n+W)/\mathcal M_n\) is all of \(W\). Thus
\[
 \mathcal M_n+S^*\mathcal M_n=\mathcal M_n\oplus W,
 \qquad \dim\frac{\mathcal M_n+S^*\mathcal M_n}{\mathcal M_n}=2n+1.
\]

**Step 3: optimality.** Every vector of \(\mathcal M_n\) vanishes at zero, so the condition \(f(0)=0\) restricts no vector of \(\mathcal M_n\). If \(D\) is a nearly invariant defect space, then \(S^*\mathcal M_n\subset\mathcal M_n+D\), and the quotient dimension just computed forces \(\dim D\geq 2n+1\). Taking \(D=W\) realizes equality. Theorem 5.4 of [1] gives the same universal upper bound for arbitrary scalar truncated Toeplitz operators perturbed by \(n\) rank-one terms. Thus that universal coefficient and additive constant are simultaneously attained for every \(n\geq1\). \(\square\)

## Verification

The included self-contained `verify_defect.py` uses exact symbolic matrices (not floating-point tolerances) to check, for each integer \(1\le n\le8\), that \(QU=0\), the claimed inverse factorization, rank \(n\) of the perturbation, the exact kernel graph, the vanishing constant coefficient, and quotient rank \(2n+1\). Run with `python verify_defect.py` after installing SymPy. It prints `TRUNCATED_TOEPLITZ_SHARP_DEFECT_EXACT_OK 8` on successful completion.

The quantifier **every** \(n\geq1\) is proved by the coordinate argument, not by this finite checker.

## Relationship to prior work

Chattopadhyay and Khan [1, Theorem 5.4] prove the universal upper defect bound \(2n+1\) for kernels of finite-rank perturbed scalar truncated Toeplitz operators. They supply the upper estimate and several low-rank realizations of an auxiliary block Toeplitz construction, but do not establish attaining examples for each \(n\). The contribution here is an explicit family witnessing the exact **minimum** defect \(2n+1\), demonstrating that the published uniform bound is sharp in every rank.

O'Loughlin [2] gives a structural theory of nearly invariant subspaces with finite defect, including unperturbed truncated Toeplitz kernels. Liang and Partington [3] analyze finite-rank perturbations of ordinary Toeplitz operators on the full Hardy space; Chattopadhyay, Das and Pradhan [4] extend such methods to vector-valued Hardy spaces. Neither of those ordinary-Toeplitz settings identifies the sharp defect of the finite-dimensional compressed operators in the present family.

## Limitations

The construction treats scalar complex Hardy space and finite-degree inner functions. It proves sharpness of the existing general bound, not a new upper bound. It does not classify the defect of every finite-rank perturbation, nor give a dimension-minimizing example for fixed rank. A distinct earlier construction expressed in different notation is not excluded by the literature comparison; independent priority review has not occurred.

## References

[1] A. Chattopadhyay and A. Khan, *Perturbations of Truncated Toeplitz operators*, arXiv:2610.40295v1 (29 October 2026), Theorem 5.4, https://arxiv.org/html/2610.40295v1 .

[2] R. O'Loughlin, *Nearly Invariant Subspaces with Applications to Truncated Toeplitz Operators*, Complex Analysis and Operator Theory 14, article 86 (2020), https://doi.org/10.1007/s11785-020-01049-4 .

[3] Y. Liang and J. R. Partington, *Representing kernels of perturbations of Toeplitz operators by backward shift-invariant subspaces*, arXiv:1911.10072, https://arxiv.org/abs/1911.10072 .

[4] A. Chattopadhyay, S. Das and C. Pradhan, *Kernels of Perturbed Toeplitz Operators in vector-valued Hardy spaces*, arXiv:2005.02255, https://arxiv.org/abs/2005.02255 .
