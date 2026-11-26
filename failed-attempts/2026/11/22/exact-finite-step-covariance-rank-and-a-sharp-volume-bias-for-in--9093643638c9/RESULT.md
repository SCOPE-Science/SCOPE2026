# Exact finite-step covariance rank and a sharp volume bias for integrating-factor Lyapunov Runge–Kutta schemes

## Finding

For every integer \(d\ge2\), let \(A\in\mathbb R^{d\times d}\) have only real eigenvalues, let \(b\in\mathbb R^d\) be cyclic for \(A\), and set \(Q=bb^{\mathsf T}\), \(X(0)=0\) in
\[
\dot X=AX+XA^{\mathsf T}+bb^{\mathsf T}.
\]
"Cyclic" means the Kalman matrix \([b,Ab,\ldots,A^{d-1}b]\) is invertible. Apply the unmodified integrating-factor SSPRK2 and SSPRK3 schemes in Zhang–Lan–Jing [1] with exact matrix exponentials and any common step length \(h>0\). At the end of every integer number \(m\ge1\) of steps, their numerical covariance ranks are **exactly**
\[
\boxed{\operatorname{rank}X_m^{(2)}=\min\{d,m+1\},\qquad
\operatorname{rank}X_m^{(3)}=\min\{d,2m+1\}.}
\]
Meanwhile the exact solution \(X(mh)\) is positive definite for every \(h>0\) and \(m\ge1\). Thus IF-SSPRK2 first becomes positive definite at precisely \(m=d-1\) steps, and IF-SSPRK3 at precisely \(m=\lceil(d-1)/2\rceil\), regardless of the numerical step length or real eigenvalue spacing. Every earlier numerical covariance is singular despite exact strict positive definiteness.

The dimension-three nilpotent chain gives an exact one-step volume benchmark. For
\[
A=\begin{pmatrix}0&0&0\\1&0&0\\0&1&0\end{pmatrix},
\qquad b=(1,0,0)^{\mathsf T},
\]
the second-order one-step output has determinant zero, whereas
\[
\boxed{\det X_1^{(3)}=\frac{h^9}{3456},\qquad
\det X(h)=\frac{h^9}{8640},\qquad
\frac{\det X_1^{(3)}}{\det X(h)}=\frac52.}
\]
In particular, formal third-order matrix accuracy does not yield asymptotically correct *relative determinant* on the one-step \(h\downarrow0\) horizon from singular initialization. The factor \(5/2\) holds identically for all \(h>0\).

## Assumptions and scope

All matrices and arithmetic in the theorem are real and exact. The drift \(A\) is constant, has real spectrum (algebraic multiplicities and Jordan blocks are allowed), and \(b\) is cyclic. The forcing is constant and rank one; the initial state is zero. The time grid has \(m\) constant positive steps \(h\). The numerical methods are exactly the IF-SSPRK2 and IF-SSPRK3 Shu–Osher stages in equations (5)–(6) of [1], without low-rank truncation, approximate exponentials, stabilization, or postprocessing. Positive definiteness concerns the *completed step* and real exact arithmetic, not intermediate stages or the floating-point Cholesky safety margin.

The qualifier "real spectrum" is substantial: oscillatory conjugate eigenvalues can cause temporal aliasing of sampled forcing directions [2]. Nothing here claims unconditional strict positivity for arbitrary complex-spectrum controllable pairs.

## Proof

