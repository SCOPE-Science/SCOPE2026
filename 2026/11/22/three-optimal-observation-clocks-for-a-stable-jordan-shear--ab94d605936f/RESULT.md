# Three optimal observation clocks for a stable Jordan shear

## Finding
Let \(a,s,T,\sigma>0\). Consider the known stable two-state dynamics and a noisy scalar output
\[
\dot X(t)=\begin{pmatrix}-a&s\\0&-a\end{pmatrix}X(t),\qquad
Y(t)=X_1(t)+\eta_t,
\]
where the two observation errors at the selected events are independent, centered Gaussian random variables of variance \(\sigma^2\). The two coordinates of \(X(0)\) are unknown. Choose exactly two observation times \(0\le t_1<t_2\le T\), freely and without additional costs. Denote their Fisher information for \(X(0)\) by \(\mathcal I(t_1,t_2)\).

The three distinct standard information criteria have **unique optimal ordered designs**:
\[
\begin{aligned}
\text{D-optimal: }&(t_1,t_2)=\bigl(0,\min\{T,1/a\}\bigr), &&\max\det\mathcal I,\\
\text{A-optimal: }&(t_1,t_2)=\bigl(0,\min\{T,c/a\}\bigr), &&\min\operatorname{tr}(\mathcal I^{-1}),\\
\text{E-optimal: }&(t_1,t_2)=\bigl(0,\min\{T,z_\rho/a\}\bigr), &&\max\lambda_{\min}(\mathcal I),
\end{aligned}
\]
where \(\rho=s/a>0\), \(c>1\) is the unique positive root of \((c-1)e^{2c}=1\), and \(z_\rho>c\) is the unique solution of
\[
\rho^2=\frac{e^{2z_\rho}}{z_\rho}-\frac{1}{z_\rho(z_\rho-1)}.
\]
Thus \(1<c<z_\rho\): without a restrictive horizon, the determinant criterion samples earliest, the average-variance criterion next, and the worst-direction criterion latest. The A-optimal delay \(c/a\) is independent of the shear strength \(s\), while the E-optimal delay strictly increases with \(s/a\).

The exact limits and strict growth of the E-optimal delay are
\[
\begin{aligned}
c&=1+\tfrac12 W(2e^{-2})=1.108857552878545\ldots,\\
z_\rho&=c+\frac{c(c-1)^2}{2c-1}\rho^2+O(\rho^4), && \rho\to0^+,\\
z_\rho&=\log\rho+\tfrac12\log\log\rho+o(1), &&\rho\to\infty.
\end{aligned}
\]
When \(T\ge z_\rho/a\), the E-optimal normalized smallest information eigenvalue is
\[
\sigma^2\lambda_{\min}(\mathcal I_*)
=\frac{\rho^2z_\rho(z_\rho-1)}{1+\rho^2z_\rho(z_\rho-1)}<1.
\]

## Assumptions and scope
The system is precisely the dissipative, genuinely defective real size-two Jordan block displayed above with known \(a,s>0\). The initial state, expressed in the given Euclidean coordinates, is the unknown deterministic parameter. The same fixed scalar sensor observes the first coordinate twice; the noise covariance is \(\sigma^2 I_2\). Two events must have distinct times, and the horizon is \([0,T]\) with \(T>0\). The three criteria use this common Fisher matrix and are separately optimized, not combined as a weighted objective. The normalization \(\rho=s/a\) is dimensionless. No process noise, uncertainty in \(a\) or \(s\), sensor mobility costs or arbitrary coordinate rescaling is included. The result is basis-dependent for A- and E-optimality, as those criteria are generally not invariant under changes of state coordinates.

## Proof
**1. Information and temporal shift.** In dimensionless time \(z=at\), the observation row is \(v(z)=e^{-z}(1,\rho z)\). For two dimensionless times \(u\) and \(u+d\), \(u\ge0\), \(d>0\), their two-row design matrix is
\[
V(u,d)=e^{-u}B(d)S(u),\quad
B(d)=\begin{pmatrix}1&0\\e^{-d}&\rho d e^{-d}\end{pmatrix},\quad
S(u)=\begin{pmatrix}1&\rho u\\0&1\end{pmatrix}.
\]
Consequently \(\mathcal I=\sigma^{-2}V^{\mathsf T}V\), and \(\det V=\rho d e^{-2u-d}\). Thus for any fixed gap \(d\), its determinant criterion strictly improves by replacing \((u,u+d)\) with \((0,d)\).

