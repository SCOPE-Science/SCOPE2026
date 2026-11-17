# Exact equatorial bifurcation and universal marked area law for pole-anchored spherical triangles

## Finding

Fix the north pole \(N\) of the unit sphere. For \(0<\theta<\pi\), choose two points independently and uniformly by arclength on the latitude circle at colatitude \(\theta\). Join each pair of the three points by its shorter great-circle arc; almost surely the arcs bound a unique proper geodesic triangle. Write \(A_\theta\in(0,2\pi)\) for its intrinsic spherical area, and set
\[
q=\tan^2(\theta/2)>0,\qquad \Delta\in[0,\pi]
\]
where \(\Delta\) is the smaller azimuthal separation of the two sampled points. Then \(\Delta\) is uniform on \([0,\pi]\), and the **exact area law**, including the branch for the southern hemisphere, is
\[
A_\theta=2\operatorname{Arg}(1+qe^{i\Delta}),\qquad \operatorname{Arg}\in[0,\pi].
\]
The cumulative distribution \(F_q(x)=\Pr(A_\theta\le x)\) is as follows, in each case extended by zero below the indicated support and one above it:
\[
\boxed{\begin{aligned}
0<q<1:\quad &F_q(x)=\frac2\pi\arcsin\left(\frac{\sin(x/2)}q\right),&&0\le x\le2\arcsin q;\\
q=1:\quad &F_1(x)=\frac{x}{\pi},&&0\le x\le\pi;\\
q>1:\quad &F_q(x)=\frac1\pi\left(\frac x2+\arcsin\frac{\sin(x/2)}q\right),&&0\le x\le2\pi.
\end{aligned}}
\]
Thus the support changes abruptly from \([0,\pi]\) at the equator to \([0,2\pi]\) immediately south of it. Precisely,
\[
\boxed{\Pr(A_\theta>\pi)=\frac1\pi\arccos(1/q)\quad(q>1),}
\]
whereas the probability is zero for \(q\le1\). This is a square-root onset:
\[
\Pr(A_\theta>\pi)\sim\frac{\sqrt{2(q-1)}}\pi\quad(q\downarrow1,\ q>1).
\]
There is a nontrivial **conditional boundary-layer law**. Let \(t_q=\arccos(1/q)\) for \(q>1\). Conditioned on \(A_\theta>\pi\), the variable \(U_q=(\pi-\Delta)/t_q\) is exactly uniform on \((0,1)\). Moreover,
\[
\boxed{\left.\frac{A_\theta-\pi}{t_q}\ \right|\ (A_\theta>\pi)
\ \Longrightarrow\ W=U^{-1}-U,\qquad U\sim\operatorname{Uniform}(0,1).}
\]
In particular,
\[
\Pr(W>w)=\frac{\sqrt{w^2+4}-w}{2},\qquad w\ge0.
\]
The limiting law has an infinite mean; the convergence just asserted is weak, not convergence of expectations.

**Universality under biased sampling.** The same conditional limit holds if the folded azimuthal gap has any probability density \(h\) continuous at \(\pi\) with \(h(\pi)>0\). Then, as \(q\downarrow1\) from above,
\[
\Pr(A_\theta>\pi)\sim h(\pi)t_q\sim h(\pi)\sqrt{2(q-1)},
\]
and the conditional pair \((U_q,(A_\theta-\pi)/t_q)\) converges weakly to \((U,U^{-1}-U)\). This includes any two independent points drawn from a fixed strictly positive continuous azimuthal density on the latitude circle.

The area laws also obey the exact north--south duality \(A_q(\Delta)+A_{1/q}(\Delta)=2\Delta\), and the distribution strictly increases in the stochastic order with \(q\). Hence the full area law uniquely recovers the colatitude \(\theta\), including the hemisphere, without a reflection ambiguity.

## Assumptions and scope

The sphere has radius one; the triangle area is intrinsic solid angle in steradians, not planar chord-triangle area. The north pole is one fixed vertex. The two remaining vertices have the **same** prescribed colatitude \(\theta\), independently sampled by uniform azimuth (equivalently uniform arclength). Each side is its shorter great-circle arc, length strictly below \(\pi\) almost surely. Points at the poles and antipodal degeneracies have probability zero in the stated parameter range. Limits \(q\downarrow1\) are taken through real \(q>1\), i.e. southward of the equator. The general biased-gap statement requires a density continuous and strictly positive at its endpoint \(\pi\), but not independence of the two longitudes.

