# Codimension-only beta law for random-plane ascent with a repeated top eigenvalue

## Finding

Consider the exact random-plane Rayleigh–Ritz ascent described below with a real symmetric two-level matrix whose **largest eigenvalue has multiplicity at least two**. If its top eigenspace has codimension \(m\ge 2\), the ratio of successive small squared distances to that eigenspace converges in distribution to
\[
W\sim\operatorname{Beta}\!\left(\frac{m-1}{2},\frac12\right).
\]
Thus the exact limiting one-step mean contraction is \((m-1)/m\), independent of the top-eigenvalue multiplicity, spectral gap, and eigenvalue scale. More strongly, for every fixed \(k\ge1\) the first \(k\) normalized squared-error trajectories converge jointly to products of \(k\) independent variables with this beta law. In particular,
\[
\lim_{\varepsilon_0\downarrow0}\mathbb E\!\left[\frac{\varepsilon_k}{\varepsilon_0}\right]
=\left(\frac{m-1}{m}\right)^k.
\]
The formula characterizes a local, finite-horizon stochastic limit, not a uniform-in-time convergence rate.

## Assumptions and scope

Let \(r,m\) be integers with \(r\ge2\) and \(m\ge2\), let \(d=r+m\), and let \(P\) be any rank-\(r\) orthogonal projector in \(\mathbb R^d\). Fix \(\lambda_->0\), \(\Delta>0\), and set \(H=\lambda_-I+\Delta P\) and \(Q=I-P\). One may take any real \(A\) satisfying \(A^TA=H\).

Given a unit vector \(v_j\), sample \(x_j\) independently and uniformly from the unit sphere of \(v_j^\perp\), conditionally on the past. Then choose a unit vector \(v_{j+1}\in\operatorname{span}\{v_j,x_j\}\) maximizing the Rayleigh quotient \(v^THv\). Define the squared top-eigenspace error \(\varepsilon_j=\|Qv_j\|^2\). For every deterministic sequence of initial unit vectors such that \(0<\varepsilon_0<1\) and \(\varepsilon_0\to0\), all convergence statements below hold; the distribution of the errors is invariant under rotations within the top and bottom eigenspaces. The orientation and sign selected for a maximizing vector have no effect on the errors.

For each fixed \(q\ge0\), the exact limiting one-step moment and the fixed-horizon moment are respectively
\[
\lim_{e\downarrow0}\mathbb E\!\left[\left.\left(\frac{\varepsilon_{j+1}}{\varepsilon_j}\right)^q\right|\varepsilon_j=e\right]
=\frac{\Gamma((m-1)/2+q)\Gamma(m/2)}{\Gamma((m-1)/2)\Gamma(m/2+q)},
\]
\[
\lim_{\varepsilon_0\downarrow0}\mathbb E\!\left[\left(\frac{\varepsilon_k}{\varepsilon_0}\right)^q\right]
=\left[\frac{\Gamma((m-1)/2+q)\Gamma(m/2)}{\Gamma((m-1)/2)\Gamma(m/2+q)}\right]^k.
\]
Here \(q=0\) has the usual constant-function interpretation. For \(m=2\) the limiting multiplier has the arcsine distribution, with CDF \(2\arcsin(\sqrt t)/\pi\) for \(0\le t\le1\).

## Proof

**Exact two-plane reduction.** Fix a current unit vector \(v\) with \(e=\|Qv\|^2\in(0,1)\), and write \(w=Qv/\sqrt e\). For the sampled unit tangent \(x\), set \(D=\|Qx\|^2\) and \(c=\langle w,Qx\rangle\). Since \(v\) and \(x\) form an orthonormal basis of their plane, the restriction of \(Q\) to that plane is
\[
G=\begin{pmatrix}e&\sqrt e\,c\\\sqrt e\,c&D\end{pmatrix}.
\]
Maximizing \(v^THv\) on the plane is equivalent to minimizing its \(Q\)-Rayleigh quotient. Hence the next squared error is the smaller eigenvalue of \(G\), namely
\[
\varepsilon^+=\frac{e+D-\sqrt{(D-e)^2+4ec^2}}2,
\qquad
R_e:=\frac{\varepsilon^+}{e}
=\frac{2(D-c^2)}{e+D+\sqrt{(D-e)^2+4ec^2}}.
\]
The last identity follows by rationalizing the numerator. By the variational minimum principle, \(0\le R_e\le1\).

