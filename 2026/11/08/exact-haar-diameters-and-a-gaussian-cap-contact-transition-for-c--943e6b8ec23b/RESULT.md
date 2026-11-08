# Exact Haar diameters and a Gaussian cap-contact transition for central sections of Euclidean cylinders

## Finding

For integers \(d\ge 3\) and \(2\le m<d\), and real \(h>0\), let \(C_{d,h}=B_2^{d-1}\times[-h,h]\subset\mathbb R^d\). Let \(L\) be an independent Haar-uniform \(m\)-dimensional linear subspace and set \(D=\operatorname{diam}_2(C_{d,h}\cap L)\). If \(B=\|P_L e_d\|_2^2\), then
\[
 B\sim\operatorname{Beta}\left(\frac m2,\frac{d-m}{2}\right),\qquad
 \boxed{D=2\sqrt{1+\min\left\{h^2,\frac{B}{1-B}\right\}}}\quad\text{almost surely}.
\]
For \(0\le t<h\), the complete interior cumulative distribution is
\[
 \boxed{\mathbb P\{D\le 2\sqrt{1+t^2}\}
 =I_{t^2/(1+t^2)}\left(\frac m2,\frac{d-m}{2}\right)},
\]
where \(I_z\) is the regularized incomplete beta integral. The law has no atom except at the **maximum** \(D_*=2\sqrt{1+h^2}\), where the atom is strictly positive and equals
\[
 \boxed{p_{d,m,h}=1-I_{h^2/(1+h^2)}\left(\frac m2,\frac{d-m}{2}\right)}.
\]
In the planar-section case \(d=3,m=2\), its continuous CDF equals \(1-(1+t^2)^{-1/2}\), and the endpoint atom is \((1+h^2)^{-1/2}\).

There is a sharp high-dimensional cap-contact transition. Suppose \(d\to\infty\) with \(m/d\to\rho\in(0,1)\). At fixed \(h\) one has \(p_{d,m,h}\to1\) if \(h<\sqrt{\rho/(1-\rho)}\), and \(p_{d,m,h}\to0\) if \(h>\sqrt{\rho/(1-\rho)}\). More precisely, for fixed \(u\in\mathbb R\) and
\[
 h_d=\sqrt{\frac{m}{d-m}}+\frac{u}{\sqrt d},
 \qquad\boxed{p_{d,m,h_d}\longrightarrow1-\Phi\bigl(u\sqrt2(1-\rho)\bigr)},
\]
where \(\Phi\) is the standard normal CDF; \(h_d>0\) for all sufficiently large \(d\). There is also a distinct fixed-codimension limit: if \(m=d-k\), with a fixed positive integer \(k\), and \(h_d=c\sqrt d\) for \(c>0\), then
\[
 \boxed{\frac{D_{d,d-k,h_d}}{2\sqrt d}\ \Longrightarrow\
 \min\left\{c,\frac{1}{\sqrt{\chi_k^2}}\right\}},
 \qquad
 \boxed{p_{d,d-k,h_d}\longrightarrow
 \mathbb P\left\{\chi_k^2\le c^{-2}\right\}}.
\]

## Assumptions and scope

The cylinder is **solid**, with a Euclidean unit ball in the first \(d-1\) coordinates and half-height \(h>0\). The random plane is linear and central (through the origin), sampled from normalized Haar probability on the Grassmannian; this differs from a motion-invariant randomly offset slicing plane. Diameters are ordinary Euclidean diameters in the ambient space. The condition \(m\ge2\) is essential to the transverse-direction argument. All finite-dimensional equalities concern every integer \(d\ge3\), every \(2\le m<d\), and every \(h>0\). The limiting proportions and codimensions are stated separately and not conflated.

## Proof

**Exact geometric radius.** Fix a subspace \(L\) and let \(b=\|P_Le_d\|\), \(a=\sqrt{1-b^2}\); first take \(0<b<1\). Write \(p=P_Le_d/b\in L\), so that its last coordinate equals \(b\), and its horizontal component has length \(a\). The \((m-1)\)-dimensional subspace \(H=L\cap e_d^\perp\) is orthogonal to \(p\). Every \(x\in L\) with last coordinate \(z\) has the unique decomposition
\[
 x=\frac zb p+v,\qquad v\in H.
\]
Horizontal orthogonality gives
\[
 \|x_{1:d-1}\|^2=\frac{a^2z^2}{b^2}+\|v\|^2.
\]
Consequently the cylinder conditions imply \(|z|\le\min(h,b/a)\) and \(\|x\|^2=\|x_{1:d-1}\|^2+z^2\le 1+\min(h^2,b^2/a^2)\). For \(z_*=\min(h,b/a)\), since \(\dim H=m-1\ge1\), choose \(v\in H\) of squared norm \(1-a^2z_*^2/b^2\). This yields an \(x\) in the cylinder section with \(\|x\|^2=1+z_*^2\). The section is centrally symmetric, so its diameter is twice this radius. The cases \(b=0\) and \(b=1\) follow directly or by continuity and are null events under the stated Haar law.

