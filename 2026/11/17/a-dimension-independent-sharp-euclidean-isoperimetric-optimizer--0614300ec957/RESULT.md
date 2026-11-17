# A dimension-independent sharp Euclidean isoperimetric optimizer for uniform chainlink polytopes

## Finding

For every integer \(s\ge3\), let the *uniform chainlink polytope* be
\[
P_s(t)=\left\{x\in[0,1]^s:x_i-x_{i+1}\le 1-t\text{ for }i=1,\ldots,s\right\},
\qquad x_{s+1}=x_1,\quad 0\le t\le \tfrac12.
\]
Let \(f_s(t)=\operatorname{Vol}_s(P_s(t))\), \(S_s(t)=\mathcal H^{s-1}(\partial P_s(t))\), and \(Q_s(t)=S_s(t)/f_s(t)^{(s-1)/s}\), the Euclidean surface area after normalizing to unit volume. Then
\[
\begin{aligned}
\lambda_{\pm}(t)&=\frac{1\pm\sqrt{1-2t^2}}{2},\\
f_s(t)&=\lambda_+(t)^s+\lambda_-(t)^s,\\
S_s(t)&=2s f_s(t)+(2-\sqrt2-2t)f_s'(t).
\end{aligned}
\]
The **unique global minimizer of \(Q_s\)** on \([0,1/2]\) is
\[
\boxed{t_*=1-\frac1{\sqrt2},}
\]
**independently of the dimension \(s\)**. The quotient decreases strictly up to this point and increases strictly thereafter. Its exact minimum is
\[
\boxed{Q_s(t_*)=2s\left(\alpha_+^s+\alpha_-^s\right)^{1/s}},\qquad
\alpha_{\pm}=\frac{1\pm\sqrt{2\sqrt2-2}}2.
\]
For every \(s\ge3\), this is strictly below the cube's equal-volume quotient \(2s\). The sharp ratio tends to \(\alpha_+=0.955089860562\ldots\) as \(s\to\infty\). Thus cyclic corner truncation reduces the fixed-volume Euclidean boundary area by a limiting fraction \(1-\alpha_+=0.044910139438\ldots\).

A companion identity evaluates the **entire Euclidean surface area** of the real, not necessarily uniform, chainlink family. Let \(s\ge3\), \(a_i>0\), and \(0<2\ell<\min_i a_i\). Put
\[
P(\mathbf a,\ell)=\left\{x\in\mathbb R^s:0\le x_i\le a_i,\quad x_i-x_{i+1}\le a_i-\ell\right\}
\]
with cyclic indices, and let \(V(\mathbf a,\ell)\) and \(S(\mathbf a,\ell)\) be its ordinary Euclidean volume and surface area. Then
\[
\boxed{S(\mathbf a,\ell)=2\sum_{i=1}^s\frac{\partial V}{\partial a_i}+(2-\sqrt2)\frac{\partial V}{\partial\ell}.}
\]
Here \(V\) is explicitly the matrix trace in Proposition 6.8 of the cited primary source:
\[
V(\mathbf a,\ell)=\operatorname{tr}\left[\prod_{i=1}^s
\begin{pmatrix}a_i&-\ell^2/2\\1&0\end{pmatrix}\right].
\]
The identities for the uniform family extend continuously to both endpoints.

## Assumptions and scope

All volumes and boundary measures are ordinary Euclidean (Lebesgue and Hausdorff) measures in their indicated full ambient dimension, not lattice-normalized facet measures. The cyclic convention is \(x_{s+1}=x_1\). The surface identity with arbitrary \(\mathbf a\) is asserted in the open admissible range \(0<2\ell<\min_i a_i\), in which its indicated facet families are stable; the uniform closed-interval formula follows by continuity. The isoperimetric optimality is **within the one-parameter uniform chainlink family**, compared after rescaling each body to a fixed volume; it is not an inequality over all convex bodies.

## Proof

**1. Boundary area from volume derivatives.** Denote by \(U_i\) and \(L_i\) the Euclidean \((s-1)\)-areas of the faces supported by \(x_i=a_i\) and \(x_i=0\). Denote by \(D_i\) the area of the diagonal facet supported by \(x_i-x_{i+1}=a_i-\ell\). The unit outward normal to this last facet is \((e_i-e_{i+1})/\sqrt2\); its offset changes by \(1/\sqrt2\) per unit change in \(a_i\) and by \(-1/\sqrt2\) per unit change in \(\ell\). First variation under shifts of supporting hyperplanes therefore gives
\[
\frac{\partial V}{\partial a_i}=U_i+\frac{D_i}{\sqrt2},\qquad
\frac{\partial V}{\partial\ell}=-\sum_i\frac{D_i}{\sqrt2}.
\]
The vector identity \(\sum_F\operatorname{Area}(F)n_F=0\) for the boundary of any polytope, dotted with \(\mathbf1=(1,\ldots,1)\), yields \(\sum_i U_i=\sum_i L_i\), because each diagonal normal is orthogonal to \(\mathbf1\). Hence
\[
S=\sum_i(U_i+L_i+D_i)=2\sum_iU_i+\sum_iD_i
=2\sum_i\partial_{a_i}V+(2-\sqrt2)\partial_\ell V.
\]
The primary source's exact transfer-matrix trace evaluates these derivatives without computing any facets individually.

