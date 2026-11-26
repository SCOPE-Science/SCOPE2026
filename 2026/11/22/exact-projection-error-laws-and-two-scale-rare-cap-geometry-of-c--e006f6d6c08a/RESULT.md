# Exact projection-error laws and two-scale rare-cap geometry of crown root polytopes

## Finding

For each integer \(n\ge3\), define the standard simplex \(\Delta_{n-1}=\{x\in\mathbb R^n:x_i\ge0,\sum_i x_i=1\}\) and two polytopes
\[
P_n=\Delta_{n-1}\times\Delta_{n-1},\qquad
Q_n=\operatorname{conv}\{(e_i,e_j):1\le i,j\le n,\ i\ne j\}.
\]
The crown root polytope \(Q_n\) is obtained from the product \(P_n\) by removing the \(n\) matching-diagonal vertices. All distances use the unscaled Euclidean metric in \(\mathbb R^{2n}\). Let \(X=(p,q)\) be uniformly distributed by intrinsic \((2n-2)\)-dimensional Euclidean volume in \(P_n\) and set \(D_n=\operatorname{dist}_2(X,Q_n)\). Write
\[
h_n=\sqrt{\frac{n}{2(n-1)}},\qquad
\eta_n=\frac{n}{\binom{2n-2}{n-1}}.
\]

**Exact global projection.** If all \(p_i+q_i\le1\), then \(X\in Q_n\) and its projection is itself. Otherwise there is exactly one index \(i\) for which \(\delta=p_i+q_i-1>0\). Its unique Euclidean projection \((p',q')\) onto \(Q_n\) is
\[
p'_j=p_j+\begin{cases}-\delta/2,&j=i,\\\delta/[2(n-1)],&j\ne i,\end{cases}\qquad
q'_j=q_j+\begin{cases}-\delta/2,&j=i,\\\delta/[2(n-1)],&j\ne i.\end{cases}
\]
In particular,
\[
\boxed{D_n=h_n\max_{1\le i\le n}(p_i+q_i-1)_+.}
\]

**Entire distance law and vector-valued projection error.** For \(0\le t\le h_n\),
\[
\boxed{\Pr(D_n>t)=\eta_n(1-t/h_n)^{2n-2}.}
\]
The event \(D_n=0\) has probability \(1-\eta_n\). Conditional on \(D_n>0\), the normalized distance \(D_n/h_n\) has the exact \(\operatorname{Beta}(1,2n-2)\) distribution. For each integer \(r\ge1\),
\[
\mathbb E[D_n^r]=\eta_n h_n^r\frac{r!(2n-2)!}{(2n-2+r)!}.
\]
The outward projection-error direction, conditional on \(D_n>0\), is uniform over \(n\) regular-simplex unit vectors, independent of its length. Different directions have mutual inner product \(-1/(n-1)\). The error-vector covariance is zero on the \((n+1)\)-dimensional orthogonal complement of the diagonal zero-sum space, and is scalar on
\[
H_+=\{(z,z):z\in\mathbb R^n,\ \sum_i z_i=0\},\qquad \dim H_+=n-1.
\]
Its sole positive eigenvalue, of multiplicity \(n-1\), is
\[
\boxed{\lambda_n=\frac{\eta_n}{2(n-1)^2(2n-1)}.}
\]

**Exact conditional shape and a two-scale limit.** Conditional on the cap indexed by \(i\), define
\[
S=(1-p_i)+(1-q_i),\qquad W=\frac{1-p_i}{S}.
\]
Then \(S,W\) are independent with
\[
S\sim\operatorname{Beta}(2n-2,1),\qquad W\sim\operatorname{Beta}(n-1,n-1).
\]
Thus distance depth and transverse imbalance are independent up to the factor \(S\). With \(E\) standard exponential and \(Z\) standard normal, independent,
\[
\boxed{\left((2n-2)D_n/h_n,\ \sqrt{2n}(p_i-q_i)\right)\ \Bigm|\ (D_n>0)
\ \Longrightarrow\ (E,Z).}
\]
The cap index is uniform in \(\{1,\ldots,n\}\). The deleted volume is exponentially small as a fraction of the product volume. Within that volume, the normal depth has scale \(n^{-1}\) and an exponential limiting law, while the tangential imbalance has scale \(n^{-1/2}\). The maximum pointwise gap remains macroscopic. More precisely, a normal layer of thickness \(c_n/n\) contains a fraction tending to one of the deleted volume when \(c_n\to\infty\); a layer of thickness \(o(n^{-1})\) contains a fraction tending to zero.

## Assumptions and scope

The Euclidean norm is the ordinary ambient norm, restricted to the common affine hull \(\sum_i p_i=\sum_i q_i=1\). Uniform volume means normalized intrinsic Euclidean Hausdorff measure. The product polytope is full-dimensional in its \((2n-2)\)-dimensional affine hull, and \(Q_n\) is also full-dimensional for \(n\ge3\). All formulae are for every integer \(n\ge3\), and the limit is along integers \(n\to\infty\). The two random variables in the conditional limit use the uniquely violated coordinate index, not an arbitrary independently chosen coordinate. The phrase 'regular-simplex directions' refers to Euclidean angles in the intrinsic ambient space, not a claim that \(Q_n\) is a regular simplex.

