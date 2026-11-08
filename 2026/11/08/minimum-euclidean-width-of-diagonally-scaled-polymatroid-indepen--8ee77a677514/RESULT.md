# Minimum Euclidean width of diagonally scaled polymatroid independence polytopes

## Finding
Let \(E\) be a nonempty finite set, let \(f:2^E\to\mathbb R_{\ge0}\) be normalized, monotone, and submodular, with \(f(\{e\})>0\) for every \(e\in E\), and let \(s_e>0\). Define
\[
P_f=\left\{x\in\mathbb R_{\ge0}^E:\sum_{e\in S}x_e\le f(S)\ \text{for every }S\subseteq E\right\},\qquad K=\operatorname{diag}(s_e)P_f.
\]
For a compact convex body \(K\), write \(w_K(u)=\max_{x\in K}\langle u,x\rangle-\min_{x\in K}\langle u,x\rangle\) for its width in a unit direction \(u\). Put \(c(S)=\sum_{e\in S}s_e^{-2}\). Then
\[
\boxed{\min_{\|u\|_2=1}w_K(u)=\min_{\emptyset\ne S\subseteq E}\frac{f(S)}{\sqrt{c(S)}}.}
\]
Moreover, **all** minimizing unit directions, without exception, are
\[
\boxed{u_e=\begin{cases}\sigma s_e^{-1}/\sqrt{c(S)},&e\in S,\\0,&e\notin S,\end{cases}\quad \sigma\in\{-1,1\},\quad S\in\arg\min_{\emptyset\ne T\subseteq E}\frac{f(T)}{\sqrt{c(T)}}.}
\]
In particular, for a loopless matroid \(M\), with rank function \(r_M\), every minimizing support is a flat whose restriction is connected. For the unscaled independence polytope of the uniform matroid \(U_{r,n}\) (\(1\le r\le n\)), the minimum width is \(\min\{1,r/\sqrt n\}\): the only minimizing directions are signed coordinate axes for \(n<r^2\), the only ones are signed all-ones directions for \(n>r^2\), and both kinds attain the minimum at \(n=r^2\). More generally the displayed full minimizing-direction formula describes all ties.

## Assumptions and scope
Here \(f(\varnothing)=0\); submodularity means \(f(A)+f(B)\ge f(A\cup B)+f(A\cap B)\) for all \(A,B\subseteq E\). All weights \(s_e\) are strictly positive. Positivity of singleton capacities ensures that \(P_f\) and \(K\) are full-dimensional. No integrality or matroid representability is assumed. Distances and unit normals always use the ordinary ambient Euclidean metric after applying the diagonal map, not an intrinsic metric on a base-polytope hyperplane.

## Proof
**Support-function reduction.** Because \(P_f\subseteq\mathbb R_{\ge0}^E\) is down-closed, maximizing a linear form of arbitrary coefficients discards the negative ones: \(h_{P_f}(v)=h_{P_f}(v_+)\). For \(v\ge0\), let \(S_t=\{e:v_e\ge t\}\) for \(t>0\). The standard polymatroid greedy theorem (proved by sorting the coefficients and telescoping the submodular rank increments) gives
\[
h_{P_f}(v)=\int_0^\infty f(S_t)\,dt.
\]
Indeed, for any order \(v_{e_1}\ge\cdots\ge v_{e_m}\ge0\), set \(A_j=\{e_1,\ldots,e_j\}\). The greedy point with entries \(f(A_j)-f(A_{j-1})\) is nonnegative, lies in \(P_f\) by diminishing returns, and has scalar product \(\sum_j(v_{e_j}-v_{e_{j+1}})f(A_j)\), with \(v_{e_{m+1}}=0\). Every point of \(P_f\) has scalar product at most that sum by the defining subset inequalities. Thus the integral identity holds, including tied levels.

**Lower bound.** Set
\[
R=\max_{\emptyset\ne S\subseteq E}\frac{\sqrt{c(S)}}{f(S)}<\infty.
\]
For any \(v\ge0\), the layer-cake identity and the triangle inequality for Euclidean vector integrals imply
\[
\|\operatorname{diag}(s_e^{-1})v\|_2
=\left\|\int_0^\infty\operatorname{diag}(s_e^{-1})\mathbf1_{S_t}\,dt\right\|_2
\le\int_0^\infty\sqrt{c(S_t)}\,dt
\le R\int_0^\infty f(S_t)\,dt=R h_{P_f}(v).
\]
Apply this separately to \(v=(\operatorname{diag}(s)u)_+\) and \(v=(\operatorname{diag}(s)u)_-\). Their inverse-scaled Euclidean norms are \(\|u_+\|_2\) and \(\|u_-\|_2\). Therefore
\[
w_K(u)=h_{P_f}((\operatorname{diag}(s)u)_+)+h_{P_f}((\operatorname{diag}(s)u)_-)
\ge R^{-1}(\|u_+\|_2+\|u_-\|_2)\ge R^{-1}\|u\|_2.
\]
For a unit \(u\), the last quantity is \(R^{-1}\).

