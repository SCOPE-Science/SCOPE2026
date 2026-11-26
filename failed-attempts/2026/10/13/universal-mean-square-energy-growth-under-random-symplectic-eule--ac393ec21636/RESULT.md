# Universal mean-square energy growth under random symplectic-Euler steps

## Finding
For the unit-frequency oscillator \(q''=-q\), kick--drift symplectic Euler with independent and identically distributed positive steps strictly below the deterministic stability threshold has an exact dichotomy: a single fixed step produces uniformly bounded trajectories, whereas **every** nonconstant step distribution produces exponential mean-square energy growth from **every** nonzero deterministic initial state.

Let \(m_j=\mathbb E[H^j]\), \(j=1,2,3,4\). The exact second-moment transfer matrix \(T\) satisfies
\[
\det(I-T)=-2m_1^2\mathbb E\left[\left(H^2-\frac{m_2}{m_1}H\right)^2\right].
\]
This vanishes for a positive distribution only when the step is constant, and is strictly negative for every nonconstant positive law. In particular, two independently sampled stable step values can have unbounded expected energy despite each constant-step map being power bounded.

## Assumptions and scope
Normalize the oscillator frequency to one by measuring steps in units of inverse frequency. Let \(H_0,H_1,\ldots\) be independent, identically distributed real variables satisfying \(\Pr(0<H_k<2)=1\). They are independent of the deterministic starting position and momentum \((q_0,p_0)\in\mathbb R^2\). At every integer index \(k\ge0\), define
\[
p_{k+1}=p_k-H_k q_k,\qquad q_{k+1}=q_k+H_k p_{k+1}.
\]
For a nonconstant step law, there exist \(\rho>1\) and \(c>0\), depending only on that law, such that for every deterministic initial state and every integer \(k\ge0\),
\[
\mathbb E(q_k^2+p_k^2)\ge c\rho^k(q_0^2+p_0^2).
\]
For an almost-surely constant step value in \((0,2)\), trajectories are bounded uniformly in \(k\). No discrete-time mean-square convergence-to-zero claim is made for the oscillator.

## Proof
**One-step matrices and deterministic side.** For \(x_k=(q_k,p_k)^\mathsf T\),
\[
x_{k+1}=A(H_k)x_k,\qquad A(h)=\begin{pmatrix}1-h^2&h\\-h&1\end{pmatrix}.
\]
For every \(0<h<2\), \(\det A(h)=1\) and \(\operatorname{tr}A(h)=2-h^2\in(-2,2)\). Thus the two eigenvalues are distinct unit-modulus nonreal conjugates. More explicitly, the symmetric matrix
\[
G_h=\begin{pmatrix}1&-h/2\\-h/2&1\end{pmatrix}\succ0
\]
satisfies \(A(h)^\mathsf T G_h A(h)=G_h\). Since its eigenvalues are \(1\pm h/2>0\), its invariant quadratic norm is equivalent to Euclidean norm. For constant \(H_k=h\), all initial-state trajectories remain bounded.

**Exact second-moment operator.** Independence implies for the covariance \(X_k=\mathbb E[x_kx_k^\mathsf T]\) that \(X_{k+1}=\mathcal L(X_k)\), where
\[
\mathcal L(X)=\mathbb E[A(H)XA(H)^\mathsf T].
\]
Represent a symmetric matrix by its independent entries \((X_{11},X_{12},X_{22})^\mathsf T\), and put \(m_j=\mathbb E[H^j]\). Direct expansion gives the real matrix
\[
T=\begin{pmatrix}
1-2m_2+m_4&2(m_1-m_3)&m_2\\
-m_1+m_3&1-2m_2&m_1\\
m_2&-2m_1&1
\end{pmatrix}.
\]
Its characteristic determinant at one factors exactly as
\[
\begin{aligned}
\det(I-T)&=-2(m_1^2m_4-2m_1m_2m_3+m_2^3)\\
&=-2m_1^2\mathbb E\left[\left(H^2-\frac{m_2}{m_1}H\right)^2\right].
\end{aligned}
\]
Since \(H>0\) almost surely and \(m_1>0\), the expectation vanishes if and only if \(H=m_2/m_1\) almost surely. Therefore nondegeneracy gives \(\det(I-T)<0\). The real monic cubic \(\det(zI-T)\) is negative at \(z=1\) and tends to positive infinity for positive large \(z\). By continuity, \(T\) has a real eigenvalue \(\lambda>1\). In particular, the spectral radius \(\rho\) of \(\mathcal L\) satisfies \(\rho>1\).

**Growth for every initialization.** The adjoint map for the trace pairing is
\[
\mathcal L^*(P)=\mathbb E[A(H)^\mathsf T P A(H)].
\]
It preserves the closed, solid, pointed cone of positive semidefinite symmetric matrices. The finite-dimensional Perron--Frobenius theorem for cone-preserving linear operators therefore supplies a nonzero positive-semidefinite \(P\) with \(\mathcal L^*(P)=\rho P\), where \(\rho>1\) is the spectral radius found above. To check strict positivity, suppose for contradiction that \(P\) has rank one and write \(P=vv^\mathsf T\) with real \(v\ne0\). For every real \(w\) orthogonal to \(v\),
\[
0=\rho w^\mathsf T Pw=\mathbb E[(v^\mathsf T A(H)w)^2].
\]
Hence \(v^\mathsf T A(H)w=0\) almost surely, so \(A(H)^\mathsf T v\) is real-proportional to \(v\) almost surely. This would make \(v\) a real eigenvector of \(A(H)^\mathsf T\), contradicting the strictly negative discriminant \((2-H^2)^2-4=H^2(H^2-4)<0\) on the support. Therefore \(P\succ0\).

