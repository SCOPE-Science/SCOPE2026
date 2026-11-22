# A universal regular-simplex John contact frame and Gaussian-window volume law for spherical caps

## Finding

**Theorem.** Fix any integer \(d\ge2\) and \(-1<t<1\). For the one-sided Euclidean unit-ball cap
\[
K_{d,t}=\{(x,z)\in\mathbb R\times\mathbb R^{d-1}:x\ge t,\ x^2+\|z\|^2\le1\},
\]
put
\[
S=\sqrt{(d-1)^2t^2+4d},\qquad
u=\frac{S-(d+1)t}{2(d+1)},\qquad c=t+u,\qquad v=\sqrt{u^2+dcu}.
\]
The **unique maximum-volume inscribed ellipsoid**, over all centers and orientations, is
\[
J_{d,t}=\left\{(x,z):\frac{(x-c)^2}{u^2}+\frac{\|z\|^2}{v^2}\le1\right\}.
\]
After transforming this ellipsoid to the Euclidean unit ball, there are precisely two kinds of boundary contacts: the single flat-face point \(-e_1\), and the latitude \(\{(1/d,\sqrt{1-d^{-2}}\,\omega):\omega\in S^{d-2}\}\). Exactly \(d+1\) of these contacts, chosen as a regular simplex, carry the equal positive John weights \(d/(d+1)\); this normalized frame is independent of \(t\).

Writing \(\kappa_j=\pi^{j/2}/\Gamma(j/2+1)\), the exact occupied fraction is
\[
Q_d(t)=\frac{\operatorname{Vol}_d(J_{d,t})}{\operatorname{Vol}_d(K_{d,t})}
=\frac{\kappa_d}{\kappa_{d-1}}
\frac{u v^{d-1}}{\int_t^1(1-x^2)^{(d-1)/2}\,dx}.
\]
Its endpoint limits are \(\lim_{t\downarrow-1}Q_d(t)=1\) and
\[
\lim_{t\uparrow1}Q_d(t)=\frac{\kappa_d}{\kappa_{d-1}}\left(\frac d{d+1}\right)^d.
\]
For each fixed real \(\lambda\), the sharp high-dimensional central-limit window is
\[
\lim_{d\to\infty}\sqrt d\,Q_d(\lambda/\sqrt d)
=G(\lambda)=\frac{\alpha(\lambda)\exp(-\beta(\lambda)^2/2)}{\overline\Phi(\lambda)},
\quad \alpha(\lambda)=\frac{\sqrt{\lambda^2+4}-\lambda}{2},\quad
\beta(\lambda)=\frac{\sqrt{\lambda^2+4}+\lambda}{2},
\]
where \(\overline\Phi(\lambda)=\int_\lambda^\infty(2\pi)^{-1/2}e^{-s^2/2}\,ds\). The profile \(G\) is **strictly decreasing on the whole real line**, with
\[
\lim_{\lambda\to-\infty}G(\lambda)=+\infty,\qquad
\lim_{\lambda\to+\infty}G(\lambda)=\frac{\sqrt{2\pi}}{e},
\qquad G(\lambda)>\frac{\sqrt{2\pi}}e.
\]
The last endpoint matches \(\lim_{d\to\infty}\sqrt d\,\lim_{t\uparrow1}Q_d(t)=\sqrt{2\pi}/e\).

## Assumptions and scope

The cap includes the cutting disk and curved ball boundary, is full-dimensional, and is equipped with ordinary \(d\)-dimensional Euclidean volume. An ellipsoid is any nondegenerate affine image of the unit ball; no axial-symmetry restriction is imposed on competitors. The strict range \(-1<t<1\) avoids the degenerate cap at \(t=1\) and the redundant cut at \(t=-1\). The contact set is described after the affine normalization \((s,w)\mapsto(c+us,vw)\). In the planar case \(S^0\) has its usual two points. The claimed Gaussian limit is pointwise for fixed \(\lambda\), not asserted uniformly for growing \(\lambda\).

## Proof

