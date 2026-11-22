# Sharp square-root rigidity and twisted skew witnesses for three weighted cylinders around a sphere

## Finding

Fix any positive labeled weights \(b_1,b_2,b_3\). Consider three infinite solid right circular cylinders with radii \(r_i=\lambda b_i\), each externally tangent to the closed Euclidean unit ball, with pairwise disjoint interiors. Put \(u_i=1/b_i\) and
\[
\Lambda=\sum_{i=1}^3u_i+2\sqrt{u_1u_2+u_2u_3+u_3u_1}.
\]
The **sharp admissible scale** is \(\lambda\le\Lambda\). Every configuration attaining \(\lambda=\Lambda\) has three mutually parallel axes perpendicular to a great-circle plane. Its three perpendicular planar sections are mutually externally tangent disks, each tangent to the central unit disk. For prescribed labeled weights this configuration is unique up to Euclidean orthogonal transformations and reversal of axis orientations.

The main new quantitative assertion is **sharp stability in the full cylinder configuration space**. For each fixed triple of positive weights there exist \(\varepsilon_0,C,c>0\) such that whenever \(0\le\varepsilon=\Lambda-\lambda<\varepsilon_0\), and \(q_i\in\mathbb S^2\) is the contact normal and \(v_i\in\mathbb S^2\) an arbitrary oriented representative of the \(i\)-th axis, there are an orthogonal transformation \(R\), a unit vector \(e\), and a fixed canonical maximizing triple \((q_i^*,e)\) with
\[
 \max_i\bigl(\|q_i-Rq_i^*\|+\min_{\sigma_i\in\{-1,1\}}\|v_i-\sigma_i Re\|\bigr)\le C\sqrt\varepsilon.
\]
The exponent \(1/2\) cannot be replaced by any larger exponent uniformly over configurations, **even if all three axes are required to be pairwise nonparallel**: for each sufficiently small \(\varepsilon>0\) an explicit packing has this radial deficit and at least one pair of unoriented axes separated by \(c\sqrt\varepsilon\). The constants are allowed to depend on the fixed weights.

For example, \((b_1,b_2,b_3)=(1,2,3)\) gives \(\Lambda=23/6\); the minimizing rigidity exponent is again exactly \(1/2\), despite the three distinct cylinder radii.

## Assumptions and scope

An infinite cylinder of radius \(r_i\) is the closed \(r_i\)-neighborhood of an affine line \(L_i=p_i+\mathbb Rv_i\), where \(\|v_i\|=1\). External tangency to the unit ball means the distance of \(L_i\) from the origin is \(1+r_i\). Choose the unique nearest point \(p_i\perp v_i\), so \(\|p_i\|=1+r_i\), and set \(q_i=p_i/(1+r_i)\). Disjoint interiors are equivalent to \(\mathrm{dist}(L_i,L_j)\ge r_i+r_j\) for all pairs. Reversing any \(v_i\) does not change its cylinder. We fix the weights, vary only \(\lambda>0\), the contact points, and axis directions. The stability assertion is near the global optimum; it does not claim uniform constants as the weights degenerate, nor apply to four or more cylinders.

## Proof

**1. A spherical packing bound.** The closed ball of radius \(r_i\) centered at \(p_i\) lies inside the corresponding cylinder. Therefore cylinder nonoverlap gives
\[
 \|p_i-p_j\|\ge r_i+r_j.
\]
Writing \(a_{ij}=\arccos(q_i\cdot q_j)\), the cosine law makes this equivalent to
\[
 a_{ij}\ge\alpha_{ij}(\lambda):=2\arcsin\left(
 \frac{\lambda\sqrt{b_ib_j}}{\sqrt{(1+\lambda b_i)(1+\lambda b_j)}}\right).
\]
Each \(\alpha_{ij}\) lies in \((0,\pi)\) and is strictly increasing in \(\lambda\). Every triple of unit vectors satisfies
\[
 a_{12}+a_{23}+a_{31}\le 2\pi.
\]
Indeed, the spherical triangle inequality through the antipode \(-q_3\) reads \(a_{12}\le(\pi-a_{13})+(\pi-a_{23})\). At equality, the three vectors lie on one great circle, with the three consecutive gaps below \(\pi\). Consequently every feasible \(\lambda\) obeys \(\sum_{i<j}\alpha_{ij}(\lambda)\le2\pi\).