## Proof

**1. Spherical area and branch.** Put \(c=\cos\theta\), \(s=\sin\theta\), and, after a rotation, take
\[
N=(0,0,1),\quad X=(s,0,c),\quad Y=(s\cos\Delta,s\sin\Delta,c),\quad 0<\Delta<\pi.
\]
The solid-angle identity, or equivalently Girard's formula together with the spherical cosine rule, gives
\[
\frac{A_\theta}{2}=\operatorname{atan2}\bigl(N\cdot(X\times Y),\ 1+N\cdot X+X\cdot Y+Y\cdot N\bigr).
\]
Here the two arguments are respectively \(s^2\sin\Delta\) and \((1+c)^2+s^2\cos\Delta\). Since \(1+c>0\) and \(s^2/(1+c)^2=q\), this becomes \(A_\theta=2\operatorname{Arg}(1+qe^{i\Delta})\). The upper-half-plane argument is the correct continuous branch even when the real part is negative; ordinary principal-value arctangent without its quadrant would give an incorrect southern law. Independently, the side opposite \(N\) has cosine \(c^2+s^2\cos\Delta\), the two base angles have cosine \(\cot\theta\tan(\text{opposite side}/2)\), and Girard gives the same area.

**2. Inverse maps.** Let \(\psi=A_\theta/2\). The identity
\[
q\sin(\Delta-\psi)=\sin\psi
\]
follows by taking the imaginary part of \(e^{-i\psi}(1+qe^{i\Delta})\). For \(q>1\), \(\Delta\mapsto A_\theta\) is strictly increasing, since
\[
\frac{d\psi}{d\Delta}=\frac{q(q+\cos\Delta)}{1+2q\cos\Delta+q^2}>0.
\]
The unique inverse is \(\Delta=\psi+\arcsin(\sin\psi/q)\), for \(0<\psi<\pi\). Uniformity of \(\Delta\) proves the third CDF line. At \(q=1\), \(1+e^{i\Delta}=2\cos(\Delta/2)e^{i\Delta/2}\), giving \(A_\theta=\Delta\). For \(0<q<1\), the derivative changes sign at \(\Delta_*=\arccos(-q)\), and the maximal argument is \(\arcsin q\), from tangency to the circle centered at one of radius \(q\). For \(0<\psi<\arcsin q\), the two inverse branches are
\[
\Delta_-=\psi+\arcsin(\sin\psi/q),\qquad
\Delta_+=\psi+\pi-\arcsin(\sin\psi/q).
\]
Consequently \(\Pr(A_\theta\le2\psi)=[\Delta_-+(\pi-\Delta_+)]/\pi\), proving the first CDF line. The support endpoints follow as stated.

**3. Threshold and marked universality.** When \(q>1\), \(A_\theta>\pi\) exactly when the real part of \(1+qe^{i\Delta}\) is negative, or \(\Delta>\pi-t_q\), where \(t_q=\arccos(1/q)\). Uniformity of \(\Delta\) gives the exact probability and conditional uniformity. The Taylor expansion \(\cos t_q=1/q\) shows \(t_q\sim\sqrt{2(q-1)}\). On \(\Delta=\pi-t_q u\), \(0<u<1\), quadrant-safe angular subtraction gives
\[
\frac{A_\theta-\pi}{t_q}
=\frac2{t_q}\arctan\left(\frac{q\cos(t_qu)-1}{q\sin(t_qu)}\right)
\longrightarrow\frac{1-u^2}{u}.
\]
The limit holds for every fixed \(u\in(0,1)\). Since the conditional variable \(u\) is uniform exactly, the continuous-mapping theorem proves joint weak convergence. Solving \(u^{-1}-u>w\) for \(u\in(0,1)\) yields the displayed survival function; its \(1/w\) tail proves infinite mean.

