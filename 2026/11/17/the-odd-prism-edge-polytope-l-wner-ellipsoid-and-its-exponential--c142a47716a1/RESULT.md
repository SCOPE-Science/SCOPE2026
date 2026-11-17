# The odd-prism edge-polytope Löwner ellipsoid and its exponential spoke-weight law

## Finding
For every **odd integer** \(m\ge3\), let \(G_m=C_m\square K_2\) be the circular ladder (polygonal prism) with two \(m\)-vertex rims and \(m\) connecting spokes. Write \(v_e=e_i+e_j\in\mathbb R^{2m}\) for the endpoint-incidence vector of each edge \(e=\{i,j\}\), and set \(P_m=\operatorname{conv}\{v_e:e\in E(G_m)\}\). Its affine dimension is \(d=2m-1\). The following gives its **unique intrinsic Euclidean minimum-volume enclosing (Löwner) ellipsoid**, including every semiaxis and contact point.

Let \(R\) and \(S\) be the sets of \(2m\) rim edges and \(m\) spokes, respectively, and set \(\mu=m^{-1}\mathbf1\), \(z_e=v_e-\mu\), \(L=\{z\in\mathbb R^{2m}:\langle z,\mathbf1\rangle=0\}\). There is a unique \(u_m\in(0,1/2)\) satisfying
\[
\left(\frac{1-u_m}{1+u_m}\right)^m=\frac{1-2u_m}{1+2u_m}.
\]
Define \(x_m=u_m^2\) and the positive-definite-on-\(L\) covariance operator
\[
 C_m=\frac{1-x_m}{2m}\sum_{e\in R}z_ez_e^{\mathsf T}+\frac{x_m}{m}\sum_{e\in S}z_ez_e^{\mathsf T}.
\]
Then the exact enclosing ellipsoid is
\[
 \boxed{\ \mathcal E_m=\{\mu+z:z\in L,\ \langle z,C_m^{-1}z\rangle\le 2m-1\}\ .\ }
\]
**All \(3m\) edge vertices are contact points**: \(\langle z_e,C_m^{-1}z_e\rangle=2m-1\) for every \(e\). The optimal covariance's *total spoke weight* satisfies the sharp asymptotic law
\[
\boxed{\ x_m=\tfrac14-3^{-m}+O(m9^{-m})\qquad(m\to\infty\text{ through odd integers}).\ }
\]
In particular the spokes receive strictly less than one quarter of the optimal total weight for every odd \(m\), yet approach one quarter exponentially rapidly.

The \(d\) positive eigenvalues of \(C_m\) (with multiplicities) are, for \(k=1,\ldots,m-1\),
\[
\lambda_k^+=\frac{(1-x_m)(1+\cos(2\pi k/m))+2x_m}{m},
\]
and, for \(k=0,\ldots,m-1\),
\[
\lambda_k^-=\frac{(1-x_m)(1+\cos(2\pi k/m))}{m}.
\]
Thus the intrinsic principal semiaxes are \(\sqrt{(2m-1)\lambda_k^\pm}\). Moreover, putting \(F_m=(1+u_m)^m+(1-u_m)^m\),
\[
\det{}_L C_m=\frac{F_m^2(1-u_m^2)^m}{(2m)^{2m-1}},\qquad
\operatorname{vol}_{2m-1}(\mathcal E_m)
=\kappa_{2m-1}(2m-1)^{(2m-1)/2}\sqrt{\det{}_L C_m},
\]
where \(\kappa_d=\pi^{d/2}/\Gamma(1+d/2)\) is the Euclidean unit-ball volume.

## Assumptions and scope
The graph is simple, connected and **odd-rimmed** (\(m=3,5,7,\ldots\)); its \(3m\) vertices in the edge polytope are the unsigned incidence vectors \(e_i+e_j\), *not* signed root vectors \(\pm(e_i-e_j)\). All Euclidean quantities use the inherited metric on the affine hyperplane \(\sum_i y_i=2\), without an arbitrary lattice-coordinate transformation. The ellipsoid's inverse covariance is taken on the tangent space \(L\), where it is invertible. The weights are only a construction and description of the ellipsoid; no conductance-budget optimization on the graph is claimed. No even-rim result is asserted.

