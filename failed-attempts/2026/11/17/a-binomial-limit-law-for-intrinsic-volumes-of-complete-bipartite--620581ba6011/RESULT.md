# A binomial limit law for intrinsic volumes of complete-bipartite graphical zonotopes

## Finding
For every integer \(q\ge 2\), let \(G_q=K_{2,q}\) have two distinguished vertices \(u,v\), and other vertices \(w_1,\ldots,w_q\). In \(\mathbb R^{q+2}\), with its standard Euclidean metric, form the graphical zonotope
\[
Z_q=\sum_{j=1}^{q}\bigl([0,e_u-e_{w_j}]+[0,e_v-e_{w_j}]\bigr).
\]
Its affine dimension is \(q+1\). Write \(V_k(Z_q)\) for the intrinsic volumes normalized by the intrinsic Steiner identity
\[
\operatorname{vol}_{q+1}(Z_q+sB_2^{q+1})=
\sum_{k=0}^{q+1}\kappa_{q+1-k}V_k(Z_q)s^{q+1-k}.
\]
Binomial coefficients with an invalid lower index are defined to be zero. For every \(0\le k\le q+1\), **all intrinsic volumes have the exact closed form**
\[
\boxed{
V_k(Z_q)=\binom qk\sum_{a=0}^{k}\binom ka\sqrt{(a+1)(k-a+1)}
+q\binom{q-1}{k-2}2^{k-2}\sqrt{k+1},}
\]
where the second summand is interpreted as zero when \(k<2\). In particular \(V_0(Z_q)=1\), \(V_1(Z_q)=2q\sqrt2\), and the intrinsic top-dimensional volume is
\[
\boxed{V_{q+1}(Z_q)=q2^{q-1}\sqrt{q+2}.}
\]

For every **fixed real** \(t>0\), set
\[
p=\frac{2t}{1+2t},\qquad C_t=\frac{t^2\sqrt p}{1+2t},\qquad W_q(t)=\sum_{k=0}^{q+1}V_k(Z_q)t^k.
\]
The total weighted intrinsic-volume profile has a **two-term asymptotic law**:
\[
\boxed{W_q(t)=(1+2t)^q\left(C_tq^{3/2}+\frac p2q+O_t(\sqrt q)\right).}
\]
Let \(K_{q,t}\) be the random index with \(\mathbb P(K_{q,t}=k)=t^kV_k(Z_q)/W_q(t)\). Then, in total variation,
\[
\boxed{d_{\rm TV}\bigl(\mathcal L(K_{q,t}),\mathcal L(2+\operatorname{Bin}(q-1,p))\bigr)=O_t(q^{-1/2}).}
\]
Consequently the standardized index satisfies the quantitative Gaussian law
\[
\sup_{x\in\mathbb R}\left|\mathbb P\left\{\frac{K_{q,t}-2-(q-1)p}{\sqrt{(q-1)p(1-p)}}\le x\right\}-\Phi(x)\right|=O_t(q^{-1/2}).
\]
Here \(\Phi\) denotes the standard normal cumulative distribution function; all limits are as \(q\to\infty\) with \(t>0\) fixed. For the unweighted Wills profile \(t=1\), the index is asymptotically \(2+\operatorname{Bin}(q-1,2/3)\), up to vanishing total-variation error, and
\[
W_q(1)=3^q\left(\frac{\sqrt{2/3}}3q^{3/2}+\frac13q+O(\sqrt q)\right).
\]

## Assumptions and scope
The graph is a **simple** complete bipartite graph with one part of size two and the other part of size \(q\ge2\). Edge generators have unit coefficient and are embedded as actual coordinate differences, each of Euclidean norm \(\sqrt2\), not rescaled to unit vectors. Translations of the zonotope do not change the result. All intrinsic volumes and balls use the inherited Euclidean metric on the affine span, not lattice-normalized volume; the top coefficient differs from the lattice spanning-tree count by \(\sqrt{q+2}\). For asymptotic claims, \(t\) is fixed strictly between zero and infinity; constants implicit in \(O_t\) may depend on it. No uniformity for \(t=t(q)\) is asserted.