For E-optimality, \(B(d)S(u)\) and \(B(d)\) have the same positive squared determinant, but the former has strictly greater squared Frobenius norm whenever \(u>0\): the increase is exactly
\[
\rho^2\{u^2+e^{-2d}(2ud+u^2)\}>0.
\]
For positive definite two-by-two Gramians, increasing trace at fixed determinant strictly decreases the smaller eigenvalue. The prefactor \(e^{-2u}<1\) decreases it again. Hence E-optimality forces \(u=0\).

For A-optimality, the direct inverse-Gram formula is
\[
\sigma^{-2}\operatorname{tr}\mathcal I(u,u+d)^{-1}
=\frac{e^{2u}}{\rho^2d^2}
\bigl[e^{2d}(1+\rho^2u^2)+1+\rho^2(u+d)^2\bigr].
\]
This is strictly increasing in \(u\ge0\) for each \(d>0\), so A-optimality also forces \(u=0\). (Here \(\mathcal I(u,u+d)\) abbreviates the information for the physical times \(u/a\) and \((u+d)/a\).)

**2. D- and A-optimal delays.** Setting \(u=0\), the determinant is proportional to \(d^2e^{-2d}\), strictly increasing through \(d=1\) and strictly decreasing afterwards. The normalized A-objective is
\[
\sigma^{-2}\operatorname{tr}\mathcal I(0,d)^{-1}
=1+\frac{e^{2d}+1}{\rho^2d^2}.
\]
Its derivative has the sign of \((d-1)e^{2d}-1\). This expression is negative on \((0,1]\), strictly increasing from zero to infinity on \([1,\infty)\), and has exactly one root \(c>1\). Solving gives \(c=1+\frac12 W(2e^{-2})\). Restriction to \(d\le aT\) therefore clips each unrestricted optimum at the horizon.

