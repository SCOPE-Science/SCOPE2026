# A universal algebraic relaxation and winding clock for a nilpotent non-Morse attractor

## Finding

For every fixed \(\varepsilon>0\), consider the planar polynomial differential equation
\[
\dot x=y-\varepsilon x^3,\qquad \dot y=-x^3-y^3.
\]
Let \(E(t)=x(t)^4/4+y(t)^2/2\) along any nonzero real solution, and count \(N(t)\), with multiplicity one, the crossings of the positive \(y\)-semiaxis \(\{x=0,y>0\}\) during \((0,t]\). Introduce the positive beta integrals
\[
I_r=\int_0^1\frac{u^r\,du}{\sqrt{1-u^4}}
=\frac14B\left(\frac{r+1}{4},\frac12\right),\qquad r=0,6.
\]
**Every nonzero forward orbit has infinitely many such transverse crossings**, and its energy and crossing count have initial-condition-independent sharp limits in the *original physical time*:
\[
\boxed{\lim_{t\to\infty}t^2E(t)
=\frac{I_0^2}{16\varepsilon^2 I_6^2}},\qquad
\boxed{\lim_{t\to\infty}\frac{N(t)}{\sqrt t}
=\frac{1}{4\sqrt{\varepsilon I_0 I_6}}}.
\]
In particular, the envelope of the position satisfies
\[
\limsup_{t\to\infty}\sqrt t\,|x(t)|
=\frac{1}{\sqrt{2\varepsilon (I_6/I_0)}}.
\]
The origin is globally asymptotically stable, but this oscillator slows down: its oscillation count grows as \(\sqrt t\), rather than linearly in time.

## Assumptions and scope

The parameter \(\varepsilon\) is any **fixed strictly positive real number**; no smallness assumption is imposed. All initial conditions in \(\mathbb R^2\setminus\{(0,0)\}\) are admitted. Time \(t\) is the original time of the displayed polynomial vector field, not an orbit-dependent reparameterization. Solutions are unique for all forward times by local polynomial well-posedness and the coercive energy identity below. The count includes only transverse intersections with \(x=0,y>0\); any convention differing by finitely many initial crossings yields the same limit. The critical boundary \(\varepsilon=0\) is excluded.

The two beta integrals are finite and strictly positive. The \(\limsup\) assertion concerns the original signed coordinate, not a pointwise limit of \(\sqrt t\,|x(t)|\), which oscillates down to zero infinitely often. The first two displayed limits are the single quantitative relaxation-and-winding claim.

## Proof

**1. Global attraction and strict dissipation.** Define
\[
E(x,y)=\frac{x^4}{4}+\frac{y^2}{2}.
\]
It is proper and positive away from the origin. Direct differentiation gives the exact identity
\[
\dot E=x^3(y-\varepsilon x^3)+y(-x^3-y^3)
=-\varepsilon x^6-y^4<0\quad\text{off the origin}.
\]
Consequently every solution remains within a compact sublevel set and exists for every forward time. Its energy has a nonnegative limit. Any nonzero omega-limit point would lie on an invariant set with \(\dot E=0\), which here consists solely of the origin. Thus every trajectory tends to the origin. By uniqueness a nonzero orbit never reaches the origin at a finite time.