## Proof
**Step 1: exact Gram determinants.** The general zonotope intrinsic-volume identity [2] states that \(V_k\) is the sum of the \(k\)-dimensional Euclidean parallelepiped volumes over all independent \(k\)-subsets of generators. An incidence-vector subset is independent exactly when its corresponding graph edge set is a forest. For a tree on \(m\) vertices, its oriented incidence matrix \(D\), with \(m-1\) columns, satisfies \(\det(D^{\mathsf T}D)=m\): all \(m\) maximal square minors obtained by deleting one row have determinant \(\pm1\), and Cauchy–Binet gives their sum of squares. For a forest, distinct tree-component incidence matrices have disjoint row supports, so the squared Gram determinant is the product of the component sizes; isolated vertices contribute the factor one.

**Step 2: a complete enumeration, including the cyclic obstruction.** Every \(w_j\) has either zero, one, or two chosen incident edges. If two different \(w_j\) have both incident edges chosen, those four edges form a 4-cycle; conversely, every cycle in \(K_{2,q}\) is such a 4-cycle, so the edge set is a forest exactly when *at most one* \(w_j\) has both its incident edges selected.

With no doubly selected vertex, a size-\(k\) forest consists of two disjoint stars with respectively \(a\) and \(k-a\) leaves, and \(q-k\) isolated opposite-part vertices. There are \(\binom qk\binom ka\) such forests; their Gram determinant is \((a+1)(k-a+1)\). This gives the first term (for \(k\le q\)). With exactly one doubly selected \(w_j\), all chosen edges form one tree on \(k+1\) vertices; there are \(q\binom{q-1}{k-2}2^{k-2}\) such forests, each with Gram determinant \(k+1\). This gives the second term, including \(k=q+1\). These are disjoint and exhaustive.

**Step 3: independent probability representations.** Put \(a=t/(1+2t)=p/2\). Choose independent labels for \(q\) positions, with probabilities \(a,a,1-2a\) for \(u\)-attached, \(v\)-attached, and unused. If \(L\) and \(R\) count the first two labels, the contribution of the first family to \(W_q\) is exactly
\[
A_q(t)=(1+2t)^q\mathbb E\sqrt{(L+1)(R+1)}.
\]
For \(H\sim\operatorname{Bin}(q-1,p)\), the second family contributes exactly
\[
B_q(t)=qt^2(1+2t)^{q-1}\mathbb E\sqrt{H+3}.
\]
Both identities hold for every integer \(q\ge2\), not just asymptotically.

**Step 4: two-term asymptotics.** Standard binomial/multinomial concentration gives \(\mathbb E\sqrt{(L+1)(R+1)}=qa+O_t(1)\). Explicitly, on the event \(|L-qa|,|R-qa|\le qa/2\), the Hessian of \((x,y)\mapsto\sqrt{(x+1)(y+1)}\) is bounded by \(C_t/q\). Taylor expansion at \((qa,qa)\), cancellation of centered linear terms, and second moments \(O_t(q)\) give an \(O_t(1)\) error; the complement has exponentially small probability and the function is bounded by \(q+1\).

Likewise, writing \(\mu=(q-1)p\), a Taylor expansion of \(x\mapsto\sqrt{x+3}\) around \(\mu\), with binomial variance \(O_t(q)\) and exponentially small tails, gives \(\mathbb E\sqrt{H+3}=\sqrt{qp}+O_t(q^{-1/2})\). Substitution yields
\[
A_q(t)=(1+2t)^q\left(qa+O_t(1)\right),\quad
B_q(t)=(1+2t)^q\left(C_tq^{3/2}+O_t(\sqrt q)\right).
\]
Their sum proves the two-term formula.

