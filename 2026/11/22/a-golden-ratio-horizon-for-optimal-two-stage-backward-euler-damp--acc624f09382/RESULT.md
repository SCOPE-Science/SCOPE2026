# A golden-ratio horizon for optimal two-stage backward-Euler damping of a Jordan shear

## Finding
For every real decay rate \(a>0\), shear magnitude \(s\ge0\), and horizon \(H>0\), consider the defective but stable planar generator
\[
A=\begin{pmatrix}-a&s\\0&-a\end{pmatrix},
\]
and at most two ordinary backward-Euler resolvent stages, with nonnegative step durations \(h_1+h_2=H\). The optimization criterion is the final induced Euclidean operator norm
\[
\mathcal G(h_1,h_2)=\big\|(I-h_2A)^{-1}(I-h_1A)^{-1}\big\|_2.
\]
Put \(t=aH\), \(\beta=s/a\), and \(t_c=1+\sqrt5\). When \(0<t<t_c\), define the sharp, finite threshold
\[
\beta_*(t)=\frac{t^2+8t+8}{\sqrt{8(t+2)(4+2t-t^2)}}.
\]
Then the complete minimizing **unordered** step multisets are
\[
\begin{array}{c|c}
\text{condition}&\text{all optimal multisets}\\\hline
0<t<t_c,\ \beta<\beta_*(t)&\{H/2,H/2\}\\
0<t<t_c,\ \beta=\beta_*(t)&\{H/2,H/2\},\ \{0,H\}\\
0<t<t_c,\ \beta>\beta_*(t)&\{0,H\}\\
t\ge t_c\ \text{(any finite }\beta\ge0\text{)}&\{H/2,H/2\}.
\end{array}
\]
There are no positive unequal minimizing steps. The threshold \(\beta_*(t)\) increases strictly from \(1\) to infinity as \(t\) increases from \(0\) to \(t_c\). Thus every \(\beta\le1\) favors two equal steps at every horizon, while for each fixed \(\beta>1\) the optimal design switches exactly once from a single active step to two equal steps as the horizon grows. If both durations must be strictly positive, the \(\{0,H\}\)-only optimum is an unattained infimum. At a tie, equal positive steps still attain the optimum.

The common explicit objective at an arbitrary admissible allocation is, on writing \(v=a^2 h_1h_2\),
\[
\mathcal G=\frac{\sqrt{4(1+t+v)^2+\beta^2(t+2v)^2}+\beta(t+2v)}{2(1+t+v)^2},\quad0\le v\le t^2/4.
\]
Consequently the exact minimum is the smaller of the expressions obtained at \(v=0\) and \(v=t^2/4\). It is not an endpoint integration-error bound or a computational-cost guarantee.

## Assumptions and scope
The initial vector may be any nonzero real or complex vector, and the norm is the induced Euclidean operator \(2\)-norm, not Frobenius norm, spectral radius or averaged energy. Both resolvents use the **same** constant real generator and are composed in either order (they commute). A zero-duration stage is allowed and acts as the identity. The two prescribed stage opportunities may therefore include one unused solve. The horizon \(H\) denotes physical elapsed time, not an expected random duration. Only nonnegative shear is displayed; changing its sign gives the same norm under an orthogonal sign change.

## Proof
**1. Exact resolvent and one-dimensional reduction.** Let \(N\) be the matrix with a single entry \(N_{12}=1\), so \(N^2=0\) and \(A=-aI+sN\). For \(w=ah_1\), \(z=ah_2\), \(w+z=t\) and \(v=wz\), direct inversion and nilpotency give
\[
(I-h_2A)^{-1}(I-h_1A)^{-1}
=\begin{pmatrix}
D^{-1}&\beta(t+2v)D^{-2}\\0&D^{-1}
\end{pmatrix},\quad D=(1+w)(1+z)=1+t+v.
\]
For \(c>0\), \(d\ge0\), the largest singular value of \(\left(\begin{smallmatrix}c&d\\0&c\end{smallmatrix}\right)\) equals \((\sqrt{4c^2+d^2}+d)/2\), proving the displayed formula. Every \(v\in[0,t^2/4]\) occurs for an unordered nonnegative pair \(w,z\), by solving \(X^2-tX+v=0\). In particular \(v=0\) corresponds to \(\{0,H\}\), and \(v=t^2/4\) to \(\{H/2,H/2\}\).

