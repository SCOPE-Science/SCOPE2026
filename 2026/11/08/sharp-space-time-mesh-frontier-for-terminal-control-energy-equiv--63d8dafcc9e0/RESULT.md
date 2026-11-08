# Sharp space–time mesh frontier for terminal control-energy equivalence of theta heat schemes

## Finding

For fully distributed minimum-energy steering of the one-dimensional heat equation on *the same finite-difference spatial grid*, the full-family equivalence between the theta-discrete and continuous-time terminal-control energies has a sharp two-parameter boundary. Write \(m\ge2\) for the number of spatial subintervals, \(k_m=T/N_m\) for the time step, and \(\theta_m\in[1/2,1]\). Under \(N_m\to\infty\) and fixed \(T>0\), define \(\lambda_{\max,m}=4m^2\cos^2(\pi/(2m))\). There exist constants \(0<c<C<\infty\), independent of \(m\), such that

\[
cW_m^{\mathrm{cts}}\preceq W_m^{\theta}\preceq CW_m^{\mathrm{cts}}
\]

for every grid if and only if

\[
\sup_m \lambda_{\max,m}k_m^2<\infty,
\qquad
\sup_m(2\theta_m-1)\lambda_{\max,m}k_m<\infty.
\]

Equivalently, \(k_m=O(m^{-1})\) and \((2\theta_m-1)k_m=O(m^{-2})\). For fixed Crank–Nicolson weight \(\theta=1/2\) this allows \(k_m=O(m^{-1})\), while any fixed \(\theta>1/2\) requires \(k_m=O(m^{-2})\). It is a statement about **uniform equivalence** of minimal terminal-control energies, not their convergence to equality.

More precisely, put

\[
a_m=(2\theta_m-1)\lambda_{\max,m}k_m,
\qquad b_m=\lambda_{\max,m}k_m^2.
\]

If these parameters have finite limits \(a,b\ge0\), the ratio of the discrete and exact controllability Gramians in the highest spatial-frequency mode converges to

\[
\mathcal F_T(a,b)=
\begin{cases}
\displaystyle \frac{2}{2+a}\left(1-e^{-4T(2+a)/b}\right), & b>0,\\
\displaystyle \frac{2}{2+a}, & b=0.
\end{cases}
\]

If \(a_m\to\infty\), the same ratio vanishes; if \(b_m\to\infty\) while \(a_m\) stays bounded, it also vanishes. These statements supply explicit high-frequency targets whose relative minimal discrete control energy diverges when the equivalence conditions fail.

## Assumptions and scope

Fix \(T>0\) and, for every integer \(m\ge2\), set \(h=1/m\), define the Dirichlet second-difference positive operator on \(m-1\) interior nodes,

\[
L_m=m^2\begin{pmatrix}
2&-1&&\\[-3pt]
-1&2&\ddots&\\[-3pt]
&\ddots&\ddots&-1\\[-3pt]
&&-1&2
\end{pmatrix},\qquad
\langle v,w\rangle_m=h\sum_{j=1}^{m-1}v_jw_j.
\]

(The displayed matrix has the usual one-by-one interpretation at \(m=2\).) The eigenvalues are

\[
\lambda_{j,m}=4m^2\sin^2\!\left(\frac{j\pi}{2m}\right),
\quad 1\le j\le m-1,
\quad\lambda_{1,m}\ge4,
\quad\lambda_{m-1,m}=\lambda_{\max,m}\asymp m^2.
\]

The reference dynamics are \(\dot y=-L_my+u(t)\), \(y(0)=0\), with \(\int_0^T\|u(t)\|_m^2\,dt\) minimized subject to \(y(T)=d\). The numerical dynamics are

\[
(I+\theta_m k_mL_m)y^{n+1}=(I-(1-\theta_m)k_m L_m)y^n+k_m u^{n+1},
\qquad k_m=T/N_m,
\]

with \(y^0=0\), \(N_m\) positive integers tending to infinity, and cost \(k_m\sum_{n=1}^{N_m}\|u^n\|_m^2\). Both are fully actuated: there is an independent control value at each spatial node. In either model every finite-dimensional terminal target is reachable. If \(W\) denotes the respective positive-definite endpoint Gramian, its minimum energy (without a factor \(1/2\)) is \(\langle d,W^{-1}d\rangle_m\).

