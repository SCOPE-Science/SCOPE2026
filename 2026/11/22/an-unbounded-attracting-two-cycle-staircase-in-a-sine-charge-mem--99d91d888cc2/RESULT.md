# An unbounded attracting two-cycle staircase in a sine-charge memristive map

## Finding

For the three-dimensional real map defined below, the exact number of **hyperbolically attracting primitive period-two orbits modulo vertical charge translations** at zero input gain is
\[
N(h)=\max\!\left\{0,\left\lceil\frac{\rho^{-1}-\theta}{\pi}\right\rceil\right\},\qquad
\rho=\sqrt{4h^2-1},\quad \theta=\arccos\frac1{2h},\quad h>\frac12.
\]
At the equality values of the stability inequalities, a cycle has a unit-modulus multiplier and is not included in this *hyperbolic-sink count*. The count has the sharp divergence
\[
N(h)\sim\frac{1}{2\pi\sqrt{h-1/2}}\qquad(h\downarrow1/2).
\]
More significantly, for every positive integer \(M\) and every fixed amplification factor \(\gamma>0\), there exist a coupling \(h\in(1/2,1)\) and a number \(\varepsilon>0\) such that, for **every** input gain \(0<\mu<\varepsilon\), the original three-dimensional map has at least \(M\) mutually inequivalent hyperbolically attracting primitive period-two orbits, each possessing an open attraction basin. Inequivalence is modulo \(z\mapsto z+2\pi j\), \(j\in\mathbb Z\), and interchange of the two temporal phases. At the zero-input boundary the count is exact; for positive gain this is a persistence lower bound, not an exhaustive count.

## Assumptions and scope

Fix the published coefficient \(k=1/10\) and any finite \(\gamma>0\). On the full real state space \(\mathbb R^3\), define
\[
P_{\mu,\gamma}(u)=\frac{k\cos(4\pi\mu\gamma u(1-u))}{\log(3-4\mu u(1-u))},
\]
\[
F_{\mu,h,\gamma}(x,y,z)=\left(P_{\mu,\gamma}(x)+h\sin z\,(x-y),\quad
P_{\mu,\gamma}(y)-h\sin z\,(x-y),\quad z+x-y\right).
\]
The published input range includes \(0\le\mu\le1\). The logarithm is everywhere positive on real \(u\) in this range, because \(u(1-u)\le1/4\) and \(3-4\mu u(1-u)\ge 3-\mu\ge2\). We take \(h\in[0,1]\). There are no restrictions on the initial state coordinates. A hyperbolic sink of a primitive period-two orbit means that all eigenvalues of its two-step derivative have modulus strictly below one. Vertical translation of \(z\) by \(2\pi j\) commutes with the map; it does not identify distinct states in the full real state space, but is factored out when counting geometrically different cycles.

For \(h<1/2\), the zero-input map has **no** primitive period-two orbits. For \(h=1/2\), it has primitive period-two orbits, but each has two unit two-step multipliers and is not a hyperbolic sink. The exact count formula above applies only for \(h>1/2\).

## Proof

**1. Exact reduction and all possible two-cycles.** Introduce \(s=(x+y)/2\), \(d=x-y\), and \(C=k/\log3\). At \(\mu=0\), \(P_{0,\gamma}\equiv C\), so the map is exactly
\[
(s,d,z)\longmapsto(C,\ K\sin z\,d,\ z+d),\qquad K=2h.
\]
A primitive two-cycle must have \(s=C\) at both phases, and \(d\ne0\) (since \(d=0\) makes \(z\) fixed, while \(s\) becomes \(C\) after one step). Writing the two phases with subscripts \(0,1\), the charge equation implies \(d_1=-d_0\); the difference equation therefore requires
\[
K\sin z_0=K\sin z_1=-1,\qquad z_1=z_0+d_0.
\]
Thus no primitive two-cycle exists for \(K<1\). At \(K=1\), \(z_0,z_1\equiv-\pi/2\pmod{2\pi}\), and \(d_0\) is a nonzero multiple of \(2\pi\). For \(K>1\), put \(\theta=\arccos(1/K)\in(0,\pi/2)\), \(\rho=\sqrt{K^2-1}\). Every allowed charge belongs to one of the two congruence classes
\[
z_A=-\pi/2+\theta+2\pi j,\qquad z_B=-\pi/2-\theta+2\pi j,\qquad j\in\mathbb Z.
\]
A two-cycle is exactly a pair of *distinct* such charges, with \(d_0=z_1-z_0\), \(d_1=-d_0\), and \(x=C+d/2\), \(y=C-d/2\). This exhausts the primitive two-cycle census, including same-class pairs.