**2. Normalize a small complete turn.** At a positive-semiaxis crossing write \(E=e>0\); then the crossing state is \((x,y)=(0,\sqrt{2e})\). During the subsequent excursion introduce
\[
x=\sqrt2\,e^{1/4}u,\quad y=\sqrt{2e}\,v,
\quad s=e^{1/4}(t-t_{\rm crossing}),\quad h=e^{1/4}.
\]
The normalized initial state is \((u,v)=(0,1)\), and the exact rescaled ODE is
\[
\frac{du}{ds}=v-2\varepsilon h u^3,
\qquad\frac{dv}{ds}=-2u^3-2h^3v^3.
\]
For fixed \(\varepsilon\) this vector field converges in \(C^1\) on compact sets to the quartic Hamiltonian oscillator
\[
u'=v,\qquad v'=-2u^3,\qquad u^4+v^2=1.
\]
The limiting periodic orbit through \((0,1)\) is regular and has first positive return time
\[
T_0=4\int_0^1\frac{du}{\sqrt{1-u^4}}=4I_0.
\]
All its section crossings are transverse. Continuous dependence on \(h\), including transversality and the implicit function theorem at the next positive crossing, gives the small-energy return time
\[
\Delta t(e)=e^{-1/4}\bigl(4I_0+O(e^{1/4})\bigr).
\]
There are no unexpected intermediate positive-section crossings, since the limiting orbit stays strictly on one side of the section between its finitely many transverse crossings. The same compactness argument applied to the entire normalized unit oval shows that every sufficiently small nonzero state has a positive-section crossing within a bounded normalized time. Since all nonzero trajectories eventually enter the small-energy region, *every* nonzero orbit has infinitely many positive-section crossings.

**3. Compute the per-turn energy defect.** At normalized energy \(e\), the exact dissipation over one turn is
\[
e_{\rm next}-e=-\varepsilon\int x^6\,dt-\int y^4\,dt.
\]
Under the scaling in step 2,
\[
\int x^6\,dt=8e^{5/4}\int_0^{T_0}u_0(s)^6\,ds
+O(e^{3/2}),\qquad \int y^4\,dt=O(e^{7/4}),
\]
where \((u_0,v_0)\) is the limiting unit-energy quartic orbit. The four symmetric quadrants give
\[
\int_0^{T_0}u_0(s)^6\,ds
=4\int_0^1\frac{u^6\,du}{\sqrt{1-u^4}}=4I_6.
\]
The resulting exact leading return-map expansion, with a uniform error for small positive \(e\), is
\[
\boxed{e_{\rm next}=e-32\varepsilon I_6 e^{5/4}+O(e^{3/2})}.
\]
The \(O(e^{3/2})\) term follows from smooth dependence of the rescaled orbit and return time on \(h=e^{1/4}\). Note that the velocity-cubic dissipation \(y^4\) contributes only at order \(e^{7/4}\), so the positive position-cubic damping controls the leading law.

**4. Sum cycles and return to physical time.** Let \(e_j\) be energy at the \(j\)-th sufficiently late positive-section crossing and let \(t_j\) be the corresponding original-time crossing. Then \(e_j\searrow0\) and
\[
e_{j+1}^{-1/4}-e_j^{-1/4}
=8\varepsilon I_6+O(e_j^{1/4}).
\]
Cesàro averaging yields
\[
\frac{e_j^{-1/4}}{j}\longrightarrow 8\varepsilon I_6.
\]
The return-time law from step 2 then gives
\[
t_{j+1}-t_j=4I_0e_j^{-1/4}(1+o(1))
\sim 32\varepsilon I_0I_6\,j,
\]
so
\[
\boxed{\frac{t_j}{j^2}\longrightarrow16\varepsilon I_0I_6}.
\]
Combining these gives
\[
t_j^2 e_j\longrightarrow\frac{I_0^2}{16\varepsilon^2I_6^2}.
\]
For \(t\in[t_j,t_{j+1}]\), monotonicity bounds the energy by \(e_{j+1}\le E(t)\le e_j\), while \(e_{j+1}/e_j\to1\) and \(t_{j+1}/t_j\to1\). Thus the energy limit holds at all physical times, not just at crossings. Likewise the crossing count differs from \(j\) by at most a fixed integer, giving the announced \(N(t)/\sqrt t\) limit.

**5. Position envelope.** Throughout the \(j\)-th turn, normalized trajectories converge uniformly to the unit quartic oval, whose maximum absolute \(u\)-coordinate is \(1\). Every turn approaches both turning points, and the energy is asymptotically constant relative to the leading scale within one turn. Hence its maximum absolute physical position is \(\sqrt2 e_j^{1/4}(1+o(1))\). Substitution of the energy law gives exactly the claimed \(\limsup\). This completes the proof.