Conversely, if this inequality holds, choose three cyclic gaps \(\ell_{12},\ell_{23},\ell_{31}\in[\alpha_{ij},\pi]\) summing to \(2\pi\). Such gaps exist because their lower-sum is at most \(2\pi\), while their upper-sum is \(3\pi\). Place \(q_i\) on a great circle in that cyclic order and choose all cylinder axes perpendicular to its plane. The distances of the parallel axes then satisfy the required clearance bounds, so the inequality is also sufficient. The increasing sum starts at zero and tends to \(3\pi\), hence a unique \(\Lambda>0\) satisfies \(\sum_{i<j}\alpha_{ij}(\Lambda)=2\pi\).

**2. Explicit scale and equality rigidity.** At \(\Lambda\) the three planar disks with radii \(\Lambda b_i\) and the central unit disk are pairwise tangent. The classical Descartes circle theorem gives
\[
 \left(1+\frac{\sum_i u_i}{\Lambda}\right)^2
 =2\left(1+\frac{\sum_i u_i^2}{\Lambda^2}\right),
\]
so \(\Lambda=\sum_i u_i\pm2\sqrt{\sum_{i<j}u_iu_j}\). The desired root is the plus sign: the root selected by the strictly increasing spherical-angle sum varies continuously with the weights, the roots never coincide for positive weights, and at equal weights the selected root is the familiar \(3+2\sqrt3\) times the reciprocal common weight.

At the optimum \(a_{ij}=\alpha_{ij}(\Lambda)\) for every pair, because the sum of all three nonnegative slack angles must vanish. Equality in the spherical perimeter bound forces a great-circle contact triple. Thus the three center separations \(p_j-p_i\) are coplanar and have lengths exactly \(r_i+r_j\). On the other hand, \(\mathrm{dist}(L_i,L_j)\le\|p_j-p_i\|\), and equality together with \(\mathrm{dist}(L_i,L_j)\ge r_i+r_j\) forces both \(v_i\) and \(v_j\) perpendicular to \(p_j-p_i\). For each \(i\), the two independent separations from \(p_i\) therefore force \(v_i\) to be perpendicular to their plane. The three axes are parallel; the labeled contact triple is unique up to orthogonal transformations.

**3. Quantitative contact-point control.** Write \(\varepsilon=\Lambda-\lambda\ge0\). Smoothness of the \(\alpha_{ij}\) near \(\Lambda\) gives
\[
 0\le a_{ij}-\alpha_{ij}(\lambda)
 \le2\pi-\sum_{k<l}\alpha_{kl}(\lambda)=O_b(\varepsilon),
\]
where \(O_b\) denotes constants depending only on the fixed weights. Therefore each \(a_{ij}=\alpha_{ij}(\Lambda)+O_b(\varepsilon)\). After one rigid transformation, take \(q_1=q_1^*\), \(q_2\) within \(O_b(\varepsilon)\) of \(q_2^*\), both in the canonical equatorial plane. The two scalar products \(q_3\cdot q_1\) and \(q_3\cdot q_2\) determine the equatorial projection of \(q_3\) to within \(O_b(\varepsilon)\) because the limiting pair is linearly independent. Its limiting projection has unit length; \(\|q_3\|=1\) then bounds the perpendicular component by \(O_b(\sqrt\varepsilon)\). Thus all three contact normals are \(O_b(\sqrt\varepsilon)\) from the canonical triple. The argument also covers the limiting equality case directly.

**4. Quantitative axis control.** The squared distance slack
\[
 E_{ij}:=\|p_i-p_j\|^2-(r_i+r_j)^2
\]
is nonnegative and \(O_b(\varepsilon)\), by the angular estimates and smooth dependence of the radii. Since every point on \(L_i\) remains at distance at least \(r_i+r_j\) from \(L_j\), and in particular the distance from \(p_j\) to \(L_i\) is at least \(r_i+r_j\), orthogonal projection onto the line yields
\[
 |v_i\cdot(p_j-p_i)|^2\le E_{ij}\le C_b\varepsilon.
\]
For each \(i\), its two outgoing separation vectors converge to two linearly independent vectors spanning the canonical equatorial plane. Their uniformly bounded inverse Gram matrix implies the projection of \(v_i\) onto that plane is \(O_b(\sqrt\varepsilon)\). Because \(v_i\) is a unit vector, it is within \(O_b(\sqrt\varepsilon)\) of one of the two common unit normals. Combining with step 3 establishes the displayed stability estimate.

