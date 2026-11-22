# Universal exact-mean random Lie order for two-state Markov generators, with a sharp three-state obstruction

## Finding

**Theorem.** Let \(A,B\) be arbitrary conservative two-state continuous-time Markov generators, under the row-vector convention,
\[
A=\begin{pmatrix}-a&a\\b&-b\end{pmatrix},\qquad
B=\begin{pmatrix}-c&c\\d&-d\end{pmatrix},
\]
with \(a,b,c,d\ge0\), \(s=a+b>0\), \(t=c+d>0\). For every \(h>0\), put \(u=e^{-sh}\), \(v=e^{-th}\) and
\[
\boxed{q_{s,t}(h)=
\frac{\frac{s}{s+t}(1-uv)-v(1-u)}{(1-u)(1-v)}\in(0,1).}
\]
Randomly perform the reverse-order step \(e^{hB}e^{hA}\) with probability \(q_{s,t}(h)\), or the forward-order step \(e^{hA}e^{hB}\) otherwise. The expected step is **exactly** the full Markov semigroup:
\[
\boxed{(1-q_{s,t}(h))e^{hA}e^{hB}+q_{s,t}(h)e^{hB}e^{hA}=e^{h(A+B)}.}
\]
The weight is universal across all individual rates having the given exit-rate sums \(s,t\). If \(A,B\) do not commute, it is the *unique* order probability with this property; if they commute, either step is already exact. Moreover,
\[
q_{s,t}(h)=\frac12+\frac{s-t}{12}h+O(h^3)\quad(h\downarrow0),
\qquad \lim_{h\to\infty}q_{s,t}(h)=\frac{s}{s+t}.
\]

With independent fresh order choices at each step, for any deterministic initial row probability vector and every integer \(n\ge1\), the ensemble mean is exactly the time-\(nh\) Markov solution. Write \(\pi_A=b/s\), \(\pi_B=d/t\), \(r=e^{-(s+t)h}\), and \(\Delta=(1-u)(1-v)(\pi_A-\pi_B)\). The exact Euclidean mean-square vector error is
\[
\boxed{\mathbb E\|P_n-p_0e^{nh(A+B)}\|_2^2
=2q_{s,t}(h)(1-q_{s,t}(h))\Delta^2\frac{1-r^{2n}}{1-r^2},}
\]
where \(P_n\) is the **random propagated probability row vector**, not the matrix product itself. For a fixed horizon \(T=nh>0\), as \(h\downarrow0\) through such grids and for noncommuting \(A,B\), this error equals
\[
\frac{s^2t^2(\pi_A-\pi_B)^2}{4(s+t)}
(1-e^{-2(s+t)T})h^3+o(h^3).
\]

**Sharp dimension boundary.** In dimension three, no analogous universal two-order exact-mean principle holds. Specifically, for
\[
A_3=\begin{pmatrix}-1&1&0\\1&-1&0\\0&0&0\end{pmatrix},\qquad
B_3=\begin{pmatrix}0&0&0\\0&-1&1\\0&0&0\end{pmatrix},
\]
no affine combination (even with real, nonprobability coefficients summing to one) of the two ordered exponentials agrees with \(e^{h(A_3+B_3)}\) for **any** \(h>0\). Thus two states are the largest state-space size for which all conservative generator pairs have the exact positive two-order mixture property.

## Assumptions and scope

Rows are probability vectors; stochastic matrices have row sums one. All individual off-diagonal rates are nonnegative. Both total exit rates \(s,t\) are strictly positive and \(h>0\); reducible one-way generators are permitted. If one generator is zero, either product equals the exact exponential and order probabilities are irrelevant. The random choices are independent across steps, both subflows use the *full* length \(h\), and their individual matrix exponentials are evaluated exactly. The analysis concerns ensemble mean, finite-horizon mean-square error, and a dimension-three obstruction. It does not identify an exact sample-path CTMC simulator or assert that individual random numerical trajectories are exact.

## Proof

**1. Two-state scalar reduction.** For any row probability vector \((x,1-x)\), evolution under \(A\) sends the first-state probability to \(F_A(x)=ux+(1-u)\pi_A\); evolution under \(B\) sends it to \(F_B(x)=vx+(1-v)\pi_B\). The exact joint generator has relaxation rate \(s+t\) and fixed point \(\pi_*=(s\pi_A+t\pi_B)/(s+t)\), so its time-\(h\) scalar map is \(rx+(1-r)\pi_*\), where \(r=uv\).