**1. Exact integrating-factor stage reduction.** Put
\[
W(t)=e^{-tA}X(t)e^{-tA^{\mathsf T}},\qquad
v(t)=e^{-tA}b,\qquad F(t)=v(t)v(t)^{\mathsf T}.
\]
Then \(W'=F(t)\), \(W(0)=0\). Because the transformed derivative depends on time but not on \(W\), direct substitution into the published Shu–Osher stages gives, on every panel,
\[
W_{j+1}^{(2)}=W_j^{(2)}+\frac h2\big[F(jh)+F((j+1)h)\big],
\]
and
\[
W_{j+1}^{(3)}=W_j^{(3)}+\frac h6\big[F(jh)+4F((j+\tfrac12)h)+F((j+1)h)\big].
\]
Consequently \(W_m^{(2)}\) is the composite trapezoidal Gramian at the \(m+1\) distinct times \(0,h,\ldots,mh\), with strictly positive weights \(h/2,h,\ldots,h,h/2\). The third-order matrix \(W_m^{(3)}\) is the composite Simpson Gramian at the \(2m+1\) distinct times \(0,h/2,h,\ldots,mh\), with strictly positive weights \(h/6,2h/3,h/3,\ldots,2h/3,h/6\). For *any* such finite positive weighted sum,
\[
\operatorname{rank}\Big(\sum_{\nu}w_\nu v(t_\nu)v(t_\nu)^{\mathsf T}\Big)
=\dim\operatorname{span}\{v(t_\nu)\}.
\]
Finally \(X_m^{(p)}=e^{mhA}W_m^{(p)}e^{mhA^{\mathsf T}}\); invertible congruence preserves rank and definiteness.

**2. Real-spectrum sampled-vector lemma.** For any \(d\) distinct real times \(t_1,\ldots,t_d\), the vectors \(e^{-t_jA}b\) are independent. Indeed, suppose a nonzero row vector \(z^{\mathsf T}\) annihilates all of them. The scalar function
\[
g(t)=z^{\mathsf T}e^{-tA}b
\]
has \(d\) distinct real zeros. Since \(A\) has only real eigenvalues, its real Jordan form expresses \(g\) as an exponential polynomial
\[
g(t)=\sum_{\ell=1}^r e^{-\lambda_\ell t}P_\ell(t),
\quad \lambda_\ell\in\mathbb R\ \text{distinct},
\quad \deg P_\ell<m_\ell,\quad \sum_{\ell=1}^r m_\ell=d.
\]
Here the sizes \(m_\ell\) are algebraic multiplicities, and one may take a zero polynomial for any missing contribution. The standard real exponential-polynomial zero bound says a nonzero such function has at most \(d-1\) distinct real zeros. For completeness, multiply by \(e^{\lambda_1t}\), differentiate \(m_1\) times to annihilate the first polynomial, and apply Rolle's theorem iteratively. Any \(d\) zeros would yield at least \(d-m_1\) zeros for the resulting sum of at most \(d-m_1\) real-exponent terms, contradicting the inductive bound unless that derivative is identically zero. In the latter case the original transformed function is a polynomial of degree below \(m_1\), which cannot possess \(d\) zeros unless zero. Induction starts with the ordinary polynomial zero bound for one exponent.

It follows that \(g\) must vanish identically. Differentiating at zero gives \(z^{\mathsf T}A^kb=0\) for \(k=0,\ldots,d-1\). Cyclicity forces \(z=0\), contradiction. This proves independent sampling at any \(d\) distinct times. For fewer \(K<d\) distinct times, extend the \(K\) times to a set of \(d\) distinct times; the original \(K\) vectors are a subset of an independent set, so have rank \(K\). For more than \(d\) distinct times, their span has rank \(d\). Therefore every finite distinct sample set of size \(K\) has rank exactly \(\min\{d,K\}\).

**3. Sharp rank staircase and exact positivity.** Apply the lemma to the \(m+1\) and \(2m+1\) positive-weight nodes from step 1. This gives the rank identities and exact step thresholds. For the continuous solution,
\[
W(T)=\int_0^T v(t)v(t)^{\mathsf T}\,dt,\qquad T>0.
\]
If \(z^{\mathsf T}W(T)z=0\), nonnegativity and continuity imply \(z^{\mathsf T}v(t)=0\) for every \(t\in[0,T]\). Analyticity and cyclicity then imply \(z=0\). Hence \(W(T)\succ0\), and its invertible congruence \(X(T)\) is also positive definite.

**4. Exact three-state determinant.** On the stated nilpotent chain, \(v(t)=(1,-t,t^2/2)^{\mathsf T}\). The Simpson one-panel Gramian is a three-column weighted Vandermonde Gram matrix at nodes \(0,h/2,h\), with weights \(h/6,2h/3,h/6\). Its sample matrix determinant has absolute value \(h^3/8\); the product of weights is \(h^3/54\). Hence
\[
\det W_1^{(3)}=\frac{h^3}{54}\Big(\frac{h^3}{8}\Big)^2
=\frac{h^9}{3456}.
\]
The trapezoidal one-panel Gramian has only two rank-one sample terms, so its determinant vanishes. Direct integration gives
\[
(W(h))_{ij}=\frac{(-1)^{i+j}h^{i+j+1}}{i!\,j!\,(i+j+1)},
\qquad i,j\in\{0,1,2\}.
\]
The determinant of the order-three Hilbert moment matrix \((1/(i+j+1))_{0\le i,j\le2}\) is \(1/2160\). Taking account of the factorial scaling yields \(\det W(h)=h^9/8640\). The matrix \(A\) has zero trace, so \(\det(e^{hA})=1\) and the congruence \(X=e^{hA}We^{hA^{\mathsf T}}\) leaves both determinants unchanged. Division proves the constant \(5/2\).

## Verification

The standalone `verify_rank.py` is a pure Python standard-library, exact-rational checker. It implements the published Shu–Osher stages separately from their composite quadrature reductions, compares the complete output matrices, and checks all exact rank predictions across dimensions \(2,\ldots,7\), five positive step counts, and three rational step lengths. It separately checks stable diagonal drifts at exact exponential sample times, finite-dimensional weighted Vandermonde determinant identities, the three-dimensional Simpson determinant \(1/3456\), and the integrated exact determinant \(1/8640\). The packaged checker reports `VERIFY_OK 248`. These finite checks support reproducibility; the universal claims follow from the preceding Chebyshev-zero and Gram-matrix proofs, not from enumeration.

## Relationship to prior work

Zhang, Lan and Jing [1] proposed the two methods, showed positive-semidefinite preservation, and established second-order error estimates; their published stage equations are used without modification here. Their inspected method, theorem, experiment, and conclusion sections do not give an arbitrary-dimension real-spectrum exact rank staircase, first strictly-positive time step, or the nilpotent three-state determinant ratio. The general real-exponential Chebyshev zero bound and Kalman controllability criterion are established mathematical tools and are not claimed as new.

The published planar-rotation analysis [2] derives exact covariance aliasing and eigenvalue crossover for the same integrators but addresses complex conjugate oscillatory modes in dimension two; it does not assert the all-real-spectrum, arbitrary-dimension no-aliasing rank theorem or the three-state determinant bias. The sampled Gaussian-quadrature analysis [3] examines one- through four-node Gauss–Legendre rules on a planar rotation, not these multistep SSPRK stage grids. The stationary two-mode Loewner comparison [4] examines forcing correlation and long-time covariance bias, not finite-step ranks. General sampled-system controllability theory [5] and real exponential-polynomial Chebyshev theory underpin parts of the argument; these generic principles may make the rank lemma accessible, but they do not themselves give the stated two-method sharp launch indices or the exact one-step volume factor.

## Limitations

The theorem requires a cyclic rank-one source, a drift with real eigenvalues, fixed positive steps, no low-rank approximation, and exact matrix exponentials. With non-real eigenvalues temporal aliasing may occur [2]. A noncyclic forcing direction, nonzero initial covariance, nonlinear or time-varying forcing, rounding, and actual Cholesky tolerance can change the rank behavior. Although the exact three-state ratio is \(5/2\) at every step length, it is not a claim about the global determinant convergence rate at a fixed terminal time. All historical-priority conclusions are best-knowledge comparisons of inspected sources; an earlier equivalent derivation may exist. Independent validation has not been performed.

## References

[1] W. Zhang, R. Lan, and X. Jing, *Strong Stability Preserving Integrating Factor Runge-Kutta Methods for Differential Lyapunov Equations with Positivity Preservation*, arXiv:2606.15703v1 (first publicly available 2026-06-14), https://arxiv.org/abs/2606.15703.

[2] *Exact covariance aliasing and a sharp ellipticity crossover for integrating-factor Lyapunov integrators*, published-finding corpus, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-covariance-aliasing-and-a-sharp-ellipticity-crossover-for--620c3297a160.

[3] *Four Gauss–Legendre Nodes Are the Minimal Resonance-Free Quadrature for a Planar Controllability Gramian*, published-finding corpus, 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-four-gauss-legendre-nodes-are-the-minimal-resonance-free-quadrat--8a559074bdfd.

[4] *A sharp covariance-order frontier for positivity-preserving IF-SSPRK2*, published-finding corpus, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-covariance-order-frontier-for-positivity-preserving-if-s--3f16ed31cfd1.

[5] A. Fúster-Sabater and J. M. Guillén, *Characterisation of observability and controllability for nonuniformly sampled discrete systems*, arXiv:1006.4288 (2010), https://arxiv.org/abs/1006.4288.
