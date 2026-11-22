# Bistable coexistence and an exact antidiagonal basin separator in a coupled Gaussian map

## Finding
Consider the smooth map of Soula, Jahanshahi, Al-Barakati and Moroz [1],
\[
F_{a,b}(x,y)=\bigl(f_a(x)+b(y-x),\ f_a(y)+b(x-y)\bigr),\qquad
f_a(t)=a t(1-t^2)e^{-t^2}.
\]
Fix any real \(0<a<1\) and put
\[
b_c(a)=\frac{1-ae^{-2}}2.
\]
For every \(b_c(a)<b<1/2\), two distinct hyperbolic attracting invariant objects coexist: the fixed point \((0,0)\) and one primitive period-two orbit, while a second primitive period-two orbit is a saddle. More precisely, define \(\tau=(1-2b)/a\), so \(0<\tau<e^{-2}\), and
\[
s_-=1-W_0(-e\tau),\quad s_+=1-W_{-1}(-e\tau),\quad
r_-=\sqrt{s_-},\quad r_+=\sqrt{s_+},
\]
where \(W_0\) and \(W_{-1}\) are the two real Lambert-W branches. Then \(1<r_-<\sqrt2<r_+\). The **only nonzero antipodal primitive period-two orbits supported on the invariant antidiagonal** are
\[
\mathcal C_- =\{(r_-,-r_-),(-r_-,r_-)\},\qquad
\mathcal C_+ =\{(r_+,-r_+),(-r_+,r_+)\}.
\]
The inner orbit \(\mathcal C_-\) is a hyperbolic saddle, and the outer orbit \(\mathcal C_+\) is a hyperbolic sink. The origin is a hyperbolic sink. Each of the two sinks has a nonempty open basin in the ambient plane.

There is an **exact global basin partition on the entire antidiagonal**, with no restriction on the magnitude of the initial coordinate. For any real \(x\), the trajectory starting at \((x,-x)\) tends to \((0,0)\) if \(|x|<r_-\); belongs to \(\mathcal C_-\) if \(|x|=r_-\); and approaches \(\mathcal C_+\) with alternating sign if \(|x|>r_-\). The word "global" here refers only to the invariant antidiagonal, not to all planar initial conditions.

At the creation threshold, with \(\delta=b-b_c(a)\downarrow0\), the two squared amplitudes obey the sharp fold law
\[
r_\pm^2=2\pm\frac{2e}{\sqrt a}\sqrt\delta+O_a(\delta).
\]
As \(b\uparrow1/2\), the attracting cycle moves to infinity while the separating saddle approaches finite radius:
\[
r_+^2=L+\log L+O\!\left(\frac{\log L}{L}\right),
\qquad r_-\longrightarrow1,
\qquad L=\log\frac{a}{1-2b}\longrightarrow\infty.
\]
Thus a bounded-parameter, globally dissipative regime can exhibit simultaneous attraction to an equilibrium and to an increasingly remote two-cycle separated by an exact one-dimensional saddle orbit.

## Assumptions and scope
All coordinates and parameters are real, with \(0<a<1\) and \((1-ae^{-2})/2<b<1/2\). Time is discrete and nonnegative. The map is evaluated in exact real arithmetic. The antidiagonal is \(\mathcal A=\{(x,-x):x\in\mathbb R\}\). An **antipodal two-cycle** is a primitive period-two orbit consisting of \(p\ne0\) and \(-p\); because the map is odd, every displayed orbit has this form. The theorem enumerates antipodal primitive two-cycles **on \(\mathcal A\)**, not all periodic orbits elsewhere in the plane. Hyperbolicity and stability refer to the derivative of the second iterate in the full plane.

## Proof
**1. Reduction and exact two-cycle equation.** Oddness of \(f_a\) makes \(\mathcal A\) invariant. In its coordinate \(x\), the map is
\[
T_b(x)=f_a(x)-2bx.
\]
Since \(T_b\) is odd, a nonzero antipodal two-cycle is exactly a solution to \(T_b(r)=-r\) with \(r>0\), and its negative. Writing \(s=r^2\) gives
\[
a(1-s)e^{-s}=2b-1,
\qquad (s-1)e^{-s}=\tau=\frac{1-2b}{a}.
\]
The function \(h(s)=(s-1)e^{-s}\) is strictly increasing from zero to \(e^{-2}\) on \((1,2)\), then strictly decreasing to zero on \((2,\infty)\). Hence precisely two positive squared amplitudes exist under the stated strict inequalities; there are no others. Inverting \((s-1)e^{-s}=\tau\) gives the displayed two Lambert-W branches. The two points of each orbit are distinct, because \(r>0\), and primitive, because \(T_b(r)=-r\ne r\).

