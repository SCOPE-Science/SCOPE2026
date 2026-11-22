# A unique finite tightness horizon for damped-Jordan orbit frames

## Finding

Let \(a,b,T>0\), let \(J=\begin{pmatrix}0&1\\0&0\end{pmatrix}\), and define the nonnormal semigroup \(S(t)=e^{t(-aI+bJ)}\) on \(\mathbb C^2\), equipped with its standard Euclidean inner product. For any nonzero generating vector \(v\), define the finite-horizon continuous orbit frame \(\{S(t)v:0\le t\le T\}\) relative to Lebesgue measure. Let \(\kappa_T(v)\) be the ratio of its optimal upper to lower frame bounds, with value infinity if the family is not a frame.

Put
\[
\mu_T=\frac1{2a}-\frac{T}{e^{2aT}-1},\qquad
\rho_T=\frac{b^2}{4a^2}\left[1-\left(\frac{aT}{\sinh(aT)}\right)^2\right].
\]

**Complete sharp design statement.** The unique generating-vector direction minimizing \(\kappa_T(v)\), up to nonzero complex scaling, is
\[
\boxed{v_T\ \propto\ (-b\mu_T,1).}
\]
Its exact optimal squared-analysis condition number is
\[
\boxed{\min_{v\ne0}\kappa_T(v)=\max\{\rho_T,\rho_T^{-1}\}.}
\]
For the unit-norm choice \(v_T=(-b\mu_T,1)/\sqrt{1+b^2\mu_T^2}\), the sharp lower and upper frame bounds are
\[
\boxed{\ A_T=\frac{1-e^{-2aT}}{2a(1+b^2\mu_T^2)}\min\{1,\rho_T\},\qquad
 B_T=\frac{1-e^{-2aT}}{2a(1+b^2\mu_T^2)}\max\{1,\rho_T\}.\ }
\]

**Exact horizon phase transition.** For every fixed \(a,b>0\), \(T\mapsto\rho_T\) increases strictly from zero to \((b/(2a))^2\). Consequently:

- If \(b>2a\), there is one and only one finite horizon \(T_*\) at which a tight orbit frame is possible. It is the unique positive solution of
\[
\boxed{\frac{aT_*}{\sinh(aT_*)}=\sqrt{1-\frac{4a^2}{b^2}}.}
\]
The best squared-analysis condition number decreases strictly from infinity to one on \((0,T_*)\) but **increases strictly** from one toward \((b/(2a))^2\) on \((T_*,\infty)\).
- If \(b=2a\), the best squared-analysis condition number strictly decreases toward one as \(T\to\infty\) but never equals one at finite \(T\).
- If \(0<b<2a\), the best squared-analysis condition number strictly decreases toward \((2a/b)^2>1\), and no tight horizon exists.

In every case \(\min_v\kappa_T(v)\sim12/(b^2T^2)\) as \(T\downarrow0\). In particular, a longer acquisition horizon can make the *best possible* condition number strictly worse, although the unnormalized frame operator for each fixed generator increases in positive-semidefinite order with horizon.

## Assumptions and scope

All parameters \(a,b,T\) are strictly positive real numbers. The state space is exactly the complex Euclidean plane in the displayed Jordan coordinates; nonunitary changes of state coordinates alter frame condition numbers. The orbit is sampled continuously with **Lebesgue measure** on \([0,T]\), and all nonzero generating vectors are allowed. There is no time-dependent sensor weighting. The optimization minimizes the ratio of the optimal frame bounds, not their difference, determinant, smallest eigenvalue under an absolute gain constraint, or a statistically weighted inverse covariance.

Because \(J^2=0\), \(S(t)=e^{-at}(I+btJ)\). The result does not concern the entire half-line frame on \([0,\infty)\) (although its limit can be computed), higher Jordan blocks or multiple independent generators. The primary subject is sharp continuous-frame conditioning and its finite-horizon geometry (MSC2020 42C15).

