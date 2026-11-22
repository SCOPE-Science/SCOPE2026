# Global synchronization in a nested delayed-logistic coupling near gain four

## Finding
Let \(g(t)=t(1-t)[1-t(1-t)]\). For every real \(a\in[399/100,4]\), consider the four-dimensional delayed recurrence
\[
\begin{aligned}
x_{n+1}&=[a+(4-a)\min(x_{n-1},x_n)]g(y_n),\\
y_{n+1}&=[a+(4-a)\min(y_{n-1},y_n)]g(x_n).
\end{aligned}
\]
For any \(x_{-1},x_0,y_{-1},y_0\in(0,1)\), both coordinate sequences converge to the **same** equilibrium \(s_a\in(13/20,71/100)\), which is the unique positive interior equilibrium and is characterized by
\[
s_a=[a+(4-a)s_a]s_a(1-s_a)[1-s_a(1-s_a)].
\]
Every such orbit enters the four-coordinate box \([13/20,71/100]^4\) after a finite initial-condition-dependent time. On this box, the **second iterate of the four-dimensional state map** is a strict contraction in the sup norm with factor at most \(991/1000\). Thus convergence is exponential after entry; in the strictly positive open state cube there are no nonconstant periodic orbits and no invariant Borel probability measures other than the point mass at the synchronized equilibrium.

## Assumptions and scope
All iterates are computed with exact real arithmetic. The gain is fixed along an orbit, \(399/100\le a\le4\). The initial four coordinates are strictly between zero and one; boundary states are excluded. The model is the **explicit compositional instantiation** of Huang, Deng, Liu and Li's 2023 framework: apply their logistic seed \(f(t,p)=pt(1-t)\) to their state control \(h(t)=t(1-t)\), with coefficient control \(a+(4-a)\min(\text{previous},\text{current})\). It follows algebraically from their equations (3), (5), (6) and (7). The separately printed equation (8) is not algebraically identical as rendered; accordingly the theorem is **not** asserted for a different literal reading of (8) or for an unknown software implementation. This scope distinction is essential.

## Proof
**1. Positive invariance and escape from the small-state region.** Put \(u=t(1-t)\), so \(0<u\le1/4\) when \(0<t<1\), and hence \(0<g(t)=u(1-u)\le3/16\). Since each coefficient lies in \([399/100,4]\), the next coordinates are in \((0,3/4]\). For \(0<t\le1/4\),
\[
\frac{(399/100)g(t)}t=(399/100)(1-t)[1-t(1-t)]
\ge(399/100)(3/4)(13/16)>12/5.
\]
For \(t\in[1/4,3/4]\), \(t(1-t)\in[3/16,1/4]\), and monotonicity of \(u(1-u)\) on that range yields
\[
(399/100)g(t)\ge(399/100)(39/256)=15561/25600>3/5.
\]
For \(n\ge1\) write \(m_n=\min(x_n,y_n)>0\). The two estimates imply
\[
m_{n+1}\ge\min\{(12/5)m_n,3/5\}.
\]
It follows that eventually \(m_n\ge1/4\). From that point \([1/4,3/4]^2\) is forward invariant and one further iterate lies in \([15561/25600,3/4]^2\).

**2. Exact absorbing-box certificate.** On \([1/2,3/4]\), the polynomial \(g\) is decreasing. Starting with the outward-rounded rational interval \([607851/10^6,750000/10^6]\), apply five times the bounds
\[
\ell_{j+1}=10^{-6}\big\lfloor10^6(399/100)g(u_j)\big\rfloor,
\qquad
u_{j+1}=10^{-6}\big\lceil10^6\,4g(\ell_j)\big\rceil.
\]
All calculations are rational. The lower and upper numerators, always over \(10^6\), are:

| Step \(j\) | Lower numerator | Upper numerator |
|---:|---:|---:|
| 0 | 607851 | 750000 |
| 1 | 607851 | 726196 |
| 2 | 635606 | 726196 |
| 3 | 635606 | 711870 |
| 4 | 650531 | 711870 |
| 5 | 650531 | 702628 |

Therefore both coordinates enter \([13/20,71/100]\), then after one more step all four current-and-delayed coordinates are in \(K=[13/20,71/100]^4\). The bounds
\[
(399/100)g(71/100)>13/20,
\qquad 4g(13/20)<71/100
\]
prove that \(K\) is forward invariant.

