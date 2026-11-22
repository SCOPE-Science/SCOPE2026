# A sharp positivity–energy gap for second-order two-sided filtered Heun on a three-site diffusion path

## Finding

Consider the second-order, two-sided filtered Heun (SSP-EIN2) method with a fixed, positive diffusion coefficient and a fixed scalar splitting coefficient. On the unweighted three-vertex path its completed timestep matrix has a **sharp all-steps entrywise-positivity boundary**, strictly stronger than its unconditional Euclidean-energy stability condition.

Define, for \(t>0\),
\[
q(t)=\frac{16t(1+t)^2}{(2+t)^4},\qquad
R(t)=\frac{2[3q(t)-q(3t)]}{3q(t)^2-q(3t)^2}
\]
where the second expression is used only when its denominator is positive. Let \(t_*\) be the unique positive root in \((3,4)\) of the polynomial \(P\) displayed in the proof, and put
\[
\rho_*=R(t_*)=1.4809208923423025557\ldots,
\quad \sigma_*=\rho_*^{-1}=0.6752555151128614852\ldots.
\]
Let \(C_2=(107+51\sqrt{17})/512=0.619684349426759\ldots\). For **every** \(a,s>0\) with \(s/a\ge C_2\), the completed SSP-EIN2 step is symmetric, mass preserving, and Euclidean nonexpansive for all \(h>0\). Within exactly this energy-stable parameter class it is entrywise nonnegative for **every** \(h>0\) if and only if
\[
\boxed{s/a\ge\sigma_*}. 
\]
At \(s/a=\sigma_*\), there is exactly one positive timestep with a zero endpoint-to-endpoint entry, namely \(h=t_*/s\). For \(C_2\le s/a<\sigma_*\), the step has a *single bounded open interval of timesteps* with a negative endpoint-to-endpoint entry, but remains Euclidean nonexpansive at every timestep. All other entries remain nonnegative. No connected graph with fewer than three vertices has this defect under the same energy-stability condition.

An exact witness is \(s=1\), \(a=3/2\), \(h=4\). Its remote-node transition is
\[
\boxed{T_{13}=-\frac{37010590}{4202539929}<0,}
\]
although \(s/a=2/3>C_2\) ensures unconditional Euclidean-energy stability.

## Assumptions and scope

Let \(L\) be the combinatorial Laplacian of the unweighted path on vertices \(1,2,3\):
\[
L=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix},
\qquad \dot u=-aLu.
\]
The splitting operator is \(S=sL\), with both \(a\) and \(s\) constant across time and stages and both positive. For \(h>0\), set
\[
J_h=(I+hS/2)^{-1},\quad H_h=2J_h-J_h^2,
\quad E_h=I-haH_hLH_h,
\quad T_h=\tfrac12(I+E_h^2).
\]
These are exactly the order-two filtered Euler stage and the completed Heun composition of the 2026 SSP-EIN2 construction for constant linear diffusion. The conclusions concern the *completed* time step, not nonnegativity of every intermediate stage, noncommuting splitting operators, nonlinear diffusion, or arbitrary graphs.

A matrix is entrywise nonnegative if every real matrix element is \(\ge0\). Its Euclidean nonexpansiveness means \(\|T_hu\|_2\le\|u\|_2\) for every vector \(u\). Set \(\rho=a/s\), \(t=sh\), and only assert the if-and-only-if classification for \(0<\rho\le C_2^{-1}\).

## Proof