**Step 5: total variation and Gaussian fluctuations.** Since \(A_q(t)/W_q(t)=O_t(q^{-1/2})\), it suffices to compare the second-family index with \(2+H\). The index under the second family is distributed as \(2+H^*\), where \(\mathbb P(H^*=h)\) is the binomial probability of \(h\) reweighted by \(\sqrt{h+3}\). With \(M=\mathbb E\sqrt{H+3}\),
\[
d_{\rm TV}(H,H^*)\le\frac{\mathbb E|\sqrt{H+3}-M|}{2M}.
\]
The elementary identity \(|\sqrt{x+3}-\sqrt{y+3}|=|x-y|/(\sqrt{x+3}+\sqrt{y+3})\), centered at \(y=\mu\), and Cauchy–Schwarz show the numerator is \(O_t(1)\). Meanwhile \(M\asymp_t\sqrt q\). Hence this total-variation distance is \(O_t(q^{-1/2})\), and the mixture with the first-family contribution has the same bound. The classical binomial Berry–Esseen estimate gives the displayed Gaussian bound.

## Verification
The standalone `k2q_intrinsic_verify.py` verifies *from the actual signed incidence generators* all independent-subset Gram determinants, grouped by intrinsic rank and determinant, for \(1\le q\le6\), using integer exact arithmetic. It compares them with the two disjoint formula classes. There are **4,445** such Gram calculations (one per tested subset), plus top-volume equalities, profile sanity checks, and optional independent numerical convex-hull computations for \(q=2,3\). The exact Gram counts by size are 4, 15, 57, 219, 848, and 3302. The convex hulls give volumes 8 and \(12\sqrt5\), agreeing with the formula. The code also reports finite-\(q\) comparisons against the limiting binomial law; these are illustrative only and not used as an infinite proof. Run `python k2q_intrinsic_verify.py` with SymPy, NumPy, and SciPy installed. The proof above supplies the unrestricted assertions.

## Relationship to prior work
The graphical zonotope and its forest/Ehrhart interpretation are classical; [1] recalls them while developing hypergraphic zonotopes and acyclohedra. The all-zonotopes Euclidean intrinsic-volume formula used in Step 1 is explicitly due to earlier authors and is supplied by [2]; it is not claimed as new. The present claim is the full evaluated family-specific spectrum together with the *two-term* total intrinsic-volume asymptotic and an explicit binomial approximation in total variation. The complete-bipartite two-hub forest dichotomy is what makes the weighted law accessible. The general concentration/entropy theory of [3] does not supply the asserted exact coefficients, binomial parameter, or total-variation estimate. Work on graphical-zonotope deformation cones [4] and equivariant Ehrhart invariants [5] concerns different geometric/combinatorial functionals. A related accessible classification of *cycle* graphical zonotope intrinsic volumes has a cyclic-composition profile, not this two-hub forest decomposition, and does not imply these formulas.

## Limitations
Historical priority is provisional: exhaustive worldwide priority cannot be inferred from indexed searches, and an unindexed explicit complete-bipartite specialization or an equivalent high-dimensional limit theorem may exist. The nontrivial new content is not the general intrinsic-volume formula nor the well-known spanning-tree count. The total-variation bound is asymptotic and for each fixed positive \(t\); it does not state sharp constants, a local relative-error theorem, or uniformity when \(t\) approaches zero or infinity with \(q\). The finite verifier cannot prove the all-\(q\) theorem or the probabilistic limit by itself.

## References
[1] C. Pohoata and D. G. Zhu, *Hypergraphic zonotopes and acyclohedra*, first public 2025-03-27, arXiv:2503.21752v1, https://arxiv.org/html/2503.21752v1. Primary MSC2020 52B05.

[2] A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, arXiv:2206.03204 (first released 2022-06-07), especially Corollary 1 and Eq. (4), https://arxiv.org/pdf/2206.03204; *Mathematika* 69 (2023), 508–534.

[3] M. Lotz, M. B. McCoy, I. Nourdin, G. Peccati, and J. A. Tropp, *Concentration of the intrinsic volumes of a convex body*, arXiv:1810.12412 (2018), https://arxiv.org/abs/1810.12412.

[4] A. Padrol, V. Pilaud, and G. Poullot, *Deformed graphical zonotopes*, *Discrete & Computational Geometry*, first public online 2023-10-13, https://link.springer.com/article/10.1007/s00454-023-00586-x.

[5] S. Elia, D. Kim, and M. Supina, *Techniques in equivariant Ehrhart theory*, *Annals of Combinatorics*, first public online 2023-11-21, https://link.springer.com/article/10.1007/s00026-023-00673-z.