## Proof

**1. Exact frame matrix.** Write \(v=(x,y)\). Then \(S(t)v=e^{-at}(x+bty,y)\), and its frame operator is
\[
W_T(v)=\int_0^T (S(t)v)(S(t)v)^*\,dt.
\]
Set \(M_j=\int_0^T t^j e^{-2at}\,dt\) for \(j=0,1,2\), and \(\mu=M_1/M_0\), \(\sigma^2=M_2/M_0-\mu^2\). Direct integration yields
\[
M_0=\frac{1-e^{-2aT}}{2a},\quad
\mu=\frac1{2a}-\frac{T}{e^{2aT}-1},\quad
\sigma^2=\frac1{4a^2}\left[1-\left(\frac{aT}{\sinh(aT)}\right)^2\right]>0.
\]
The strict positivity of \(\sigma^2\) also follows because \(e^{-2at}\) is a strictly positive density on the nondegenerate interval. If \(y=0\), every orbit vector is collinear, so the lower frame bound is zero. If \(y\ne0\), define \(z=x/y+b\mu\). Centering \(t\) at its weighted mean gives exactly
\[
\boxed{
W_T(v)=M_0|y|^2
\begin{pmatrix}
 |z|^2+b^2\sigma^2 &z\\
 \overline z&1
\end{pmatrix}. }
\]
Its determinant equals \(M_0^2|y|^4b^2\sigma^2>0\); hence any \(y\ne0\) generates a continuous frame.

**2. Global optimization over every complex vector.** Since multiplication of \(v\) by a nonzero scalar only rescales \(W_T(v)\), fix \(y=1\) without loss. The determinant above is then independent of the unconstrained complex parameter \(z\), whereas its trace equals \(M_0(1+b^2\sigma^2+|z|^2)\), uniquely minimized at \(z=0\). For any positive-definite Hermitian two-by-two matrix with eigenvalues \(\lambda_-\le\lambda_+\),
\[
\frac{(\operatorname{tr}W)^2}{\det W}=\frac{\lambda_+}{\lambda_-}+\frac{\lambda_-}{\lambda_+}+2,
\]
which is strictly increasing as a function of \(\lambda_+/\lambda_-\ge1\) except that the derivative vanishes at the isolated endpoint one. Therefore the unique global optimum has \(z=0\), equivalently \(x/y=-b\mu\), and its frame matrix is diagonal with diagonal entries \(M_0|y|^2(b^2\sigma^2,1)\). Substitution of \(\rho_T=b^2\sigma_T^2\) gives the sharp bounds and condition-number formulas; normalizing the vector gives the unit-norm formulas.

**3. Horizon dependence.** Put \(s=aT>0\). Since
\[
\frac{d}{ds}\left(\frac{s}{\sinh s}\right)=\frac{\sinh s-s\cosh s}{\sinh^2s}<0,
\]
the ratio \(s/\sinh s\) decreases strictly from one to zero. For the strict inequality, the function \(s\cosh s-\sinh s\) vanishes at zero and has derivative \(s\sinh s>0\). Thus \(\rho_T\) increases strictly through its stated range. If \(b>2a\), the intermediate value theorem gives one unique finite \(T_*\) with \(\rho_{T_*}=1\); the equation above is its exact characterization. The function \(u\mapsto\max\{u,u^{-1}\}\) is strictly decreasing for \(0<u\le1\) and strictly increasing for \(u\ge1\), proving all three regimes and the late-horizon conditioning reversal. Finally
\[
\frac{s}{\sinh s}=1-\frac{s^2}{6}+O(s^4),\qquad
\rho_T=\frac{b^2T^2}{12}+O(T^4),
\]
which gives the stated short-horizon asymptotic. For every fixed \(v\), \(W_{T_2}(v)-W_{T_1}(v)\) is positive semidefinite when \(T_2>T_1\), by its defining integral, despite the optimized conditioning reversal. No limiting numerical experiment is used to infer these conclusions.