**2. Global dynamics on the antidiagonal.** Put \(u=|x|\). For \(0<u\le1\),
\[
|T_b(u)|=u\left|a(1-u^2)e^{-u^2}-2b\right|<u,
\]
since \(0\le a(1-u^2)e^{-u^2}<1\) and \(0<2b<1\). For \(u\ge1\), the next radius is exactly
\[
G(u)=u\left[2b+a(u^2-1)e^{-u^2}\right]>0.
\]
Writing \(s=u^2\) and \(q(s)=2s^2-5s+1\), differentiation gives
\[
G'(u)=2b-ae^{-s}q(s).
\]
For every \(s\ge1\), \(q(s)\le2(s-1)^2\) and \(2(s-1)^2e^{-s}\le8e^{-3}\). Consequently,
\[
G'(u)\ge2b-8ae^{-3}>
1-a(e^{-2}+8e^{-3})>0,
\]
because \(0<a<1\) and \(e^{-2}+8e^{-3}<1\). Thus \(G\) is strictly increasing on \([1,\infty)\).

The sign of \(G(u)-u\) equals the sign of \(h(u^2)-\tau\). It is negative for \(1\le u<r_-\), positive for \(r_-<u<r_+\), and negative for \(u>r_+\). Monotonicity of \(G\) ensures that a radius in \((r_-,r_+)\) moves monotonically upward without overshooting \(r_+\), and a radius above \(r_+\) decreases without crossing below it; both converge to \(r_+\). Every radius below \(r_-\) decreases; it cannot converge to a positive fixed radius because \(G(u)<u\) for \(1\le u<r_-\) and \(|T_b(u)|<u\) for \(0<u\le1\). The only possible limit is zero. At \(r_-\) the radius remains fixed, and the antidiagonal sign flips each step at either nonzero cycle, proving the complete partition.

