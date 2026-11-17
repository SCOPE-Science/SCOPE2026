# Gauss-hypergeometric flow coordinates and global isochrons of an algebraic polynomial oscillator

## Finding
For the specific polynomial oscillator of Belattar, Cheurfa, Bendjeddou and Santana [1], with \(h>0\) and \(0<w<4\), every trajectory other than the repelling equilibrium has **an exact Gauss-hypergeometric representation in original physical time** and an explicit global asymptotic phase. The phase is defined on the entire punctured plane, not only on the known attracting algebraic limit cycle. Its level sets are the oscillator's isochrons, and it evolves by exact rigid rotation at angular velocity \(-\Omega\), where \(\Omega=\sqrt{1-w^2/16}\).

Here is a complete evaluation formula. Set
\[
z=y+\frac{w}{2h}(x^2-h)x,\qquad q=\frac{x^2+z^2}{h},\qquad \Omega=\sqrt{1-\frac{w^2}{16}}.
\]
For \(q>0\), \(q\ne1\), define
\[
\begin{aligned}
\alpha&=\frac{i}{w},&\beta&=\frac14+\frac{i\Omega}{w},\\
a&=\alpha+\beta,& b&=\alpha+\beta+\frac12,& \gamma&=\frac12+2\beta,\\
F(q)&=q^\alpha|1-q|^\beta\,{}_2F_1(a,b;\gamma;1-q),
&G(q)&=wq(1-q)F'(q).
\end{aligned}
\]
Powers of positive real bases use the real logarithm; the hypergeometric function is continued along the real interval \(1-q<1\), without crossing its standard cut. For \((x,z)\ne(0,0)\), \(q\ne1\), put
\[
A=\frac{x\overline{G(q)}-z\overline{F(q)}}{F(q)\overline{G(q)}-G(q)\overline{F(q)}}.
\]
The denominator never vanishes on either component \(0<q<1\) or \(q>1\). Moreover \(A\ne0\). Define the circle-valued phase
\[
\boxed{\quad \Phi(x,y)=\arg\!\left(A\left(\frac{|1-q|}{q}\right)^{i\Omega/w}\right)\pmod{2\pi}.\quad}
\]
For \(q=1\), use the continuous value
\[
\boxed{\quad \Phi(x,y)=\arg\!\left(x+\frac{i}{\Omega}\left(z+\frac w4x\right)\right)\pmod{2\pi}.\quad}
\]
This makes \(\Phi\) continuous on \(\mathbb R^2\setminus\{(0,0)\}\), with
\[
\boxed{\quad\Phi(\varphi_t(x,y))=\Phi(x,y)-\Omega t\pmod{2\pi},\quad t\ge0,\quad}
\]
where \(\varphi_t\) is the original polynomial flow. If two starting points have equal phase, then their trajectories converge to the **same time-parameterized point of the cycle**, in the sense that their phase-aligned cyclic positions differ by \(o(1)\); if their phases differ, their limiting cyclic positions retain that phase difference. Thus the level sets are global isochrons. Unlike the already known limit cycle or its period [1,2], this constructs the phase of every non-equilibrium initial condition.

## Assumptions and scope
The precise source vector field [1, Eq. (1.2)] is \(\dot x=y\), \(\dot y=f_3(x)y^3+f_2(x)y^2+f_1(x)y+f_0(x)\), with
\[
\begin{aligned}
f_3(x)&=-\frac{w}{2h},\\
f_2(x)&=-\frac{3w^2(x^3-hx)}{4h^2},\\
f_1(x)&=-\frac38\left(\frac wh\right)^3x^6+\frac{3w^3}{4h^2}x^4-\frac{w(3w^2+20)}{8h}x^2+w,\\
f_0(x)&=-\frac{x}{16h^4}(w^2x^4-hw^2x^2+4h^2)(w^2x^4-2hw^2x^2+h^2w^2+4h^2).
\end{aligned}
\]
Assume \(h>0\) and \(0<w<4\) throughout. The origin is excluded because it is an equilibrium and has no asymptotic phase. The established attracting algebraic cycle is \(q=1\), i.e. \(x^2+(y+w(x^2-h)x/(2h))^2=h\). The claim includes both \(0<q<1\) and \(q>1\), and does not use a uniform-in-initial-data or uniform-in-parameter error bound.

