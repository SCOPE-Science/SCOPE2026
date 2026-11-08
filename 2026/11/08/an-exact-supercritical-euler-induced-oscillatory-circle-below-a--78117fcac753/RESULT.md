# An exact supercritical Euler-induced oscillatory circle below a descending prey nullcline

## Finding

Consider the positive-population quadratic Gause predator–prey flow
\[
\dot x=x(1-x-y),\qquad \dot y=y\left(x-\frac14-\frac12y\right)
\]
and its forward Euler map, for the step size \(h>0\),
\[
F_h(x,y)=\left(x+h x(1-x-y),\quad y+h y\left(x-\frac14-\frac12 y\right)\right).
\]
The unique positive coexistence state \(P=(1/2,1/2)\) is a stable focus of the continuous flow, on the *strictly decreasing* prey nullcline \(y=1-x\), but the Euler map undergoes a **supercritical Neimark–Sacker bifurcation exactly at \(h=2\)**. More precisely, there is \(\delta>0\) such that for each \(2<h<2+\delta\), the map has a locally attracting, simple closed, smooth invariant curve near \(P\), entirely within the positive quadrant, while \(P\) is a repelling focus. For \(0<2-h<\delta\), \(P\) is a locally attracting focus. In the eigenvector normalization specified below, the first Lyapunov coefficient at the crossing is exactly
\[
d=-\frac{17}{4},\qquad \left.\frac{d}{dh}|\lambda(h)|\right|_{h=2}=\frac38.
\]
For \(\varepsilon=h-2\downarrow0\), the radius of the attracting circle in the complex near-identity normal-form coordinate is \(\sqrt{3\varepsilon/34}+o(\sqrt\varepsilon)\), uniformly in angle. The oscillatory circle is a discretization-induced phenomenon, not a Hopf cycle of the underlying flow.

## Assumptions and scope

Both species have strictly positive local population densities, the predator self-limitation coefficient is exactly \(1/2\), and the predator mortality coefficient is \(1/4\). The map is treated locally near \(P\); it need not preserve the whole positive quadrant for coarse steps. No claim is made about long-term dynamics far from \(P\) or about rational versus irrational rotation on the small invariant circle. The primary mathematical subject is planar bifurcation theory of maps.

## Proof

**1. Continuous equilibrium and spectrum.** The positive coexistence conditions yield \(y=1-x\) and \(x-1/4-y/2=0\), so the unique positive equilibrium is \(P=(1/2,1/2)\). Its continuous-time Jacobian is
\[
J=\begin{pmatrix}-1/2&-1/2\\ 1/2&-1/4\end{pmatrix},\quad
\operatorname{tr}J=-\frac34,\quad\det J=\frac38,\quad (\operatorname{tr}J)^2-4\det J=-\frac{15}{16}<0.
\]
Thus the flow has a locally attracting spiral equilibrium. The prey nullcline derivative is exactly \(-1\), so the system has no continuous Hopf bifurcation at this equilibrium as \(h\) varies: \(h\) is a parameter of the discretization, not of the flow.

**2. Exact unit-circle crossing.** The Jacobian of the Euler map at \(P\) is \(A_h=I+hJ\), with
\[
\operatorname{tr}A_h=2-\frac{3h}{4},\qquad
\det A_h=1-\frac{3h}{4}+\frac{3h^2}{8}.
\]
At \(h=2\),
\[
A=A_2=\begin{pmatrix}0&-1\\1&1/2\end{pmatrix},\qquad
\lambda=\frac{1+i\sqrt{15}}4,\quad \bar\lambda=\frac{1-i\sqrt{15}}4.
\]
Both multipliers have modulus one and are not roots of unity of orders one through four: \(\cos\arg\lambda=1/4\) is different from all corresponding low-order possibilities. The determinant is less than one for \(0<h<2\), and exceeds one for \(h>2\), so the complex pair crosses outwards, with derivative \(\left.\partial_h|\lambda(h)|\right|_{2}=3/8>0\). The discriminant of the characteristic polynomial is negative near \(h=2\), and \(\det A_2=1\ne0\), so the family consists locally of smooth diffeomorphisms.

