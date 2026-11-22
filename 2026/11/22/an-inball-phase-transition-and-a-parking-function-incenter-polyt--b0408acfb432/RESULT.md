# An inball phase transition and a parking-function incenter polytope in two-row generalized Pitman–Stanley geometry

## Finding

For an integer \(m\ge1\) and a real parameter \(t\ge0\), let \(P_m(t)\subset\mathbb R^{2m}\) consist of nonnegative real matrices \(x=(x_{ij})\), with \(i=1,2\) and \(j=1,\ldots,m\), satisfying
\[
 x_{11}\ge x_{12}\ge\cdots\ge x_{1m}\ge0,\qquad
 x_{11}+x_{21}\ge\cdots\ge x_{1m}+x_{2m}\ge0,
\]
\[
 x_{11}\le1,\qquad x_{11}+x_{21}\le1+t.
\]
This is the native matrix-coordinate realization of the two-row generalized Pitman–Stanley polytope with initial vector \((1,t)\) and zero lower vector, extended continuously to real \(t\). All distances below use the standard Frobenius metric on the matrix entries; integral equivalence to a flow polytope is not asserted to preserve this metric.

Set
\[
 \rho_m=\frac1{2+(m-1)\sqrt2},\quad
 \sigma_m(t)=\frac{1+t}{2m+\sqrt2},\quad
 \tau_m=\frac{2m+\sqrt2}{2+(m-1)\sqrt2}-1.
\]
Then the exact largest inscribed Euclidean ball radius is
\[
 r_m(t)=\min\{\rho_m,\sigma_m(t)\}.
\]
The complete set \(\mathcal I_m(t)\) of centers of largest balls has three regimes. Write \(r=r_m(t)\), \(c=(2-\sqrt2)r\), and \(u_j=x_{1j}\), \(v_j=x_{2j}\).

If \(0\le t<\tau_m\), all centers are exactly
\[
 u_j=r[1+\sqrt2(m-j)]+z_j,\qquad
 v_j=r[1+(2-\sqrt2)(m-j)]-z_j,
\]
where
\[
 z_m=0,\quad z_1\ge z_2\ge\cdots\ge z_m=0,\quad
 z_j\le c(m-j),\quad
 z_1\le h:=1-[2+(m-1)\sqrt2]r.
\]
The center locus has affine dimension \(m-1\) (zero when \(m=1\)). At the boundary parameter \(t=0\), the final cap is redundant; after scaling and reversing coordinates, \(\mathcal I_m(0)\) is affinely equivalent to the classical \((m-1)\)-dimensional Pitman–Stanley parking-function polytope with all unit parameters. Consequently it has exactly \(2^{m-1}\) vertices and its intrinsic Euclidean \((m-1)\)-volume, for \(m\ge2\), is
\[
 \operatorname{Vol}_{m-1}(\mathcal I_m(0))
 =\frac{m^{m-2}}{(m-1)!}
 \left(\frac{2\sqrt2-2}{2m+\sqrt2}\right)^{m-1}.
\]
Meanwhile \(P_m(0)\) itself has only \(\binom{m+2}{2}\) vertices.

If \(t=\tau_m\), the center is unique, with
\[
 u_j=r[1+\sqrt2(m-j)],\qquad
 v_j=r[1+(2-\sqrt2)(m-j)].
\]
If \(t>\tau_m\), all centers are exactly
\[
 u_j=r[1+\sqrt2(m-j)],\qquad
 v_j=r[1+(2-\sqrt2)(m-j)]+w_j,
\]
where \(0\le w_m\le\cdots\le w_1\le t-\tau_m\). This is an \(m\)-simplex of intrinsic volume \((t-\tau_m)^m/m!\). Thus the center-locus dimension undergoes the sharp change \(m-1\), then \(0\), then \(m\) across the transition.

## Assumptions and scope

The ambient dimension is \(2m\), and the native matrix coordinates, rather than any integrally equivalent flow coordinates, carry the ordinary Euclidean metric. The case \(t=0\) allows one zero initial supply; for \(t>0\), both supplies are positive. The polytope remains full-dimensional in all cases. The auxiliary \((m-1)\)-volume is intrinsic to the affine hull of the center set. For \(m=1\), that center set has dimension zero and its conventional zero-dimensional volume is one.

## Proof

