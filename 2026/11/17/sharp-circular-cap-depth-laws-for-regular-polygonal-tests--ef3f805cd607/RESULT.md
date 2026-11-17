# Sharp circular-cap depth laws for regular polygonal tests

## Finding
Let \(m\ge3\) be an integer. Let \(P_m\subset\mathbb R^2\) be the regular \(m\)-gon with inradius one, written
\[
P_m=\bigcap_{j=0}^{m-1}\{x:\langle u_j,x\rangle\le1\},\qquad
u_j=(\cos(2\pi j/m),\sin(2\pi j/m)).
\]
Let \(\mu\) be a rotationally invariant probability on the closed radius-\(R\) disk, \(R>0\), with a strictly positive continuous radial density throughout the open disk and zero mass outside the disk. For \(t>0\), define the translate depth
\[
d_t(y)=1-\sup_{x:\,y\notin tP_m+x}\mu(tP_m+x),\qquad y\in\mathbb R^2.
\]
Take \(Y\sim\mu\) independently and put \(Z_t=d_t(Y)\). Let \(H(s)=\mu\{x:\langle u_0,x\rangle\ge s\}\), \(0\le s\le R\), and define
\[
a=\frac\pi m,\qquad T_m=\frac{2R}{1-\cos(2\pi/m)},\qquad z_*=H(R\cos a)>0.
\]
**Sharp distribution-free lower-tail theorem.** For every \(t\ge T_m\),
\[
\boxed{\Pr(Z_t\le z)=mz\quad(0\le z\le z_*).}
\]
For \(z_*<z\le\frac12\) one has the strict inequality \(\Pr(Z_t\le z)<mz\); hence the interval is maximal. The law on its entire lower interval is exactly linear and does not depend on the positive radial density. The threshold \(T_m\) is sufficient, not asserted optimal.

**Complete uniform-disk specialization.** If \(\mu\) is uniform area on the disk, rescale \(R\) to one and write
\[
h(q)=\frac{\arccos q-q\sqrt{1-q^2}}\pi,\quad 0\le q\le1,
\qquad z_* =\frac{a-\sin a\cos a}{\pi}.
\]
For any \(z\in[0,\frac12]\), let \(q(z)\in[0,1]\) denote the unique solution of \(h(q(z))=z\). Then, for every \(t\ge T_m\), the entire CDF is
\[
\boxed{\Pr(Z_t\le z)=
\begin{cases}
mz,&0\le z\le z_*,\\
1-\dfrac{\tan a}{a}\,q(z)^2,&z_*\le z\le\frac12.
\end{cases}}
\]
It is zero below zero and one above one-half. The CDF is continuously differentiable but not twice differentiable at its internal threshold \(z_*\). Its exact mean is
\[
\boxed{\mathbb E Z_t=\frac{a}{2\pi}+\frac{(\pi/2-a)\tan a-\sin^2 a}{4\pi a}
=\frac18+\frac{\pi^2}{24m^2}+O(m^{-4})\quad(m\to\infty).}
\]
The limiting value \(1/8\) is the known mean unrestricted halfspace depth of a uniform point in a disk; the positive finite-normal bias and its sharp coefficient are identified here.

## Assumptions and scope
The radial density is strictly positive on the open disk; no differentiability at the boundary is needed. Thus the projected cap function \(H\) is continuous and strictly decreasing from \(H(0)=1/2\) to \(H(R)=0\). Rotation invariance means every orientation has the same cap probability. All formulas concern the **oriented outward facet-normal family** of \(P_m\), not an arbitrary collection of unoriented projection lines. For odd \(m\), doubling the directions to include opposites would define a different depth functional. The random query point has the same law \(\mu\) used for testing.

## Proof
**1. Reduction to finitely many facet caps.** The polygon has supporting halfplanes \(\langle u_i,x\rangle\le1\). If a translate \(tP_m+x\) misses \(y\), the point violates at least one facet inequality, say \(\langle u_i,y\rangle>t+\langle u_i,x\rangle\). Hence the translate is contained in \(\{z:\langle u_i,z\rangle<\langle u_i,y\rangle\}\); this bounds the missed-translate mass by the maximum of these facet halfspace masses.