**1. Parameters and containment.** For \(-1<t<1\), \(S>(d+1)|t|\), so \(u>0\) and \(c>0\). From the displayed radical one obtains
\[
 c-u=t,\qquad v^2-u^2=dcu,\qquad c^2+v^2+\frac{cu}{d}=1.
\]
These identities follow equivalently by substituting \(c=t+u\) into the last two and solving the resulting quadratic for its positive root. For every \(s\in[-1,1]\) and \(\omega\in S^{d-2}\), the boundary point of the proposed ellipsoid satisfies
\[
 (c+us)^2+v^2(1-s^2)
 =1-dcu\left(s-\frac1d\right)^2\le1,
\quad c+us\ge c-u=t.
\]
Therefore its entire boundary, and hence its solid convex hull, lies in the cap. Equality with the cutting plane holds only at \(s=-1\); equality with the sphere holds exactly at \(s=1/d\). The flat supporting normal in normalized coordinates is \(-e_1\). At a curved contact, the normal to the transformed sphere constraint is a positive multiple of the corresponding unit vector \(p=(1/d,\sqrt{1-d^{-2}}\,\omega)\), because
\[
 \left(u(c+u/d),\;v^2\sqrt{1-d^{-2}}\,\omega\right)=v^2p.
\]
Thus each listed contact gives a true supporting inequality \(p\cdot w\le1\) for the normalized cap.

**2. A finite universal John frame and unrestricted optimality.** Select \(d\) vertices \(\omega_1,\dots,\omega_d\in S^{d-2}\) of a centered regular \((d-1)\)-simplex: \(\omega_i\cdot\omega_j=-1/(d-1)\) for \(i\ne j\). Set
\[
 p_0=-e_1,\qquad p_i=\left(\frac1d,\sqrt{1-\frac1{d^2}}\,\omega_i\right),\quad 1\le i\le d.
\]
Their pairwise inner products equal \(-1/d\). Consequently \(\sum_{i=0}^dp_i=0\) and \(\sum_{i=0}^dp_ip_i^{\mathsf T}=\frac{d+1}{d}I_d\). Equal weights \(w_i=d/(d+1)\) satisfy
\[
 \sum_iw_ip_i=0,\qquad\sum_iw_ip_ip_i^{\mathsf T}=I_d.
\]
For completeness, these certificates imply *global*, not merely symmetric-class, optimality. Any ellipsoid inside the affine-normalized cap may be written \(y+A B_d\) with \(A\) symmetric positive definite. Supporting inequalities at all \(p_i\) imply
\[
 p_i\cdot y+\|Ap_i\|\le1.
\]
Since \(\|Ap_i\|\ge p_i^{\mathsf T}Ap_i\), the weighted sum yields \(\operatorname{tr}A\le\sum_iw_i=n\), with \(n=d\). The arithmetic-geometric mean inequality on the eigenvalues gives \(\det A\le(\operatorname{tr}A/d)^d\le1\). Equality forces \(A=I_d\), then all \(p_i\cdot y=0\) by the weighted-sum equality, so \(y=0\) because the contacts span \(\mathbb R^d\). Therefore the unit ball is the unique largest inscribed ellipsoid of the normalized cap, proving the asserted formula and contact classification.

**3. Exact volumes and thin-cap endpoint.** Slicing the cap gives
\[
 \operatorname{Vol}_d(K_{d,t})=\kappa_{d-1}\int_t^1(1-x^2)^{(d-1)/2}dx;
\quad\operatorname{Vol}_d(J_{d,t})=\kappa_d u v^{d-1}.
\]
At \(t\downarrow-1\), the parameters approach \((c,u,v)=(0,1,1)\), while the cap fills the unit ball, proving the first limit. As \(\eta=1-t\downarrow0\), exact parameter expansions give
\[
 u=\frac{2d}{(d+1)^2}\eta+O_d(\eta^2),\qquad
 v=\frac{\sqrt2\,d}{d+1}\sqrt\eta+O_d(\eta^{3/2}),
\]
and
\[
 \int_t^1(1-x^2)^{(d-1)/2}dx
 \sim\frac{2^{(d+1)/2}}{d+1}\eta^{(d+1)/2}.
\]
Their quotient yields \(\frac{\kappa_d}{\kappa_{d-1}}(d/(d+1))^d\) exactly as stated.

**4. The Gaussian window.** Put \(t=\lambda/\sqrt d\). The explicit root and normalization imply
\[
 \sqrt d\,u\to\alpha(\lambda),\quad
 \sqrt d\,c\to\beta(\lambda),\quad
 d(1-v^2)\to\beta(\lambda)^2,
\]
so \(v^{d-1}\to\exp(-\beta(\lambda)^2/2)\). If \(X_d\) denotes the first coordinate of a uniform random point of the \(d\)-ball, its density is \(\frac{\kappa_{d-1}}{\kappa_d}(1-x^2)^{(d-1)/2}\) on \([-1,1]\). Scaling by \(\sqrt d\) and the gamma-ratio asymptotic show \(\sqrt d X_d\) converges to the standard normal distribution. Hence the cap-volume fraction tends to \(\overline\Phi(\lambda)\), giving \(G\).