## Proof

**1. The crown polytope and disjoint caps.** The exact linear description
\[
Q_n=\{(p,q)\in P_n:p_i+q_i\le1\text{ for each }i\}
\]
was established as background for the previously known crown volume and Hausdorff computation [2]. It also follows directly from the bipartite transportation/coupling criterion: a coupling with no diagonal entries exists exactly when every singleton row mass \(p_i\) is at most the complement \(1-q_i\) of the corresponding diagonal column; all larger row sets see every column. Two inequalities cannot be simultaneously strictly violated, because \(\sum_i(p_i+q_i)=2\). Set \(C_i=\{(p,q)\in P_n:p_i+q_i>1\}\); these caps are pairwise disjoint.

**2. Orthogonal projection is globally feasible.** Fix \((p,q)\in C_i\) and put \(\delta=p_i+q_i-1>0\). Since \(p_i,q_i\le1\), one has \(\delta\le\min(p_i,q_i)\), so decreasing each by \(\delta/2\) preserves nonnegativity. Increase every other coordinate of each simplex by \(\delta/[2(n-1)]\). The resulting \((p',q')\) has each coordinate sum equal to one, and satisfies \(p'_i+q'_i=1\). For \(j\ne i\),
\[
p_j+q_j\le\sum_{\ell\ne i}(p_\ell+q_\ell)=1-\delta,
\]
so
\[
p'_j+q'_j\le1-\delta+\delta/(n-1)\le1.
\]
Consequently \((p',q')\in Q_n\). The displacement in each simplex is a positive scalar multiple of the centered coordinate normal \(e_i-\mathbf1/n\), so it is perpendicular, inside the common affine hull, to the cut hyperplane \(p_i+q_i=1\). It is therefore the metric projection onto the containing halfspace, and because the projected point belongs to its subset \(Q_n\), also the global unique projection onto \(Q_n\). Direct summation gives
\[
\|(p,q)-(p',q')\|_2^2
=\delta^2\left(\frac12+\frac1{2(n-1)}\right)=h_n^2\delta^2.
\]
This establishes the exact pointwise formula, including identity projection outside the caps.

**3. Factorization of a uniform cap.** Under uniform product-volume sampling, \(p\) and \(q\) are independent uniform-simplex vectors. Their fixed coordinates \(p_i,q_i\) are independent \(\operatorname{Beta}(1,n-1)\). Put \(U=1-p_i\), \(V=1-q_i\); their densities are proportional to \(u^{n-2}\) and \(v^{n-2}\) on \((0,1)\), independently, and \(C_i\) is exactly \(U+V<1\). With \(S=U+V\) and \(W=U/S\), the change-of-variables Jacobian is \(S\); the conditional joint density factors as
\[
\text{const}\cdot S^{2n-3}\,W^{n-2}(1-W)^{n-2}
\qquad (0<S<1,\ 0<W<1).
\]
Hence independently \(S\sim\operatorname{Beta}(2n-2,1)\) and \(W\sim\operatorname{Beta}(n-1,n-1)\). The cap probability, by a beta integral, is
\[
\Pr(C_i)=(n-1)^2\int_{u+v<1}u^{n-2}v^{n-2}\,du\,dv
=\frac{(n-1)!^2}{(2n-2)!}=\binom{2n-2}{n-1}^{-1}.
\]
The \(n\) caps have equal probability and are disjoint. Thus \(\Pr(D_n>0)=\eta_n\), and conditional on positive distance, \(\delta=1-S\sim\operatorname{Beta}(1,2n-2)\). The tail follows from \(\Pr(1-S>u)=(1-u)^{2n-2}\), and the moment formula is the beta integral. No finite computation is being used to infer the all-dimensional formula.

**4. Regular-simplex error directions and isotropic residual covariance.** On cap \(C_i\), the residual is \(R=X-\Pi_{Q_n}X=\delta v_i\), where \(v_i\in\mathbb R^{2n}\) has entries \(1/2\) at the two coordinates indexed by \(i\) and \(-1/[2(n-1)]\) at all other entries in each block. The vectors satisfy \(\|v_i\|=h_n\), \(\sum_i v_i=0\), and \(\langle v_i/h_n,v_j/h_n\rangle=-1/(n-1)\) for \(i\ne j\). The cap label is uniform and independent of the beta variable \(\delta\); therefore \(\mathbb E R=0\). The normalized frame identity
\[
\frac1n\sum_i(v_i/h_n)(v_i/h_n)^\mathsf T
=\frac1{n-1}\Pi_{H_+}
\]
follows either from direct coordinates or from the regular-simplex tight-frame identity. Since \(\mathbb E D_n^2=\eta_n h_n^2\cdot2/[(2n-1)(2n)]\),
\[
\operatorname{Cov}(R)=\frac{\mathbb E D_n^2}{n-1}\Pi_{H_+}
=\frac{\eta_n}{2(n-1)^2(2n-1)}\Pi_{H_+}.
\]
This proves the entire error-vector law and its covariance spectrum, not only a scalar distance statistic.