**3. Full-plane Floquet classification.** At either cycle point the Jacobian is the same matrix, because \(f_a'\) is even:
\[
DF_{a,b}(r,-r)=\begin{pmatrix}f_a'(r)-b&b\\b&f_a'(r)-b\end{pmatrix},
\qquad f_a'(r)=ae^{-s}q(s).
\]
The symmetric and antisymmetric one-step eigenvalues are respectively
\[
\lambda_{\rm s}=ae^{-s}q(s),\qquad
\lambda_{\rm a}=ae^{-s}q(s)-2b
=-1+2as(s-2)e^{-s}.
\]
The two eigenvalues of the return derivative \(D(F_{a,b}^2)\) are their squares. On \(1\le s\le2\), \(-17/8\le q(s)\le-1\), so
\[
|\lambda_{\rm s}|\le\frac{17a}{8e}<1.
\]
For \(s\ge2\), \(-1\le q(s)\le2(s-1)^2\), so
\[
|\lambda_{\rm s}|\le a\max(e^{-2},8e^{-3})<1.
\]
If \(1<s<2\), then \(\lambda_{\rm a}<-1\), giving a transverse-contracting/antidiagonal-expanding saddle at \(\mathcal C_-\). If \(s>2\), then
\[
0<2as(s-2)e^{-s}\le8ae^{-3}<1,
\]
so \(-1<\lambda_{\rm a}<0\), giving an attracting full-plane two-cycle at \(\mathcal C_+\). At the origin the eigenvalues are \(a\) and \(a-2b\), both strictly between \(-1\) and \(1\). Standard local contraction for a hyperbolic sink gives nonempty open planar attraction basins; they are disjoint because the two invariant limits are distinct.

**4. The two endpoint asymptotics.** Differentiation of \(h(s)=(s-1)e^{-s}\) gives \(h'(2)=0\) and \(h''(2)=-e^{-2}\). With \(\tau=e^{-2}-2\delta/a\), the Taylor formula
\[
e^{-2}-h(s)=\frac{e^{-2}}2(s-2)^2+O(|s-2|^3)
\]
yields \(s_\pm=2\pm2e\sqrt{\delta/a}+O_a(\delta)\). At \(b=b_c(a)\), these branches coalesce in a neutral antipodal cycle at \(r=\sqrt2\) whose antisymmetric one-step multiplier is \(-1\). At the other endpoint, \(s_+\to\infty\) and its equation becomes
\[
s_+-\log(s_+-1)=L,
\qquad L=\log\frac{a}{1-2b}.
\]
Substitution, using \(s_+/L\to1\), gives \(s_+=L+\log L+O((\log L)/L)\). The smaller root converges to \(s_-=1\). This finishes the proof.

## Verification
A standalone Python-standard-library checker, `verify.py`, implements the exact recurrence and independently numerically solves the two scalar root branches. It tests 20 parameter pairs, both primitive two-cycles and full-plane multipliers, 80 representative antidiagonal attraction cases, the origin's Jacobian and four near-fold asymptotic ratios. The checker returns `PASS: 140 cycle, stability, and basin checks` plus fold ratios approaching one. The finite numerical checks are not proofs of the universal quantifiers: all such assertions follow from Steps 1–4 above. The closed interval boundaries are excluded from the main hyperbolicity claim.

## Relationship to prior work
The exact coupled map originates in Soula et al. [1], whose full article examines critical curves, numerical attractor coexistence and synchronization, concentrating largely on stronger gain. Its numerical phenomena do not give the explicit low-gain global antidiagonal basin partition established here. A previously published all-real boundedness theorem for this same map [2] proves common compact absorption exactly for \(-1/2\le b<1/2\), together with a critical-endpoint escape law. That theorem expressly does **not** classify finite attractors or their basins within this absorbing region; the present bistable sink/saddle result is inside its absorbing region and logically compatible with it.

The scalar equation for the antipodal two-cycle is algebraically the same as the antiphase fixed-point equation after shifting coupling by one unit. Therefore **the Lambert-W root count and the square-root fold alone are not asserted as independent novelties**. The additional result here is the complete global antidiagonal basin separator, the exact full-plane stability division between the two cycles, and the robust coexistence of the origin sink with an outer periodic sink at positive coupling. The classical output-coupled map of Ding and Yang [3] and the related coupled-sine maps [4] have different recurrence laws and do not directly imply this theorem.

## Limitations
The antidiagonal is a one-dimensional invariant set, and no assertion is made that its separator equals the full planar basin boundary. Other off-antidiagonal periodic orbits may exist; their census is not claimed. The theorem is restricted to \(0<a<1\), the strict open coupling band and exact real arithmetic. It does not assert that the outer cycle remains finite at the excluded endpoint \(b=1/2\), where a different escape law is known [2]. Classical one-dimensional monotone dynamics and local Floquet stability provide parts of the method, so novelty resides in this map's exact coexistence and global restricted-basin classification. Unindexed equivalent work could alter publication priority. The finite checker is supplemental and not an independent mathematical audit.

## References
[1] Y. Soula, H. Jahanshahi, A. A. Al-Barakati and I. Moroz, *Dynamics and Global Bifurcations in Two Symmetrically Coupled Non-Invertible Maps*, Mathematics **11** (2023), article 1517, first published 21 March 2023. https://doi.org/10.3390/math11061517

[2] *A sharp global boundedness interval and logarithmic critical escape in a coupled Gaussian map* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-global-boundedness-interval-and-logarithmic-critical-esc--f463338d3c52

[3] M. Ding and W. Yang, *Observation of intermingled basins in coupled oscillators exhibiting synchronized chaos*, Physical Review E **54** (1996), 2489–2494. https://doi.org/10.1103/PhysRevE.54.2489

[4] Y. Soula, A. K. Taha, D. Fournier-Prunaret and N.-E. Hamri, *Bifurcations and Dynamical Behavior of 2D Coupled Chaotic Sine Maps*, Applied and Computational Mathematics **11** (2022), 18–30. https://doi.org/10.11648/j.acm.20221101.12