## Proof

**1. Exact modal Gramians.** For a spatial eigenvalue \(\lambda>0\), abbreviate \(k=k_m\), \(\theta=\theta_m\), \(z=\lambda k\), \(\alpha=2\theta-1\ge0\). The scalar transition factor and control coefficient are

\[
r=\frac{1-(1-\theta)z}{1+\theta z},\qquad
p=\frac{k}{1+\theta z}.
\]

Since \(\theta\ge1/2\) and \(z>0\), \(|r|<1\). Cauchy–Schwarz in the time-weighted control space gives the discrete modal endpoint Gramian \(W_\theta(\lambda)=\sum_{i=0}^{N-1}p^2r^{2i}/k\). The elementary identity

\[
1-r^2=\frac{z(2+\alpha z)}{(1+\theta z)^2}
\]

gives the exact finite-horizon expression

\[
W_\theta(\lambda)=\frac{1-r^{2N}}{\lambda(2+\alpha\lambda k)}.
\]

For continuous semidiscrete time, direct integration gives \(W_0(\lambda)=(1-e^{-2\lambda T})/(2\lambda)\). Therefore the exact ratio is

\[
F(\lambda;k,\theta,N)=\frac{W_\theta(\lambda)}{W_0(\lambda)}=
\frac{2}{2+\alpha\lambda k}
\frac{1-r^{2N}}{1-e^{-2\lambda T}}.
\tag{1}
\]

Both full Gramians share the orthogonal eigenbasis of \(L_m\) in the \(h\)-weighted inner product. Thus uniform spectral equivalence is exactly uniform lower and upper bounds on all instances of \(F\).

**2. Sufficiency, with explicit uniform bounds.** Let \(B_1=\sup_m\alpha_m\lambda_{\max,m}k_m<\infty\) and \(B_2=\sup_m\lambda_{\max,m}k_m^2<\infty\). For every spatial mode \(\lambda\le\lambda_{\max,m}\),

\[
1-r^2=\frac{\lambda k(2+\alpha\lambda k)}{(1+\theta\lambda k)^2}
\ge\frac{2\lambda k}{(1+\lambda k)^2}.
\]

Use \(r^{2N}\le\exp[-N(1-r^2)]\), \(Nk=T\), \(\lambda\ge4\), and \(k\le T\), to obtain

\[
N(1-r^2)\ge\frac{2T}{1/\lambda+2k+\lambda k^2}
\ge\frac{2T}{1/4+2T+B_2}.
\]

Then (1) yields, uniformly in spatial mode and grid,

\[
\frac{2}{2+B_1}\left(1-e^{-2T/(1/4+2T+B_2)}\right)
\le F\le\frac{1}{1-e^{-8T}}.
\]

Both constants are positive and finite for fixed \(T\). This proves sufficiency.

**3. Necessity.** Evaluate the highest eigenmode \(\lambda=\lambda_{\max,m}\to\infty\) and set \(a_m=\alpha_m\lambda k\), \(b_m=\lambda k^2\). If \(a_m\to\infty\) along a subsequence, (1) implies \(F\le2/[(2+a_m)(1-e^{-8T})]\to0\). If \(b_m\to\infty\) along a subsequence and \(a_m\) is bounded there, use \(1-r^{2N}\le N(1-r^2)\), and \(\theta\ge1/2\), to obtain

\[
1-r^{2N}\le\frac{T\lambda(2+a_m)}{(1+\theta\lambda k)^2}
\le\frac{4T(2+a_m)}{b_m}\longrightarrow0.
\]

Equation (1) then yields \(F\to0\). For any unbounded \(a_m+b_m\), a subsequence satisfies one of these cases. Thus there cannot be a uniform positive lower Gramian bound, and the ratio of discrete to exact minimum-energy costs for normalized highest-mode targets diverges. Since \(\lambda_{\max,m}\asymp m^2\), the claimed mesh conditions follow.

**4. Exact critical two-parameter profile.** Suppose \(a_m\to a<\infty\) and \(b_m\to b\in[0,\infty)\), with \(k_m\to0\). If \(b=0\), then \(N(1-r^2)\ge2T/(1/\lambda+2k+b_m)\to\infty\), hence \(r^{2N}\to0\). If \(b>0\), then \(z=\lambda k=b_m/k\to\infty\) and