**3. Uniform two-step contraction.** Differentiation gives \(g'(t)=(1-2t)(1-2t+2t^2)\). On \([13/20,71/100]\), its absolute value is increasing, so
\[
4\max |g'(t)|=4(42/100)(1-142/100+2(71/100)^2)
=988176/10^6.
\]
Since \(\min\) is one-Lipschitz for the sup norm, the difference of one updated coordinate from two states in \(K\) is bounded by
\[
\frac{988176}{10^6}\,\delta_n
+\frac{3}{1600}\max(\delta_{n-1},\delta_n),
\]
where \(\delta_n=\max(|x_n-\tilde x_n|,|y_n-\tilde y_n|)\). Thus
\[
\delta_{n+1}\le\frac{990051}{10^6}
\max(\delta_{n-1},\delta_n)
<\frac{991}{1000}\max(\delta_{n-1},\delta_n).
\]
Applying this twice shows that the square of the delayed state map contracts \(K\) in sup norm by at most \(991/1000\).

**4. Unique synchronized limit.** The Banach fixed-point theorem gives a unique fixed point of the second iterate on \(K\). Because the original state map commutes with its square, it fixes that unique point. Swapping the two coordinate histories also commutes with the map and preserves \(K\), so the unique fixed point must be synchronized, of the form \((s_a,s_a,s_a,s_a)\). The fixed-point equation in the statement follows. All strictly positive initial states eventually enter \(K\), proving global convergence. Any strictly positive periodic orbit would eventually enter \(K\) and thus must equal this fixed point. If \(\mu\) is any invariant Borel probability supported on the open positive state cube, invariance and pointwise convergence imply \(\int\psi\,d\mu=\psi(s_a,s_a,s_a,s_a)\) for every bounded continuous \(\psi\), so \(\mu\) is the claimed Dirac measure.

## Verification
Run `python checker.py` in the same directory. Its standard-library exact-rational computations verify the five outward-rounded interval transitions, the strict invariant-box inequalities, the derivative and delayed-feedback coefficient, and endpoint signs for the fixed-point equation. It additionally performs 360 floating-point orbit sanity checks, which are supplementary and are **not** used to prove the universal statement. The mathematical proof relies on the exact rational inequalities plus the standard contraction theorem; the checker alone is not an infinite-orbit proof.

## Relationship to prior work
Huang, Deng, Liu and Li (2023) give the delayed-coupling scheme and its logistic/state-control formulas and report numerical chaotic behavior for their equation (8), using \(a=3.99\) in examples. The present result concerns the mathematically explicit *composition* of their equations (3), (5)–(7); it provides a global synchronization theorem that is not established in the inspected source. Because the article's printed equation (8) does not render the same algebraic composition, no implication about their software trajectories is claimed. Cánovas (2022) treats convex mixtures of two ordinary logistic maps without the nested state control or delayed gain. Bosisio, Naimzada and Pireddu (2024) prove chaos for an additively coupled planar logistic system without this state control or delay. Neither model implies the theorem here.

## Limitations
The threshold \(399/100\) is a convenient rigorously certified interval endpoint, **not** an optimal bifurcation threshold. Entry time into the absorbing box is not uniform over initial states arbitrarily close to the coordinate boundary. The theorem is about exact-real dynamics of the explicitly written four-dimensional recurrence, not floating-point simulation, cryptographic security, or any differently interpreted formula. Boundary equilibria and boundary invariant measures are excluded from the uniqueness claim. Publication priority outside the inspected sources is not independently certified.

## References
1. S. Huang, G. Deng, L. Liu and X. Li, *Technique for Enhancing the Chaotic Characteristics of Chaotic Maps Using Delayed Coupling and Its Application in Image Encryption*, Mathematics **11** (2023), 3295, https://doi.org/10.3390/math11153295. Online publication date: 2023-07-26.
2. J. S. Cánovas, *The dynamics of coupled logistic maps*, Networks and Heterogeneous Media **18** (2023), 275–290, first published 2022-12-20, https://doi.org/10.3934/nhm.2023010.
3. A. Bosisio, A. Naimzada and M. Pireddu, *Proving chaos for a system of coupled logistic maps: A topological approach*, Chaos **34** (2024), 033112, https://doi.org/10.1063/5.0175789.