The forward matrix product acts as \(F_B\circ F_A\), giving
\[
 x_{AB}=rx+v(1-u)\pi_A+(1-v)\pi_B.
\]
The reversed matrix product acts as \(F_A\circ F_B\), giving
\[
 x_{BA}=rx+(1-u)\pi_A+u(1-v)\pi_B.
\]
Both have contraction \(r\). Their first-state outputs differ by \(\Delta=(1-u)(1-v)(\pi_A-\pi_B)\), independently of \(x\).

**2. Exact convex mixture and strict uniqueness.** The weight of \(\pi_A\) in the forward offset, divided by \(1-r\), is \(w_{AB}=v(1-u)/(1-r)\); in the reverse offset it is \(w_{BA}=(1-u)/(1-r)\). The true fixed point uses weight \(w_*=s/(s+t)\). Since \(z\mapsto(1-e^{-zh})/z\) is strictly decreasing on \((0,\infty)\),
\[
 w_{AB}<\frac{s}{s+t}<w_{BA}.
\]
For the left inequality, equivalently apply the same monotonicity with \(t\) and \(s+t\), using \(1-w_{AB}=(1-v)/(1-uv)\). Hence there is exactly one \(q\in(0,1)\) satisfying \((1-q)w_{AB}+qw_{BA}=w_*\); solving gives the boxed formula. The resulting first-state maps match for every \(x\); conservation of total probability proves equality of both full matrices. If \(\pi_A\ne\pi_B\), the two products are distinct and the order probability is uniquely determined. If \(\pi_A=\pi_B\), the two generators share a fixed point and commute, making both products exact.

Expanding \(e^{-sh}\) and \(e^{-th}\), and cancelling the removable factors, gives \(q=1/2+(s-t)h/12+O(h^3)\); the even-power coefficient vanishes because the analytic continuation obeys \(q_{s,t}(-h)=1-q_{s,t}(h)\). Letting \(h\to\infty\) gives \(q\to s/(s+t)\).

**3. Exact multistep risk.** The two random scalar maps share slope \(r\) and have constants separated by \(\Delta\). Each freshly selected constant has the exact mean constant of the full generator and variance \(q(1-q)\Delta^2\). If \(x_k\) is the numerical first-state mass and \(x(kh)\) the true first-state mass, then \(e_{k+1}=re_k+\xi_k\), \(e_0=0\), with independent centered \(\xi_k\) of variance \(q(1-q)\Delta^2\). Thus \(\mathbb E e_n=0\) and
\[
\mathbb E e_n^2=q(1-q)\Delta^2\sum_{j=0}^{n-1}r^{2j}
=q(1-q)\Delta^2\frac{1-r^{2n}}{1-r^2}.
\]
Because the vector error is \((e_n,-e_n)\), its squared norm is twice the scalar square. The fixed-horizon expansion follows from \(q\to1/2\), \(\Delta=st(\pi_A-\pi_B)h^2+O(h^3)\), and \(1-r^2=2(s+t)h+O(h^2)\). This is a rigorous finite-horizon asymptotic, not an appeal to an empirical fit.

**4. Impossibility on three states at every positive step.** The two displayed three-state generators preserve the absorbing state \(2\). Restrict their exponentials to the transient states \(0,1\). The two transient generator blocks are
\[
\widetilde A=\begin{pmatrix}-1&1\\1&-1\end{pmatrix},\qquad
\widetilde B=\begin{pmatrix}0&0\\0&-1\end{pmatrix}.
\]
Cyclicity of trace makes the traces of \(e^{h\widetilde A}e^{h\widetilde B}\) and \(e^{h\widetilde B}e^{h\widetilde A}\) equal. A direct two-by-two exponential calculation gives their common trace as
\[
2e^{-3h/2}\cosh(h)\cosh(h/2),
\]
whereas the transient block of the exact exponential has trace
\[
2e^{-3h/2}\cosh(\sqrt5h/2).
\]
For \(h>0\), the function \(z\mapsto\cosh(h\sqrt z)\) is strictly convex on \([0,\infty)\), as seen directly from its power series with positive coefficients of \(z^k\), \(k\ge2\). Since \((9/4+1/4)/2=5/4\), strict Jensen inequality gives
\[
\cosh(h)\cosh(h/2)
=\tfrac12\bigl(\cosh(3h/2)+\cosh(h/2)\bigr)
>\cosh(\sqrt5h/2).
\]
Every affine combination of the two products has the same (strictly larger) trace than the exact exponential; the absorbing state contributes the same additional one to all three traces. Thus no affine combination can be exact at any positive step, proving the dimension boundary.

