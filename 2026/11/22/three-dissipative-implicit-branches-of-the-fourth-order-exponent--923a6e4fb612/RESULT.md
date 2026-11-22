# Three dissipative implicit branches of the fourth-order exponential AVF step on a convex quartic

## Finding

Consider the exponential-completion fourth-order averaged-vector-field (AVF) discrete-gradient update of Lautwein, Marheineke, Myhr and Schäfers (Theorem 6 of [1]). Applied to the globally well-posed scalar gradient flow with \(\mathcal H(x)=x^4/4\), \(R=1\) and any initial \(x>0\), its single-step implicit equation has **exactly three distinct real solutions** whenever \(t=h x^2\ge20\). Every solution strictly decreases \(\mathcal H\), but two reverse the sign of the state and the third makes an exponentially small relative change.

Writing the three distinct solutions in increasing order \(y_1<y_2<y_3\), the large-step behavior at fixed \(x>0\) is
\[
\frac{y_1}{x}=-1+\frac4t+o(t^{-1}),\qquad
\frac{y_2}{x}=-1+2t^{-1/2}\bigl(\tfrac23\log t\bigr)^{1/4}(1+o(1)),
\]
\[
\frac{y_3}{x}=1-t e^{-3t^2/4}(1+o(1)),\qquad t\longrightarrow\infty.
\]
In contrast, the exact physical solution at time \(h\) obeys \(x(h)/x=(1+2t)^{-1/2}\to0\). Consequently, unconditional dissipation does not give global step uniqueness or control which large-step physical behavior an implicit root selection will realize.

## Assumptions and scope

The energy is the smooth convex but not globally strongly convex function \(\mathcal H:\mathbb R\to\mathbb R\), \(\mathcal H(v)=v^4/4\). The dissipative structure is \(R=1\), the skew-symmetric part vanishes, the initial state \(x\) is strictly positive, and the timestep \(h\) is strictly positive. The result concerns *exact real solutions* of the implicit **exponential completion** in [1, §2.4, Theorem 6], not its rational/Padé alternatives, iterative solver convergence, or multi-step error at a prescribed branch-selection rule. Three-root exactness holds for every \(h x^2\ge20\); this sufficient threshold is not asserted optimal.

The fourth-order exponential-completion method is
\[
\frac{y-x}{h}=-\exp\!\left[-\frac{h^2}{12}\mathcal H''\bigl(\tfrac{x+y}{2}\bigr)^2\right] \overline{\nabla}_{\!AVF}\mathcal H(x,y),
\quad \overline{\nabla}_{\!AVF}\mathcal H(x,y)=\int_0^1\mathcal H'((1-s)x+sy)\,ds.
\]
The original source proves energy consistency and small-timestep fourth-order behavior. Our statement addresses root multiplicity and large-step branches for this exact method, beyond those local guarantees.

## Proof