**A coupled zero-error limit.** The symmetry group \(O(r)\times O(m)\) acts transitively on vectors having a prescribed \(e\), and preserves both the matrix and the random tangent law. We may therefore take \(v_e=\sqrt{1-e}\,u_1+\sqrt e\,w_1\), where \(u_1\) is a top-eigenspace unit vector and \(w_1\) is a bottom-eigenspace unit vector. Let \(g\sim N(0,I_d)\) and couple all tangent draws through
\[
x_e=\frac{g-\langle g,v_e\rangle v_e}{\|g-\langle g,v_e\rangle v_e\|}.
\]
As \(e\downarrow0\), almost surely \(x_e\to x_0\), the normalized projection of \(g\) onto \(u_1^\perp\). With an orthonormal basis of the bottom eigenspace beginning with \(w_1\), write its Gaussian components as independent \(Z_1,\ldots,Z_m\sim N(0,1)\). Almost surely \(D_0>0\) and therefore the rationalized formula yields
\[
R_e\longrightarrow1-\frac{Z_1^2}{Z_1^2+\cdots+Z_m^2}
=\frac{Z_2^2+\cdots+Z_m^2}{Z_1^2+\cdots+Z_m^2}.
\]
The independent chi-square numerator and its independent one-degree-of-freedom complement give the stated \(\operatorname{Beta}((m-1)/2,1/2)\) law. This also proves that the limiting law does not depend on \(r\), \(\lambda_-\), or \(\Delta\). Bounded convergence applies to all nonnegative power moments because \(R_e\in[0,1]\). The beta moment formula follows from the beta integral.

**Fixed-horizon independence.** At each iteration the conditional law of the ratio \(R_j=\varepsilon_{j+1}/\varepsilon_j\) depends on the current state only through \(\varepsilon_j\), by the same symmetry argument. Its kernel converges weakly, and on bounded continuous test functions uniformly as the scalar argument approaches zero, to the beta law just proved. The exact plane optimization also makes \(0\le\varepsilon_{j+1}\le\varepsilon_j\); for \(m\ge2\), a random plane has zero error only on a probability-zero event when the current error is positive. Thus, for every fixed number of steps and \(\varepsilon_0\downarrow0\), every conditional error supplied to the next kernel is at most \(\varepsilon_0\). Iterated conditional expectation and induction give joint convergence of \((R_0,\ldots,R_{k-1})\) to \(k\) independent beta variables. The continuous product mapping proves
\[
\left(\frac{\varepsilon_1}{\varepsilon_0},\ldots,\frac{\varepsilon_k}{\varepsilon_0}\right)
\ \Longrightarrow\ (W_1,W_1W_2,\ldots,W_1\cdots W_k),
\]
where the \(W_j\) are independent copies of \(W\). Products lie in \([0,1]\), so bounded convergence gives the asserted fixed-horizon moments. Taking \(q=1\) gives \(((m-1)/m)^k\), completing the proof.

## Verification

The self-contained accompanying `verify.py` reproduces the exact two-by-two eigenvalue identity across five pairs of eigenspace dimensions and several error magnitudes. It independently draws Gaussian tangent vectors, checks the rationalized formula against the smaller eigenvalue, and compares the observed local multiplier CDF and first three moments with the beta law. The script additionally checks the closed-form first-moment identity in ten codimensions and directly simulates three consecutive plane optimizations to stress-test the fixed-horizon product law. An execution with a fixed random seed passed 1,851 checks. Numerical finite samples test the formulas but are not used to prove the distributional limit or joint independence.

## Relationship to prior work

Bresch and Melnyk, *Stochastic Rayleigh–Ritz Ascent: Global Linear Convergence under a Spectral Gap* (arXiv:2610.42071v1, first public October 30, 2026), prove expected linear rates when the top eigenvalue is simple. Their rank-one two-level example gives a local **mean** contraction in the simple-top regime. In contrast, this theorem treats a repeated top eigenvalue \(r\ge2\), a regime in which their strict top spectral-gap assumption fails, and gives a complete beta multiplier law plus fixed-horizon product laws.

The earlier matrix-free random-plane algorithm of Bresch, Lorenz, Schneppe, and Winkler (arXiv:2410.08297) establishes the underlying iteration and almost-sure convergence machinery but does not provide the stated repeated-top local beta law in the inspected sections. Bresch, Melnyk, Schoen, and Steidl (arXiv:2512.05520) analyze a generalized Rayleigh quotient and eigenspace-multiplicity phenomena but likewise do not state this law in the inspected convergence and multiplicity sections. This is a literature comparison, not a claim of exhaustive historical priority.

## Limitations

The claim is confined to real two-eigenvalue matrices, full-sphere uniform tangent sampling, exact plane maximization, initial errors approaching zero, and each **fixed** iteration horizon. It does not provide a uniform-in-horizon bound, a finite-precision error estimate, or a rate for general multi-level matrices. The top eigenspace has dimension at least two and the bottom eigenspace has dimension at least two. Historical coverage by equivalent random-projection formulations cannot be ruled out categorically.

## References

- J. Bresch and O. Melnyk, *Stochastic Rayleigh–Ritz Ascent: Global Linear Convergence under a Spectral Gap*, arXiv:2610.42071v1 (2026). https://arxiv.org/abs/2610.42071
- J. Bresch, D. Lorenz, T. Schneppe, and W. Winkler, *Matrix-free stochastic calculation of operator norms without using adjoints*, arXiv:2410.08297 (2024). https://arxiv.org/abs/2410.08297
- J. Bresch, O. Melnyk, A. Schoen, and G. Steidl, *Stochastic Zeroth-Order Method for Computing Generalized Rayleigh Quotients*, arXiv:2512.05520 (2025). https://arxiv.org/abs/2512.05520