**Sharpness.** If \(S\ne\varnothing\) attains the defining minimum, choose \(u_e=s_e^{-1}\mathbf1_S(e)/\sqrt{c(S)}\). Then \(\|u\|_2=1\); its scaled positive coefficients equal the constant \(1/\sqrt{c(S)}\) on \(S\). The support value is \(f(S)/\sqrt{c(S)}=R^{-1}\), the opposite support is zero, and the same conclusion holds for \(-u\).

**Exhaustive equality classification.** If a unit direction attains equality, the last inequality \(\|u_+\|_2+\|u_-\|_2\ge\sqrt{\|u_+\|_2^2+\|u_-\|_2^2}\) is an equality only if one sign part is zero. Assume \(u\ge0\) after changing sign. Equality in the vector-integral triangle inequality implies that the nonzero vectors \(\operatorname{diag}(s_e^{-1})\mathbf1_{S_t}\) are collinear for almost every positive level \(t\). Since all diagonal weights are positive and the vectors have zero-or-fixed-positive entries, two nonempty nested level sets give collinear vectors only if the sets are identical. Thus the scaled positive coefficient vector is constant on a single nonempty support \(S\). Equality in \(\sqrt{c(S_t)}\le R f(S_t)\) forces \(S\) to attain the global minimum. Normalization gives exactly the displayed formula.

**Matroid support structure.** When \(f=r_M\), a minimizing \(S\) must be a flat: otherwise adjoining any nonloop \(e\in\operatorname{cl}(S)\setminus S\) keeps rank fixed but strictly increases \(c(S)\), contradicting minimality. It must have connected restriction: if \(S=A\sqcup B\), with both nonempty and \(r_M(S)=r_M(A)+r_M(B)\), then positive rank and weights yield
\[
\frac{r_M(S)}{\sqrt{c(S)}}>
\min\left\{\frac{r_M(A)}{\sqrt{c(A)}},\frac{r_M(B)}{\sqrt{c(B)}}\right\},
\]
a contradiction. For \(U_{r,n}\), subsets of cardinality \(k\le r\) have quotient \(\sqrt k\), minimized at \(k=1\), and subsets of cardinality \(k\ge r\) have quotient \(r/\sqrt k\), minimized at \(k=n\). Comparing \(1\) and \(r/\sqrt n\) proves the rank-square transition.

## Verification
Run `python3 verify.py` with Python 3 standard library. The fixed-seed checker checks the submodular inequalities exactly for 126 generated rank/capacity profiles (coverage polymatroids, binary-representable matroids, and partition matroids), verifies support widths of 160 minimizing supports, and tests 15,120 additional random unit normals against the bound. It also checks the uniform-matroid quotient formula for finite parameters. Observed output: `POLYMATROID_WIDTH_FINITE_CHECKS_PASSED profiles= 126 critical_sets= 160 random_normals= 15120`. These finite tests do not establish the universal theorem; its proof is above.

## Relationship to prior work
The greedy support-function formula and layer-cake extension are classical polymatroid results, as presented in Bach's survey and Lovász's treatment of submodular set functions. Lasoń and Michałek analyze algebraic properties of matroid independence polytopes, while Berggren, Martin, and Samper investigate generalized matroidal polyhedra. The present geometric statement concerns **minimum ambient Euclidean width, all equality directions, and the rank-square transition**; none of the inspected statements identifies this invariant. Nearby exact inball, minimum enclosing sphere, and Minkowski-asymmetry results optimize different functionals and do not imply an exact minimum-width classification. Historical priority remains provisional; an equivalent result in polyhedral thickness, norm/gauge, or submodular optimization terminology could exist.

## Limitations
The theorem does not cover signed/nonmonotone submodular functions, zeros among singleton capacities, arbitrary non-diagonal linear maps, matroid **base** polytopes with intrinsic width, or non-Euclidean width norms. Determining a minimizing support may require nontrivial combinatorial optimization. No polynomial-time algorithm, novel polytope face census, or independent audit is claimed.

## References
1. M. Lasoń and M. Michałek, *On algebraic properties of matroid polytopes*, arXiv:2005.08359, first public version 2020-05-17, https://arxiv.org/abs/2005.08359.
2. J. Berggren, J. L. Martin, and J. A. Samper, *Unbounded Matroids*, arXiv:2312.02040, https://arxiv.org/abs/2312.02040.
3. L. Lovász, *Submodular setfunctions, matroids and graph limits*, arXiv:2302.04704, https://arxiv.org/abs/2302.04704.
4. F. Bach, *Learning with Submodular Functions: A Convex Optimization Perspective*, arXiv:1111.6453, https://arxiv.org/abs/1111.6453.