**5. Independent normal and tangential scales.** Under the conditional law, \(\delta=1-S\) is independent of \(W\). Its tail shows \((2n-2)\delta\Rightarrow\operatorname{Exp}(1)\). Independently, the elementary central-limit theorem for independent gamma variables of shape \(n-1\) implies \(\sqrt{8n}(W-1/2)\Rightarrow N(0,1)\). Since \(p_i=1-SW\) and \(q_i=1-S(1-W)\),
\[
p_i-q_i=S(1-2W).
\]
Also \(S\to1\) in probability. Slutsky's lemma and finite-sample independence give the claimed joint independent exponential/normal limit after scaling \(p_i-q_i\) by \(\sqrt{2n}\).

## Verification

Run `python checks/check_crown_distance.py` using Python 3 and SciPy. The standalone code checks 1,050 rational test points across dimensions \(3\) to \(9\): exact simplex constraints, cap uniqueness, feasible projection, squared distance identity, and nonnegativity. It also runs 96 constrained quadratic programs in dimensions \(3\) to \(6\), initialized at the proposed projected points. Twenty-seven exact factorial beta-integral checks verify cap normalization; the moment expressions are checked for positivity, not independently rederived by the script. Recorded output: `CROWN_DISTANCE_PASS rational_projection_points=1050 independent_qp=96 max_gap=0.00e+00 beta_integrals=27`. The finite tests corroborate the proof and do not certify the all-dimensional assertions.

## Relationship to prior work

Almousa, Dochtermann and Smith [1] establish the setting of bipartite root polytopes as subpolytopes of products of simplices, with combinatorial triangulations and toric constructions. The crown analysis [2] proves the crown halfspace description, exact excised volume fraction \(\eta_n\), and sharp Hausdorff radius \(h_n\), identifies the projection of each removed vertex, and gives a Gaussian-direction width-deficit law. The vertex projection already gives the interior cap projection by interpolation: each cap point is a convex combination of its deleted vertex and a point of the base cut face. Replacing the vertex with its projection leaves the combination in that face, and subtracts precisely the normal displacement. From that identity, cap homothety gives the radial beta law, and the cut normals give the error directions and covariance by symmetry. The additional calculation here resolves the conditional distribution of the transverse imbalance jointly with depth, including its exact independent ratio representation and the two distinct fluctuation scales. A uniform-interior imbalance is not a width statistic in a random direction.

A sparse-paving matroid result [3] gives a similar **scalar beta distance law** and pointwise projection on an ambient hypersimplex, not on a product of two simplices. Its matroid-specific hypotheses do not directly apply to \(Q_n\). A deleted-biclique result [4] concerns one complete forbidden rectangle and classifies distances of *deleted vertices*, not all uniformly sampled interior points after deleting a matching. The fixed-rank bipartite matching-polytope formulation [5] supplies a related inequality framework. A related hypersimplex covering result [6] also uses cap homothety to obtain a scalar beta law, for distance to a union of vertex copies rather than conditional transverse imbalance for this projection.

## Limitations

The exact factorization here uses independent **uniform-simplex** inputs and the standard unweighted Euclidean embedding. The same statements do not follow for arbitrary graph deletions, anisotropic metrics, or nonuniform interior densities. The limiting law is **conditional** on an exponentially rare event and is not a statement that an ordinary unconditioned random point has a nondegenerate large distance. The beta/gamma identities and regular-simplex tight-frame identity are standard ingredients. The comparisons do not establish historical priority for the conditional joint law.

## References

[1] A. Almousa, A. Dochtermann, B. Smith, *Root polytopes, tropical types, and toric edge ideals*, arXiv:2209.09851, initial public version 2022-09-20, https://arxiv.org/abs/2209.09851.

[2] *Rare exponential directional loss despite constant Hausdorff distance in crown-graph root polytopes*, 2026, https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-rare-exponential-directional-loss-despite-constant-hausdorff-dis--771379f5fcb8.

[3] *Exact Euclidean projection and a universal beta distance law for sparse-paving matroid polytopes*, 2026, https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-exact-euclidean-projection-and-a-universal-beta-distance-law-for--8d39b121255f.

[4] *A sharp metric–volume separation under biclique deletion from a product of simplices*, 2026, https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-a-sharp-metric-volume-separation-under-biclique-deletion-from-a--70f9cced854f.

[5] J. C. Torres, *Normality of \(k\)-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910, initial public version 2023-06-20, https://arxiv.org/abs/2306.11910.

[6] *Sharp metric–volume birth and a universal distance law in hypersimplex vertex covers*, 2026, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-metric-volume-birth-and-a-universal-distance-law-in-hypers--811b582a843b.
