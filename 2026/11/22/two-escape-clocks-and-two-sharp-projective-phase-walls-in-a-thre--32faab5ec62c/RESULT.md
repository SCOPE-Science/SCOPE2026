# Two escape clocks and two sharp projective phase walls in a three-dimensional quadratic Hénon map

## Finding
Let
\[
F_{a,b}(x,y,z)=(a-y^2-bz,x,y),\qquad a,b\in\mathbb R,\quad b\ne0.
\]
For every parameter pair there exists a nonempty open set of real initial conditions whose forward orbits escape superexponentially, and two positive continuous functions \(H_o,H_e\) on that set with the following sharp laws. Writing \(x_n\) for the first coordinate of \(F_{a,b}^n\),
\[
\log|x_{2m+1}|=2^mH_o+o(1),\qquad
\log|x_{2m+2}|=2^mH_e+o(1)\quad(m\to\infty).
\]
The values \(x_n\) are negative for all sufficiently large \(n\). Define \(r=H_e/H_o\) and \(u_n=F^n(x_0,y_0,z_0)/\|F^n(x_0,y_0,z_0)\|_2\). Then
\[
\lim_{m\to\infty}u_{2m+2}=
\begin{cases}
(0,-1,0)&r<1,\\
(-1,-1,0)/\sqrt2&r=1,\\
(-1,0,0)&r>1,
\end{cases}
\]
and
\[
\lim_{m\to\infty}u_{2m+3}=
\begin{cases}
(-1,0,0)&r<2,\\
(-1,-1,0)/\sqrt2&r=2,\\
(0,-1,0)&r>2.
\end{cases}
\]
All five phase regimes \(r<1\), \(r=1\), \(1<r<2\), \(r=2\), and \(r>2\) occur for this same fixed parameter pair. The three strict regimes contain nonempty open sets, and the two equality regimes are nonempty level sets of continuous escape-height functions.

## Assumptions and scope
The map is a real polynomial diffeomorphism for \(b\ne0\). For a constructive choice of escaping initial conditions, write \(L=\log R\) and choose \(R>1\), sufficiently large depending only on \((a,b)\). Define an open seed chamber
\[
\mathcal U_R=\{(X_0,X_1,X_2):R^{0.9}<X_0<R^{1.1},\ 
R^{0.99}<X_1<R^{1.01},\ R^{0.78}<X_2<R^{2.30}\}.
\]
For each seed triple define the initial state uniquely by
\[
(x_0,y_0,z_0)=\left(X_0,\frac{a-X_0^2-X_2}{b},
\frac{a-[(a-X_0^2-X_2)/b]^2-X_1}{b}\right).
\]
The first three scalar coordinates of its forward orbit are precisely \((x_0,x_1,x_2)=(X_0,X_1,X_2)\). Because the seed-to-state map is a polynomial diffeomorphism, its image is open and nonempty. No claim is made about every unbounded orbit or about the boundaries of the full bounded-orbit set.

## Proof
**1. Two-step recurrence.** The map satisfies \((x_n,y_n,z_n)=(x_n,x_{n-1},x_{n-2})\) for \(n\ge2\), hence
\[
x_{n+1}=a-x_{n-1}^2-bx_{n-2}\qquad(n\ge2).
\]
Set \(s_n=\log|x_n|\) wherever \(x_n\ne0\), and
\[
\delta_n=\frac{b x_{n-2}-a}{x_{n-1}^2}.
\]
Thus \(x_{n+1}=-x_{n-1}^2(1+\delta_n)\). When \(|\delta_n|<1/4\), the next coordinate is negative and
\[
s_{n+1}=2s_{n-1}+e_n,\qquad e_n=\log(1+\delta_n).
\]

**2. Uniform invariant logarithmic cone.** We claim, for every integer \(m\ge0\),
\[
0.96\,2^mL\le s_{2m+1}\le1.04\,2^mL,
\qquad0.74\,2^mL\le s_{2m+2}\le2.34\,2^mL.
\]
The seed restrictions satisfy these inequalities strictly at \(m=0\). If the bounds hold up through a step, the term \(b x_{n-2}\) is exponentially smaller than \(x_{n-1}^2\): for \(n=2\), the logarithmic gap is at least \((2\cdot0.96-1.1)L=0.82L\); for \(n=2m+2\), \(m\ge1\), it is at least \((2\cdot0.96-2.34/2)2^mL=0.75\cdot2^mL\); and for \(n=2m+3\) it is at least \((2\cdot0.74-1.04)2^mL=0.44\cdot2^mL\). The constant \(a\) contributes a still smaller term. Consequently, with \(K=|a|+|b|\),
\[
|\delta_{2m+2}|,\ |\delta_{2m+3}|\le K e^{-0.4\,2^mL}\quad(m\ge0).
\]
Take \(R\) so large that the right side is below \(1/4\) and every \(|e_{2m+2}|,|e_{2m+3}|\le 2K e^{-0.4\,2^mL}\le0.01L\). The recurrence gives
\[
\left|2^{-m}s_{2m+1}-s_1\right|\le\sum_{j=0}^{m-1}2^{-j-1}|e_{2j+2}|\le0.01L,
\]
with the identical bound for even indices around \(s_2\). Therefore the provisional bands improve to \([0.98,1.02]\) and \([0.77,2.31]\) (after division by \(2^mL\)), strictly inside the claimed bands. Induction closes, all terms remain nonzero, and all coordinates generated after the first three are strictly negative.