**1. Reduction and admissible interval.** Since \(\mathcal H'(v)=v^3\) and \(\mathcal H''(v)=3v^2\), put \(m=(x+y)/2\). Direct integration gives
\[
\overline{\nabla}_{\!AVF}\mathcal H(x,y)
=\frac{x^3+x^2y+xy^2+y^3}{4}
=\frac{(x+y)(x^2+y^2)}4,
\quad \exp[-h^2\mathcal H''(m)^2/12]=e^{-3h^2m^4/4}.
\]
The defining AVF chain rule gives, for every solution,
\[
\mathcal H(y)-\mathcal H(x)
=-h e^{-3h^2m^4/4}\bigl(\overline{\nabla}_{\!AVF}\mathcal H(x,y)\bigr)^2<0.
\]
Strictness follows because a zero AVF gradient would imply \(y=x\) from the update, contradicting \(\mathcal H'(x)=x^3>0\). Thus \(|y|<x\). Parameterize \(y=x(2z-1)\) with \(0<z<1\); setting \(t=h x^2\), \(q(z)=1-2z+2z^2>0\), the update becomes
\[
2(1-z)=t z q(z)e^{-3t^2z^4/4},\qquad
G_t(z):=\frac{t z q(z)}{2(1-z)}e^{-3t^2z^4/4}=1.
\]
Conversely, each root of \(G_t(z)=1\) in \((0,1)\) defines an admissible solution; none is lost in the reduction.

**2. Three sign-changing intervals for \(t\ge20\).** The continuous function \(G_t\) satisfies \(G_t(0)=0\) by extension and \(G_t(z)\to\infty\) as \(z\uparrow1\). At \(z=1/2\),
\[
G_t(1/2)=\frac t4 e^{-3t^2/64}<1
\]
for every \(t>0\), because \(e^{3t^2/64}\ge1+3t^2/64>t/4\); the final strict inequality follows from \(3t^2-16t+64>0\) (negative discriminant). Set \(s=1/t\in(0,1/20]\). The prefactor at \(z=3/t\) is
\[
\frac32\frac{1-6s+18s^2}{1-3s},
\]
and the fraction is decreasing in \(s\in[0,1/20]\), as its derivative is \(-3(18s^2-12s+1)/(1-3s)^2<0\). Using \(e^{-a}\ge1-a\),
\[
G_t(3/t)\ge\frac{447}{340}\left(1-\frac{243}{1600}\right)=\frac{606579}{544000}>1.
\]
Since \(0<3/t<1/2<1\), the intermediate value theorem supplies a root in each of \((0,3/t)\), \((3/t,1/2)\), and \((1/2,1)\).

**3. No other real roots.** Define
\[
T(z)=\frac{4z^3-8z^2+4z-1}{3z^4(z-1)q(z)},\qquad
P(z)=32z^6-128z^5+200z^4-170z^3+88z^2-27z+4.
\]
Differentiation yields the identities
\[
\frac{G_t'(z)}{G_t(z)}=3z^3(T(z)-t^2),\qquad
T'(z)=-\frac{P(z)}{3z^5(z-1)^2q(z)^2}.
\]
The polynomial \(P\) has exactly one zero in \((0,1)\). Indeed, on \((0,3/4)\) substitute \(z=(3u/4)/(1+u)\) with \(u>0\). Then \((1+u)^6P(z)\) has descending coefficients
\[
\left(\frac{17}{128},\frac{57}{32},\frac{21}{8},\frac{121}{32},\frac{33}{4},\frac{15}{4},4\right),
\]
so is strictly positive. On \((3/4,1)\) substitute \(z=(3/4+u)/(1+u)\). The analogous polynomial has descending coefficients
\[
\left(-1,-\frac{15}{4},-\frac{41}{8},-\frac{91}{32},-\frac18,\frac{15}{32},\frac{17}{128}\right).
\]
There is exactly one positive zero by Descartes' rule and the opposing signs at \(u=0\) and \(u\to\infty\). As \(P(3/4)=17/128>0\) and \(P(1)=-1\), the function \(T\) is strictly decreasing then strictly increasing. Hence the horizontal equation \(T(z)=t^2\) has at most two solutions. By Rolle's theorem, \(G_t(z)=1\) has at most three distinct solutions. With step 2, it has exactly three, one in each displayed interval. The first two have \(z<1/2\), so \(y<0\); the third has \(y>0\).

**4. Branch asymptotics.** For any fixed \(c>0\), \(G_t(c/t)\to c/2\). The first root is unique in \((0,3/t)\), so comparing \(c=2\pm\varepsilon\) shows \(t z_1\to2\), giving \(y_1/x=-1+4/t+o(t^{-1})\). Next, for \(C>0\) and \(z=Ct^{-1/2}(\log t)^{1/4}\),
\[
\log G_t(z)=\left(\frac12-\frac{3C^4}{4}\right)\log t+O(\log\log t).
\]
Comparisons with constants \(C\) on either side of \((2/3)^{1/4}\) and uniqueness in \((3/t,1/2)\) give \(z_2\sim t^{-1/2}((2/3)\log t)^{1/4}\). Finally, the third root has \(z_3\ge1/2\) and obeys
\[
0<1-z_3=\frac t2 z_3q(z_3)e^{-3t^2z_3^4/4}\le\frac t2e^{-3t^2/64}.
\]
Thus \(t^2(1-z_3)\to0\), \(z_3q(z_3)\to1\), and the exponential in the exact equation equals \(e^{-3t^2/4}(1+o(1))\). Therefore \(1-z_3\sim(t/2)e^{-3t^2/4}\), as claimed. The physical solution of \(\dot x=-x^3\) is \(x(h)=x/\sqrt{1+2hx^2}\). This completes the proof.

## Verification

The independently runnable `verification.py` checks the rational polynomial substitutions and derivative identity with exact fractions, the rational inequality underlying the three-root existence argument, and high-precision bracketing of all three roots at \(t=20\). It does not replace the analytic proof of exact root count or asymptotics. Run using `python3 verification.py` with standard Python 3.10 or newer; no additional libraries are required. For \(t=20\), approximate roots in \(z\) are \(0.1180826877\), \(0.2086647729\), and \(1-5.1482002\times10^{-130}\); the last requires high precision.

## Relationship to prior work

Source [1], especially Theorem 6 and the formula in §2.4, establishes the particular fourth-order exponential-completion method and pointwise nonnegative dissipation. This theorem does not supply an all-timestep uniqueness statement or classify the real quartic roots. Source [2], §5.1, establishes uniqueness for an ordinary AVF descent update with a *fixed* scalar multiplier under convexity assumptions; its monotonicity argument does not apply to the midpoint-dependent exponential multiplier in [1]. Thus source [2]'s theorem neither contradicts nor implies our root count. The finding concerns neither the source's rational completion nor other discrete-gradient methods. Results about unrelated scalar auxiliary-variable integrators, including their energy-loss versus state-convergence behavior, do not imply the exponential AVF scalar root polynomial or its three-branch asymptotics.

## Limitations

The bound \(t\ge20\) is sufficient, not asserted sharp. No rule is specified for choosing among the three roots, and no statement is made about convergence of Newton iteration, existence of alternative complex roots, branch continuation, a multi-step trajectory, or global practical failure of a prescribed solver. Small-step fourth-order accuracy is not challenged. Strict energy decrease does not imply positivity of the physical state. Novelty has been checked against the explicitly named primary sources and accessible mathematical records but not independently certified against every prior treatment of nonlinear implicit integration.

## References

[1] L. Lautwein, N. Marheineke, H. N. Myhr and K. Schäfers, *Fourth-Order Energy-Consistent Average Vector Field Discrete Gradient Methods for Dissipative Hamiltonian Systems*, arXiv:2609.24692, first released 2026-09-21. https://arxiv.org/abs/2609.24692 . Specifically §2.4, Theorem 6, and §3.

[2] M. J. Ehrhardt, E. S. Riis, T. Ringholm and C.-B. Schönlieb, *A geometric integration approach to smooth optimisation: Foundations of the discrete gradient method*, arXiv:1805.06444, §5.1 and Lemma 5.1. https://arxiv.org/abs/1805.06444 .
