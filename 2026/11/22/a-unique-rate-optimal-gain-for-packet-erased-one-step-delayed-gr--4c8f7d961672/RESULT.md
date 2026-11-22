# A unique rate-optimal gain for packet-erased one-step-delayed gradient descent

## Finding
Consider the scalar strongly convex quadratic \(f(x)=a x^2/2\), with \(a>0\), and the fixed-gain iteration
\[
X_{k+1}=X_k-h B_k X_{k-1},\qquad k\ge0,
\]
where \(h=a\eta>0\), the independent \(B_k\) have \(\Pr(B_k=1)=p\in(0,1)\), and the initial pair \((X_{-1},X_0)\ne(0,0)\) is deterministic. A missing packet means *no update*, not a fresh-gradient replacement. Whenever an update arrives, its gradient is one iteration old.

For every \(p\in(0,1)\) and \(h>0\), the limit
\[
\Lambda_p(h)=\lim_{k\to\infty}\bigl(\mathbb E X_k^2\bigr)^{1/k}
\]
exists, is independent of the nonzero initial pair, and equals the simple Perron eigenvalue of the exact second-moment transfer matrix
\[
M_p(h)=\begin{pmatrix}1&-2ph&ph^2\\1&-ph&0\\1&0&0\end{pmatrix}.
\]
Its characteristic equation is
\[
F_p(r,h)=r^3+(ph-1)r^2+ph(1-h)r-p^2h^3=0.
\]
The stability boundary, included here to delimit the rate optimization, is
\[
0<h<h_c(p),\qquad h_c(p)=\frac4{1+\sqrt{1+8p}}.
\]

**The sharp rate-tuning result:** among all positive constant gains, \(\Lambda_p(h)\) has a **unique** global minimum at the unique root \(h_*(p)\in(1/4,h_c(p))\) of
\[
\boxed{(1-p)^2h^3-8(1+p)h^2+8h-1=0.}
\]
The optimal gain strictly decreases with packet-delivery probability and obeys
\[
\lim_{p\downarrow0}h_*(p)=1,\qquad
\lim_{p\uparrow1}h_*(p)=\frac14.
\]
Its low-delivery asymptotics are \(h_*(p)=1-2p+5p^2+O(p^3)\) and \(\Lambda_p(h_*(p))=1-p+p^2+O(p^3)\). For every \(p\in(0,1)\), even optimally tuned stale packets are strictly slower than optimally tuned *fresh* Bernoulli-delivered gradients: \(\Lambda_p(h_*(p))>1-p\).

For instance, at \(p=1/2\) the unique rate-optimal gain is \(h_*=0.508001532586\ldots\), the best second-moment contraction is \(\Lambda=0.630225254562\ldots\), and the stability ceiling is \(\sqrt5-1=1.2360679775\ldots\). In contrast, without the one-step delay the optimum gain \(h=1\) gives contraction \(1-p=1/2\).

## Assumptions and scope
The samples \(B_k\) are independent of each other and of the pre-update states, with the same fixed success probability. The iteration uses the true, noiseless gradient of a scalar quadratic whenever it arrives, with fixed one-update staleness, unrescaled packets and a constant gain. The rate is the asymptotic factor per calendar update of the expected squared iterate, not the almost-sure Lyapunov exponent or the rate per successful packet. The strict theorem is stated for \(0<p<1\); the two limits describe approaching zero and perfect delivery, respectively. With exactly \(p=0\), the iteration never progresses; with \(p=1\), the deterministic lagged recurrence has its worst-initialization squared-state rate minimized by \(h=1/4\), although individual special initializations can have different rates.

## Proof
**1. Positive covariance transfer and the exact rate.** Set \(Y_k=(X_k,X_{k-1})^{\mathsf T}\). The erasure and delivery matrices are
\[
A_0=\begin{pmatrix}1&0\\1&0\end{pmatrix},\qquad
A_1=\begin{pmatrix}1&-h\\1&0\end{pmatrix}.
\]
The covariance map is \(T(C)=(1-p)A_0CA_0^{\mathsf T}+pA_1CA_1^{\mathsf T}\). Acting on the three entries \((\mathbb E X_k^2,\mathbb E[X_kX_{k-1}],\mathbb E X_{k-1}^2)\), it gives \(M_p(h)\) above. Its displayed characteristic polynomial follows by an exact determinant expansion.

For \(p\in(0,1)\), \(h>0\), \(T^3\) maps every nonzero positive semidefinite \(2\)-by-\(2\) matrix to a positive definite one. Indeed, for a rank-one vector \(v=(u,v_2)\), the images \(A_0v\) and \(A_1v\) are linearly independent if \(uv_2\ne0\). If \(v_2=0\), their common image is proportional to \((1,1)\), and the *next* pair of images is independent since \(h>0\). If \(u=0\), the first nonzero image is proportional to \((1,0)\), followed by the preceding two-step argument. Since \(A_1\) is invertible, later applications preserve strict positivity. Rank-one decompositions establish the claim for any nonzero semidefinite input. The Perron–Frobenius theorem for this primitive positive map therefore gives a simple strictly dominant positive eigenvalue \(\Lambda_p(h)\), positive left and right eigenmatrices, and the claimed limit for **every** nonzero deterministic initial pair.