## Proof
**1. Exact polynomial reduction and positive global solutions.** Direct expansion of the displayed source coefficients in the shear \(z=y+w(x^2-h)x/(2h)\) yields
\[
\dot x=z+\frac w{2h}(h-x^2)x,\qquad
\dot z=-x+\frac w{2h}(h-2x^2-z^2)z.
\]
Consequently \(S=x^2+z^2\) satisfies
\[
\dot S=wS(1-S/h),\qquad \dot q=wq(1-q).
\]
For every \(q_0>0\), the exact solution is \(q(t)=(1+c e^{-wt})^{-1}\), \(c=(1-q_0)/q_0>-1\). In particular, for all \(t\ge0\), \(q(t)>0\) and tends to \(1\); \(x,z\), hence \(y\), remain bounded and the solution is forward complete. Since \(S\) never reaches zero, its angular direction is defined throughout.

**2. Projective linearization.** Where \(x\ne0\), write \(u=z/x\). The reduced equations give exactly
\[
\dot u=-1-\frac w2q(t)u-u^2.
\]
If \(\psi\) solves
\[
\boxed{\quad\ddot\psi+\frac w2q(t)\dot\psi+\psi=0,\quad}
\]
with \((\psi(0),\dot\psi(0))=(x_0,z_0)\), its projective ratio \(\dot\psi/\psi\) follows the same Riccati equation wherever defined. At zeros of \(\psi\), passage to the other projective chart gives a continuous global equality of directions. The vector \((\psi,\dot\psi)\) cannot vanish at any time, by uniqueness of the second-order linear initial-value problem; hence
\[
(x(t),z(t))=\sqrt{h q(t)}\,\frac{(\psi(t),\dot\psi(t))}{\sqrt{\psi(t)^2+\dot\psi(t)^2}}.
\]
This identity is exact, not asymptotic: it follows from the common projective equation and the independently determined radius. It also handles all angular zero crossings without singularities.

**3. Gauss equation and independent basis.** For \(q_0\ne1\), use \(q\) as the time variable, with \(\dot q=wq(1-q)\). The linear equation becomes
\[
q^2(1-q)^2\psi_{qq}+q(1-q)\left(1-\frac32q\right)\psi_q+\frac1{w^2}\psi=0.
\]
Its exponents at \(q=0\) are \(\pm i/w\), and at \(q=1\) are \(1/4\pm i\Omega/w\). Substitution \(\psi(q)=q^\alpha|1-q|^\beta U(1-q)\), with the \(\alpha,\beta\) defined above, reduces the equation on each interval \((0,1)\) and \((1,\infty)\) to the ordinary Gauss equation with parameters \((a,b,\gamma)\). Thus \(F\) and \(\overline F\) solve the equation, and their time derivatives are \(G\) and \(\overline G\). Near \(q=1\),
\[
F(q)=|1-q|^{1/4+i\Omega/w}(1+O(|1-q|)),\quad
G(q)=(-w/4-i\Omega)F(q)(1+O(|1-q|)).
\]
Their time-Wronskian therefore satisfies
\[
F\overline G-G\overline F=2i\Omega |1-q|^{1/2}(1+O(|1-q|)),
\]
nonzero sufficiently near the cycle. Abel's identity for the linear equation propagates nonvanishing throughout each open radial component. Consequently the two conjugate solutions form a real fundamental basis, and the unique real solution with initial data \((x,z)\) is
\[
\psi(t)=A F(q(t))+\overline A\,\overline{F(q(t))},\qquad
\dot\psi(t)=A G(q(t))+\overline A\,\overline{G(q(t))},
\]
with \(A\) as stated. Combining with Step 2 yields the complete original-time nonlinear trajectory, including the original velocity \(y=z-w(x^2-h)x/(2h)\).

