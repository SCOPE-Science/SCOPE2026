# Three-leaf semigroup rigidity of star-graph total-variation resolvents

## Finding

For each integer \(m\ge 1\), let \(S_m\) be the unweighted star with hub \(0\) and leaves \(1,\ldots,m\). Define, for \(x\in\mathbb R^{m+1}\),
\[
J_m(x)=\sum_{i=1}^{m}|x_0-x_i|,
\qquad
P_t(y)=\operatorname*{arg\,min}_{x\in\mathbb R^{m+1}}
\left\{\frac12\|x-y\|_2^2+tJ_m(x)\right\},\quad t\ge0.
\]
The minimizer is unique. The **complete star classification** is
\[
\boxed{\quad P_s(P_t(y))=P_{s+t}(y)\text{ for every }y\in\mathbb R^{m+1}
\text{ and }s,t\ge0\quad\Longleftrightarrow\quad 1\le m\le3.\quad}
\]
For \(1\le m\le3\), the entire variational regularization path equals the continuous subgradient-flow path, for every starting vector. For each \(m\ge4\) the failure already occurs at \(s=t=1/2\), with explicit rational data, not merely an infinitesimal obstruction. Thus the first obstruction is the unweighted five-vertex star.

## Assumptions and scope

All vector spaces, penalties and norms are real; fidelity is the *unweighted Euclidean* squared norm. Each edge has unit total-variation weight. The star has one hub and at least one leaf, with no other edges. The regularization parameters \(s,t\) range independently over all nonnegative real values. The result is not asserted for unequal edge penalties, nonquadratic fidelity, arbitrary graphs, or anisotropic vertex weights. The statement concerns exact minimizers, not convergence of a numerical denoising algorithm.

Orient each edge from its hub toward its leaf. A vector \(p\) belongs to \(\partial J_m(x)\) exactly when there are fluxes \(z_i\) satisfying
\[
p_0=\sum_{i=1}^{m}z_i,\qquad p_i=-z_i,
\qquad z_i=\begin{cases}
1&x_0>x_i,\\ -1&x_0<x_i,\\ \left[-1,1\right]&x_0=x_i.
\end{cases}
\]
The expression \([-1,1]\) in the third case is the interval of allowable real fluxes. For any \(\tau>0\), the optimality condition for \(u=P_\tau(y)\) is \(y-u=\tau p\) for some such \(p\in\partial J_m(u)\). This condition is sufficient as well as necessary by strong convexity.

## Proof

**1. Positive classification via the minimum subgradient.** Fix \(x\), and let \(S=\{i:x_i=x_0\}\) contain \(k\) leaves. When \(k=0\), \(\partial J_m(x)\) is a singleton and the orthogonality condition below is automatic. Suppose \(k\ge1\). Put
\[
a=\sum_{i\notin S}\operatorname{sgn}(x_0-x_i),\qquad |a|\le m-k.
\]
For the unique minimum-Euclidean-norm subgradient \(p\), symmetry and strict convexity imply that all \(k\) free fluxes are equal to a value \(z\). Indeed the part of \(\|p\|_2^2\) depending on these fluxes is
\[
\left(a+\sum_{i\in S}z_i\right)^2+\sum_{i\in S}z_i^2,
\qquad -1\le z_i\le1,
\]
whose symmetric minimizer is
\[
z=\operatorname{clip}\!\left(-\frac{a}{k+1},-1,1\right).
\]
If \(m\le3\), then \(|a|\le m-k\le k+1\). Therefore no clipping occurs and
\[
p_0=a+kz=-z=p_i\quad(i\in S).
\]
For every \(q\in\partial J_m(x)\), the difference \(q-p\) is a combination of vectors \(e_0-e_i\), \(i\in S\); hence
\[
\langle p,q-p\rangle
=\sum_{i\in S}(p_0-p_i)(\zeta_i-z)=0,
\]
where \(\zeta_i\) are the free fluxes representing \(q\). Thus \(J_m\) satisfies the *MINSUB* condition at every \(x\). It is also an absolutely one-homogeneous convex **polyhedral** functional: \(J_m(x)=\max_{z\in[-1,1]^m}\sum_i z_i(x_0-x_i)\). The polyhedrality hypothesis (PS) of Burger--Gilboa--Moeller--Eckardt--Cremers, Theorem 5, therefore holds. That theorem proves for such an operator that the variational proximal path agrees at every nonnegative time with the unique subgradient gradient flow. The latter is an autonomous maximal-monotone flow and obeys the semigroup law; consequently \(P_s\circ P_t=P_{s+t}\) for every \(s,t\ge0\) and \(m\le3\). The case of zero parameter is the identity by definition.

**2. An exact five-vertex obstruction.** All tuples below have the hub in the first coordinate. Define
\[
\begin{aligned}
y&=(3,0,-3,2,-1),\\
u&=(7/4,1/2,-5/2,7/4,-1/2),\\
v&=(7/8,7/8,-2,5/4,0),\\
w&=(1,1,-2,1,0).
\end{aligned}
\]
The respective edge-flux certificates for the three optimality equations \(u=P_{1/2}(y)\), \(v=P_{1/2}(u)\) and \(w=P_1(y)\) are
\[
(1,1,-1/2,1),\qquad (3/4,1,-1,1),\qquad (1,1,-1,1).
\]
For each tuple, the associated flux lies in \([-1,1]\) and equals the correct sign whenever the final hub and leaf differ. Direct coordinate arithmetic verifies \(u=y-\frac12 p(z^{(u)})\), \(v=u-\frac12p(z^{(v)})\) and \(w=y-p(z^{(w)})\); by the preceding KKT characterization these are **exact unique proximal minimizers**. But \(v\neq w\), with \(\|v-w\|_\infty=1/4\). Thus the semigroup identity fails for \(m=4\).