**2. Exact stability interval.** Substitution into the characteristic polynomial yields
\[
F_p(1,h)=ph(2-h-ph^2).
\]
For small positive \(h\), perturbing the simple eigenvalue at \(h=0\) gives \(\Lambda_p(h)=1-2ph+O(h^2)<1\). The only positive nonzero solution of \(F_p(1,h)=0\) is \(h_c(p)\), and at that crossing
\[
\frac{\partial F_p}{\partial h}(1,h_c)=p(h_c-4)<0,
\]
while \(\partial_rF_p(\Lambda_p(h),h)>0\) by strict Perron dominance. Thus \(\Lambda_p(h)\) crosses from below to above one at \(h_c\), cannot cross back, and yields the sharp interval, including instability at its boundary.

**3. A uniform lower bound and the stationary equation.** Write \(z=ph>0\). Direct factorization gives
\[
64F_p(1/4,h)=-(4z-1)^2(4z+3)-\left(\frac1p-1\right)(16z^2+64z^3)<0.
\]
If all characteristic roots had modulus at most \(1/4\), the real monic cubic evaluated there would be nonnegative (positive for strict inequality); thus strict Perron dominance implies \(\Lambda_p(h)>1/4\). Differentiate its defining equation with respect to \(h\):
\[
\Lambda_p'(h)=-\frac{\partial_hF_p(\Lambda_p(h),h)}{\partial_rF_p(\Lambda_p(h),h)},
\quad
\frac{\partial_hF_p(r,h)}p=r^2+(1-2h)r-3ph^2.
\]
For \(0<h\le1/4\), the last expression is strictly positive at \(r=\Lambda_p(h)>1/4\), hence \(\Lambda'_p(h)<0\). Eliminating \(r\) from \(F_p(r,h)=0\) and \(\partial_h F_p(r,h)=0\) yields the exact resultant identity
\[
\operatorname{Res}_{r}\bigl(F_p,\,\partial_hF_p/p\bigr)
=4h^3p^2\,Q_p(h),\quad
Q_p(h)=(1-p)^2h^3-8(1+p)h^2+8h-1.
\]
Thus every stationary gain must be a positive zero of \(Q_p\).

**4. Root count and global optimality.** On \([0,h_c]\), one has \(Q_p''(h)=6(1-p)^2h-16(1+p)<0\), since \(h_c<2\). Also
\[
Q_p(0)=-1,\qquad Q_p(1/4)=\frac{(1-p)(33-p)}{64}>0.
\]
At \(h=h_c\), substitute \(p=(2-h_c)/h_c^2\) to obtain
\[
Q_p(h_c)=\frac{(h_c-4)(h_c^3-2h_c^2+5h_c-1)}{h_c}<0.
\]
Indeed \(1<h_c<2\) and the second factor is positive. Strict concavity gives exactly one zero below \(1/4\) and exactly one above it but below \(h_c\). The first cannot be stationary for \(\Lambda_p\) by step 3. At \(h=h_c\), the derivative \(\Lambda'_p(h_c)>0\), so the second root must be its unique stationary point in \((0,h_c)\), a strict global minimum there. Since \(\Lambda_p(h)>1\) for all \(h>h_c\), the same point is the unique global minimum over all \(h>0\).

**5. Dependence on reliability and the fresh-packet gap.** The larger root lies on the strictly decreasing branch of \(Q_p\). Since \(\partial_pQ_p=-2(1-p)h^3-8h^2<0\), implicit differentiation gives \(h_*'(p)=-\partial_pQ_p/\partial_hQ_p<0\). The endpoints and expansions follow by substitution into \(Q_p(h_*)=0\) and \(F_p(\Lambda_p(h_*),h_*)=0\); the low-\(p\) branch tends to the middle positive root \(h=1\) of \(Q_0\). Finally, \(T\) dominates the erasure-only map \(C\mapsto(1-p)A_0CA_0^{\mathsf T}\). Applying the strictly positive left Perron functional of \(T\) to the nonzero rank-one matrix \((1,1)(1,1)^{\mathsf T}\) gives \(\Lambda_p(h)>1-p\), because the additional delivered contribution is strictly positive. Fresh-dropout iteration \(X_{k+1}=(1-hB_k)X_k\) instead has exact factor \(1-2ph+ph^2\), uniquely minimized at \(h=1\) with factor \(1-p\).

## Verification
The standalone `verify.py` checks the three-moment matrix and characteristic polynomial exactly; the stability factorization; the resultant defining the unique optimizer; the critical signs at \(h=1/4\) and \(h=h_c\); and rational independent branch enumeration through five updates. It also compares the cubic optimizer against direct spectral minimization for 99 delivery probabilities. `requirements.txt` records the software versions tested. Finite computations do not prove primitivity, concavity or global optimality; the proof above supplies those quantified arguments.

## Relationship to prior work
Arjevani, Shamir and Srebro (2018/2020) study tight convergence of consistently delayed gradient descent on quadratics, with and without additive stochastic gradient noise; their delay-one recursion always applies an update, rather than erasing it independently. Wu, Magnusson, Feyzmahdavian and Johansson (2022) give general delay-adaptive step-size guarantees for asynchronous optimization, but no exact rate-optimal fixed gain for the erasure-plus-one-lag scalar recurrence. Su, Li and Lu (2021) study i.i.d. random channel-induced delays and packet drops using a general frequency-domain mean-square input-output stability criterion; their optimization is of controller stabilizability, not the asymptotic iterate second-moment rate for a prescribed scalar gradient-feedback law. The published result *Exact quadratic energy and the sharp mean-square frontier for Bernoulli stale-gradient descent* (2026) analyzes random **fresh versus stale** updates. Its published stability inequality \(qz^2+z<2\) is **algebraically identical to the stability boundary above under \(q=p, z=h\)**. The boundary formula is therefore **not claimed to be novel**. Nevertheless the two recursions have different covariance transfer matrices: for the published fresh-or-stale rule, its \((1,1)\) moment coefficient is \((1-p)(1-h)^2+p\), while ours is exactly \(1\); the fresh-or-stale \((2,1)\) coefficient is \((1-p)(1-h)+p\), while ours is exactly \(1\). The strict rate-optimality formula is not a corollary of a common stability boundary. At \(p=1/2\), direct spectral analysis gives the **fresh-or-stale** optimal gain \(0.381966\ldots\) and factor \(0.309016\ldots\), versus the erased-or-stale gain \(0.508001\ldots\) and factor \(0.630225\ldots\) proved here. The second published result *A three-objective conflict for Bernoulli-erased heavy-ball optimization* (2026) considers random **fresh versus erased** gradients with momentum and no fixed one-step lag. Gomez, Qin, Orosz and Murray (2014) already establish the general lifted-second-moment method for randomly delayed linear systems and exact stability regions; that general method and its covariance lift are likewise not claimed to be novel. Their fixed-coefficient model does not state the optimized erased-versus-stale scalar rate, its cubic or its reliability monotonicity. A general random-packet control theorem can imply an implicit lifted-covariance stability test but does not by itself identify the specific minimizing root or strict monotone calibration law proved here.

## Limitations
This is an exact scalar, constant-gain, iid-packet model; it does not address arbitrary nonlinear or multidimensional objectives, noise in delivered gradients, correlated losses, variable delays, adaptive gains, or wall-clock throughput. Optimizing the asymptotic second-moment rate is not the same as optimizing a fixed finite horizon or almost-sure convergence. Related random-switching control literature might contain equivalent specialized results not located in the inspected papers; independent historical-priority validation remains open.

## References
- Y. Arjevani, O. Shamir, N. Srebro, *A Tight Convergence Analysis for Stochastic Gradient Descent with Delayed Updates*, first arXiv release June 26, 2018, https://arxiv.org/abs/1806.10188 ; full text https://proceedings.mlr.press/v117/arjevani20a/arjevani20a.pdf.
- X. Wu, S. Magnusson, H. R. Feyzmahdavian, M. Johansson, *Delay-Adaptive Step-sizes for Asynchronous Learning*, 2022, https://proceedings.mlr.press/v162/wu22g/wu22g.pdf.
- M. M. Gomez, W. B. Qin, G. Orosz, R. M. Murray, *Exact Stability Analysis of Discrete-Time Linear Systems with Stochastic Delays*, American Control Conference (2014), https://websites.umich.edu/~orosz/articles/ACC_2014_paper2.pdf (full paper inspected; general lifted-moment technique is prior work).
- W. Su, J. Li, J. Lu, *Mean-Square Input-Output Stability and Stabilizability of a Networked Control System with Random Channel Induced Delays*, first arXiv release August 29, 2021, https://arxiv.org/abs/2108.12795 (relevant sections and theorem inspected).
- J. Xu, H. Zhang, G. Gu, Y. Tang, *Stabilization of Discrete-Time Systems with Random Delays and Packet Drops: A Predictor-Like Controller*, 2023, https://doi.org/10.1137/22M1496062 (abstract inspected; full paper not read).
- *Exact quadratic energy and the sharp mean-square frontier for Bernoulli stale-gradient descent*, public research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-quadratic-energy-and-the-sharp-mean-square-frontier-for-be--1b8d6aef9d3a/RESULT.md.
- *A three-objective conflict for Bernoulli-erased heavy-ball optimization*, public research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-three-objective-conflict-for-bernoulli-erased-heavy-ball-optim--11f2caf45cc5/RESULT.md.