**4. Explicit asymptotic phase and uniform drift.** Along a trajectory with \(q_0\ne1\), the same linear combination remains valid after any time shift, up to a common **positive real scalar** imposed by radial normalization. Thus the new coefficient \(A_t\) has the same complex argument as \(A_0\). However \(c_t=(1-q(t))/q(t)=c_0e^{-wt}\). This proves directly, without limiting arguments,
\[
\arg(A_t|c_t|^{i\Omega/w})=\arg(A_0|c_0|^{i\Omega/w})-\Omega t\pmod{2\pi}.
\]
Write \(\delta=\Phi(x_0,y_0)\). As \(t\to\infty\), \(|1-q(t)|=|c_0|e^{-wt}(1+O(e^{-wt}))\), so the explicit basis and the projective normalization give
\[
\begin{aligned}
(x(t),z(t))&=\sqrt h\,\frac{(\cos\chi,\;-\frac w4\cos\chi+\Omega\sin\chi)}{\sqrt{\cos^2\chi+(-\frac w4\cos\chi+\Omega\sin\chi)^2}}+O(e^{-wt}),\\
\chi&=\delta-\Omega t.
\end{aligned}
\]
The denominator is bounded away from zero for fixed \(w\in(0,4)\), since \(\Omega>0\). The rate constant can depend on the initial condition and parameters. On \(q=1\), the same expression is **exact**: its phase at time zero is \(\arg(x+i(z+wx/4)/\Omega)\), and the two-dimensional constant-coefficient linear oscillator with damping \(w/2\) gives rigid phase evolution. The displayed expression shows that equal phase gives asymptotically identical cyclic positions, and distinct phases do not; hence the phase fibers are the actual global isochrons. Taking \(q\to1\) in the coefficient formula proves its continuous extension to the circular formula (the leading factor reduces to \(x/2+i(z+wx/4)/(2\Omega)\)).

## Verification
The standalone `CHECK.py` performs exact symbolic expansion of the original polynomial vector field and its radial reduction, confirms the Gauss-equation residual numerically at multiple interior and exterior radial values, and integrates the **original** reduced physical-time flow to test the exact phase covariance at multiple points. Running `python CHECK.py` prints `GLOBAL_ISOCHRON_HYPERGEOMETRIC_CHECK_OK`. The proof in Steps 1–4, rather than finite tests, establishes the theorem for every admissible parameter and nonzero initial condition.

## Relationship to prior work
Belattar et al. [1] provide the nonautonomous radial first integral, the unique algebraic limit cycle and a global qualitative phase portrait. The prior detailed study [2] obtains exact stationary **on-cycle** physical-time statistics, the cycle period and the Floquet multiplier, none of which is claimed here. The new claim is the **off-cycle full-flow Gauss basis and its explicit global isochron map**. The later degree-six system of the same authors [3] has a different polynomial field and explicit solutions for that other system; it does not imply the present phase map. A global analytic phase gauge for a different three-dimensional polynomial oscillator [4] does not cover the original two-dimensional oscillator here. The Riccati-to-Gauss reduction itself is classical; novelty is not asserted for that general technique, only for its complete application to this particular nonlinear model and to its global basin.

## Limitations
No result is asserted at \(w=0\), at or beyond \(w=4\), or at the origin, where the phase construction degenerates. The representation involves analytic continuation of the standard Gauss hypergeometric function and may be numerically ill-conditioned for extreme radial starts or near the critical parameter \(w=4\). The \(O(e^{-wt})\) estimate is pointwise in fixed initial data and parameter, not uniform over the basin. The result is a classical special-function solution, not an elementary formula; it does not by itself yield perturbation-robust phase-response estimates. Equivalent derivations in unindexed integrability literature remain a publication-priority risk.

## References
[1] M. Belattar, R. Cheurfa, A. Bendjeddou and P. Santana, “A class of nonlinear oscillators with non-autonomous first integrals and algebraic limit cycles,” *Electronic Journal of Qualitative Theory of Differential Equations*, 2023, No. 50, 1–13, appeared 2023-12-14. DOI: 10.14232/ejqtde.2023.1.50. Full text: https://acta.bibl.u-szeged.hu/88793/1/ejqtde_2023_050.pdf .

[2] “Exact physical-time statistics and arrest scaling of an algebraic limit cycle,” 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-physical-time-statistics-and-arrest-scaling-of-an-algebrai--49449bc217a6 .

[3] M. Belattar, R. Cheurfa, A. Bendjeddou and P. Santana, “An Exactly Solvable Planar Differential System Of Degree Six With An Explicit Algebraic Limit Cycle,” *Applied Mathematics E-Notes* 24 (2024), 180–191. Full text: https://www.math.nthu.edu.tw/~amen/2024/AMEN-A230413.pdf .

[4] “Global analytic phase-gauge conjugacy and a sharp Hurwitz obstruction in a periodic polynomial flow,” 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-global-analytic-phase-gauge-conjugacy-and-a-sharp-hurwitz-obstru--41e7de6a0455 .