**Haar projection law and CDF.** By rotational invariance, the squared length of the projection of any fixed unit vector on a Haar \(m\)-plane has law \(G_m/(G_m+G_{d-m})\), where \(G_m\) and \(G_{d-m}\) are independent chi-squared variables with their indicated positive integer degrees of freedom. Thus \(B=b^2\sim\operatorname{Beta}(m/2,(d-m)/2)\) and \(b^2/a^2=B/(1-B)\). For \(t<h\), the event \(D\le2\sqrt{1+t^2}\) is exactly \(B\le t^2/(1+t^2)\). For \(t\ge h\) its probability is one. Continuity of the beta density on \((0,1)\) shows that the only atom is at the maximum, corresponding to \(B\ge h^2/(1+h^2)\), with the displayed positive probability. For \(d=3,m=2\), \(B\sim\operatorname{Beta}(1,1/2)\) gives the elementary special case.

**Proportional dimensions and sharp critical window.** Under \(m/d\to\rho\), the chi-square law of large numbers yields \(B\to\rho\) in probability. Put \(f(v)=\sqrt{v/(1-v)}\) for \(v\in(0,1)\). The cap-contact probability is \(p_{d,m,h}=\mathbb P\{f(B)\ge h\}\), giving the fixed-\(h\) zero-one alternatives. The beta law has mean \(m/d\), variance \(2m(d-m)/(d^2(d+2))\), and the chi-square central limit theorem yields
\[
 \sqrt d\left(B-\frac md\right)\Longrightarrow N(0,2\rho(1-\rho)).
\]
Since \(f'(\rho)=1/(2\sqrt\rho(1-\rho)^{3/2})\), the delta method yields
\[
 \sqrt d\left(f(B)-\sqrt{\frac m{d-m}}\right)
 \Longrightarrow N\left(0,\frac1{2(1-\rho)^2}\right),
\]
which is precisely the asserted Gaussian transition for \(h_d\).

**Fixed codimension.** With \(m=d-k\), the odds \(B/(1-B)=G_{d-k}/G_k\). For fixed \(k\), \(G_{d-k}/d\to1\) in probability and \(G_k\) retains its \(\chi_k^2\) law. Substituting \(h_d=c\sqrt d\) in the exact diameter and atom formulas, and applying Slutsky and continuity of the chi-square distribution, proves both fixed-codimension limits.

## Verification

Run `python verify_cylinder.py` with NumPy and SciPy available. The verifier independently optimizes the squared Euclidean norm over the actual linear-section constraints (rather than using the closed formula) for \(90\) random subspaces, compares \(69\) empirical beta CDF and atom probabilities, and checks \(18\) proportional-dimension/fixed-codimension asymptotic values: \(168\) supplementary checks passed. The infinite-dimensional quantifiers and weak limits follow from the proof, not from Monte Carlo sampling.

## Relationship to prior work

Guédon, Litvak, Tatarko, and Vritsiou (2026) study high-probability upper/lower diameter bounds for general random central sections and give \(\ell_p\)-ellipsoid applications. The present theorem is an exact law for the **non-ellipsoidal cylinder**, including the complete endpoint atom and two critical-dimensional limits. The complete text of that paper was unavailable for direct comparison, so priority relative to potentially uninspected specialized examples is provisional.

The published *Exact random-radius law for one-spike ellipsoids in every codimension* gives a beta-transform law for a smooth axial ellipsoid; its continuous law, obtained by compressing a quadratic form, does not yield the finite-cylinder endpoint atom or the cap-contact phase transition. The published *Exact cylinder shadow mixed moment and sharp positive covariance* studies **orthogonal projections**, not central sections, and area–perimeter covariance, not Euclidean section diameters. Dirksen (2017) studies cylinder-section volumes; Kim–Yaskin–Zvavitch (2015/2017) study distributions of section and projection volumes. Their inspected material does not establish the present distributional claim. These are implication comparisons rather than claims of uniqueness from keyword searches.

## Limitations

The proof uses the Euclidean product structure of the right circular cylinder, centered Haar slicing, and at least two sectional dimensions. It does not provide an exact diameter law for arbitrary convex bodies, off-center randomly positioned planes, or elliptical/oblique cylinders. Neither the available searches nor the inspected sources establish absolute historical priority. The full 2026 motivating paper was not accessible via the available lawful paths, and an older specialized stereology calculation might contain a three-dimensional analogue. Independently verifying historic priority remains appropriate before publication.

## References

1. O. Guédon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131v1, submitted 21 September 2026, https://arxiv.org/abs/2609.24131 .
2. *Exact random-radius law for one-spike ellipsoids in every codimension*, published research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-random-radius-law-for-one-spike-ellipsoids-in-every-codime--e99f37d3b7ae/RESULT.md .
3. *Exact cylinder shadow mixed moment and sharp positive covariance*, published research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-cylinder-shadow-mixed-moment-and-sharp-positive-covariance--1feeb231b707/RESULT.md .
4. H. Dirksen, *Hyperplane sections of cylinders*, Colloquium Mathematicum (2017), doi:10.4064/cm6909-5-2016 .
5. J. Kim, V. Yaskin, A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289, https://arxiv.org/abs/1512.07289 .
6. L. M. Cruz-Orive, *Stereology for the Weibel-Palade Bodies*, Image Analysis & Stereology 45 (2026), doi:10.5566/ias.4005 (isotropic offset sampling rather than Haar-central slicing).