For general folded-gap density \(h\), the event is still exactly \(\pi-t_q<\Delta<\pi\); therefore its mass is \(\int_{\pi-t_q}^\pi h(\delta)d\delta\sim h(\pi)t_q\). The conditional density of \(U_q\) on \((0,1)\) is \(t_qh(\pi-t_qu)/\int_{\pi-t_q}^\pi h\), which converges uniformly to one by continuity at \(\pi\). The same geometric map gives the joint weak limit. For independent longitude samples with continuous strictly positive periodic density \(f\), the folded-gap density is
\[
h(d)=2\int_0^{2\pi}f(v)f(v+d)\,dv,\quad 0<d<\pi,
\]
with arguments taken modulo \(2\pi\), so \(h(\pi)>0\) and the assumptions hold.

**4. Duality and identifiability.** Factoring
\[
1+qe^{i\Delta}=qe^{i\Delta}(1+q^{-1}e^{-i\Delta})
\]
shows \(A_q(\Delta)+A_{1/q}(\Delta)=2\Delta\), with the arguments on the stated branches. At every \(\Delta\in(0,\pi)\),
\[
\frac{\partial A_q(\Delta)}{\partial q}
=\frac{2\sin\Delta}{1+2q\cos\Delta+q^2}>0.
\]
Thus quantile coupling with the same uniform \(\Delta\) gives strict stochastic ordering. If \(q\le1\), the area support endpoint \(2\arcsin q\) (or \(\pi\) at \(q=1\)) identifies \(q\); if \(q>1\), the strictly increasing value \(\Pr(A_\theta>\pi)=\arccos(1/q)/\pi\) does so. Since \(q=\tan^2(\theta/2)\), the colatitude is identified.

## Verification

The standalone `checks/pole_area_checker.py` implements the phase formula and independently computes spherical excess using the spherical law of cosines and Girard's theorem. It checks agreement at seven colatitudes on a dense grid; compares the analytic CDF against deterministic angular quadrature for both hemispheres and the equator; verifies north--south duality, the superhemispheric probability, convergence of the conditional marks, and a nonuniform angular-density example. It uses only the Python standard library. Invoke `python checks/pole_area_checker.py` from the package root. The code is numerical corroboration, not a substitute for the preceding exact analytic proof.

## Relationship to prior work

The van Oosterom--Strackee solid-angle identity and Girard's spherical-excess theorem supply the underlying deterministic triangle-area formula, but neither supplies a random latitude-gap pushforward or a conditional equatorial marked limit. Finch and Jones, *Random Spherical Triangles* (first public version 2010-09-27), analyze three independent **whole-sphere** uniform vertices and the classical unconditioned spherical area density, not a fixed pole plus two boundary points of one small circle. H. Le, *Random spherical triangles II: Shape densities* (1989), studies three points sampled **inside a spherical cap**; the full paper was not available, leaving a priority caveat. A related published calculation on the mean area for **three** random points all on one latitude circle also has a different object, with no pinned pole and with degeneracy at the equator. The claims here are the full pinned-pole CDF, an explicit support bifurcation, a universal conditional critical law and strict latitude identification, not the classical deterministic area formula.

## Limitations

No claim is made for area-uniform sampling in a cap or for three latitude-circle vertices. The exact CDF requires angular-uniform sampling; the marked universality statement only requires a positive continuous folded-gap density at \(\pi\). The marked limit is weak, not a total-variation assertion or a convergence-of-means theorem. For a physical sphere of radius \(R\), divide the physical area by \(R^2\) before applying the formulas. The historical-priority comparison is limited by the inaccessible full text of Le (1989) and by possible older specialized results. Independent verification has not been performed.

## References

1. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, first posted 2010-09-27, https://arxiv.org/abs/1009.5329 (HTML full text: https://arxiv.org/html/1009.5329v3).
2. A. van Oosterom and J. Strackee, *The Solid Angle of a Plane Triangle*, *IEEE Transactions on Biomedical Engineering* **30** (1983), 125--126, DOI:10.1109/TBME.1983.325207.
3. H. Le, *Random spherical triangles II: Shape densities*, *Advances in Applied Probability* **21** (1989), 581--594, DOI:10.1017/S0001867800018826.
4. *Dilogarithmic mean area of random fixed-latitude spherical triangles*, publicly available 2026 work on three latitude-circle vertices, compared by exact hypotheses and implications.
5. Classical spherical law of cosines and Girard's spherical-excess identity, as collected in standard spherical trigonometry references.
