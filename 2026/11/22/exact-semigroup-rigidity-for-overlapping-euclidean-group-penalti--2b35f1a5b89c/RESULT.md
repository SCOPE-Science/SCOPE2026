# Exact semigroup rigidity for overlapping Euclidean group penalties

## Finding

Let \(n\ge1\). Let \(G_1,\dots,G_m\subseteq\{1,\dots,n\}\) be nonempty sets, \(m\ge1\), with positive weights \(w_1,\dots,w_m\). For \(x\in\mathbb R^n\), define
\[
F(x)=\sum_{k=1}^{m}w_k\|x_{G_k}\|_2,\qquad
T_t(x)=\mathop{\mathrm{argmin}}_{z\in\mathbb R^n}
\left\{\frac12\|z-x\|_2^2+tF(z)\right\},\quad t\ge0.
\]
Then the following statements are equivalent:

1. \(T_s(T_t(x))=T_{s+t}(x)\) for every \(x\in\mathbb R^n\) and every \(s,t\ge0\).
2. For every \(k,\ell\), either \(G_k=G_\ell\) or \(G_k\cap G_\ell=\varnothing\).

Thus duplicate groups may be merged by adding their positive weights; after merging, **pairwise disjointness is necessary and sufficient for the full parameter-additive proximal semigroup**. Whenever two distinct groups overlap, there is a strictly positive \(x\) with
\[
T_h(T_h(x))-T_{2h}(x)
=-h^2\nabla^2F(x)\nabla F(x)+O_x(h^3),
\qquad \nabla^2F(x)\nabla F(x)\ne0,
\]
so failure occurs even at arbitrarily small positive \(h\).

For \(G_1=\{1,2\}\), \(G_2=\{2,3\}\), \(w_1=w_2=1\), and \(x=(1,1,1)\), the coefficient is explicit:
\[
T_h(T_h(x))-T_{2h}(x)
=h^2(1/4,-1/2,1/4)+O(h^3).
\]

## Assumptions and scope

All spaces are real Euclidean spaces; \(x_G\) is the coordinate subvector with indices in \(G\). Every group is nonempty and every coefficient is strictly positive. The quadratic fidelity has coefficient \(1/2\). The objective is strongly convex, so \(T_t\) is single-valued for every \(t\ge0\). Coordinates outside the union of the groups remain unchanged. Repeated group sets are permitted. This is the **direct sum-of-group-Euclidean-norms** penalty, not a latent-variable/infimal-convolution version of overlapping group lasso.

## Proof

**Sufficiency.** When distinct groups are disjoint, merge equal sets and write their aggregate weights as \(W_G>0\). The minimization separates across groups, and on any group \(G\) it is radial soft thresholding:
\[
(T_t(x))_G=\left(1-\frac{tW_G}{\|x_G\|_2}\right)_+x_G
\]
when \(x_G\ne0\), and zero for \(x_G=0\). If the first step does not annihilate the block, its norm decreases by exactly \(tW_G\); subsequent shrinkage by \(sW_G\) equals single-step shrinkage by \((s+t)W_G\). If annihilated, all subsequent outputs are zero. The identity follows block by block, including untouched coordinates and zero blocks.

**Local resolvent calculus.** Let \(x\in(0,\infty)^n\). Each \(x_{G_k}\) is nonzero and \(F\) is real analytic near \(x\). Set \(g=\nabla F(x)\) and \(H=\nabla^2F(x)\). The proximal optimality equation \(z+t\nabla F(z)=x\), and the implicit function theorem at \((z,t)=(x,0)\), give
\[
T_h(x)=x-hg+h^2Hg+O_x(h^3).
\]
Applying the expansion once again, with first-step input \(T_h(x)\), gives
\[
T_h(T_h(x))=x-2hg+3h^2Hg+O_x(h^3),\qquad
T_{2h}(x)=x-2hg+4h^2Hg+O_x(h^3).
\]
Consequently global time-additivity would imply \(Hg=0\) at every strictly positive \(x\).

**Positive-semidefinite obstruction.** Let \(P_G\) be coordinate projection onto \(G\) and \(u_G=P_Gx/\|x_G\|_2\) its normalized extension in \(\mathbb R^n\). Direct differentiation gives
\[
H=\sum_k\frac{w_k}{\|x_{G_k}\|_2}(P_{G_k}-u_{G_k}u_{G_k}^{\mathsf T}),\qquad
 g_i=x_i c_i(x),\qquad c_i(x)=\sum_{k:i\in G_k}\frac{w_k}{\|x_{G_k}\|_2}.
\]
Every summand in \(H\) is positive semidefinite. Therefore, \(Hg=0\) implies \(g^{\mathsf T}Hg=0\) and each \(g_{G_k}\) is proportional to \(x_{G_k}\). Since all \(x_i>0\), this forces
\[
c_i(x)=c_j(x)\quad\text{for all }i,j\in G_k,\quad\text{for every }k.
\]