## Verification

The standalone Python 3 standard-library checker `verify.py` independently evaluates the frame integral by Simpson quadrature for random complex generators, compares the exact centered moment identity, tests the sharp optimum against arbitrary alternative vectors, and checks horizon monotonicity and tightness roots. Execute `python3 verify.py` in the directory containing the script. It reports 862 numerical assertions on the tested cases; its numerical tests support, but do not certify, the complete continuum proof above. Symbolic direct integration independently confirms \(M_1/M_0\) and the displayed variance identity; the proof itself relies on elementary exact integration and the explicit matrix argument.

## Relationship to prior work

Bailey, Gallardo-Gutiérrez and Partington (first public 10 November 2026) study general continuous semigroup frames on \([0,\infty)\), using cogenerator and shift-model structure, and characterize classes with tight generators. Their full accessible preprint develops structural and infinite-horizon frame existence, not the sharp finite-horizon two-dimensional damped-Jordan vector and horizon optimization here. Aldroubi, Huang and Petrosyan (2018) study continuous powers and finite intervals under normal-operator assumptions. The present stable Jordan semigroup is not normal when \(b>0\), and the sharp condition-number objective is different. Assif, Sheriff and Chatterjee (2019) relate controllability Gramians and frame tightness; that general principle motivates the question and is not claimed to be new.

A published finite-dimensional result on pinned damped-Jordan observation timing optimizes the determinant of **three discrete independent observations with compulsory endpoints**. A distinct published diagonal two-mode result optimizes the condition number for a discrete **infinite-horizon** actuator Gramian. A third published cyclic-permutation result optimizes the spectrum of **discrete-time cyclic orbits**. Their available full statements and proofs were compared: none supplies the continuous Lebesgue-frame finite-horizon sharp ratio, unique generator, or the three-regime tightness threshold. The matrix moment formula, variance identity, Gramian interpretation, and elementary two-by-two spectral relation are acknowledged standard tools; the contribution asserted here is their complete sharp specialization and horizon bifurcation.

## Limitations

No claim is made for higher-dimensional Jordan blocks, arbitrary stable matrices, non-Lebesgue time weights, discrete sampling, or coordinate-invariant numerical conditioning. No overall gain constraint is optimized: scalar multiples of the generator leave the frame-bound ratio unchanged. The state-space Euclidean metric matters. Bibliographic priority is provisional: equivalent results could occur in historical two-regressor exponential optimal-design or finite-time nonnormal actuator-placement literature not exhaustively inspected. The independent audit of the mathematical statement has not been performed.

## References

1. V. Bailey, E. A. Gallardo-Gutiérrez and J. R. Partington, *Frames Associated with \(C_0\)-Semigroups*, arXiv:2611.13867v1, publicly posted 2026-11-10, https://arxiv.org/abs/2611.13867.
2. A. Aldroubi, L. Huang and A. Petrosyan, *Frames Induced by the Action of Continuous Powers of an Operator*, arXiv:1801.10103v1, 2018-01-30, https://arxiv.org/abs/1801.10103.
3. M. Assif PK, M. R. Sheriff and D. Chatterjee, *Measure of quality of finite-dimensional linear systems: A frame-theoretic view*, arXiv:1902.04548v1, 2019-02-12, https://arxiv.org/abs/1902.04548.
4. *A sharp horizon bifurcation for pinned damped-Jordan observation timing*, publicly available scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-horizon-bifurcation-for-pinned-damped-jordan-observation--8ad879b45d26.
5. *Exact condition-optimal scalar actuator for a two-mode discrete-time Gramian*, publicly available scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-condition-optimal-scalar-actuator-for-a-two-mode-discrete--0ffcc7242b3f.
6. *Horizon-universal spectral majorization for a damped cyclic actuator*, publicly available scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-horizon-universal-spectral-majorization-for-a-damped-cyclic-actu--50b398f70222.