**2. Exact Floquet multipliers.** At the zero-input boundary, the derivative in \((s,d,z)\) has one vanishing multiplier and the two-dimensional block
\[
J(d,z)=\begin{pmatrix}K\sin z&Kd\cos z\\1&1\end{pmatrix}.
\]
Every phase of a two-cycle satisfies \(K\sin z=-1\). Let \(q=Kd_0\cos z_0\). If the charges belong to the same class, then \(Kd_1\cos z_1=-q\), and the two-step block is
\[
\begin{pmatrix}-1&-q\\1&1\end{pmatrix}
\begin{pmatrix}-1&q\\1&1\end{pmatrix}
=\begin{pmatrix}1-q&-2q\\0&1+q\end{pmatrix}.
\]
Here \(q\ne0\) because the charges are distinct, so at least one of \(1-q,1+q\) has modulus greater than one. Same-class cycles are never hyperbolic sinks.

If the charges belong to opposite classes, both one-step blocks coincide, because both \(d\) and \(\cos z\) change sign. With the same \(q\), their product is
\[
\begin{pmatrix}-1&q\\1&1\end{pmatrix}^{\!2}=(1+q)I_2.
\]
Hence the complete ambient two-step multiplier multiset is \(\{0,1+q,1+q\}\). Represent each opposite-class orbit by starting at \(z_A=-\pi/2+\theta\). When the second charge is \(z_B=-\pi/2-\theta-2\pi n\), \(n\ge0\), we have
\[
d_0=-2(\theta+\pi n),\quad q=-2\rho(\theta+\pi n),\quad
\lambda_n=1-2\rho(\theta+\pi n).
\]
This cycle is a hyperbolic sink **if and only if**
\[
0<\rho(\theta+\pi n)<1.
\]
For the other opposite-class pairs, with the second charge \(z_B+2\pi m\), \(m\ge1\), one gets \(q=2\rho(\pi m-\theta)>0\), hence a repeated multiplier larger than one. These alternatives together exhaust all two-cycles. The sink representatives, one per \(n\ge0\) satisfying the strict inequality, are
\[
p_n=\bigl(C-L_n/2,\ C+L_n/2,\ -\pi/2+\theta\bigr),\qquad
p'_n=\bigl(C+L_n/2,\ C-L_n/2,\ -\pi/2-\theta-2\pi n\bigr),
\quad L_n=2(\theta+\pi n).
\]
They are distinct up to phase interchange and vertical translations because the absolute charge displacement \(L_n\) is invariant under these operations and strictly increases with \(n\).

**3. Count, sharp staircase, and limiting growth.** The strict sink inequality is equivalent to
\[
n<\frac{\rho^{-1}-\theta}{\pi}.
\]
Counting nonnegative integers strictly below the right-hand side gives exactly \(N(h)\). In particular each sink threshold is the unique solution \(h_n>1/2\) of \(\sqrt{4h_n^2-1}\,(\arccos(1/(2h_n))+\pi n)=1\), and these thresholds decrease to \(1/2\). There are no hyperbolic sinks at or above the last threshold \(h_0\), characterized equivalently by \(\theta\tan\theta=1\) and \(h_0=1/(2\cos\theta)\). As \(h\downarrow1/2\), \(\rho\sim2\sqrt{h-1/2}\) and \(\theta=O(\rho)\), giving
\[
N(h)=\frac1{\pi\rho}+O(1)\sim\frac1{2\pi\sqrt{h-1/2}}.
\]
At \(K=1\), the permitted nonzero two-cycles have \(q=0\) and two unit multipliers (the third is zero), as claimed.

