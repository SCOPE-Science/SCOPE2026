# Codimension-controlled mean-square stability and transient growth in Gaussian control-variate zeroth-order descent

## Finding
For the Gaussian control-variate zeroth-order estimator with a fixed oracle reference in a \(k\)-dimensional hint subspace, the exact mean-square boundedness ceiling on the isotropic quadratic depends on the **unhinted codimension** \(m=d-k\), not the ambient dimension \(d\). With the source's forward-difference smoothing radius \(\tau>0\), the sharp normalized step-size boundary is
\[
0<\eta<\frac{2}{m+2}.
\]
At and beyond the boundary the second moments diverge, and the hinted/unhinted energy ratio approaches \(k/(m+1)\). Below the boundary the moments converge to explicitly computable nonzero stationary levels. A one-dimensional unhinted subspace can nevertheless generate arbitrarily large first-step amplification as the number of perfectly hinted coordinates increases.

## Assumptions and scope
Fix integers \(d\ge2\), \(1\le k<d\), and a fixed orthogonal projector \(P\in\mathbb R^{d\times d}\) of rank \(k\). Set \(Q=I_d-P\) and \(m=d-k\ge1\). Fix \(\lambda>0\), smoothing radius \(\tau>0\), and \(\eta>0\). The objective is the isotropic strongly convex quadratic \(f(x)=\lambda\|x\|^2/2\), whose minimizer is the origin. The exact oracle hint-reference is \(r_t=P\nabla f(x_t)=\lambda P x_t\). Given a fresh independent standard Gaussian \(u_t\sim N(0,I_d)\), use the **forward-difference** CV-ZOD estimator of Ryabchenko, Qian and Mou,
\[
 G(x,r;u)=r+\frac{f(x+\tau u)-f(x)-\tau\langle r,u\rangle}{\tau}u,
 \qquad x_{t+1}=x_t-\frac{\eta}{\lambda}G(x_t,r_t;u_t).
\]
The initial vector \(x_0\in\mathbb R^d\) is deterministic, all Gaussian probes are independent across iterations, and every expression is in exact real arithmetic. Define
\[
a_t=\mathbb E\|Px_t\|^2,\quad b_t=\mathbb E\|Qx_t\|^2,\quad D=(d+2)(d+4),\quad \rho=1-2\eta+(m+2)\eta^2.
\]
The full-hint limit \(k=d\), which lies outside the main quantifiers, has the ordinary deterministic contraction coefficient \((1-\eta)^2\) plus an additive smoothing-noise term and hence cutoff \(\eta=2\).

## Proof
**1. Exact stochastic update.** Write \(p=Px\), \(q=Qx\) and decompose \(u=v+w\), with \(v=Pu\) and \(w=Qu\); the Gaussian blocks are independent of dimensions \(k\) and \(m\). Since
\[
 f(x+\tau u)-f(x)=\lambda\tau\langle x,u\rangle+\frac{\lambda\tau^2}{2}\|u\|^2,
\]
the estimator and update are exactly
\[
 G=\lambda p+\lambda\langle q,w\rangle u+\frac{\lambda\tau}{2}\|u\|^2u,
\]
\[
 p'=(1-\eta)p-\eta\langle q,w\rangle v-\frac{\eta\tau}{2}\|u\|^2v,\qquad
 q'=q-\eta\langle q,w\rangle w-\frac{\eta\tau}{2}\|u\|^2w.
\]
**2. Gaussian moments and conditional second moments.** Orthogonal invariance and the independent-block Gaussian fourth moments yield
\[
\begin{aligned}
\mathbb E[\langle q,w\rangle^2\|v\|^2]&=k\|q\|^2,\\
\mathbb E[\langle q,w\rangle^2\|w\|^2]&=(m+2)\|q\|^2,\\
\mathbb E[\|u\|^4\|v\|^2]&=k(d+2)(d+4),\\
\mathbb E[\|u\|^4\|w\|^2]&=m(d+2)(d+4).
\end{aligned}
\]
The last identities follow by symmetry: \(\mathbb E[u_i^2\|u\|^4]=d^{-1}\mathbb E\|u\|^6=(d+2)(d+4)\). Mixed finite-difference cross terms vanish under \(u\mapsto-u\) (they are odd polynomials); centered Gaussian quadratic terms vanish in the other mixed terms. Conditioning on the past and taking expectations therefore gives the **exact**, all-time affine triangular recursion
\[
\boxed{\ b_{t+1}=\rho b_t+C_q,\qquad a_{t+1}=A a_t+\eta^2k b_t+C_p\ },
\]
where \(A=(1-\eta)^2\), \(C_q=\eta^2\tau^2mD/4>0\), and \(C_p=\eta^2\tau^2kD/4>0\).

