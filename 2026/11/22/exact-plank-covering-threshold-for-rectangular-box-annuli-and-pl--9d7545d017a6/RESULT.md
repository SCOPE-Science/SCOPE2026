# Exact plank-covering threshold for rectangular-box annuli and planar optimizer rigidity

## Finding
For every integer \(d\ge2\), let \(Q=\prod_{j=1}^d[a_j,b_j]\subset\mathbb R^d\) be an axis-parallel rectangular box with positive side lengths \(L_j=b_j-a_j\), and let \(H=\prod_{j=1}^d[c_j,d_j]\subset\operatorname{int}Q\) be another axis-parallel box, with \(0<h_j=d_j-c_j<L_j\). A plank is the closed slab between two distinct parallel affine hyperplanes; its width is their Euclidean distance. Let \(\tau(Q,H)\) be the infimum of the sum of widths over finite plank coverings of \(Q\setminus\operatorname{int}H\), with plank normals unrestricted. Then
\[
\boxed{\tau(Q,H)=\min\left\{\min_{1\le j\le d}L_j,\ \sum_{j=1}^d(L_j-h_j)\right\}.}
\]
Both competing bounds are attained by explicit finite coordinate-parallel covers. In particular, the shell retains the full minimum width of its outer box exactly when \(\sum_j(L_j-h_j)\ge\min_jL_j\), regardless of the hole's position.

There is also a sharp optimizer classification in dimension two. When \(d=2\) and \(S=(L_1-h_1)+(L_2-h_2)<\min(L_1,L_2)\), **every** finite minimum-cost covering consists of coordinate-parallel planks. For each coordinate, the projected intervals of its planks partition, up to endpoints, the two exterior intervals of \([a_j,b_j]\setminus\operatorname{int}[c_j,d_j]\), without overlaps of positive length. Conversely, every such finite subdivision is minimizing. No classification of minimizers in higher dimensions or in the other planar phases is asserted.

## Assumptions and scope
All coordinates are Euclidean and orthogonal, both boxes have positive volume, the inner box is strictly interior and aligned with the outer box, and only finite families of positive-width closed planks are considered. The inner *open* box is removed, so the entire boundary of \(H\) remains part of the required covering. The hole may be off-center. No restriction is imposed on the orientation or position of the competing planks. The result is exact, not asymptotic. The two-dimensional optimizer statement requires the strict large-hole regime shown above.

## Proof
Write \(g_j=L_j-h_j>0\), \(L_*=\min_jL_j\), and \(S=\sum_jg_j\). Translation puts the center of \(Q\) at the origin without changing costs. A single coordinate slab of width \(L_*\) covers \(Q\). Alternatively, for each \(j\) take the two coordinate planks whose \(j\)-intervals are \([a_j,c_j]\) and \([d_j,b_j]\). These \(2d\) planks cover \(Q\setminus\operatorname{int}H\) and have total width \(S\). Thus \(\tau\le\min(L_*,S)\).

For the lower bound, suppose a finite closed-plank cover has total width strictly below \(\min(L_*,S)\). Compactness of \(Q\setminus\operatorname{int}H\) permits a small enlargement and perturbation to a covering by *open* planks, with total width \(T<\min(L_*,S)\), and with every component of every unit normal nonzero. Write these planks as
\[
P_i=\{x:|\langle n_i,x\rangle-t_i|<w_i/2\},\quad \|n_i\|_2=1,\quad \sum_iw_i=T.
\]
Put \(c_{ik}=|n_{ik}|>0\) and split the total width into the directional budgets
\[
R_k=\sum_i\frac{w_ic_{ik}}{\sum_{\ell=1}^dc_{i\ell}},\qquad \sum_{k=1}^dR_k=T<S=\sum_{k=1}^dg_k.
\]
Thus at least one \(j\) satisfies \(R_j<g_j\).