**Supporting inequalities and distances.** Write \(s_j=u_j+v_j\). An irredundant halfspace description for \(t>0\) is
\[
 v_j\ge0\ (1\le j\le m),\quad u_m\ge0,\quad
 u_j-u_{j+1}\ge0,\quad s_j-s_{j+1}\ge0\ (1\le j<m),
\]
\[
 u_1\le1,\qquad s_1\le1+t.
\]
Every displayed inequality defines a facet: its equality can be achieved while all other displayed inequalities remain strict, using strictly decreasing positive sequences with arbitrarily small perturbations. For \(t=0\), the row-one upper inequality is redundant, and the others are facets. The respective outward-normal lengths are \(1,1,\sqrt2,2,1,\sqrt2\); these are measured in the full matrix coordinates. A Euclidean ball of radius \(r\) with center \((u,v)\) lies in the polytope if and only if
\[
 v_j\ge r,\quad u_m\ge r,\quad u_j-u_{j+1}\ge\sqrt2r,\quad
 s_j-s_{j+1}\ge2r,\quad u_1\le1-r,\quad s_1\le1+t-\sqrt2r.
\]
(The redundant row bound when \(t=0\) can be retained without changing feasibility.)

**Sharp bound.** From \(u_m\ge r\) and the \(m-1\) first-row differences, \(u_1\ge[1+(m-1)\sqrt2]r\). Combining with \(u_1\le1-r\) gives \(r\le\rho_m\). Similarly, \(s_m=u_m+v_m\ge2r\), and the \(m-1\) total-column differences imply \(s_1\ge2mr\). The total upper facet then gives \(r\le\sigma_m(t)\). Both bounds are attained simultaneously whenever they allow the radius: take
\[
 u_j^0=r[1+\sqrt2(m-j)],\qquad
 v_j^0=r[1+(2-\sqrt2)(m-j)].
\]
These coordinates satisfy all margin constraints as soon as \(r\le\min\{\rho_m,\sigma_m(t)\}\), proving the radius formula.

**All optimal centers below the transition.** For \(t<\tau_m\), \(r=\sigma_m(t)\). The chain of inequalities \(1+t\ge s_1+\sqrt2r\ge (2m+\sqrt2)r=1+t\) forces equality at every stage: \(s_m=2r\), \(s_j-s_{j+1}=2r\), and \(s_1=1+t-\sqrt2r\). Hence \(s_j=2r(m-j+1)\), \(u_m=v_m=r\). Subtract the minimal first-row profile \(u_j^0\): setting \(z_j=u_j-u_j^0\), the first-row differences give \(z_j\ge z_{j+1}\), while \(v_j=s_j-u_j\ge r\) gives \(z_j\le(2-\sqrt2)r(m-j)\). The extra upper facet \(u_1\le1-r\) gives \(z_1\le h\). These conditions are also sufficient. When \(t<\tau_m\), \(h>0\), so for \(m\ge2\) they admit strictly decreasing small positive \(z_1,\ldots,z_{m-1}\), proving the dimension assertion.

**The unique transition and the post-transition simplex.** At \(t=\tau_m\), \(h=0\), so nonincreasing nonnegative \(z_j\) all vanish. Above \(\tau_m\), the first-row margin chain saturates instead: \(u_m=r\), every \(u_j-u_{j+1}=\sqrt2r\), and \(u_1=1-r\), forcing \(u_j=u_j^0\). Writing \(v_j=v_j^0+w_j\), the constraints become \(w_m\ge0\), \(w_j\ge w_{j+1}\) and \(w_1\le t-\tau_m\). Conversely, those inequalities imply every original margin bound. Their region is an ordinary order simplex in the \(v\)-coordinates and has volume \((t-\tau_m)^m/m!\).