**3. Exact escape heights and remainder.** By the recurrence,
\[
H_o=s_1+\sum_{j=0}^{\infty}2^{-j-1}e_{2j+2},\qquad
H_e=s_2+\sum_{j=0}^{\infty}2^{-j-1}e_{2j+3}.
\]
Both series converge uniformly on the chamber because \(|e_{2j+k}|\le2K\exp(-0.4\,2^jL)\); each height is positive, continuous, and differs from its seed logarithm by at most \(0.01L\). Subtracting the finite partial sums yields
\[
s_{2m+1}-2^mH_o=-\sum_{j=m}^{\infty}2^{m-j-1}e_{2j+2}=o(1),
\]
and the corresponding even-index identity. Notice the \(o(1)\) error is additive **in the logarithm**, rather than merely relative to the divergent leading term.

**4. Sharp phase walls and existence.** The third coordinate of the state is \(x_{n-2}\). For even \(n=2m+2\), its logarithm is asymptotic to \(2^{m-1}H_e\), while the first and second coordinate logarithms are asymptotic to \(2^mH_e\) and \(2^mH_o\). For odd \(n=2m+3\), the three analogous rates are \(2^{m+1}H_o\), \(2^mH_e\), and \(2^mH_o\). The strict inequalities yield the axis limits. At each equality, logarithmic differences tend to zero; since all relevant coordinates are eventually negative, their absolute-value ratios tend to one and the normalized limit is the negative coordinate bisector.

Fix \(X_0=X_1=R\) and vary \(X_2=R^q\) continuously for \(q\in[0.8,2.25]\). The height estimates give \(|H_o-L|\le0.01L\) and \(|H_e-qL|\le0.01L\). Hence the continuous ratio \(r\) is below \(1\) at \(q=0.8\) and above \(2\) at \(q=2.25\), and takes the two critical values by the intermediate-value theorem. Continuity gives open chambers for the three strict regimes. This completes the proof.

## Verification
The standalone `checker.py` regenerates the seed-to-state reconstruction for rational parameters, compares scalar and full-map iterates exactly, verifies large-seed dominance and the negative signs, and computes finite partial-height estimates in several parameter regimes. These finite tests check algebra and selected numerical behavior; the invariant logarithmic cone, uniform convergence and the critical-level existence are established analytically above, not certified by finite iteration.

## Relationship to prior work
Muni's 2024 study introduces the exact three-dimensional generalized Hénon map and investigates bounded attractors, periodic saddles, Lyapunov exponents, and routes to hyperchaos. The present theorem instead concerns the previously unquantified escape geometry at infinity. Hampton and Meiss (2022) study three-dimensional generalized Hénon bifurcations and attractors. Published same-map results on primitive two-cycle stability and a dimension-general fixed-point recurrence threshold concern bounded dynamics or global recurrence rather than two distinct parity escape clocks and their projective walls. General Böttcher-coordinate and escaping-set literature provides broader context, but its available formulations do not give these explicit real three-dimensional parity phase regimes. Exact priority relative to all unindexed or inaccessible works is not asserted.

## Limitations
The theorem constructs a specific nonempty open escape region, not the full escaping set; it does not classify bounded dynamics, invariant measures, or other infinity channels. Equality-level sets are shown nonempty and continuous, not proved smooth or codimension one. The result is an analytic classification within the stated logarithmic cone; finite checks are not substitutes for the inductive estimates. Independent verification remains unperformed.

## References
1. S. S. Muni, *Pathways to hyperchaos in a three-dimensional quadratic map*, arXiv:2406.08317v1 (2024-06-12), Section 2, equation (2.1). https://arxiv.org/abs/2406.08317
2. A. E. Hampton and J. D. Meiss, *Visualizing Attractors of the Three-Dimensional Generalized Hénon Map*, arXiv:2206.07855 (2022). https://arxiv.org/abs/2206.07855
3. A. E. Hampton and J. D. Meiss, *Connecting Anti-integrability to Attractors for Three-Dimensional, Quadratic Diffeomorphisms*, arXiv:2305.06302 (2023). https://arxiv.org/abs/2305.06302
4. K. Ueno, *Newton polygons and Böttcher coordinates near infinity for polynomial skew products*, Dynamical Systems 40 (2025), 346–374. https://doi.org/10.1080/14689367.2025.2459088