**3. Explicit cubic normal-form coefficient.** In local coordinates \(u=x-1/2\), \(v=y-1/2\), at \(h=2\) the map is exactly
\[
\binom{u'}{v'}=A\binom uv+\binom{-2u^2-2uv}{2uv-v^2}
=A w+\frac12 B(w,w),\qquad w=(u,v)^T,
\]
with symmetric bilinear form
\[
B(s,t)=\binom{-4s_1t_1-2(s_1t_2+s_2t_1)}{2(s_1t_2+s_2t_1)-2s_2t_2}.
\]
There is no cubic derivative tensor. Choose the right eigenvector \(q=(1,-\lambda)^T\), its complex conjugate \(\bar q\), and the complex *row* functional
\[
\ell=\left(\frac12+\frac{i\sqrt{15}}{30},\quad \frac{2i\sqrt{15}}{15}\right),
\qquad \ell q=1,\quad \ell\bar q=0.
\]
This fixes the normal-form normalization. Define the second-order resolvents
\[
H_{11}=(I-A)^{-1}B(q,\bar q),\qquad
H_{20}=(\lambda^2 I-A)^{-1}B(q,q).
\]
They exist by the nonresonance conditions, and exact evaluation gives \(H_{11}=(1,-4)^T\). The standard Neimark–Sacker cubic coefficient in the convention \(w=zq+\bar z\bar q+O(|z|^2)\) is
\[
c=\ell\left(B(q,H_{11})+\frac12 B(\bar q,H_{20})\right)
=\frac{23}{6}-\frac{25i\sqrt{15}}{18}.
\]
Consequently the *real radial cubic coefficient* is
\[
d=\operatorname{Re}(\bar\lambda c)
=\frac{23}{24}-\frac{125}{24}=-\frac{17}{4}<0.
\]
The identities defining both resolvents and the final exact simplification can be reproduced using the attached standalone SymPy checker; they are symbolic identities rather than numerical approximations.

**4. Bifurcation and amplitude.** Since the eigenvalues cross transversely, no low-order strong resonance occurs, and \(d<0\), the nondegenerate supercritical Neimark–Sacker theorem gives an attracting invariant Jordan curve for all sufficiently small \(h-2>0\), with its local smoothness and attraction. The normal form reads
\[
z'=\lambda(h)z+c z|z|^2+O(|z|^4+|h-2||z|^2),
\]
where the remainder may be made of sufficiently high order for the bifurcation. The radial growth coefficient is \((3/8)(h-2)\), so its leading stable nonzero radius satisfies \(r^2=(3/34)(h-2)+o(h-2)\). Positivity of the curve follows from its shrinking to the strictly interior point \(P\) as \(h\downarrow2\). For \(h<2\) sufficiently close, the two multipliers lie strictly inside the unit disk and \(P\) is a local attractor; for \(h>2\) they lie outside, so \(P\) is a local repeller.

## Verification

Run `python verify_ns_euler.py` with SymPy and optionally NumPy. It independently reconstructs the translated quadratic map, Jacobian and characteristic polynomial, the normalized eigenpair, low-order nonresonance, both resolvent identities, the cubic coefficient \(-17/4\), and the amplitude factor \(3/34\). Its optional finite-orbit checks for three values just above the bifurcation agree with the predicted leading horizontal amplitude to within four percent. Finite iterations support but cannot prove the existence theorem; the analytic crossing, coefficient calculation, and standard local bifurcation theorem establish it.

## Relationship to prior work

Chan-López, Martín-Ruiz and Castellanos (2026) prove the general forward-Euler spectral identity and explain why coarse discretization can put a Neimark–Sacker *spectral crossing* on a descending prey-nullcline branch. In their section on discrete-time localization they do not calculate a first Lyapunov coefficient for this polynomial predator-self-limited example or prove the existence of its attracting invariant circle. Thus the spectral mechanism is prior knowledge; the claimed contribution here is specifically the nondegenerate **supercritical nonlinear realization with an exact coefficient** and leading invariant-circle scale. The classical Neimark–Sacker theorem and its standard cubic coefficient formula are used, not claimed as new. Khan (2016, 2019) develops Neimark–Sacker analysis for a different quadratic predator–prey map without the predator self-limitation term; those formulas do not directly establish the present coefficient or continuous-flow/discretization contrast. Database and literature coverage do not establish absolute historical priority.

## Limitations

The conclusion is local around the specified coexistence state, for a fixed simple quadratic model and sufficiently small positive \(h-2\). It does not imply that the Euler map globally preserves nonnegative populations or that a particular orbit on its attracting invariant circle is quasiperiodic. The exact cubic coefficient is normalization-dependent, with the eigenvector convention specified above, whereas its negative sign and the supercritical nature are intrinsic. Priority is provisional, and there has been no independent validation.

## References

- E. Chan-López, A. Martín-Ruiz and V. Castellanos (2026), *Spectral Rigidity and Geometric Localization of Hopf Bifurcations in Planar Predator-Prey Systems*, arXiv:2603.24418v1 (first public version 2026-03-25), especially sections 2 and 6. https://arxiv.org/abs/2603.24418
- A. Q. Khan (2016), *Neimark-Sacker bifurcation of a two-dimensional discrete-time predator-prey model*, SpringerPlus 5, 126, DOI:10.1186/s40064-015-1618-y. https://link.springer.com/article/10.1186/s40064-015-1618-y
- A. Q. Khan (2019), *Bifurcations of a two-dimensional discrete-time predator–prey model*, Advances in Difference Equations 2019, 56, DOI:10.1186/s13662-019-1995-6. https://link.springer.com/article/10.1186/s13662-019-1995-6
- *Neimark–Sacker bifurcation*, Scholarpedia, standard theorem and multilinear formula for the first Lyapunov coefficient. https://www.scholarpedia.org/article/Neimark-Sacker_bifurcation