**2. The uniform formula.** Write \(a_i=A\) for all \(i\), and \(\ell=At\). Homogeneity yields \(V(A,\ell)=A^sf_s(\ell/A)\), so, at \(A=1\), the sum of derivatives with respect to the \(a_i\) equals
\[
\frac{d}{dA}\bigg|_{A=1}V(A,\ell)=s f_s(t)-t f_s'(t),
\]
with \(\ell=t\) fixed. Also \(\partial_\ell V=f_s'(t)\). Substituting gives the claimed surface identity \(S_s(t)=2sf_s(t)+(2-\sqrt2-2t)f_s'(t)\). The trace of the common \(2\times2\) matrix has eigenvalues \(\lambda_\pm(t)\), proving the displayed volume formula.

**3. Strict concavity of the volume radius.** Define \(h_s(t)=f_s(t)^{1/s}\). Since every right-hand side of the defining inequalities depends affinely on \(t\), for any \(u,v\in[0,1/2]\) and \(\theta\in[0,1]\),
\[
(1-\theta)P_s(u)+\theta P_s(v)\subseteq P_s((1-\theta)u+\theta v).
\]
The Brunn–Minkowski inequality shows that \(h_s\) is concave. In fact it is *strictly* concave. Indeed \(P_s(t)\) has coordinate width one in every coordinate (both the all-zero and all-one vectors belong to it), so two different members could be homothetic only by a translation. Their volumes are strictly different: directly differentiating the transfer-matrix eigenvalue expression gives, for \(t>0\),
\[
f_s'(t)=\frac{s t}{\sqrt{1-2t^2}}\big(\lambda_-(t)^{s-1}-\lambda_+(t)^{s-1}\big)<0.
\]
Thus distinct members are not homothetic, which makes the Brunn–Minkowski inequality strict. The full-dimensionality and strictness extend across the endpoints by continuity.

**4. Sharp dimension-free optimizer.** From \(f_s=h_s^s\),
\[
Q_s(t)=2s h_s(t)+s(2-\sqrt2-2t)h_s'(t).
\]
For \(0<t<1/2\), differentiate:
\[
\boxed{Q_s'(t)=s(2-\sqrt2-2t)h_s''(t).}
\]
Because \(h_s\) is twice differentiable and strictly concave, \(h_s''\le0\) everywhere and is not identically zero on any nonempty interval. The multiplier changes sign exactly at \(t_*=1-1/\sqrt2\). Consequently \(Q_s\) strictly decreases for \(t<t_*\) and strictly increases for \(t>t_*\), including the endpoint comparisons by continuity. At \(t_*\), the derivative term in the expression for \(Q_s\) vanishes, leaving \(Q_s(t_*)=2s h_s(t_*)\). Substitution yields \(\alpha_\pm\) above, and both the strict improvement over the cube and its limit follow from \(0<\alpha_-<\alpha_+<1\).

## Verification

The accompanying executable `CHECK.py` reconstructs polytope vertices independently from intersections of \(s\) active inequalities, forms their full-dimensional convex hull, and compares its directly computed Euclidean volume and boundary area with the transfer-matrix and derivative formulas. It includes several link ratios on both sides of the predicted optimizer and the boundary value \(t=1/2\) in dimensions three and four, plus a five-dimensional instance and two nonuniform input vectors. It also checks the exact algebraic derivative identity and numerical strict improvement at the optimizer in dimensions three through twenty. This is a finite diagnostic; the all-dimensional theorem follows from the preceding proof, not from enumeration.

Run with `python CHECK.py` using Python, NumPy and SciPy.

## Relationship to prior work

Kantarcı Oğuz, Özel and Ravichandran introduced chainlink polytopes and proved the volume trace identity (Proposition 6.8), also emphasizing Ehrhart equivalence and complementary section-volume symmetries. The volume trace and the elementary supporting-hyperplane first-variation theorem are **prior ingredients**, not claimed as original. The new statements isolate the **ordinary Euclidean full-boundary area**, and, more importantly, its unique sharp fixed-volume optimizer independent of dimension; the strict Brunn–Minkowski argument is needed to establish global optimality, which does not follow merely by listing the known volume polynomial. Work on Euclidean perimeters of complementary **two-dimensional sections** concerns a distinct invariant and does not imply the full-dimensional minimizer.

## Limitations

This result does not optimize over non-uniform chain lengths, other convex bodies, or link ratios beyond \(1/2\), where the simple volume trace may fail. The derivative identity is stated in the open parameter chamber; its uniform endpoint consequences follow by continuity rather than by differentiating through a combinatorial transition. Literature and semantic-database searches cannot exclude unindexed equivalent proofs. Independent validation has not been performed.

## References

- E. Kantarcı Oğuz, C. Y. Özel and M. Ravichandran, *Chainlink Polytopes and Ehrhart-Equivalence*, arXiv:2211.08382v1 (first submitted 2022-11-15), especially Definition 1 and Proposition 6.8. https://arxiv.org/abs/2211.08382
- H. Brunn and H. Minkowski, the classical Brunn–Minkowski inequality and its equality characterization for convex bodies (standard theorem).