We use the **rescaled directional Bang-box lemma**. For any collection as above and any coordinate \(j\), there exist positive numbers \(r_j=1\), \(r_k\ge1\) for \(k\ne j\), with
\[
X_j(r)\le R_j,\qquad X_k(r)\le T\quad(k\ne j),\qquad
X_k(r)=\sum_i\frac{w_ir_kc_{ik}}{\sum_\ell r_\ell c_{i\ell}^2}.
\]
Indeed, divide every \(w_i\) by \(T\) and apply Lemma 6 of Bakaev--Polyanskii [1] to the width-one family. That lemma states the displayed bounds with \(T=1\) and is proved there by minimizing \(X_j\) under the constraints \(X_k\le1\), grouping the \(j\) coordinate against the others, applying Cauchy--Schwarz, and using their two-variable inequality. All \(X_k\) and \(R_k\) depend linearly on the widths, so multiplying by \(T\) yields the stated version. The positivity assumption and the width normalization agree exactly with those of the cited lemma. This imported lemma is not claimed as a new result.

For the chosen \(j\), the rescaled lemma gives
\[
X_j(r)+h_j\le R_j+h_j<g_j+h_j=L_j,\qquad
X_k(r)\le T<L_*\le L_k\quad(k\ne j).
\]
Add the *open* coordinate plank \(P_0\) of width \(h_j\) whose \(j\)-interval is \(\operatorname{int}[c_j,d_j]\), so \(\operatorname{int}H\subset P_0\). Under the diagonal change of coordinates with scaling matrix \(\operatorname{diag}(\sqrt{r_1},\ldots,\sqrt{r_d})\), Bang's sign lemma [1, Lemma 3] produces a point outside all \(P_0,P_1,\ldots,P_m\) among the signed sums of their transformed normal vectors mapped back to the original coordinates. The smallest axis-parallel box containing those sums has \(k\)-side at most \(X_k(r)\) for \(k\ne j\), and \(j\)-side at most \(X_j(r)+h_j\). The center of the signed-sum box is the origin regardless of the slab offsets. The preceding inequalities therefore place every possible signed sum in \(Q\). The selected point lies in \(Q\setminus\operatorname{int}H\) and outside the original covering, a contradiction. This proves the all-dimensional equality.

For planar rigidity let \(d=2\), \(S<L_*\), and suppose a covering has total width \(W=S\). For \(j=1,2\), let \(R_j\) be defined as above, now allowing zero normal components. By the strict-margin form of the preceding argument and a small perturbation, each \(R_j\ge g_j\): if \(R_j<g_j\), the positive-component approximation retains that strict inequality and the strict bound \(W<L_*\), giving an uncovered point. Since \(R_1+R_2=g_1+g_2\), we must have \(R_1=g_1\) and \(R_2=g_2\).

It remains to show that a nonaxial plank forces a strict Bang-box improvement. Write \(a_i=|n_{i1}|\), \(b_i=|n_{i2}|\), \(a_i^2+b_i^2=1\), and set
\[
X_1(\lambda)=\sum_i\frac{w_ia_i}{a_i^2+\lambda b_i^2},\qquad
X_2(\lambda)=\sum_i\frac{w_i\lambda b_i}{a_i^2+\lambda b_i^2},\quad\lambda\ge1.
\]
For \(\lambda>1\), the two-variable inequality [1, Lemma 5] gives
\[
(\lambda-1)X_1(\lambda)+X_2(\lambda)
\le W+(\lambda-1)R_1.
\]
For a unit vector with both components nonzero, this inequality is **strict**: its proof bounds the left-hand elementary fraction by its tangent at \(\lambda=1+a_i/b_i\), then uses \(1+a_ib_i>a_i+b_i\) for \(0<a_i,b_i<1\). It is non-strict for axial directions. Consequently the summed inequality is strict if even one plank is oblique.

Now \(X_2(1)\le W\), and \(X_2(\lambda)\) is nondecreasing. If it reaches \(W\) at a finite \(\lambda>1\), the strict inequality yields \(X_1(\lambda)<R_1=g_1\) and \(X_2(\lambda)=W<L_2\). Otherwise \(X_2(\lambda)<W\) for all finite \(\lambda\), while
\[
\lim_{\lambda\to\infty}X_1(\lambda)=\sum_{i:b_i=0}w_i<R_1=g_1
\]
whenever an oblique plank exists, so sufficiently large finite \(\lambda\) again gives \(X_1(\lambda)<g_1\) and \(X_2(\lambda)<L_2\). (If \(X_2(1)=W\), all normals are axial in direction two and no oblique plank exists.) Adding the coordinate plank of width \(h_1\) now contradicts Bang's sign lemma exactly as before. Thus every minimizing plank is coordinate-parallel.