Independence and the adjoint eigenmatrix identity now yield, for every deterministic \(x_0\) and \(k\ge0\),
\[
\mathbb E[x_k^\mathsf T P x_k]=\rho^k x_0^\mathsf T P x_0.
\]
Using \(\lambda_{\min}(P)\|x\|_2^2\le x^\mathsf T P x\le\lambda_{\max}(P)\|x\|_2^2\), obtain
\[
\mathbb E\|x_k\|_2^2\ge
\frac{\lambda_{\min}(P)}{\lambda_{\max}(P)}\rho^k\|x_0\|_2^2.
\]
This establishes the stated uniform-in-initialization exponential bound. For an atom pair \(H=a\) with probability \(\theta\) and \(H=b\) otherwise, direct substitution yields
\[
\det(I-T)=-2\theta(1-\theta)a^2b^2(a-b)^2,
\]
showing both strictness and its dependence on the support separation. This completes the proof.

## Verification
The companion `verify.py` symbolically expands the one-step quadratic action, reconstructs the exact moment transfer matrix and determinant factorization, verifies the two-atom formula and the invariant definite quadratic form, and cross-checks sampled rational laws and initial conditions by exact arithmetic. It also checks the explicitly stated rational witness \(H\in\{1/2,1\}\) with equal probabilities, for which
\[
T=\begin{pmatrix}9/32&3/8&5/8\\-3/16&-1/4&3/4\\5/8&-3/2&1\end{pmatrix},
\quad \det(I-T)=-1/32,
\]
and \(\rho\approx1.01797185386451\). The symbolic identity proves the all-distribution conclusion; finitely many exact examples do not prove the universal quantifiers.

## Relationship to prior work
Skeel and Gear (1992) earlier identified a loss of conventional symplectic invariants under varying steps (bibliographic abstract only). Skeel (1993) showed that variable steps can destabilize the Störmer/leapfrog/Verlet method and constructed deterministic schedules using products of distinct elliptic matrices. That establishes possibility for purposefully chosen schedules, not the quantified mean-square claim for *every* nonconstant independent step law, the explicit fourth-moment certificate, or the every-initial-state growth estimate. Quinn et al. (1997) investigated adaptive leapfrog in astrophysical simulations and emphasized accuracy and symplecticity issues, but did not give the independent-step moment characterization. Abdulle and Garegnani (2018/2020) proved properties of randomized-time-step integrators and finite, step-dependent time-window energy estimates under additional small-variance and trajectory assumptions; their Theorem 6 does not assert globally uniform-in-time bounded energy for a fixed nonzero variance, and their setting does not give the present exact asymptotic oscillator dichotomy. General random-matrix product theorems may imply qualitative growth under additional verification, but they do not by themselves supply the displayed exact moment determinant formula.

## Limitations
The theorem covers only kick--drift symplectic Euler for the unit-frequency linear oscillator and i.i.d. strictly positive steps below two. It does not establish the almost-sure Lyapunov exponent, an explicit closed formula for the mean-square growth rate for arbitrary laws, or boundedness under correlated/adaptive step choices. The exclusion of zero is substantive: sampling \(0\) and one fixed stable positive step produces commuting maps and can remain bounded even though the step is random. Constant endpoint steps equal to two yield a parabolic matrix and are excluded. Earlier literature on random products of elliptic matrices remains a possible source of overlapping qualitative statements; only the specific statement and moment identity assessed here are claimed. A still earlier paper by Skeel and Gear has an institutionally verified public publication date of 1992-11-01; its complete text could not be obtained and remains an explicit comparison risk. That earliest day-resolved publication date is used in the metadata; the full-text Skeel 1993 article is independently inspected. No earlier preprint-day claim is made.

## References
1. R. D. Skeel and C. W. Gear, *Does variable step size ruin a symplectic integrator?*, Physica D 60 (1992), 311–313, DOI: 10.1016/0167-2789(92)90247-K; Princeton institutional bibliographic record https://collaborate.princeton.edu/en/publications/does-variable-step-size-ruin-a-symplectic-integrator/. Only the abstract was accessible.
2. R. D. Skeel, *Variable Step Size Destabilizes the Störmer/Leapfrog/Verlet Method*, BIT Numerical Mathematics 33 (1993), 172–175, DOI: 10.1007/BF01990352. Full text: https://tlakoba.w3.uvm.edu/math6737/paper_Verlet_VariableStepSize.pdf.
3. T. Quinn, N. Katz, J. Stadel, and G. Lake, *Time stepping N-body simulations*, arXiv:astro-ph/9710043v1, publicly submitted 1997-10-03, https://arxiv.org/abs/astro-ph/9710043.
4. A. Abdulle and G. Garegnani, *Random time step probabilistic methods for uncertainty quantification in chaotic and geometric numerical integration*, arXiv:1801.01340v1 (2018), https://arxiv.org/abs/1801.01340.