**Step 1: modal amplification and energy stability.** The eigenvalues of \(L\) are \(0,1,3\); normalized eigenvectors can be chosen proportional to \((1,1,1)\), \((1,0,-1)\), and \((1,-2,1)\). On an eigenvector with eigenvalue \(\lambda\),
\[
H_h\mapsto \frac{4(1+\lambda t)}{(2+\lambda t)^2},\quad
haH_hLH_h\mapsto \rho q(\lambda t),
\quad T_h\mapsto G(\rho q(\lambda t)),
\qquad G(w)=1-w+\tfrac12w^2.
\]
The rational derivative
\[
q'(t)=-\frac{16(t+1)(t^2-3t-2)}{(t+2)^5}
\]
shows that \(q\) reaches its unique global maximum \(2C_2\) at \((3+\sqrt{17})/2\). Consequently, for \(\rho\le1/C_2\), every modal \(w=\rho q(\lambda t)\) lies in \([0,2]\), hence \(1/2\le G(w)\le1\). The constant eigenmode has amplification one. This proves all-step symmetry, mass preservation, and Euclidean contraction.

**Step 2: reduction of every entrywise inequality to one scalar inequality.** Put \(w_1=\rho q(t)\), \(w_3=\rho q(3t)\), \(g_1=G(w_1)\), \(g_3=G(w_3)\). Orthogonal spectral projection gives
\[
T_h=\begin{pmatrix}
\tfrac13+\tfrac12g_1+\tfrac16g_3 & (1-g_3)/3 & (2-3g_1+g_3)/6\\
(1-g_3)/3 & \tfrac13+\tfrac23g_3 & (1-g_3)/3\\
(2-3g_1+g_3)/6 & (1-g_3)/3 & \tfrac13+\tfrac12g_1+\tfrac16g_3
\end{pmatrix}.
\]
All entries except \(T_{13}=T_{31}\) are nonnegative by \(g_1,g_3\in[1/2,1]\). The remaining entry has the exact sign law
\[
6T_{13}=\rho[3q(t)-q(3t)]-\frac{\rho^2}{2}[3q(t)^2-q(3t)^2].\tag{1}
\]
The first bracket is strictly positive for \(t>0\), since \(4(1+t)/(2+t)^2\) decreases strictly with \(t\). Thus \(T_{13}>0\) wherever the second bracket is nonpositive. Wherever the second bracket is positive, (1) is nonnegative precisely when \(\rho\le R(t)\).

**Step 3: uniqueness of the positivity boundary.** Exact simplification gives
\[
3q(t)^2-q(3t)^2=\frac{1536t^2M(t)}{(t+2)^8(3t+2)^8},
\]
with
\[
\begin{aligned}
M(t)={}&3159t^{12}+28512t^{11}+114210t^{10}+261936t^9\\
&+363279t^8+275520t^7+28560t^6-165888t^5\\
&-179296t^4-93184t^3-26880t^2-4096t-256.
\end{aligned}
\]
Read in descending powers, its coefficient signs change exactly once. Since \(M(0)<0\) and \(M(1)>0\), Descartes' rule of signs proves a unique positive root \(t_0\in(0,1)\); the quadratic bracket in (1) is positive exactly when \(t>t_0\). In this range,
\[
R(t)=\frac{t(t+2)^4(3t+2)^4(3t+4)(6t^3+17t^2+16t+4)}{4M(t)}.
\]
Differentiation, with exact polynomial collection, gives
\[
R'(t)=\frac{(t+2)^3(3t+2)^3P(t)}{2M(t)^2},
\]
where
\[
\begin{aligned}
P(t)={}&85293t^{18}+857304t^{17}+3216348t^{16}+2103894t^{15}\\
&-30456891t^{14}-156491298t^{13}-437380110t^{12}\\
&-847556556t^{11}-1222989168t^{10}-1350183024t^9\\
&-1150054752t^8-755005824t^7-380042496t^6\\
&-145907712t^5-42588672t^4-9387008t^3\\
&-1511424t^2-159744t-8192.
\end{aligned}
\]
Again, the descending coefficient signs have one change. Since \(P(3)<0\) and \(P(4)>0\), there is exactly one positive root \(t_*\in(3,4)\), and \(R\) strictly decreases up to \(t_*\) and increases thereafter on \((t_0,\infty)\). Moreover \(R(t)\to\infty\) both as \(t\downarrow t_0\) and \(t\to\infty\). Hence \(\rho_*=R(t_*)\) is the unique global minimum. Equation (1) now proves the all-step boundary and, when \(\rho_*<\rho\le1/C_2\), exactly one bounded open negativity window. Equality gives one isolated zero, and below the threshold every entry is strictly positive at positive time.