Let \(W_j\) denote the total width of planks normal to \(e_j\). Then \(W_j=R_j=g_j<L_*\le L_j\). If some coordinate \(x_j\in[a_j,b_j]\setminus\operatorname{int}[c_j,d_j]\) is missed by all \(e_j\)-normal planks, there exists \(x_k\in[a_k,b_k]\) missed by all \(e_k\)-normal planks because their total width is \(W_k<L_k\). The pair \((x_1,x_2)\) is then an uncovered shell point. Therefore the projected \(j\)-intervals of the planks cover the two exterior intervals of total length \(g_j=W_j\). Equality of length and sum of interval widths forbids positive-length overlap, wastage outside \([a_j,b_j]\), or penetration into the hole interval, proving the exact interval-partition description. The converse is immediate from the coordinate-strip construction.

## Verification
The analytic lower bound uses the exact published Bang-box lemmas with their stated positivity and normalization, not finite experimentation. The independent algebraic tests in `verify.py` check the strict two-variable inequality at rational unit normals, normal-budget identities, and representative rational-shell strip covers. Execute `python3 verify.py` using Python 3.10 or later; there are no third-party dependencies. These tests validate sample calculations only and are not an exhaustive proof of the universal theorem.

## Relationship to prior work
Bakaev--Polyanskii [1, Theorem 2] proves the unit-cube threshold when \(\sum_jh_j=d-1\), and their Lemmas 3--6 supply the machinery used here. Their paper allows rectangular *inner* boxes but fixes the *outer* box to a unit cube; the stated theorem does not determine the Euclidean width optimum for outer rectangular boxes of unequal side lengths. An anisotropic affine change from a rectangle to a unit cube changes Euclidean plank widths by a factor dependent on each normal, so it does not transfer this sharp formula. A published result [2] determines the numerical profile and all minimizers for a planar **unit-square** outer box and an arbitrary rectangular hole. Its unit-square numerical profile and rigidity are treated as covered cases, not as new claims. The present new scope is the all-dimensional **outer orthotope** phase law and the equality classification for **nonsquare outer rectangles**.

For example, an outer rectangle of sides \(4\) and \(1\) with an inner rectangle of sides \(3.8\) and \(0.5\) has exact covering cost \(0.7\); normalizing this shell to a unit-square outer box gives inner side lengths \(0.95\) and \(0.5\), to which the unit-square result applies only with an *orientation-dependent transformed plank cost*, not the original Euclidean cost. Ambrus and collaborators [3] investigate homothetic holes in unit cubes and do not state the present anisotropic outer-box formula in the inspected abstract. The proof's reliance on a previously known directional Bang-box lemma and the possibility of unlocated historical equivalents remain acknowledged.

## Limitations
The assertion concerns finite covers, positive-dimensional inner boxes strictly inside the outer box, and coordinate-aligned rectangular boxes in a Euclidean space. It does not classify optimal covers in dimensions \(d>2\), or at and above the planar threshold \(S=L_*\); it does not address rotated holes, nonrectangular outer bodies, other width costs, or quantitative stability. The novelty comparison is necessarily provisional pending independent historical review. The proof imports Bakaev--Polyanskii's Lemmas 3--6, whose material statements and arguments were inspected; no independence is claimed.

## References
[1] E. Bakaev and A. Polyanskii, *A sharp plank theorem for cube annuli*, arXiv:2611.00379v1, first submitted 2026-10-30, https://arxiv.org/html/2611.00379v1 .

[2] *Rigidity of minimum-width plank coverings of rectangular square annuli*, published-finding corpus, published 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-rigidity-of-minimum-width-plank-coverings-of-rectangular-square--fb93068f6f81 .

[3] G. Ambrus, M. Corbo, D. N. Goto, D. Leitz, K. Mawhinney, *On plank coverings of cube annuli*, arXiv:2610.18770v1, first submitted 2026-10-13, https://arxiv.org/abs/2610.18770 .
