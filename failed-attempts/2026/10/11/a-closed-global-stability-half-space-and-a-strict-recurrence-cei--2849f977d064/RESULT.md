# A closed global-stability half-space and a strict recurrence ceiling in the Huang–Li financial flow
## Finding
Consider the financial differential equation
\[
\dot x=z+(y-a)x,\qquad \dot y=1-by-x^2,\qquad \dot z=-x-cz,
\]
with \(a,b,c>0\). This is the three-state chaotic financial model used as the master plant in Yao et al. (2022), where \(x\) is the interest rate, \(y\) is investment demand, and \(z\) is the price index.

Let \(Q_0=(0,1/b,0)\). On the entire closed parameter half-space \(a\ge 1/b\), \(Q_0\) is globally asymptotically stable. If \(a>1/b\), the convergence is globally exponential. At the boundary \(a=1/b\), the equilibrium remains globally attracting although the basic energy derivative is only semidefinite.

There is also a parameter-independent recurrence restriction: every bounded complete trajectory other than \(Q_0\) satisfies
\[
y(t)<1/b\qquad\text{for every }t\in\mathbb R.
\]
Thus no non-equilibrium compact invariant set can touch the plane \(y=1/b\). In particular, for \(a\ge1/b\), the only compactly supported invariant probability measure is the Dirac mass at \(Q_0\).

## Assumptions and scope
The parameters satisfy \(a,b,c>0\), and solutions are classical solutions of the displayed autonomous polynomial system. The global-stability conclusion is restricted to \(a\ge1/b\). The recurrence ceiling applies to bounded complete trajectories for all positive \(a,b,c\).

The statement does not claim that \(a=1/b\) is the full global-stability boundary. The classical local stability region can extend beyond this half-space for some \(c\); the result here is an exact closed region certified by a global energy identity.

## Proof
Write \(Y=y-1/b\). Then
\[
\dot x=z+(Y+1/b-a)x,\qquad \dot Y=-bY-x^2,\qquad \dot z=-x-cz.
\]
For
\[
V=\frac12(x^2+Y^2+z^2),
\]
direct differentiation gives
\[
\begin{aligned}
\dot V
&=x[z+(Y+1/b-a)x]+Y(-bY-x^2)+z(-x-cz)\\
&=(1/b-a)x^2-bY^2-cz^2.
\end{aligned}
\]
The mixed terms \(xz\) cancel, as do the cubic terms \(x^2Y\).

If \(a>1/b\), let \(m=\min\{a-1/b,b,c}\). Then
\[
\dot V\le -2mV,
\]
so \(V(t)\le e^{-2mt}V(0)\) and \(Q_0\) is globally exponentially stable.

If \(a=1/b\), then
\[
\dot V=-bY^2-cz^2\le0.
\]
Because \(V\) is proper, every forward orbit remains in a compact sublevel set and is forward complete. The zero-derivative set is \(Y=0\), \(z=0\). A trajectory can remain in that set only if \(\dot z=-x=0\), hence only if \(x=0\). Therefore its largest invariant subset is \(Q_0\), and LaSalle's invariance principle gives global asymptotic stability at the endpoint.