\[
r=\frac{2+a_m-z}{2+a_m+z},\qquad
N\log(r^2)=\frac{T}{k}\left[-\frac{4(2+a_m)}{z}+O(z^{-2})\right]
\longrightarrow -\frac{4T(2+a)}{b}.
\]

Here the remainder after multiplying by \(1/k\) tends to zero because \(z\asymp1/k\). Substitution into (1) and \(e^{-2\lambda T}\to0\) gives \(\mathcal F_T(a,b)\).

**5. Illustrations.** With \(T=1\), \(k_m=1/m\), and Crank–Nicolson \(\theta=1/2\), \((a_m,b_m)\to(0,4)\), giving a highest-mode Gramian ratio \(1-e^{-2}\approx0.8646647168\). For backward Euler \(\theta=1\), \(k_m=1/m^2\), the limit is \((a_m,b_m)\to(4,0)\) and the ratio is \(1/3\). With \(k_m=1/m\) and \(\theta_m=1/2+1/m\), the limit is \((8,4)\) and the ratio is \((1-e^{-10})/5\). (These examples use integer \(N_m=T/k_m\).)

## Verification

The accompanying standalone `verify.py` checks 72 exact-rational scalar geometric-Gramian identities, numerical high-mode limits, the two mechanisms of Gramian-ratio collapse, and exact finite-horizon minimum-energy control identities for rational examples. Run `python3 verify.py` from a directory containing this file. Its successful output begins `VERIFY_OK 108`; this finite verification supplements the four analytic proof steps above. The arguments proving all mesh sizes and all admissible sequences are not finite experiments.

## Relationship to prior work

Kwon and Nunda (arXiv:2610.40461v1, §3) study finite-difference Crank–Nicolson soft-to-hard terminal penalization, checking refinement primarily with a first-eigenmode target. Their paper motivates testing simultaneous mesh limits, but does not state a uniform, all-terminal-mode controllability-cost criterion or the critical two-parameter law.

Boyer and Hernández-Santamaría (Numerische Mathematik, 2025/2026, §5.2, equation (160)) already give the infinite-horizon theta-scheme moment kernel \(1/[\lambda+\lambda'+(2\theta-1)\tau\lambda\lambda']\) for boundary-controllability analysis. In particular, its diagonal denominator agrees with the infinite-horizon factor \(1/[\lambda(2+(2\theta-1)\lambda k)]\) here, and that algebraic factor is **not claimed new**. Their formulation concerns boundary controls and filtered spectral moment methods, rather than the full-actuation finite-horizon mesh-uniform equivalence and two-parameter high-mode limit proved here.

Boyer, Hubert, and Le Rousseau (Numerische Mathematik, 2011) address space/time-discrete parabolic controllability and theta schemes with relaxed observability. Full article access was unavailable during source comparison; accessible author presentation material and the abstract were reviewed, leaving historical-priority risk rather than establishing non-coverage of their full text.

## Limitations

This result requires homogeneous Dirichlet centered differences, self-adjoint positive spatial operators with the stated spectrum, zero initial state, fixed horizon, fully distributed independent nodal controls, and the specified theta right-hand-side forcing. It compares discrete and exact **semidiscrete** minimum-energy costs on each grid, not equality or convergence to continuum infinite-dimensional control costs. It does not establish estimates for a proper subset of control nodes, boundary actuation, nonlinear dynamics, other control discretizations, rounding error, or convergence of an optimization solver. The unavailable full 2011 article and possible unindexed classical spectral-control results leave a qualified novelty risk.

## References

1. S.-S. Kwon and M. Nunda, “Numerical Investigation of Soft-to-Hard Convergence: Discretization, Admissibility, and Spectral Regularity,” arXiv:2610.40461v1 (29 October 2026), https://arxiv.org/html/2610.40461v1 .
2. F. Boyer and V. Hernández-Santamaría, “Boundary controllability of time-discrete parabolic systems: a moments method approach,” *Numerische Mathematik* (first published 18 November 2025), §5.2, https://doi.org/10.1007/s00211-025-01484-5 .
3. F. Boyer, F. Hubert and J. Le Rousseau, “Uniform controllability properties for space/time-discretized parabolic equations,” *Numerische Mathematik* 118 (2011), 601–661, https://doi.org/10.1007/s00211-011-0368-1 .