**A finite witness for every overlap.** Suppose distinct groups overlap. There exist \(i\ne j\) belonging to a common group, with at least one group containing \(i\) but not \(j\). Indeed, choose an intersecting unequal pair and take the shared coordinate plus a coordinate in their symmetric difference, interchanging the roles if needed. Put
\[
L=\sum_{k:i\in G_k,\,j\notin G_k}w_k>0,\qquad
R=\sum_{k:j\in G_k,\,i\notin G_k}\frac{w_k}{\sqrt{|G_k|}}\ge0.
\]
Take \(x_i=M\) and \(x_\ell=1\) for all \(\ell\ne i\). Choose \(M=1\) if \(R=0\), and any \(M>L/R\) if \(R>0\). Contributions from groups containing both \(i,j\) cancel when subtracting \(c_i-c_j\); the positive contributions from groups containing \(i\) but not \(j\) total at most \(L/M\), whereas the opposite contributions equal \(R\). Thus \(c_i(x)-c_j(x)\ne0\). Because \(i,j\) are in a common group, its positive-semidefinite Hessian term has strictly positive quadratic form on \(g\); hence \(g^{\mathsf T}Hg>0\) and \(Hg\ne0\). The local splitting coefficient above is nonzero, contradicting the semigroup identity. This argument also covers nested unequal groups and singleton groups.

**Smallest explicit overlapping pair.** For \(F(x)=\sqrt{x_1^2+x_2^2}+\sqrt{x_2^2+x_3^2}\), at \(x=(1,1,1)\),
\[
g=(1/\sqrt2,\sqrt2,1/\sqrt2),\quad
Hg=(-1/4,1/2,-1/4),\quad
g^{\mathsf T}Hg=\sqrt2/4>0.
\]
These are exact identities obtained by differentiating the two square roots. They give the stated nonzero quadratic two-step discrepancy.

## Verification

Run `python checker.py` with Python, NumPy and SciPy. The checker evaluates the explicit Hessian, tests the small-example quadratic defect with shrinking step sizes, constructs strict positive witnesses for every non-partition family up to three coordinates (and sampled four-coordinate families), and checks the exact disjoint-block shrinkage identity. During preparation it passed **1,044 supplementary assertions**. The quantified all-dimensional classification follows from the proof, not from finite enumeration, numerical solvers or fitted remainders.

## Relationship to prior work

Liu and Ye (2010) study the proximal map for the same direct overlapping-group regularizer and its dual optimization, but do not state a universal parameter-composition classification. Qi and Li (2022), the motivating later source, study separable approximation and statistical properties of the overlapping-group penalty. Mairal, Jenatton, Obozinski and Bach (2011) study structured sparsity and proximal/network-flow algorithms. Bungert, Burger, Chambolle and Novaga (2019, revised 2021), especially their Theorem 4.5, give broader abstract conditions under which one-homogeneous gradient flows agree with variational minimizers. Such conditions provide relevant conceptual background but do not directly supply the explicit if-and-only-if overlap criterion for finite weighted Euclidean-group sums or its local second-order witness. The Moreau *envelope* semigroup under infimal convolution must not be confused with exact semigroup composition of proximal **maps**. The novelty assessment is limited to inspected accessible texts and semantic searches, not proof of global historical uniqueness.

## Limitations

The result concerns finite-dimensional real direct group-Euclidean penalties with strictly positive coefficients. It does not classify latent/infimal-convolution group norms, non-Euclidean block norms, infinitely many groups, nonlinear data fidelities, or arbitrary sums of convex one-homogeneous functionals. The displayed nonzero splitting defect is local as \(h\downarrow0\), not an exact finite-step formula. Older unindexed or non-English equivalent formulations may exist, and independent mathematical review has not occurred.

## References

1. M. Qi and T. Li, *The non-overlapping statistical approximation to overlapping group lasso*, arXiv:2211.09221, first submitted 2022-11-16. https://arxiv.org/abs/2211.09221
2. J. Liu and J. Ye, *Fast Overlapping Group Lasso*, arXiv:1009.0306, first submitted 2010-09-02. https://arxiv.org/abs/1009.0306
3. J. Mairal, R. Jenatton, G. Obozinski and F. Bach, *Convex and Network Flow Optimization for Structured Sparsity*, JMLR 12 (2011). https://jmlr.org/papers/v12/mairal11a.html
4. L. Bungert, M. Burger, A. Chambolle and M. Novaga, *Nonlinear Spectral Decompositions by Gradient Flows of One-Homogeneous Functionals*, arXiv:1901.06979, first submitted 2019-01-21, Section 4.2. https://arxiv.org/abs/1901.06979