**3. Sharp stability and stationary levels.** The scalar unhinted recurrence is stable precisely when \(\rho<1\), equivalently \(0<\eta<2/(m+2)\). This interval implies \(A<1\); hence both moments converge for every start to
\[
\boxed{\ b_\infty=\frac{\eta\tau^2mD}{4[2-(m+2)\eta]},\qquad
 a_\infty=\frac{\eta k}{2-\eta}b_\infty+\frac{\eta\tau^2kD}{4(2-\eta)}\ }.
\]
These levels are strictly positive. At \(\eta=2/(m+2)\) one has \(\rho=1\), hence \(b_t=b_0+tC_q\), growing linearly. If \(\eta>2/(m+2)\), then \(\rho>1\) and \(b_t=\rho^t(b_0+C_q/(\rho-1))-C_q/(\rho-1)\); the rate \(\rho\) is exact. Thus neither the boundary nor its exterior has finite limiting second moments, even from the zero start.

**4. Universal asymptotic energy partition.** A direct identity gives \(\rho-A=\eta^2(m+1)>0\). Put \(c=k/(m+1)=\eta^2k/(\rho-A)\) and \(z_t=a_t-cb_t\). The recursion reduces to \(z_{t+1}=Az_t+C_p-cC_q\). At the boundary, \(A<1\), so \(z_t\) remains bounded while \(b_t\to\infty\). Above the boundary, \(b_t\) grows like \(\rho^t\), whereas \(z_t\) grows at most as \(\max\{1,A\}^t\) or linearly in the exceptional case \(A=1\); as \(\rho>\max\{1,A\}\), \(z_t/b_t\to0\). Consequently
\[
\boxed{\ \frac{a_t}{b_t}\longrightarrow\frac{k}{m+1}\quad\text{for all }\eta\ge\frac{2}{m+2}.\ }
\]
**5. Arbitrarily large stable transient.** Take \(m=1\), \(k=d-1\), \(\eta=1/2<2/3\) and deterministic \(x_0\in\operatorname{ran}Q\) with \(\|x_0\|=1\). The same moment identity gives
\[
\mathbb E\|x_1\|^2=\frac{d+2}{4}+\frac{\tau^2}{16}d(d+2)(d+4).
\]
For \(x_0=0\) the first-step mean square equals only the second term. Their difference is exactly \((d+2)/4\), which is unbounded as \(d\to\infty\), even though both trajectories have finite limiting second moments at this fixed normalized step.

## Verification
The standalone `verify.py` performs Wick/Isserlis polynomial-moment checks in dimensions \(2\) through \(6\), numerical one-step Gaussian sampling comparisons for four dimension/split pairs, and exact symbolic checks of the stability and asymptotic-partition identities. Its execution produced `CHECKS_OK`. The proof above, not finite sampling, establishes all-dimensional and infinite-time assertions. Reproduce using `python verify.py` with NumPy and SymPy.

## Relationship to prior work
Ryabchenko, Qian and Mou (arXiv:2609.08277, first public 2026-09-08) introduce the exact estimator in Eq. (2), oracle projected-gradient hints in Eq. (4), and general finite-horizon high-probability and expected-stationarity inequalities in Sections 3--4; their source does not state this triangular exact second-moment phase diagram, the unhinted-codimension threshold, the divergent energy partition, or the stable transient witness. In particular, their general bounds concern different quantities and are not contradicted. Ghadimi and Lan (arXiv:1309.5549) provide classical Gaussian zeroth-order analysis without the same projected oracle-reference recurrence. Wang, Chakraborty and Shanbhag (arXiv:2604.15525) analyze a distinct exponentially shifted Gaussian estimator, not this CV-ZOD update. Standard Gaussian-moment identities are prior ingredients, not claimed innovations.

## Limitations
The exact result requires the **oracle** reference \(P\nabla f(x_t)\) and an invariant, fixed hint subspace, not the finite-difference reference estimate of practical CV-ZOD. The objective is quadratic, is not globally gradient-bounded, and hence does not satisfy the bounded-gradient assumption used for the source's general nonconvex guarantee; no implication about that theorem is drawn. The stability notion is finite limiting second moments about the minimizer under persistent finite-difference noise, not almost-sure convergence to the minimizer. There is no robustness assertion for inaccurate hints, other objectives, non-Gaussian probes, varying steps or finite precision. Historical-priority uncertainty remains for exact prior analyses of projected-control Gaussian quadratics.

## References
- A. Ryabchenko, J. Qian, and W. Mou, *Adaptively Incorporating Directional Hints into Zeroth-Order Optimization*, arXiv:2609.08277v1 (first public 2026-09-08), https://arxiv.org/abs/2609.08277.
- S. Ghadimi and G. Lan, *Stochastic First- and Zeroth-Order Methods for Nonconvex Stochastic Programming*, arXiv:1309.5549 (2013), https://arxiv.org/abs/1309.5549.
- M. Wang, P. Chakraborty, and U. V. Shanbhag, *Complexity Guarantees for Zeroth-order Methods via Exponentially-shifted Gaussian Smoothing*, arXiv:2604.15525 (2026), https://arxiv.org/abs/2604.15525.