For the recurrence ceiling, solve the scalar equation \(\dot y+by=1-x^2\) along a bounded complete trajectory. For \(T>0\),
\[
y(t)=e^{-bT}y(t-T)+\frac{1-e^{-bT}b-\int_0^T e^{-bs}x(t-s)^2\,ds.
\]
Boundedness and \(b>0\) allow \(T\to\infty\), giving
\[
y(t)=\frac1b-\int_0^\infty e^{-bs}x(t-s)^2\,ds\le\frac1b.
\]
Equality at one time forces \(x(s)=0\) for all prior times; then the equations force \(z=0\) and bounded completeness of \(\dot y=1-by\) forces \(y=1/b\). Uniqueness propagates this state for all time, so every other bounded complete trajectory has strict inequality.

Finally, if \(a\ge1/b\) and \(\mu\) is a compactly supported invariant probability measure, invariance gives \(\int \dot V\,d\mu=0\). The displayed nonpositive identity forces the support into the zero-derivative set; the invariant-set argument then reduces the support to \(Q_0\). Hence \(\mu=\delta_{Q_0}\).

## Verification
The file `verify.py` performs an exact coefficient-level polynomial check of the centered energy identity and of the previously published special Darboux case \(b=c\), \(c(a-c)=1\). It uses only the Python standard library and returns `VERIFY_OK` when all symbolic coefficient identities match.

The boundary argument is analytic rather than experimental: the proof uses properness of \(V\), LaSalle invariance, and the exact infinite-past representation for bounded complete trajectories. No finite simulation is used to infer an infinite-time conclusion.

## Relationship to prior work
Ma and Chen's two 2001 papers analyze the same model through equilibria, local stability, pitchfork/Hopf bifurcations, periodic behavior, and numerical chaotic regimes. Their inspected full texts do not state the closed global energy estimate above or the bounded-complete recurrence ceiling.

Szumiński (2017) proves non-integrability of the same Huang–Li model by differential-Galois methods. Cândido, Llibre, and Valls (2018) study Hopf bifurcation and algebraic invariant surfaces. Aybar (2020) gives local stability and algebraic-invariant calculations and, on the special parameter curve \(b=c\), \(c(a-c)=1\), obtains the quadratic Darboux polynomial
\[
I^*=x^2+(y-1/c)^2+z^2,
\]
with cofactor \(-2c\). On that curve \(I^*=2V\), so this is an exact special case of the strict region \(a>1/b\). The present statement broadens that isolated parameter curve to the full closed half-space \(a\ge1/b\), supplies the semidefinite endpoint argument, and adds the strict bounded-complete ceiling \(y<1/b\).

Rao and Zhong (2020) establish stability results for delayed and impulsively controlled versions of the financial system, principally around the positive-interest-rate equilibrium. Yao et al. (2022) use the uncontrolled model as a chaotic master plant and develop fixed-time neural synchronization; their inspected article does not state the open-loop theorem proved here.

## Limitations
This result certifies a global-stability half-space; it does not classify all parameter triples for which \(Q_0\) is globally stable. It does not address unbounded solutions or claim that the chaotic parameter set used by Yao et al., \(a=0.9\), \(b=0.2\), \(c=1.2\), lies in the stable half-space; in fact \(a<1/b\) there.

The literature comparison is strongest for the inspected full texts of Ma–Chen I/II, Aybar, Rao–Zhong, and Yao et al.; the Cândido–Llibre–Valls comparison used its publicly available abstract/metadata rather than the publisher full text.

## References
1. Q. Yao, H. Jahanshahi, L. M. Batrancea, N. D. Alotaibi, and M.-I. Rus, “Fixed-Time Output-Constrained Synchronization of Unknown Chaotic Financial Systems Using Neural Learning,” *Mathematics* 10 (2022), 3682. DOI 10.3390/math10193682.
2. J. Ma and Y. Chen, “Study for the Bifurcation Topological Structure and the Global Complicated Character of a Kind of Nonlinear Finance System (I),” *Applied Mathematics and Mechanics* 22 (2001), 1240–1251. DOI 10.1007/BF02437847.
3. J. Ma and Y. Chen, “Study for the Bifurcation Topological Structure and the Global Complicated Character of a Kind of Nonlinear Finance System (II),” *Applied Mathematics and Mechanics* 22 (2001), 1375–1382. DOI 10.1007/BF02435540.
4. W. Szumiński, “Non-integrability of the Huang–Li nonlinear financial model,” arXiv:1703.06623v1 (2017).
5. M. R. Cândido, J. Llibre, and C. Valls, “Invariant Algebraic Surfaces and Hopf Bifurcation of a Finance Model,” *International Journal of Bifurcation and Chaos* 28 (2018), 1850150. DOI 10.1142/S021812741850150X.
6. O. O. Aybar, “Dynamical Analysis of a Nonlinear Financial System with Computational Algebra Methods,” *Düzce University Journal of Science & Technology* 8 (2020), 1142–1154. DOI 10.29130/dubited.644487.
7. R. Rao and S. Zhong, “Impulsive control on delayed feedback chaotic financial system with Markovian jumping,” *Advances in Difference Equations* 2020, 50. DOI 10.1186/s13662-020-2524-3.