For the reverse inequality, set \(p_i=u_i\), the midpoint of the \(i\)-th facet of \(P_m\), and note that, for \(j\ne i\),
\[
1-\langle u_j,p_i\rangle\ge s_m:=1-\cos(2\pi/m)>0.
\]
For any \(b\in[-R,R]\) satisfying \(b<\langle u_i,y\rangle\), consider \(Q=tP_m+bu_i-tp_i\). Its \(i\)-th facet lies at \(\langle u_i,z\rangle=b\), so \(Q\) excludes \(y\). If \(z\in B_R\) and \(\langle u_i,z\rangle\le b\), then for \(j\ne i\),
\[
\langle u_j,z-bu_i\rangle\le\|z-bu_i\|\le2R
\le t(1-\langle u_j,p_i\rangle).
\]
Therefore all such \(z\) belong to \(Q\). By varying \(b\) and taking suprema, including the trivial empty/full-projection cases, the upper bound is attained as a supremum. Since \(\mu\) charges no hyperplane, for all \(t\ge2R/s_m\) and all \(y\),
\[
\boxed{d_t(y)=\min_i\mu\{x:\langle u_i,x\rangle\ge\langle u_i,y\rangle\}
=H\bigl(\max_i\langle u_i,y\rangle\bigr).}
\]
This finite-scale facet-depth reduction is already known in general polyhedral form, and is included only as a proved premise for the new distribution law.

**2. Exact universal linear segment.** Because the \(u_i\) positively surround the origin, \(Q(Y):=\max_i\langle u_i,Y\rangle\ge0\). For \(z\in[0,1/2]\), let \(q\in[0,R]\) solve \(H(q)=z\). Then
\[
\{Z_t\le z\}=\bigcup_{i=0}^{m-1}C_i(q),\qquad
C_i(q)=\{y\in B_R:\langle u_i,y\rangle\ge q\}.
\]
Every cap has \(\mu\)-mass \(H(q)=z\). The minimum angular separation between two distinct normals is \(2a\). A point belonging to the corresponding pair of caps must satisfy
\[
q\le\left\langle y,\frac{u_i+u_j}{2}\right\rangle
\le R\cos a.
\]
(The corresponding inequality for more widely separated normals is stronger.) Hence the caps are pairwise disjoint up to null boundary intersections whenever \(q\ge R\cos a\), proving \(\Pr(Z_t\le z)=mz\) for \(0\le z\le z_*\). If \(q<R\cos a\), adjacent caps have an open lens inside \(B_R\). Strict positivity of the radial density makes their overlap have positive probability. Thus the union has strictly less mass than the sum of cap masses, establishing maximality and strict inequality for \(z_*<z\le1/2\). For \(z>1/2\) the CDF is already one.

**3. Complete circular-uniform law.** After rescaling to \(R=1\), the radial coordinate of \(Y\) has density \(2r\) on \([0,1]\). The angular distance \(\varepsilon\) to the closest of the \(m\) normals is uniform on \([0,a]\), independent of \(r\). Thus \(Q(Y)=r\cos\varepsilon\). For a given \(q\), integrate \(\Pr(r\ge q/\cos\varepsilon)=(1-q^2/\cos^2\varepsilon)_+\) over \(\varepsilon\):
\[
\Pr(Q(Y)\ge q)=\frac1a\int_0^{\min(a,\arccos q)}
\left(1-\frac{q^2}{\cos^2\varepsilon}\right)d\varepsilon.
\]
When \(q\ge\cos a\) this equals \((\arccos q-q\sqrt{1-q^2})/a\); otherwise it equals \(1-q^2\tan a/a\). Since \(Z_t=h(Q(Y))\) and \(h\) is strictly decreasing, these are exactly the displayed CDF branches. The derivatives coincide at the threshold: both equal \(\pi/a=m\). Below the threshold, the CDF has zero second derivative; on its upper branch,
\[
F''(z)=-\frac{\pi^2\tan a}{2a(1-q(z)^2)^2}<0,
\]
which has a nonzero right limit at \(z_*\), proving that the CDF is \(C^1\) but not \(C^2\) there.