**3. E-optimal delay and uniqueness.** Write \(w=e^{-2d}\) and \(\lambda(d)=\sigma^2\lambda_{\min}(\mathcal I(0,d))\). Its Gramian trace and determinant are
\[
P(d)=1+w(1+\rho^2d^2),\qquad K(d)=w\rho^2d^2,
\]
so \(\lambda^2-P\lambda+K=0\). Both rows are linearly independent for \(d>0\), and \(0<\lambda<1\) (the smaller eigenvalue is strictly less than the unit squared norm of the first row). Differentiating the characteristic equation, with \(\Delta=\sqrt{P^2-4K}>0\), yields
\[
\lambda'(d)=\frac{K'(d)-P'(d)\lambda(d)}{\Delta}
=\frac{2w}{\Delta}\bigl[\lambda+\rho^2d(1-d)(1-\lambda)\bigr].
\]
This is strictly positive for every \(0<d\le1\). For \(d>1\), put \(v=\rho^2d(d-1)>0\). The derivative has the sign of \((1+v)\lambda-v\). With \(b=v/(1+v)\), substitution into the characteristic polynomial gives the exact identity
\[
(1+v)^2\bigl[b^2-Pb+K\bigr]
=\rho^2d\bigl[e^{-2d}(1+v)-(d-1)\bigr].
\]
Because \(0<b<1\) is strictly below the larger Gramian eigenvalue, the left side has the same sign as \(\lambda-b\), hence the same sign as \(\lambda'(d)\). Therefore
\[
\operatorname{sgn}\lambda'(d)
=\operatorname{sgn}\left[1+\rho^2d(d-1)-e^{2d}(d-1)\right],\quad d>1.
\]
For \(1<d\le c\), this sign is positive. For \(d>c\), it is positive below and negative above the unique root of
\[
\rho^2=G(d):=\frac{e^{2d}}d-\frac1{d(d-1)}.
\]
Indeed \(G(c)=0\), \(G(d)\to\infty\), and
\[
G'(d)=\frac{(2d-1)e^{2d}}{d^2}+\frac{2d-1}{d^2(d-1)^2}>0
\]
for every \(d>1\). Thus \(\lambda\) has a unique global maximum at \(z_\rho>c\). The horizon-constrained maximum is again the minimum of the horizon and the unrestricted optimizing delay.

**4. Optimal value and asymptotics.** At the stationary point \(\lambda=v/(1+v)\), establishing the stated information value. The implicit-function theorem at \(G(c)=0\), using \(G'(c)=(2c-1)/[c(c-1)^2]\), gives the small-\(\rho\) expansion. For \(\rho\to\infty\), the root equation yields \(\rho^2=e^{2z_\rho}/z_\rho+O(z_\rho^{-2})\); taking logarithms and one substitution yields \(z_\rho=\log\rho+\frac12\log\log\rho+o(1)\). Monotonicity follows from \(G'>0\). This completes the global classification.

## Verification
The accompanying `verification/check.py` uses SymPy to check the exact row factorization, determinant, fixed-gap trace increment, E-objective characteristic identity, and derivative identity. It also performs 117,600 seeded direct Fisher-matrix criterion comparisons across eight dimensionless shears, seven horizons and independently generated ordered observation pairs. It reports `6 symbolic identities passed` and `117600 criterion comparisons passed`. These finite checks supplement, but do not replace, the analytical argument for all positive parameters. To reproduce from the extracted package, install `sympy` and run `python verification/check.py`.

For example, at \(a=1\), \(s=4\) and \(T=3\), the E-optimal second observation is \(1.669845528726\ldots\), versus \(1.108857552879\ldots\) for A-optimality and \(1\) for D-optimality. The respective normalized minimum information eigenvalues are approximately \(0.947080475\), \(0.918283293\), and \(0.903161655\), so the E-optimal time produces about \(4.86\%\) more worst-direction information than the D-optimal time.

## Relationship to prior work
Jost, Sager and Le (2017) analyze optimal measurement times in a general control and experimental-design framework, including finite-support design theorems, but do not solve the two-event equal-variance Jordan problem or compare the exact D/A/E sampling clocks. Aspeel and collaborators (2021) optimize finite-budget Kalman prediction on time grids, principally by combinatorial genetic search, with a different process-noise model and average prediction-error objective. Krauss, Lopez and Müller (2022) give rank-based sampled observability conditions, explicitly including Jordan blocks, rather than optimizing the smallest Fisher eigenvalue or inverse trace.

Dette, Melas and Pepelyshev (2006) study E-optimal designs for exponential regression, which can contain the same pair of regressors \(e^{-at}\) and \(t e^{-at}\) after linearization. Their Example 1 optimizes a **freely weighted approximate design**, obtaining a fixed second support point determined by \(e^{-z}=z-1\). The present theorem instead optimizes exactly two independent observations of **fixed equal information weights**. Its E-optimal support moves strictly with the shear ratio and is not inferred from that unrestricted-weight optimum. A related published exact result on damped Jordan sampling fixes two endpoint events and optimizes a **third** event for a determinant criterion; it does not give the two-event E/A design or the three-criterion ordering. General derivative identities and classical Fisher-design criteria are not claimed novel individually.

## Limitations
The complete results concern two events on a single known planar Jordan system with independent homoscedastic noise and Euclidean coordinates. They do not cover unrestricted numbers of events, freely allocated observation weights, arbitrary nonnormal matrices, unknown rates, correlated noise, or dynamic state estimation with process noise. The E-optimal unrestricted delay tends to infinity as \(s/a\to\infty\), but the constrained delay never exceeds \(T\). The small- and large-shear limits assume the other model parameters fixed. The analytic proof provides correctness for the exact model; a literature search cannot establish publication priority conclusively, and no independent external mathematical review is asserted.

## References
1. F. Jost, S. Sager, T. T.-T. Le, *A Feedback Optimal Control Algorithm with Optimal Measurement Time Points*, Processes 5(1), 10 (first publicly dated 2017-02-28), https://doi.org/10.3390/pr5010010.
2. A. Aspeel, A. Legay, R. M. Jungers, B. Macq, *Optimal measurement budget allocation for Kalman prediction over a finite time horizon by genetic algorithms*, EURASIP Journal on Advances in Signal Processing 2021, 39, https://doi.org/10.1186/s13634-021-00732-8.
3. I. Krauss, V. G. Lopez, M. A. Müller, *Sample-based observability of linear discrete-time systems*, first posted 2022-04-13, https://arxiv.org/abs/2204.06451.
4. H. Dette, V. B. Melas, A. Pepelyshev, *Local c- and E-optimal designs for exponential regression models*, Annals of the Institute of Statistical Mathematics 58 (2006), 407–426, https://doi.org/10.1007/s10463-006-0031-2.
5. *A sharp horizon bifurcation for pinned damped-Jordan observation timing*, public result and proof, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-horizon-bifurcation-for-pinned-damped-jordan-observation--8ad879b45d26.