**2. No positive unequal optimum.** Write the logarithm of the norm as
\[
L(v)=-\log D+\operatorname{arsinh}\!\left(\frac{\beta(t+2v)}{2D}\right).
\]
Exact differentiation yields
\[
L'(v)=\frac1D\left[\frac{\beta(2+t)}{\sqrt{4D^2+\beta^2(t+2v)^2}}-1\right].
\]
The radical increases strictly with \(v\) for every \(t>0\) and \(\beta\ge0\). Thus the bracket is either strictly negative throughout, strictly positive throughout, or changes sign only from positive to negative. Every interior critical point is consequently a strict maximum, never a minimum; the only global minimizers are the two endpoints, and there can be no flat minimizing interval. This also covers \(\beta=0\), when \(L'<0\).

**3. Endpoint crossing.** Put \(c=1+t/2\), \(d=1+t\), and \(y=\beta t\). The two endpoint norms are
\[
G_0(y)=\frac{\sqrt{4d^2+y^2}+y}{2d^2},\qquad
G_e(y)=\frac{\sqrt{4c^2+y^2}+y}{2c^3}.
\]
The ratio \(G_e/G_0\) is strictly increasing in \(y\ge0\): its logarithmic derivative is
\[
\frac1{\sqrt{4c^2+y^2}}-\frac1{\sqrt{4d^2+y^2}}>0,
\]
since \(c<d\). At \(y=0\), the ratio equals \(d/c^2<1\). At \(y\to\infty\), the ratio tends to \(d^2/c^3\), which is greater than one exactly when
\[
c^3-d^2=\frac{t(t^2-2t-4)}8<0\iff 0<t<1+\sqrt5.
\]
For \(t\ge t_c\), the equal-step norm is strictly smaller for every finite shear. For \(t<t_c\), exactly one positive crossing exists. If \(K\) denotes the common norm at that crossing, inversion of the two singular-value equations gives
\[
y=Kd^2-K^{-1}=Kc^3-(Kc)^{-1},\quad
K^2=\frac{1-1/c}{d^2-c^3}.
\]
Substituting yields
\[
\frac{y^2}{t^2}=\frac{(t^2+8t+8)^2}{8(t+2)(4+2t-t^2)},
\]
which proves the sharp threshold and all equality cases.

**4. Monotone phase boundary.** Differentiation of the last rational expression shows
\[
\frac{d\beta_*^2}{dt}=
\frac{(t^2+8t+8)(-t^4+8t^3+48t^2+96t+64)}{8(t+2)^2(4+2t-t^2)^2}>0
\]
for \(0<t<t_c<4\). The limits \(\beta_*(0+)=1\) and \(\beta_*(t_c-)=+\infty\) complete the horizon phase diagram. The strict-positivity statement follows by continuity and the absence of interior minimizers.

## Verification
Execute `python verify.py` with Python 3.9+, NumPy and SymPy installed. The script symbolically verifies the two-resolvent product, the endpoint crossing polynomial and the threshold identity, then independently compares direct singular values of the matrix products against the formula for 7,272 parameter/partition combinations. It also checks the endpoint lower bound, representative threshold ties and both sides of all phase boundaries. The script prints `PASS` after completion. These finite checks are supplementary; the exact theorem for all parameters is proved by the preceding inequalities.

As a physically dissipative example, let \(a=1\), \(s=3/2\), \(H=1/2\). The generator satisfies \((A+A^\mathsf T)/2\preceq0\), but its nonnormality still makes the single-active-step policy strictly preferable: \(\mathcal G(0,H)=0.853850937603\ldots\) versus \(\mathcal G(H/2,H/2)=0.860179616570\ldots\). This is a difference in numerical damping, not a statement of better solution accuracy.

## Relationship to prior work
Reuter (2019) studies transient growth of exponentials and powers of nonnormal matrices, including defective two-dimensional Jordan invariant subspaces. Its criteria neither parameterize nor optimize two sequential backward-Euler resolvents under a fixed total duration. Layton, Pei and Trenchea (2021) study a distinct, filtered variable-step Dahlquist–Liniger–Nevanlinna scheme represented using a backward-Euler solve, focusing on stability and accuracy rather than the worst-direction two-resolvent allocation here. An exact affine Jordan norm minimization result for \((1-\lambda)I+\lambda J_n\) gives related singular-value information but does not optimize the nonlinear curve of scalar and nilpotent coefficients generated by products of two resolvents. The present threshold therefore is not implied by those examined results; publication-priority risk from older specialized step-allocation work remains.

## Limitations
The optimal criterion is terminal numerical amplification at fixed duration, not consistency or local/global integration error. The result concerns exactly two stage opportunities, a planar single Jordan block and the Euclidean operator norm. It does not extend without proof to more stages, general nonnormal matrices, time-dependent dynamics, noisy measurements or the relative error against the exact semigroup. The vanishing-duration optimum requires permission to omit a solve; if each positive step is required, that branch gives an unattained infimum. No independent mathematical validation has been performed.

## References
1. M. G. Reuter, *Associating the Invariant Subspaces of a Non-Normal Matrix with Transient Effects in its Matrix Exponential or Matrix Powers*, first public 12 September 2019, arXiv:1909.05931. https://arxiv.org/abs/1909.05931
2. W. Layton, W. Pei and C. Trenchea, *Refactorization of a variable step, unconditionally stable method of Dahlquist, Liniger and Nevanlinna*, first public 20 August 2021, arXiv:2108.09339. https://arxiv.org/abs/2108.09339
3. *The sharp affine Jordan norm pencil and its scaled \(q\)-spectral-set transition*, published mathematical record, 11 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-sharp-affine-jordan-norm-pencil-and-its-scaled-q-spectral-se--00a25760cd57
4. B. Lindberg, *Characterization of Optimal Stepsize Sequences for Methods for Stiff Differential Equations*, SIAM Journal on Numerical Analysis (1977), doi:10.1137/0714058. https://doi.org/10.1137/0714058