**4. Persistence for every finite multiplicity.** Fix any \(M\ge1\). Choose \(h\in(1/2,1)\) close enough to \(1/2\) that \(\rho(\theta+\pi(M-1))<1\). The explicit orbits \(p_0,\dots,p_{M-1}\) are then hyperbolic sinks of the three-dimensional \(F_{0,h,\gamma}\). Since \(P_{\mu,\gamma}\) depends smoothly on both \(\mu\) and the state for small nonnegative \(\mu\), and because \(D(F_{0,h,\gamma}^2)-I\) is invertible at each chosen cycle (its eigenvalues differ from one), the implicit-function theorem continues all \(M\) primitive two-cycles to every sufficiently small positive \(\mu\). Their two-step multipliers remain strictly inside the unit disk by continuity. By choosing their continuation neighborhoods disjoint, the cycles remain distinct modulo the vertical \(2\pi\) symmetry; each has an open basin by the local hyperbolic sink theorem. Taking the minimum of the finitely many persistence radii yields a common \(\varepsilon>0\). This proves the positive-input statement for arbitrary fixed \(\gamma>0\).

## Verification

The accompanying `check.py` checks the two symbolic matrix identities, the exact primitive two-cycle equations and the full three-dimensional characteristic polynomial at the first three sinks for \(2h=1.01\); it also solves the perturbed two-cycle equations at \(\mu=10^{-6}\), \(\gamma=2\) and verifies that all three continued cycles have multipliers strictly inside the unit disk. It checks finite samples of the staircase formula. These finite computations are independent diagnostics, **not** the proof of the all-parameter quantifiers; those follow from the exact reductions and the implicit-function theorem above.

## Relationship to prior work

Peng et al. introduce and numerically study this three-dimensional map, including bifurcation diagrams, Lyapunov exponents and multistability; their governing equation appears as Equation (3) and their discussion of multistability as Section 3.3. Their assertion of numerous coexisting attractors does not provide a primitive-two-cycle census, the repeated two-step multiplier formula, the coupling staircase, the inverse-square-root divergence in the number of sink classes, or a proof of arbitrarily many attracting period-two orbits at **strictly positive** input gain. The present theorem addresses that exact mathematical gap.

A related two-dimensional sine–arcsine memristor map of Xiang et al. has a different governing map and does not imply the periodic-orbit identities proved here. Broader discrete memristor literature provides motivation for multistability but not this phase-lattice calculation. No publication-priority certainty is claimed beyond the inspected sources.

## Limitations

The exact enumeration is for \(\mu=0\) and counts hyperbolically attracting primitive two-cycles modulo the exact charge translation symmetry; there are infinitely many literal vertical translates of every such orbit. At the sink threshold, the multiplier has modulus one and the nonlinear endpoint dynamics are **not classified**. The positive-input conclusion proves a lower bound for sufficiently small, potentially very small \(\mu>0\), not an exhaustive two-cycle census or a uniform persistence range as \(M\to\infty\). No claims are made about chaoticity, cryptographic security, or large-input-gain basins. The theorem is for real arithmetic, not finite-precision circuits.

## References

1. S. Peng, H. Shi, R. Li, Q. Xiang, S. Dai, Y. Li, "Simulink Modeling and Analysis of a Three-Dimensional Discrete Memristor Map," *Symmetry* **16** (2024), 990, published 2024-08-05. https://doi.org/10.3390/sym16080990 . Relevant: Equation (3), Sections 3.2–3.3 and Conclusions.
2. Q. Xiang, Y. Shen, S. Peng, M. Liu, "A Two-Dimensional Discrete Memristor Map: Analysis and Implementation," *International Journal of Bifurcation and Chaos* **34** (2024), 2450124, first published 2024-07-17. https://doi.org/10.1142/S0218127424501244 . Different map, related motivation.
3. A. Mansouri, X. Wang, "A novel one-dimensional chaotic map generator and its application in a new index representation-based image encryption scheme," *Information Sciences* **563** (2021), 91–110. https://doi.org/10.1016/j.ins.2021.02.022 . Source of scalar amplifier construction.