**3. A six-vertex obstruction.** Put
\[
\begin{aligned}
y&=(-4,-2,0,0,2,0),\\
u&=(-2,-2,-1/2,-1/2,3/2,-1/2),\\
v&=(-7/8,-3/2,-7/8,-7/8,1,-7/8),\\
w&=(-1,-1,-1,-1,1,-1).
\end{aligned}
\]
The respective edge fluxes are
\[
(0,-1,-1,-1,-1),\quad(1,-3/4,-3/4,-1,-3/4),\quad(1,-1,-1,-1,-1).
\]
Again direct exact KKT substitution proves \(u=P_{1/2}(y)\), \(v=P_{1/2}(u)\), \(w=P_1(y)\), and \(\|v-w\|_\infty=1/2\).

**4. Every larger star.** Starting from either the \(m=4\) or \(m=5\) witness, append any number \(k\ge0\) of *pairs* of additional leaves with starting values \((-10,10)\). In the first half-step their values become \((-19/2,19/2)\); in the second half-step and the direct unit step, they become \((-9,9)\). On each such pair the hub-to-leaf flux is constantly \((+1,-1)\), so the two added contributions to the hub subgradient cancel, while the added leaf KKT equations hold. The original hub remains between \(-4\) and \(3\) and the new leaf signs are strict. Hence all original KKT equations stay valid, with all four proximal outputs exactly as stated. The same nonzero difference persists. Even degrees \(m=4+2k\) and odd degrees \(m=5+2k\) exhaust every \(m\ge4\), proving necessity.

Together the two directions establish the boxed equivalence.

## Verification

The standalone file `star_tv_semigroup_checker.py` uses only Python standard-library rational arithmetic. Running `python3 star_tv_semigroup_checker.py` checks: (i) every abstract sign/tie configuration for \(m=1,2,3\); (ii) saturation of the minimum-subgradient bound on test stars \(m=4,\ldots,40\); (iii) all exact KKT identities and sign constraints for both rational counterexamples; and (iv) 58 pair-padded instances. The proof, not finite enumeration, supplies the all-degree and all-parameter quantifiers. The source contains no dependency on proprietary software or external datasets.

## Relationship to prior work

Burger, Gilboa, Moeller, Eckardt and Cremers [1] establish that polyhedral absolutely one-homogeneous penalties satisfying MINSUB have identical variational and gradient-flow paths; their general diagonally-dominant construction already covers the positive small-star mechanism. The present result specializes this sufficient framework, then proves the converse for *the entire unweighted-star family* by rational two-step certificates and parity-complete extension, which the sufficient theorem does not yield.

Kirisits, Scherzer and Setterqvist [2], first publicly posted in 2018, establish graph-TV proximal/flow comparison criteria and show that the semigroup identity fails on some graphs; their existence statement and general counterexample do not establish the exact three-leaf threshold for stars. Bungert, Burger, Chambolle and Novaga [3] study abstract one-homogeneous gradient-flow/variational equivalence rather than a star-specific necessity classification. The graph fused-lasso literature [4] studies computational and statistical denoising on general graphs, not this exact parameter-addition property.

The new content is therefore **the precise all-star if-and-only-if classification**, especially the first star obstruction and explicit all-degree family; the MINSUB-to-flow implication itself is prior theory.

## Limitations

The theorem does not characterize which general trees or weighted stars have a proximal semigroup. It does not assert optimality of the rational data among all counterexamples, quantify the largest possible composition gap, or imply any numerical convergence rate. Publication precedence may be affected by less-indexed equivalent results on fused-lasso solution paths or polyhedral gradient flows; no claim of exhaustive historical priority is made. The rational checker supplements, but does not replace, the analytic proof or independent mathematical review.

## References

[1] M. Burger, G. Gilboa, M. Moeller, L. Eckardt, D. Cremers, *Spectral Decompositions using One-Homogeneous Functionals* (2016), Theorem 5 and the MINSUB condition, https://arxiv.org/abs/1601.02912.

[2] C. Kirisits, O. Scherzer, E. Setterqvist, *Invariant φ-Minimal Sets and Total Variation Denoising on Graphs* (first arXiv posting 2018-07-27), Section 5 and Theorem 5.3, https://arxiv.org/abs/1807.10514.

[3] L. Bungert, M. Burger, A. Chambolle, M. Novaga, *Nonlinear Spectral Decompositions by Gradient Flows of One-Homogeneous Functionals* (2019), https://arxiv.org/abs/1901.06979.

[4] O. H. Madrid Padilla, J. Sharpnack, J. G. Scott, R. J. Tibshirani, *The DFS Fused Lasso: Linear-Time Denoising over General Graphs* (2018), Journal of Machine Learning Research 18(176), https://jmlr.org/papers/v18/16-532.html.