**Step 4: exact witness and minimality.** At \(t=4\), \(\rho=3/2\), exact rational substitution gives \(w_1=50/27\), \(w_3=3042/2401\), and \(T_{13}=-37010590/4202539929\). Since \(\frac23>C_2\), this is inside the energy-stable region. For any connected two-vertex graph, only a constant mode and one nonzero mode occur. The mode contraction \(g\in[1/2,1]\) then gives the step matrix \(\frac12\begin{pmatrix}1+g&1-g\\1-g&1+g\end{pmatrix}\), which is entrywise nonnegative; a one-vertex graph is trivial. Thus three vertices are minimal among connected simple graphs in this class.

## Verification

Run `python verify.py` with Python 3, SymPy, NumPy and SciPy. The code recomputes the modal symbol, rational factor identities, both sign-variation certificates, the exact negative entry and a direct rational matrix-resolvent composition; it also checks numerical root isolation and 2,000 sampled parameter-step matrices as nonproof diagnostics. Proof of the global infimum uses the explicit Descartes and endpoint arguments above, not a sampled parameter grid. The source-to-specialization correspondence is Section 3.1 equations (3.6), (3.13), and Section 3.2 Example 3.2 (3.39).

## Relationship to prior work

Wu and Shu (2026), arXiv:2611.02282, introduce the high-order two-sided filter, its SSP-EIN2 composition, and the sharp universal **energy** splitting factor \(C_2\); those formulas and the contraction bound are pre-existing. The present result asks the different question whether the completed map preserves the **coordinatewise nonnegative cone** on the smallest connected symmetric diffusion path. The exact larger ratio \(\sigma_*\) and its one-window phase structure are not stated in the source. Their earlier 2026 paper arXiv:2610.34539 develops different, IMEX-based nonlinear energy estimates, not the same two-sided filtered Heun map. Horváth (1998) treats general positivity criteria for RK and diagonally split schemes but does not establish this specialized 2026 filtered-operator boundary. Other published graph-heat positivity classifications for Padé and Radau IIA methods concern distinct stability functions and do not imply this value or polynomial.

## Limitations

The classification is for one fixed constant-coefficient, three-vertex symmetric path and the all-step Euclidean-contractivity regime. It is **not** a universal lower bound for arbitrary graphs, noncommuting or state-dependent operators, and it says nothing about intermediate stage positivity. A general contractivity guarantee does not imply positivity, as shown, but another discretization may preserve both. Numerical constants are approximations to the exact algebraic definitions. Historical priority is qualified by imperfect indexing of older positivity literature and possible equivalent formulations; independent review has not been performed.

## References

1. Y. Wu and C.-W. Shu, *Unconditionally \(L^2\)-stable explicit–implicit–null filtered Runge–Kutta methods for general nonlinear degenerate parabolic equations*, arXiv:2611.02282v1, first submitted 2026-11-01, https://arxiv.org/abs/2611.02282.
2. Y. Wu and C.-W. Shu, *Energy stability of explicit–implicit–null time discretizations for nonlinear degenerate parabolic equations with state-dependent coefficients*, arXiv:2610.34539v1, first submitted 2026-10-25, https://arxiv.org/abs/2610.34539.
3. Z. Horváth, *Positivity of Runge–Kutta and diagonally split Runge–Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326, https://doi.org/10.1016/S0168-9274(98)00050-6.
4. S. Gottlieb, C.-W. Shu, and E. Tadmor, *Strong stability-preserving high-order time discretization methods*, SIAM Review 43 (2001), 89–112, https://doi.org/10.1137/S003614450036757X.