**Parking-function identification and volume.** At \(t=0\), the cap \(z_1\le h\) coincides with the bound \(z_1\le c(m-1)\). Reverse coordinates by \(Z_k=z_{m-k}/c\) for \(1\le k\le m-1\), and put \(Z_0=0\). The center constraints become
\[
 0\le Z_1\le\cdots\le Z_{m-1},\qquad Z_k\le k.
\]
Taking successive differences \(Y_k=Z_k-Z_{k-1}\) identifies this region, by a determinant-one linear map, with the classical Pitman–Stanley polytope \(\{Y_k\ge0,\sum_{i=1}^kY_i\le k\}\). Its \((m-1)\)-dimensional Euclidean coordinate volume is \(m^{m-2}/(m-1)!\), the standard parking-function volume identity. Its vertices independently choose, at each \(k\), between \(Z_k=Z_{k-1}\) and \(Z_k=k\); these \(2^{m-1}\) choices are distinct. In the original center coordinates each independent \(z_j\)-variation changes \((u_j,v_j)\) by \((1,-1)\), multiplying intrinsic volume by \(\sqrt2\) per free index. Scaling by \(c\) and substituting \(r=(2m+\sqrt2)^{-1}\) gives the displayed intrinsic-volume formula.

Finally, \(P_m(0)\) is an order-polytope realization in the variables \(u_j,s_j\): both sequences are nonincreasing in \([0,1]\), with \(u_j\le s_j\). Its vertices have each sequence binary, determined by threshold indices \(0\le k\le l\le m\); they are \(k\) columns \((1,0)\), then \(l-k\) columns \((0,1)\), and then zero columns. There are exactly \(\binom{m+2}{2}\) such vertices.

## Verification

The supplied `verify.py` uses exact integer and rational arithmetic to enumerate all \(2^{m-1}\) explicit center-polytope vertices for \(1\le m\le12\), verify every normalized facet-distance inequality, and enumerate all \(\binom{m+2}{2}\) vertices of the zero-second-supply original polytope. It also integrates the uniform classical Pitman–Stanley region by exact polynomial antiderivatives up to dimension twelve, reproducing \((n+1)^{n-1}/n!\) without floating point arithmetic. An additional independent linear program using the stated original halfspaces reproduced the weighted inradius for \(1\le m\le6\) at six parameter values per dimension. The arbitrary-dimension and arbitrary-real-parameter statements follow from the analytic facet-margin argument, not from finite tests.

## Relationship to prior work

Dugan, Hegarty, Morales and Raymond (initial public arXiv version July 19, 2023) give the generalized Pitman–Stanley defining inequalities, the grid-flow interpretation and combinatorial face/vertex results. Pitman and Stanley's original parking-function polytope work gives the classical volume identity; Hanada, Lentfer and Vindas-Meléndez identify an integrally equivalent weakly increasing parking-function polytope and its binary vertex choices. The present result concerns Euclidean inballs and their *entire center sets in the native matrix metric*. A related published result for the all-ones input of a generalized Pitman–Stanley staircase has the row-controlled radius \(\rho_m\); it does not imply the competing zero/variable-second-supply bound \(\sigma_m(t)\), the sharp switch \(\tau_m\), or the parking-function incenter locus. Affine or integral equivalence alone does not preserve the Euclidean inradius. Historical priority remains provisional because not every related full text was accessible.

## Limitations

The theorem is specific to the two-row supply family \((1,t)\), its zero lower bound and the unweighted Frobenius metric. It does not establish a general inradius classification for arbitrary initial and lower vectors or for Euclidean metrics on the flow-edge representation. The volume assertion for the boundary center set uses the known classical parking-function volume theorem. Independent mathematical review has not been performed.

## References

1. W. T. Dugan, M. Hegarty, A. H. Morales, A. Raymond, *Generalized Pitman–Stanley polytope: vertices and faces*, arXiv:2307.09925, first public version July 19, 2023. https://arxiv.org/abs/2307.09925
2. J. Pitman, R. Stanley, *A polytope related to empirical distributions, plane trees, parking functions, and the associahedron*, initial technical report June 1, 1999; Discrete & Computational Geometry 27 (2002), 603–634. https://statistics.berkeley.edu/tech-reports/560
3. M. Hanada, J. Lentfer, A. R. Vindas-Meléndez, *Generalized Parking Function Polytopes*, first online November 6, 2023, Annals of Combinatorics 28 (2024), 575–613, §4. https://doi.org/10.1007/s00026-023-00671-1
4. W. T. Dugan, M. Hegarty, A. H. Morales, A. Raymond, *Volume and Lattice Points of Generalized Pitman-Stanley Flow Polytopes*, received November 15, 2024, FPSAC 2025 proceedings. https://emis.muni.cz/journals/SLC/wpapers/FPSAC2025/94.html