## Proof
**1. Affine span and center.** Since \(G_m\) is connected and has an odd cycle, its unsigned incidence matrix has full row rank \(2m\): a vector orthogonal to each incidence column obeys \(h_i+h_j=0\) along each edge; an odd cycle forces all entries of \(h\) to vanish by connectivity. Therefore the differences \(v_e-v_{e'}\) span the \((2m-1)\)-dimensional zero-sum hyperplane \(L\). Rotations, rim interchange and reflections act transitively on the graph vertices, and the unique enclosing ellipsoid is fixed by these orthogonal symmetries. Its center must be the unique invariant point with coordinate sum \(2\), namely \(\mu\). Both edge orbits have mean \(\mu\).

**2. Positive definite covariance and spectral modes.** For \(0<x<1\) form \(C_m(x)\) from the displayed covariance formula with \(x\) in place of \(x_m\). In Fourier mode \(k\), separating vectors symmetric or antisymmetric between the two rims, the rim signless Laplacian has eigenvalue \(2+2\cos(2\pi k/m)\) on each layer; the spoke signless Laplacian has eigenvalue \(2\) on the symmetric sector and \(0\) on the antisymmetric one. Subtracting the mean covariance removes only the symmetric constant mode. The nonzero eigenvalues are exactly the two displayed families with \(x\) substituted. As \(m\) is odd, none of the antisymmetric cosines equals \(-1\), hence all \(d\) eigenvalues are positive.

**3. Determinant and strictly concave optimization.** Put \(u=\sqrt x\), \(A=1+u\), \(B=1-u\) and \(\zeta=\exp(2\pi i/m)\). The symmetric Fourier factors satisfy
\[
(1+x)+(1-x)\cos(2\pi k/m)=\tfrac12|A+B\zeta^k|^2.
\]
The root-of-unity product, for odd \(m\), equals \(\prod_k(A+B\zeta^k)=A^m+B^m\). Removing the constant \(k=0\) factor \(2\) gives \(\prod_{k=1}^{m-1}[(1+x)+(1-x)\cos(2\pi k/m)]=(A^m+B^m)^2/2^{m+1}\). Independently, \(\prod_{k=0}^{m-1}(1+\cos(2\pi k/m))=2^{2-m}\). Multiplying both eigenvalue families proves
\[
D_m(x):=\det{}_L C_m(x)=\frac{\big[(1+\sqrt{x})^m+(1-\sqrt{x})^m\big]^2(1-x)^m}{(2m)^{2m-1}}.
\]
The matrix \(C_m(x)\) depends affinely and nontrivially on \(x\). The second derivative of its log determinant is \(-\operatorname{tr}[(C_m(x)^{-1}C_m'(x))^2]<0\), so \(\log D_m(x)\) is **strictly concave** on \((0,1)\). At \(x=0\), expansion of the square-bracket term yields \((\log D_m)'(0+)=m(m-2)>0\); as \(x\uparrow1\), \(D_m(x)\to0\). Hence there is one and only one optimizer in \((0,1)\). Differentiating in \(u\), cancelling the positive factor \(m\), gives
\[
(1-2u)(1+u)^m=(1+2u)(1-u)^m.
\]
Its unique nonzero solution in \((0,1)\) necessarily belongs to \((0,1/2)\). This proves the defining equation and \(0<x_m<1/4\).

**4. Global Löwner certificate, not just a symmetric candidate.** The symmetry group is transitive on each of the two edge orbits. Thus the leverage \(\langle z_e,C_m(x_m)^{-1}z_e\rangle\) is a constant \(L_R\) for every rim edge and a constant \(L_S\) for every spoke edge. Matrix differentiation of the log determinant gives \(L_S-L_R=(\log D_m)'(x_m)=0\). Taking a covariance trace gives \((1-x_m)L_R+x_mL_S=\operatorname{tr}_L(C_m^{-1}C_m)=d\), so both leverage values equal \(d\). The ellipsoid in the finding therefore contains all vertices, with **every vertex at equality**. After the affine map \(z\mapsto d^{-1/2}C_m^{-1/2}z\), these contact points lie on the unit sphere, have weighted mean zero, and have weighted second moment \(I_L/d\). John's characterization of minimum-volume enclosing ellipsoids, or its elementary trace–determinant proof, shows the unit sphere is the unique minimum-volume ellipsoid containing them: any rival ellipsoid containing the contacts, when tested against their weights, satisfies the determinant lower bound with equality only for that sphere. Transforming back proves global optimality and uniqueness of \(\mathcal E_m\), with no restriction to symmetry-invariant rivals.

**5. Exact exponential approach.** Write \(\delta_m=1/2-u_m>0\). The stationarity equation becomes
\[
\delta_m=(1-\delta_m)\left(\frac{1+2\delta_m}{3-2\delta_m}\right)^m.
\]
For any fixed \(u\in(0,1/2)\), the left side of the preceding equation in \(u\) tends to zero with \(m\) while its positive right side stays fixed, so uniqueness forces \(u_m\to1/2\); hence \(\delta_m\to0\). Taking any fixed neighborhood of \(1/2\) first gives \(\delta_m=O(c^m)\) for some \(c<1\). Expanding the logarithm of the last displayed expression now gives
\[
\delta_m=3^{-m}\bigl(1+O(m\delta_m)\bigr).
\]
This first implies \(\delta_m\sim3^{-m}\), and substituting that bound back sharpens it to \(\delta_m=3^{-m}+O(m9^{-m})\). Finally \(x_m=(1/2-\delta_m)^2=1/4-\delta_m+\delta_m^2\) gives the claimed expansion.

## Verification
Run `python3 verify_odd_prism.py` with NumPy and SciPy installed. The checker constructs all \(3m\) incidence vectors in the original \(2m\)-coordinate embedding, independently obtains the actual tangent-space basis by singular-value decomposition, forms its weighted covariance and computes its eigenvalues, determinant and contact leverages; it also finds the determinant maximizer independently by numerical scalar optimization. Orders \(m=3,5,\ldots,19\) passed. The largest contact residual in those checks was below \(8\times10^{-14}\). Numerical checks and the plotted asymptotic ratios are finite corroboration; the unlimited-order assertions follow from the proof above.

## Relationship to prior work
The ordinary graph-edge polytope and its intrinsic affine dimension are established in Nagaoka–Tsuchiya (arXiv:1712.06078v1); their results concern reflexive embeddings and normality, not minimal Euclidean outer ellipsoids. D'Alì–Delucchi–Michałek (arXiv:1910.05193v1) concerns **symmetric** edge polytopes and combinatorial/Ehrhart properties, a different object. Existing deterministic optimal weighted-spanning-tree work includes Khosoussi et al. (arXiv:1604.01116v1) and the publicly available *D-optimal cyclic ladders with a linear-price crossover* (2026). The latter optimizes a **signed Laplacian** spanning-tree determinant and can cover a bipartite even-prism analogue by sign switching; **no even-prism claim is made here**. For odd \(m\), the graph is nonbipartite, its unsigned signless-incidence covariance cannot be converted to a Laplacian by vertex sign switching, and the root-of-unity product above has a plus-sign twist. The resulting explicit odd-prism ellipsoid, full vertex contact certificate and exponential \(3^{-m}\) correction were not found in the inspected literature or semantically searched results. Historical priority remains provisional, especially under optimal-design or signless-Laplacian terminology.

## Limitations
This result covers only ordinary unsigned incidence-vector edge polytopes of **odd** polygonal prisms with unit incidence coordinates and intrinsic Euclidean volume; it does not assert analogous results for even prisms, arbitrary weighted graphs, or signed root polytopes. The optimized weight is the unique positive implicit root, not an elementary closed radical uniformly in \(m\). The scientific review is same-model only; no independent mathematical audit or historical-priority certification is asserted.

## References
1. T. Nagaoka and A. Tsuchiya, *Reflexive polytopes arising from edge polytopes*, arXiv:1712.06078v1 (first public 2017-12-17), Sections 1–3. https://arxiv.org/html/1712.06078v2 .
2. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (first public 2019-10-11), Sections 1–4. https://arxiv.org/abs/1910.05193 .
3. K. Khosoussi, G. S. Sukhatme, S. Huang and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs*, arXiv:1604.01116v1 (2016-04-05). https://arxiv.org/abs/1604.01116 .
4. *D-optimal cyclic ladders with a linear-price crossover*, public published-finding corpus research record, 2026-11-02, identifier `1c968d5ff6c5`. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-d-optimal-cyclic-ladders-with-a-linear-price-crossover--1c968d5ff6c5 .
