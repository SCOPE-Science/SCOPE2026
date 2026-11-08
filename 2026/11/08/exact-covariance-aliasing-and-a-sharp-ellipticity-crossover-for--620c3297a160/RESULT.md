# Exact covariance aliasing and a sharp ellipticity crossover for integrating-factor Lyapunov integrators

## Finding

Consider a planar rotation driven by one-dimensional white forcing. The second- and third-order integrating-factor SSP Runge–Kutta discretizations of its differential Lyapunov equation have explicitly computable covariance eigenvalues, distinct rank-loss sets, and an exact phase boundary at which their smallest eigenvalues exchange order.

For every integer \(N\ge 1\), frequency \(\omega>0\), and step \(h>0\), put \(T=Nh\), \(\phi=\omega h\), and
\[
\rho_N(\phi)=\begin{cases}
\left|\dfrac{\sin(N\phi)}{N\sin\phi}\right|,&\sin\phi\ne0,\\[5pt]
1,&\phi\in\pi\mathbb Z.
\end{cases}
\]
The computed symmetric matrices at time \(T\), denoted \(X_N^{(2)}\) and \(X_N^{(3)}\), have eigenvalues
\[
\lambda_{\pm}(X_N^{(2)})=\frac T2\left(1\pm\rho_N(\phi)|\cos\phi|\right),\qquad
\lambda_{\pm}(X_N^{(3)})=\frac T2\left(1\pm\rho_N(\phi)\frac{2+\cos\phi}{3}\right).
\]
Here \(\lambda_-\le\lambda_+\). The second-order matrix is singular exactly when \(\phi\in\pi\mathbb Z\), whereas the third-order matrix is singular exactly when \(\phi\in2\pi\mathbb Z\). At every odd multiple of \(\pi\), the second-order smallest eigenvalue vanishes and the third-order smallest eigenvalue is exactly \(T/3\).

The exact continuous-time covariance is strictly positive definite and has eigenvalues
\[
\lambda_{\pm}(X(T))=\frac T2\left(1\pm\left|\frac{\sin(\omega T)}{\omega T}\right|\right).
\]
Moreover, the difference between the two numerical smallest eigenvalues is exactly
\[
\lambda_-(X_N^{(3)})-\lambda_-(X_N^{(2)})
=\frac{T\rho_N(\phi)}{2}\left(|\cos\phi|-\frac{2+\cos\phi}{3}\right).
\]
When \(\rho_N(\phi)>0\), this difference is strictly positive if and only if \(\cos\phi<-1/2\), and strictly negative if and only if \(-1/2<\cos\phi<1\). Equality occurs when \(\rho_N(\phi)=0\), \(\cos\phi=-1/2\), or \(\cos\phi=1\). Thus the higher-order method is strictly better conditioned in the near-half-turn phase sector but not at all phases. For each fixed \(N\), as \(\delta\to0\) with \(\phi=(2m+1)\pi+\delta\),
\[
\lambda_-(X_N^{(2)})=\frac{T(N^2+2)}{12}\delta^2+O_N(T\delta^4),\qquad
\lambda_-(X_N^{(3)})=\frac T3+\frac{T(N^2-4)}{36}\delta^2+O_N(T\delta^4).
\]

## Assumptions and scope

Let
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
A=\omega J,\quad b=\begin{pmatrix}1\\0\end{pmatrix},\quad Q=bb^{\mathsf T}.
\]
The matrix differential equation is \(\dot X=AX+XA^{\mathsf T}+Q\), \(X(0)=0\), on \(\mathbb R^{2\times2}\). All stages use exact matrix exponentials and exact arithmetic. The two methods are the classical two-stage SSPRK(2,2) and three-stage SSPRK(3,3), respectively, as used on the integrating-factor-transformed Lyapunov equation. The frequency and the step are constant, and both methods use the same equally spaced mesh and endpoint time \(T=Nh\). The claims concern covariance eigenvalues and positive definiteness, not a total accuracy ordering.

## Proof

