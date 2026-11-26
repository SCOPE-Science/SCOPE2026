# Sharp global convergence threshold and a critical trapping-energy barrier for the sinusoidal jerk flow

## Finding

For the three-dimensional smooth system
\[
\dot x=y,\qquad \dot y=az,\qquad
\dot z=-y-bz+c\sin(dx),
\qquad a,b,c,d>0,
\tag{1}
\]
**every solution with arbitrary initial state in \(\mathbb R^3\) converges to one of the equilibria \((k\pi/d,0,0)\), \(k\in\mathbb Z\), if and only if**
\[
\boxed{b\ge cd.}
\tag{2}
\]
The criterion includes equality. At the critical surface \(b=cd\), define
\[
\boxed{
E(x,y,z)=\frac a2\left(z+\frac ba y\right)^2
+\frac12\bigl(y-c\sin(dx)\bigr)^2
+\frac{c^2}{2}\bigl(1+\cos(dx)\bigr)^2.}
\tag{3}
\]
It obeys the **exact** identity
\[
\boxed{\dot E=-b\bigl(1+\cos(dx)\bigr)y^2\le0.}
\tag{4}
\]
In particular, for every integer \(k\), a trajectory beginning with
\[
\frac{2k\pi}{d}<x(0)<\frac{2(k+1)\pi}{d},
\qquad E(x(0),y(0),z(0))<2c^2
\tag{5}
\]
remains strictly inside that same strip for all forward times and converges to
\[
\left(\frac{(2k+1)\pi}{d},0,0\right).
\tag{6}
\]
When \(b<cd\), every equilibrium has positive unstable dimension and the initial conditions converging to *any* equilibrium form a set of three-dimensional Lebesgue measure zero. This last conclusion is not a claim about chaos, boundedness of \(x(t)\), or the existence of periodic solutions below threshold.

## Assumptions and scope

The four parameters \(a,b,c,d\) are strictly positive; time is continuous and forward. Solutions are classical. The phase space of (1) is all \(\mathbb R^3\), with no restriction on initial signs. Since the vector field is periodic in \(x\) with period \(L=2\pi/d\), we use the compact-in-position cylinder \(\mathcal C=(\mathbb R/L\mathbb Z)\times\mathbb R^2\) only as an auxiliary space, then lift convergence back to \(\mathbb R^3\). Stability means actual trajectory convergence to an equilibrium, not convergence to a prescribed common equilibrium. The equilibrium set is \(\{(k\pi/d,0,0):k\in\mathbb Z\}\).

## Proof

### 1. Global forward existence and bounded auxiliary variables

Set \(u=(y,z)^{\mathsf T}\). It solves
\[
\dot u=Au+\begin{pmatrix}0\\c\sin(dx)\end{pmatrix},
\qquad A=\begin{pmatrix}0&a\\-1&-b\end{pmatrix}.
\]
Because \(a,b>0\), \(A\) is Hurwitz. There are constants \(M,\gamma>0\), depending on \(a,b\), such that \(\|e^{At}\|\le M e^{-\gamma t}\), \(t\ge0\). The variation-of-constants formula therefore gives
\[
\|u(t)\|\le M e^{-\gamma t}\|u(0)\|+Mc/\gamma.
\tag{7}
\]
As \(\dot x=y\), no coordinate can blow up in finite forward time. All solutions are forward complete, and their \((y,z)\) components remain bounded even if their lifted \(x\) coordinates do not.

### 2. Strict Lyapunov function for \(b>cd\)

Choose any \(h\) with \(cd<h<b\), and define the position-periodic function
\[
V_h=\frac12\left(1+\frac{hb}{a}\right)y^2
+\frac a2z^2+hyz-cy\sin(dx)+\frac{hc}{d}\cos(dx).
\tag{8}
\]
Differentiating along (1), with no averaging, gives the polynomial-trigonometric identity
\[
\boxed{\dot V_h=-a(b-h)z^2-\bigl(h+cd\cos(dx)\bigr)y^2.}
\tag{9}
\]
Consequently,
\[
\dot V_h\le-a(b-h)z^2-(h-cd)y^2,
\tag{10}
\]
which is strictly negative whenever \((y,z)\ne(0,0)\).