**4. Mean and sharp rate.** Integrating first in \(r\) gives, for \(0\le\varepsilon\le a\),
\[
\int_0^1 2r\,h(r\cos\varepsilon)\,dr
=\frac\varepsilon\pi+
\frac{(\pi/2-\varepsilon)\sec^2\varepsilon-\tan\varepsilon-\sin(2\varepsilon)}{4\pi}.
\]
Averaging over \(\varepsilon\in[0,a]\) yields the stated exact mean because
\[
\int_0^a\big((\pi/2-\varepsilon)\sec^2\varepsilon-\tan\varepsilon\big)d\varepsilon
=(\pi/2-a)\tan a,
\qquad\int_0^a\sin(2\varepsilon)d\varepsilon=\sin^2 a.
\]
Expanding around \(a=0\) gives the sharp leading bias \(a^2/24=\pi^2/(24m^2)\). Its positivity also follows directly from \(h(r\cos\varepsilon)>h(r)\) for \(r>0,\varepsilon>0\). This completes the proof.

## Verification
The accompanying standard-library file `check_depth.py` evaluates the exact CDF against independent direct angular/radial integrals, the exact mean against a separate nested integral, and the disjoint-versus-overlapping cap test for three nonconstant radial densities, checking 116 deterministic cases in all. The calculations are consistency checks, **not** an exhaustive proof of the universal statements; Steps 1–4 supply the analytic proof. Run `python check_depth.py` from the extracted package directory.

## Relationship to prior work
Molchanov and Nagy (2026), Sections 2 and 5, define translate depth and its tangent-cone dilation limit. A published finite-scale stabilization theorem for polytopal translate depth establishes the general facet-normal reduction used in Step 1; neither is claimed as new. Cuesta-Albertos and Nieto-Reyes (2007/2008) introduce random Tukey depth from randomly selected directions. Nagy, Dyckerhoff, and Mozharovskyi (2019) derive approximation rates for randomly sampled directions, including uniform disks; those results do not give the present *fixed regular fan* depth-value CDF or its distribution-free exact interval. Silva and collaborators (2014) give the unrestricted uniform-ellipsoid average depth, whose planar specialization is \(1/8\). Here the additional content is the exact sharp universal lower-tail law, the complete uniform-disk finite-fan distribution, its smoothness transition, and the sharp mean bias.

## Limitations
The theorem requires a full-dimensional regular polygon with at least three sides and the same positive radial distribution for the test measure and the query point. The general sharp CDF interval uses strict radial positivity; without it the first-overlap threshold need not mark strict breakdown. No arbitrary anisotropic-measure result, all-direction Tukey-depth identity, or optimal finite-dilation cutoff is asserted. The new formulas have not been independently audited, and comprehensive historical priority beyond the inspected sources is not certified.

## References
1. I. Molchanov and S. Nagy (2026), *Depth based on translates of a convex body: geometry, floating bodies, and empirical theory*, arXiv:2610.26108, first public 2026-10-19. https://arxiv.org/abs/2610.26108 .
2. *Finite-scale stabilization of polyhedral translate depth* (published mathematical record, November 2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-finite-scale-stabilization-of-polyhedral-translate-depth--d872e1651aa3 .
3. J. A. Cuesta-Albertos and A. Nieto-Reyes (2007/2008), *The random Tukey depth*, arXiv:0707.0167 and Computational Statistics & Data Analysis 52, 4979–4988. https://arxiv.org/abs/0707.0167 .
4. S. Nagy, R. Dyckerhoff, and P. Mozharovskyi (2019), *Uniform convergence rates for the approximated halfspace and projection depth*, arXiv:1910.05956. https://arxiv.org/abs/1910.05956 .
5. P. C. Silva, J. O. L. Cerdeira, M. J. Martins, and T. Monteiro-Henriques (2014), *Data depth for the uniform distribution*, Environmental and Ecological Statistics 21, 27–39, DOI:10.1007/s10651-013-0242-7.