To establish strict decrease, set \(h(\lambda)=\phi(\lambda)/\overline\Phi(\lambda)\), with \(\phi\) the standard normal density. Because \(\alpha=1/\beta\), \(\beta^2-\lambda\beta=1\), and \(\beta'>0\), direct differentiation gives
\[
 \frac{G'(\lambda)}{G(\lambda)}=h(\lambda)-\beta(\lambda).
\]
For a normal random variable conditioned to be at least \(\lambda\), its mean and variance are
\[
 h(\lambda),\qquad 1+\lambda h(\lambda)-h(\lambda)^2>0.
\]
Thus \(h(h-\lambda)<1=\beta(\beta-\lambda)\). Both \(h\) and \(\beta\) are strictly larger than \(\max\{0,\lambda\}\); there \(z\mapsto z(z-\lambda)\) is strictly increasing. Consequently \(h<\beta\) and \(G'<0\). The limits follow from the normal Mills ratio and the elementary expansions \(\alpha\sim-\lambda\) at \(-\infty\), \(\alpha\sim1/\lambda\), \(\beta=\lambda+1/\lambda+o(1/\lambda)\) at \(+\infty\). Finally, \(\kappa_d/\kappa_{d-1}\sim\sqrt{2\pi/d}\) and \((d/(d+1))^d\to e^{-1}\), matching the thin-cap coefficient. This completes the proof. \(\square\)

## Verification

A standalone Python checker, `check_cap_john.py`, verifies explicit parameter identities and full-angle containment on sampled directions, finite regular-simplex isotropy, cap-to-ellipsoid volume inequalities, thin-cap constants, representative Gaussian-window convergence, and decreasing sampled values of the limiting profile. It passed **6,922 deterministic diagnostic assertions**. The all-dimensional claims are proved by the displayed identities, contact certificate, and asymptotic reasoning, not inferred from finite tests. Execute with `python check_cap_john.py`; Python, NumPy, and SciPy are required.

## Relationship to prior work

John's general maximal-inscribed-ellipsoid contact theorem is classical; Gruber and Schuster give the noncentrally symmetric isotropic-contact criterion. Todd (1982) explicitly solves the *opposite* optimization, minimum-volume **enclosing** ellipsoids of one-sided and two-sided cuts; its all-cut formula is not asserted as part of this finding. The published result [R1] gives a strictly increasing ratio of Todd's **enclosing** ellipsoid to the cap and a different Gaussian-window profile. The published symmetric-lens result [R2] has two curved-ball constraints and symmetric latitude contacts, not the single flat-face contact here. The published ball-box result [R3] treats symmetric coordinate-slab cuts, not one-sided caps. These sources supply related techniques and comparisons but do not state the complete one-sided **inscribed** formula together with its universal simplex contacts and strictly decreasing occupied-volume Gaussian profile. Exhaustive historical priority remains unverified.

## Limitations

The theorem covers a Euclidean unit ball intersected with exactly one axial halfspace, in dimensions at least two; affine images follow by affine invariance, but multiple nonparallel cuts, arbitrary convex bodies, and statistical-noise robustness are not asserted. The Gaussian-window limit is only at fixed \(\lambda\); the two endpoint orders of limits are identified numerically and analytically but no uniform double scaling is claimed. The exact global finite-dimensional monotonicity of \(Q_d(t)\) is **not claimed**. Independent mathematical validation and exhaustive historical-priority determination have not been performed.

## References

1. M. J. Todd, *On Minimum Volume Ellipsoids Containing Part of a Given Ellipsoid*, Mathematics of Operations Research **7** (1982), 253–261, published May 1, 1982, https://doi.org/10.1287/moor.7.2.253 ; full author-uploaded article https://www.researchgate.net/publication/242929698_On_Minimum_Volume_Ellipsoids_Containing_Part_of_a_Given_Ellipsoid .
2. P. M. Gruber and F. E. Schuster, *An Arithmetic Proof of John's Ellipsoid Theorem*, Archiv der Mathematik **85** (2005), 82–88, https://doi.org/10.1007/s00013-005-1326-x ; openly accessible version https://arxiv.org/abs/1207.7246 (first deposited July 31, 2012).
3. [R1] *Strict monotonicity and dimensional scaling of enclosing-ellipsoid excess volume for Euclidean ball caps*, public research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-enclosing-ellipsoid-transition-and-monotone-excess-volume--8f18f059a757 .
4. [R2] *Exact John ellipsoids and contact latitudes of symmetric ball lenses in all dimensions*, public research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-john-ellipsoids-and-contact-latitudes-of-symmetric-ball-le--02e413e91d3d .
5. [R3] *Water-filling classification of extremal ellipsoids for ball–box intersections*, public research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-water-filling-classification-of-extremal-ellipsoids-for-ball-box--cec0aced836e .