## Verification

The reproducible checker `checks/verify_relaxation.py` verifies the energy Lie-derivative identity symbolically, the beta integral constants numerically, and eight small-energy complete-return calculations with two positive parameter values. The output is:

```
VERIFY_OK symbolic_energy_identity=1 small_energy_return_cases=8
BETA_INTEGRALS I0=1.31102877715 I6=0.359442070421
LIMIT_COEFFICIENTS_EPS_QUARTER energy=13.3035220819 count=0.728365620395
MAX_LAST_SCALE_RELATIVE_ERRORS period=0.00454997 loss=0.02231037
FINITE_CHECK_ONLY: asymptotic conclusions require the analytical return-map proof.
```

The checker is a finite diagnostic and does not prove infinite-time or all-initial-condition statements. Those are obtained from the analytical first-return and summation argument, using exact equations and compact convergence.

## Relationship to prior work

Jongeneel's 2026 primary paper introduces precisely this nilpotent polynomial system, proves global asymptotic stability using the same quartic energy, and proves that no smooth Morse Lyapunov function can exist (Proposition 3.5). The field, Lyapunov function, and Morse obstruction are **not** new here. That paper does not derive the physical-time energy constant, period growth, or crossing-count law. A separate published 2026 note uses the same system to compare two flat-time-changed vector fields with identical Taylor jets; it changes their time clocks and does not imply the present original-time asymptotics.

The classic theory of weakly damped oscillators motivates the beta-function orbit average. Bárta's 2018 study of exact decay for scalar second-order ODEs addresses velocity-dependent damping with hypotheses such as \(g(v)\asymp |v|^\alpha\), \(0<\alpha<1\), and gives convergence-order information. The current vector field has a position-dependent cubic term in \(\dot x\), and its second-order elimination introduces position-dependent damping; those stated hypotheses do not cover its full return map, nor does that paper give the two displayed limiting constants. A 2026 study of a cubic Liénard weak focus supplies a different original-time amplitude law, but its linearized angular frequency is nonzero, whereas this nilpotent oscillator has a frequency vanishing at the origin. These differences are mathematical, not merely title or parameter differences.

The new claim is the paired sharp physical-time energy-and-winding asymptotics for every nonstationary orbit of Jongeneel's exact original system. It is narrower than a general theorem on degenerate nonlinear oscillators; a universal method of averaging may provide another proof, which remains a genuine residual historical-priority risk.

## Limitations

The result assumes fixed \(\varepsilon>0\). It does not assert any uniformity as \(\varepsilon\downarrow0\), determine the different critical dynamics at \(\varepsilon=0\), or provide a second asymptotic term or finite-time error rate. The original system's no-Morse-Lyapunov result is due to Jongeneel; no independent strengthening of that obstruction is claimed. This is an analytical first-order asymptotic law, not independent formal or external certification. Historical priority beyond the inspected literature remains open to independent assessment.

## References

1. W. Jongeneel, *On global Lyapunov functions being Morse*, arXiv:2610.05626v1, first publicly posted 2026-10-04. Proposition 3.5 and its proof, pp. 9–10; publicly accessible manuscript: https://borowiecki.dev/pdf/2610.05626.
2. T. Bárta, *Exact rate of decay for solutions to damped second order ODE's with a degenerate potential*, Evolution Equations and Control Theory **7** (2018), 531–543, DOI:10.3934/eect.2018025. Open author preprint: https://www.karlin.mff.cuni.cz/~barta/preprints/OptimalDecay_degenerate.pdf.
3. *Morse–Lyapunov existence is invisible to the full Taylor jet*, publicly available 2026 research note: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-morse-lyapunov-existence-is-invisible-to-the-full-taylor-jet--3937ccf41604.
4. *Global algebraic relaxation and renormalized logarithmic phase at a cubic Liénard weak focus*, publicly available 2026 research note: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-global-algebraic-relaxation-and-renormalized-logarithmic-phase-a--33495a7a3125.