The quadratic part of \(V_h\) in \((y,z)\) has symmetric matrix
\[
\begin{pmatrix}1+hb/a&h\\h&a\end{pmatrix},
\]
whose determinant is \(a+h(b-h)>0\) and whose first leading principal minor is positive. Its sine and cosine contributions are bounded by a constant plus a linear function of \(\lvert y\rvert\). Thus \(V_h\) is bounded below and coercive in \((y,z)\), uniformly in position on \(\mathcal C\). Its decreasing sublevel contains the forward orbit compactly on \(\mathcal C\). By LaSalle's invariance principle, the omega-limit set is contained in the largest invariant subset of \(\{y=z=0\}\). There \(\dot z=c\sin(dx)\), so invariance requires \(\sin(dx)=0\); hence the set consists precisely of the two equilibrium phases on \(\mathcal C\). Since a nonempty omega-limit set of a precompact continuous-time orbit is connected, it is a singleton. The quotient trajectory converges to one equilibrium phase.

### 3. Rigidity at the closed boundary \(b=cd\)

The strict choice \(cd<h<b\) is unavailable at equality. Nevertheless, substitution of \(h=b=cd\) into (8) yields
\[
E=V_b+c^2,
\]
where the exactly equal expression in (3) is a sum of three nonnegative squares. Equation (9) becomes (4). The first two squares of (3) control both \(y\) and \(z\) uniformly, so an \(E\)-sublevel on \(\mathcal C\) is compact.

Suppose a complete trajectory lies in \(\{\dot E=0\}\). If \(y(t_0)\ne0\) at any time, continuity gives an open time interval on which \(y\ne0\). On that interval \(\dot E=0\) forces \(\cos(dx)=-1\), hence \(x\) is constant, contradicting \(\dot x=y\ne0\). Thus \(y\equiv0\), whence \(z\equiv0\) by \(\dot y=az\), and finally \(\sin(dx)=0\) by \(\dot z=0\). The largest invariant subset of \(\{\dot E=0\}\) therefore comprises only the two equilibrium phases. As above, LaSalle and the connected omega-limit argument imply convergence to one equilibrium phase on \(\mathcal C\).

To pass to the original line, choose a sufficiently short neighborhood of the limiting equilibrium phase on the circle. Its inverse image under \(\mathbb R\to\mathbb R/L\mathbb Z\) is a disjoint union of open intervals. Eventually the continuous lifted coordinate \(x(t)\) lies in this union; after that time it must stay in one connected component, and therefore converges to one specific lift \(k\pi/d\). The other coordinates converge to zero. This proves global convergence for both \(b>cd\) and \(b=cd\), with no assumption about the stability of the limiting equilibrium.

### 4. Critical trapping-energy barrier

When \(b=cd\), at each even-index position \(x=2k\pi/d\), equation (3) reads
\[
E=\frac a2\left(z+\frac ba y\right)^2+\frac12y^2+2c^2\ge2c^2.
\tag{11}
\]
A solution satisfying (5) has \(E(t)\le E(0)<2c^2\) by (4), and thus cannot cross either neighboring even-index plane. Equation (2), already established on the closed boundary, forces convergence to an equilibrium in the closed strip. Only the odd-index equilibrium lies strictly inside; neither boundary equilibrium can be approached, because \(E(t)<2c^2\) remains uniformly true. This proves (6).

### 5. Necessity and sharpness of the boundary

At an equilibrium \(p_k=(k\pi/d,0,0)\), the characteristic polynomial is
\[
p_k(\lambda)=\lambda^3+b\lambda^2+a\lambda-acd(-1)^k.
\tag{12}
\]
If \(b<cd\), the Routh first column for even \(k\) has signs \((+,+,+,-)\), since its third entry is \(a+acd/b>0\). Thus even equilibria have one eigenvalue in the open right half-plane. For odd \(k\), the signs are \((+,+,-,+)\), since the third entry is \(a-acd/b<0\); thus odd equilibria have two eigenvalues in the open right half-plane. Neither polynomial has a zero imaginary-axis root in this strict region, so all equilibria are hyperbolic. The stable-manifold theorem gives immersed stable sets of dimensions two (even) and one (odd). Each has three-dimensional Lebesgue measure zero, and their countable union also has measure zero. Any initial state whose forward trajectory converges to any equilibrium must lie in one of these stable sets. Therefore for almost every initial condition convergence to an equilibrium fails when \(b<cd\). This proves the reverse implication in (2).