**1. Integrating-factor reduction.** Define \(W(t)=e^{-tA}X(t)e^{-tA^{\mathsf T}}\). Direct differentiation gives \(W'(t)=F(t)\) with \(W(0)=0\), where \(F(t)=e^{-tA}Qe^{-tA^{\mathsf T}}=v(t)v(t)^{\mathsf T}\) and \(v(t)=(\cos\omega t,-\sin\omega t)^{\mathsf T}\). This is a smooth, time-dependent but state-independent forcing. The SSPRK(2,2) update for \(W\) therefore reduces exactly, on every panel, to the trapezoidal rule
\[
W_{j+1}^{(2)}=W_j^{(2)}+\frac h2\{F(jh)+F((j+1)h)\}.
\]
The SSPRK(3,3) Shu–Osher stages give exactly the Simpson rule
\[
W_{j+1}^{(3)}=W_j^{(3)}+\frac h6\{F(jh)+4F((j+\tfrac12)h)+F((j+1)h)\}.
\]
The original numerical matrices are \(X_N^{(p)}=e^{TA}W_N^{(p)}e^{TA^{\mathsf T}}\). Since \(e^{TA}\) is orthogonal, \(W_N^{(p)}\) and \(X_N^{(p)}\) have identical eigenvalues.

**2. Exact spectral reduction.** Every sampled \(F(t)\) is a rank-one orthogonal projector with trace one. Thus either composite rule has trace \(T\). In a real symmetric \(2\times2\) matrix, eigenvalues equal half the trace plus or minus half the Euclidean norm of the two-dimensional anisotropy vector \((W_{11}-W_{22},2W_{12})\). For a sampled projector, this vector is \((\cos(2\omega t),-\sin(2\omega t))\). Representing it by the unit complex phase \(e^{2i\omega t}\) changes no modulus.

The normalized trapezoidal anisotropy sum is
\[
S_{2}=\sum_{j=0}^{N-1}\frac{e^{2ij\phi}+e^{2i(j+1)\phi}}2
=e^{iN\phi}\cos\phi\,\frac{\sin(N\phi)}{\sin\phi}.
\]
The normalized Simpson anisotropy sum is
\[
S_{3}=\sum_{j=0}^{N-1}\left(\frac{e^{2ij\phi}+e^{2i(j+1)\phi}}6
+\frac23e^{i(2j+1)\phi}\right)
=e^{iN\phi}\frac{2+\cos\phi}{3}\frac{\sin(N\phi)}{\sin\phi}.
\]
For \(\sin\phi=0\), these expressions mean their continuous limits, equivalently the original finite sums. Their moduli are \(N\rho_N(\phi)|\cos\phi|\) and \(N\rho_N(\phi)(2+\cos\phi)/3\). Multiplying by \(h/2\) and combining with trace \(T=Nh\) yields both claimed eigenvalue formulas.

**3. Sharp singular sets.** Every quadrature weight in either composite rule is strictly positive at the indicated nodes. A finite positive sum of rank-one projectors in the plane is positive definite precisely when its sampled unit vectors span the plane. The trapezoidal rule includes \(v(0)\) and \(v(h)\), whose determinant has absolute value \(|\sin\phi|\); if \(\sin\phi=0\), all mesh-point vectors are collinear. Hence the second-order numerical covariance is singular precisely at \(\phi\in\pi\mathbb Z\). Simpson additionally includes \(v(h/2)\). If \(\sin\phi\ne0\), endpoints already span; if \(\phi\in\pi\mathbb Z\), the midpoint contributes a second direction precisely at odd multiples of \(\pi\). Therefore only \(\phi\in2\pi\mathbb Z\) causes Simpson rank loss. At an odd multiple of \(\pi\), each Simpson panel contributes weight \(1/3\) to \(bb^{\mathsf T}\) and \(2/3\) to the orthogonal projector, so the resulting eigenvalues are \(T/3\) and \(2T/3\).

**4. Exact continuous solution.** The transformed exact covariance is \(W(T)=\int_0^T v(t)v(t)^{\mathsf T}\,dt\). Its complex anisotropy integral has modulus \(|\int_0^T e^{2i\omega t}\,dt|=|\sin(\omega T)|/\omega\). Therefore its eigenvalues are the stated pair. Since \(T>0\) and \(\omega T>0\), the strict inequality \(|\sin(\omega T)|<\omega T\) gives positive definiteness.

**5. Comparing smallest eigenvalues.** Subtraction of the formulas in step 2 gives the exact difference. For \(c=\cos\phi\in[-1,0)\), the sign of the bracket equals the sign of \(-4c-2\). For \(c\in[0,1]\), its sign equals the sign of \(2c-2\). This gives the stated sharp crossover and all equality cases. Finally the expansions \(\sin(N\delta)/(N\sin\delta)=1-(N^2-1)\delta^2/6+O_N(\delta^4)\), \(|\cos((2m+1)\pi+\delta)|=1-\delta^2/2+O(\delta^4)\), and \((2+\cos((2m+1)\pi+\delta))/3=1/3+\delta^2/6+O(\delta^4)\) establish the two near-resonance laws.

## Verification

The standalone \(\texttt{check.py}\) computes the complete integrating-factor Shu–Osher stage recurrences, not the composite quadrature shortcuts, for both schemes. It independently obtains matrix eigenvalues and compares them against the two closed-form spectral expressions on 20 iteration counts and 21 step phases, including resonant limits. It also checks the odd/even half-turn examples and both sides of the phase crossover. Executing it with standard Python produced \(\texttt{CHECK\_OK\ 2940}\) direct-stage/eigenvalue/phase comparisons. These are floating-point diagnostics, not a substitute for the analytic proof. At \(\phi=\pi\), the exact matrices have spectra \(\{T/2,T/2\}\), \(\{0,T\}\), and \(\{T/3,2T/3\}\) for continuous time, second order, and third order, respectively; these identities follow symbolically from the displayed sums.

## Relationship to prior work

Zhang, Lan and Jing introduced the two integrating-factor SSPRK schemes for differential Lyapunov equations and proved symmetry and positive-semidefiniteness of their updates [1]. The present result specializes their algorithms to a controllable planar rotation with rank-one forcing, but asks a stricter question: exact eigenvalues, **strict** positive definiteness, singular mesh phases, and a phase-dependent comparison between the second- and third-order outputs. Mere positive-semidefiniteness does not imply this statement. Their source does not report these sharp spectral formulas in the inspected method, theorem, numerical, or concluding sections. General SSP integrating-factor analysis in [2] does not calculate the Lyapunov covariance spectra. Standard controllability-Gramian theory [3] provides the continuous-time interpretation; the use of positive quadrature sums and geometric-series identities is classical. Earlier positivity-preserving Lyapunov discretization [4] concerns a different numerical construction. These observations are an evidence-based comparison, not a proof of global novelty.

## Limitations

The finding concerns an exactly rotated two-dimensional skew generator with one rank-one source, zero initial covariance, fixed time step, and unmodified IF-SSPRK2/3 integrators. It makes no claim about arbitrary matrices, time-varying sources, floating-point definiteness, or a general convergence ordering. The third-order scheme may have a *smaller* minimum eigenvalue than the second-order scheme for phases with \(-1/2<\cos\phi<1\). The near-resonance expansions fix the number of steps. Generic sampled-Gramian and quadrature results may provide equivalent formulations that were not found in accessible literature; historical priority is not independently certified.

## References

[1] W. Zhang, R. Lan and X. Jing, *Strong Stability Preserving Integrating Factor Runge-Kutta Methods for Differential Lyapunov Equations with Positivity Preservation*, arXiv:2606.15703v1, first public version 2026-06-14, https://arxiv.org/abs/2606.15703.

[2] S. Gottlieb, Z. J. Grant and L. Isherwood, *Strong Stability Preserving Integrating Factor Runge-Kutta Methods*, arXiv:1708.02595, https://arxiv.org/abs/1708.02595.

[3] S. Grundel, C. Himpe and J. Saak, *On Empirical System Gramians*, Proc. Appl. Math. Mech. 19 (2019), e201900006, https://doi.org/10.1002/pamm.201900006.

[4] J. Gillis and M. Diehl, *A positive definiteness preserving discretization method for Lyapunov differential equations*, Proc. 52nd IEEE Conf. Decision and Control (2013), https://doi.org/10.1109/CDC.2013.6761121.