**5. Sharpness through explicitly skew cylinders.** Fix the optimal equatorial contact normals \(q_i^*\), and for smaller \(\lambda=\Lambda-\varepsilon\) set \(p_i=(1+\lambda b_i)q_i^*\). On the equatorial plane let \(J\) be counterclockwise rotation by \(\pi/2\), and consider the axes
\[
 L_i(t)=p_i+\mathbb R\bigl(e_3+tJp_i\bigr),\qquad t\ne0.
\]
These axes remain tangent to the unit sphere because \(p_i\cdot(e_3+tJp_i)=0\). With \(s_{ij}=\|p_i-p_j\|\), \(H_{ij}=\det(p_i,p_j)/s_{ij}\), direct cross products give the **exact** skew-line distance formula
\[
 \mathrm{dist}(L_i(t),L_j(t))^2
 =\frac{s_{ij}^2}{1+t^2H_{ij}^2}.
\]
For \(\beta_{ij}=\alpha_{ij}(\Lambda)\), define the planar squared-clearance slack
\[
 F_{ij}(\lambda)=4\left[(1+\lambda b_i)(1+\lambda b_j)\sin^2(\beta_{ij}/2)-\lambda^2b_ib_j\right].
\]
It vanishes at \(\Lambda\), while its derivative there satisfies
\[
 F_{ij}'(\Lambda)=-\frac{4\Lambda b_ib_j\bigl(2+\Lambda(b_i+b_j)\bigr)}{(1+\Lambda b_i)(1+\Lambda b_j)}<0.
\]
Thus \(F_{ij}(\Lambda-\varepsilon)=K_{ij}\varepsilon+O_b(\varepsilon^2)\) with \(K_{ij}>0\). Taking \(t=k\sqrt\varepsilon\) for a fixed sufficiently small \(k>0\) ensures all three exact skew-line squared distances are at least \((r_i+r_j)^2\); hence these are admissible cylinders. Their normalized directions are \((e_3+tJp_i)/\sqrt{1+t^2\|p_i\|^2}\), and for every distinct pair their unoriented angular separation is \(k\|p_i^*-p_j^*\|\sqrt\varepsilon+O_b(\varepsilon)\), strictly positive and of order \(\sqrt\varepsilon\). No rigid transformation can simultaneously bring all three axes closer than half this pairwise separation to a common direction. This proves sharpness for every fixed positive weight triple.

## Verification

A standard-library Python program `verify.py` recomputes the angle-sum equation, all three pairwise tangencies at the threshold, their exact first-variation coefficients, and the explicit skew-line distances. It tests 205 positive weight triples, including equal weights, three distinct weights, extreme weight ratios, and 200 fixed-seed random triples. It prints `PASS 205 unequal/equal weight triples` with a nonzero angular-separation-to-square-root-deficit range when successful. These numerical tests corroborate formulas only; the continuum, uniqueness, and sharp asymptotic assertions follow from the preceding proof.

## Relationship to prior work

Glazyrin (2026, Section 1) explicitly records the *known* global optimum \(3+2\sqrt3\) for three congruent cylinders, following by replacing cylinders with tangent balls; it does not state the weighted quantitative axis-rigidity theorem. The Descartes circle theorem supplies the algebraic weighted value of \(\Lambda\) once planar equality has been established; that classical equation and the elementary three-ball reduction are credited and not asserted to be independently new. Ogievetsky and Shlosman (2019, Section 2.1) record a quadratic-decay deformation for three **equal balls**, so the square-root scaling by itself is not new. The present result controls **all contact points and axial directions of every near-optimal cylinder arrangement**, for arbitrary fixed positive and unequal radii, and attains the sharp rate with explicitly constructed pairwise skew axes. A relevant published three-cylinder result for prescribed conical **nonparallel axis directions** gives an exact finite-parameter optimum but does not compare arbitrary radii or establish the asserted free-axis stability modulus.

## Limitations

The constants \(C_b,c_b,\varepsilon_0\) are existential and depend on the fixed positive weights; no explicit optimal stability constant, uniform degenerate-weight bound, or nonlocal stability claim is made. The two-dimensional circle formula and the known congruent three-cylinder threshold are background, not the newly assessed mathematical contribution. Historical priority beyond the full texts and records inspected is not conclusively resolved. Independent mathematical validation has not been performed.

## References

1. A. Glazyrin, *Upper bounds for packings of cylinders around the unit sphere*, arXiv:2611.00251v1 (first public 2026-10-30), https://arxiv.org/html/2611.00251v1 .
2. O. Ogievetsky and S. Shlosman, *Critical configurations of solid bodies and the Morse theory of MIN functions*, arXiv:1907.01896v1 (2019), https://arxiv.org/html/1907.01896v1 .
3. D. Ismailescu and P. Laskawiec, *Dense Packings with Nonparallel Cylinders*, arXiv:1809.10721 (2018), https://arxiv.org/abs/1809.10721 .
4. *Exact two-transition packing law for three cylinders with prescribed conical axes*, publicly indexed mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-two-transition-packing-law-for-three-cylinders-with-prescr--953b1cb63fb8 .
5. Descartes circle theorem (classical); for a modern formula see https://mathworld.wolfram.com/DescartesCircleTheorem.html .