## Verification

The standard-library `verify.py` reconstructs all relevant two-state matrices for a grid including one-way and strictly bidirectional rates and checks the exact convex-mixture identity and stochasticity. It independently enumerates all two-order sequences for up to eight steps and checks both the exact expected solution and the closed finite-step variance. It also checks the explicit positive three-state trace gap. Run `python verify.py` in the directory containing the script; a successful run prints `VERIFIED numerical_assertions= 448`. The analytic monotonicity, general identity, exact risk formula, and strict convexity argument above—not the finite grid—prove the universal claims.

## Relationship to prior work

Veldman and Zuazua (2021) analyze randomized time splitting for linear-quadratic optimal control, obtaining mesh-refinement error bounds, not a step-dependent two-order mixture that exactly equals a Markov semigroup at every mesh size. Eisenmann and Stillfjord (2022) study randomized operator subproblem selection in abstract evolution equations, rather than full-length forward/reverse Lie-product order calibration. Childs, Ostrander, and Su (2018) analyze randomized product ordering for Hamiltonian simulation and the cancellation of leading commutators, not an exactly calibrated Markov transition matrix for arbitrary positive times. Sumner (2012) establishes a Lie-geometric parametrization of binary Markov matrices that explains the one-dimensional fixed-determinant geometry, but does not state this order-mixture identity or its sharp three-state failure.

Two closely related public numerical-mathematics results were also compared: *An exact positive three-factor split for two-state Markov generators* supplies a **deterministic three-exponential** exact factorization (one additional exponential), whereas this theorem concerns a convex combination of **two-exponential** orders with a single universal probability and finite-step variance. *Unique mean-exact calibration and a Cantor stationary law for randomized two-state generator splitting* selects **one importance-rescaled subgenerator per step**, with a different random map and probability. *A sharp Gaussian trajectory-error law for random-order Lie splitting* establishes the general asymptotic \(h^{3/2}\) error of *fair* random ordering; that exponent is not claimed here as an original discovery. Those results neither assert nor directly imply the current exact two-order expectation identity and sharp three-state trace obstruction.

## Limitations

The exact positive two-order weight is special to two-state conservative Markov generators, and the three-state example rules out a universal extension—not special-case exactness for particular higher-dimensional pairs. The method uses exactly evaluated subflows and rate-dependent randomization. At a fixed nonzero step the individual probability-vector output is random; mean exactness does not imply pathwise exactness. The risk concerns Euclidean squared probability-vector error, not cost or spectral-norm errors for arbitrary signed initial matrices. Published general randomized-product and Lie-algebra work may contain a less explicit equivalent formulation; publication priority is not independently certified.

## References

1. D. W. M. Veldman and E. Zuazua, *A framework for randomized time-splitting in linear-quadratic optimal control*, arXiv:2109.13798, first public 2021-09-28, https://arxiv.org/html/2109.13798v2.
2. M. Eisenmann and T. Stillfjord, *A randomized operator splitting scheme inspired by stochastic optimization methods*, arXiv:2210.05375, first public 2022-10-11, https://arxiv.org/abs/2210.05375; Numerische Mathematik 156 (2024), 435–461.
3. A. M. Childs, A. Ostrander, and Y. Su, *Faster quantum simulation by randomization*, arXiv:1805.08385, first public 2018-05-22, https://arxiv.org/html/1805.08385v2.
4. J. G. Sumner, *Lie geometry of 2x2 Markov matrices*, arXiv:1212.5311, first public 2012-12-21, https://arxiv.org/html/1212.5311v1.
5. *An exact positive three-factor split for two-state Markov generators*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-an-exact-positive-three-factor-split-for-two-state-markov-genera--9b0eeef7eade.
6. *Unique mean-exact calibration and a Cantor stationary law for randomized two-state generator splitting*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-unique-mean-exact-calibration-and-a-cantor-stationary-law-for-ra--543ac65eaf32.
7. *A sharp Gaussian trajectory-error law for random-order Lie splitting*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-gaussian-trajectory-error-law-for-random-order-lie-split--38d8d8425ab3.