At equality, the odd-index equilibrium has the factorization
\[
p_{2k+1}(\lambda)=(\lambda+b)(\lambda^2+a),
\]
showing that its conjugate imaginary eigenvalue pair makes the closed-boundary global convergence theorem genuinely stronger than a hyperbolic local-stability argument.

## Verification

The accompanying standalone `verify.py` checks, symbolically in independent parameters, the identity (9), the exact equality \(E=V_b+c^2\) when \(b=cd\), and the derivative identity (4). It then integrates 48 deterministically selected initial conditions in four parameter configurations, checking Lyapunov monotonicity on 36 traces with \(b\ge cd\) and successful numerical integration on the 12 strict subthreshold traces. Reproduce with `python verify.py` after installing Python 3 with SymPy, SciPy and NumPy. The three symbolic identities returned true, and all 48 finite numerical trajectory checks passed. The infinite-time, measure-zero, and all-initial-state assertions are consequences of the written proof; finite simulation is not used to establish them.

## Relationship to prior work

Li and Zeng (2023), Section 2, introduces precisely (1), identifies the infinite equilibrium lattice, and analyzes local characteristic polynomials for selected parameters; Sections 3–5 numerically investigate multi-scroll and multistable regimes, basin plots, and circuits. Their 12-page open-access article was inspected through its conclusion and references. The new claim is the *full all-initial-state global-convergence if-and-only-if threshold*, its critical sum-of-squares Lyapunov identity, and the explicit critical trapping barrier, not the already known equilibria or local linearization.

Ma, Wu, Chu, and Zhang (2014) studied multi-scroll Jerk circuits with sine forcing and mixed Heaviside control. Its accessible abstract does not state the global convergence theorem for the uncontrolled system (1), but its unavailable full text remains a relevant priority risk. Ding and Feng (2020) studied a related nonsmooth, special-form sine jerk model rather than precisely the smooth dynamics (1). Published work on global Hopf-slope balance for generic third-order feedback systems supplies a **prior** stationary weighted-slope necessary condition: for a feedback equation \(x^{(3)}+b x''+a x'=g(x)\), compact stationary states satisfy \(\langle-g'(x), (x')^2\rangle=ab\langle1,(x')^2\rangle\). This applies here after setting \(g(x)=ac\sin(dx)\), but it neither furnishes the pointwise Lyapunov function (8), proves all-orbit convergence at \(b=cd\), nor gives the trapping-energy barrier (11). No novelty is asserted for that generic identity.

## Limitations

The conclusion is convergence to one of infinitely many equilibria, not uniform attraction to a single common point. Which equilibrium is selected is not globally classified, although (5) provides a certified subset of critical attraction basins. For \(b<cd\), the proof establishes only that almost all trajectories fail to converge to equilibria; it does not establish the existence of non-equilibrium compact recurrent dynamics or chaos, and it does not prove lifted \(x(t)\) remains bounded. The 2014 same-topic full text and unindexed control-theory treatments remain residual originality risks. Mathematical correctness and priority have not been independently validated.

## References

1. F. Li and J. Zeng, *Multi-Scroll Attractor and Multi-Stable Dynamics of a Three-Dimensional Jerk System*, **Energies** 16 (2023), article 2494, first public March 6, 2023. https://doi.org/10.3390/en16052494 ; open-access full text https://psecommunity.org/wp-content/plugins/wpor/includes/file/2303/LAPSE-2023.20558-1v1.pdf
2. J. Ma, X. Wu, R. Chu and L. Zhang, *Selection of multi-scroll attractors in Jerk circuits and their verification using Pspice*, **Nonlinear Dynamics** 76 (2014), 1951–1962. https://doi.org/10.1007/s11071-014-1260-1
3. H. Ding and X. Feng, *Generation of Multi-Scroll Chaotic Attractors from a Jerk Circuit with a Special Form of a Sine Function*, **Electronics** 9 (2020), article 842. https://doi.org/10.3390/electronics9050842
4. *Global Hopf-slope balance for third-order feedback cycles and the Goodwin oscillator*, published mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-goodwin-global-hopf-slope-balance--69bab068e3f7/RESULT.md
