# Random-order instability of bounded alternating descent--ascent on a bilinear game

## Finding

**Theorem (complete-sweep order randomization).** Consider the unconstrained scalar zero-sum game
\[\min_{x\in\mathbb R}\max_{y\in\mathbb R}\,\kappa xy,\qquad \kappa>0.\]
Fix a step length \(\eta>0\), write \(t=\eta\kappa\), and assume \(0<t<2\). Each *complete* iteration updates both coordinates exactly once. With independent choices over iterations, process \(x\) before \(y\) with probability \(p\), and process \(y\) before \(x\) with probability \(1-p\), where \(p\in[0,1]\). In each case, the second gradient uses the **updated** first coordinate. Let \(z_n=(x_n,y_n)^\top\), with nonrandom initial state \(z_0\).

For either fixed order \(p\in\{0,1\}\), every trajectory is uniformly bounded over all \(n\ge0\). For **every** \(0<p<1\), there are constants \(r(p,t)>1\) and \(c(p,t)>0\), independent of \(n\) and \(z_0\), such that
\[\mathbb E\|z_n\|_2^2\ge c(p,t)\,r(p,t)^n\|z_0\|_2^2,\quad n\ge0.\]
In particular, *any* positive probability of choosing both orientations destroys mean-square power boundedness. At the balanced choice \(p=1/2\) there is the **exact identity**
\[\boxed{\mathbb E\|z_n\|_2^2=\left(1+\frac{t^4}{2}\right)^n\|z_0\|_2^2,\quad n=0,1,2,\ldots.}\]

## Assumptions and scope

These statements concern identical constant descent/ascent step sizes, deterministic exact gradients, independent full-sweep orientation choices, and Euclidean squared state error relative to the unique saddle \((0,0)\). There is no stochastic gradient noise and no coordinate omission. The restricted interval \(0<t<2\) is exactly the strict elliptic range of the two individual order maps; endpoint \(t=2\) is excluded because individual maps are defective and no longer power bounded.

## Proof

**1. The two maps and their conserved ellipses.** Set
\[A_t=\begin{pmatrix}1&-t\\t&1-t^2\end{pmatrix},\qquad B_t=\begin{pmatrix}1-t^2&-t\\t&1\end{pmatrix}.\]
The first is the \(x\)-then-\(y\) update, while the second is the \(y\)-then-\(x\) update. They both have determinant \(1\), trace \(2-t^2\), and therefore distinct nonreal conjugate eigenvalues of modulus one whenever \(0<t<2\). More explicitly, set
\[W_A=\begin{pmatrix}1&-t/2\\-t/2&1\end{pmatrix},\qquad W_B=\begin{pmatrix}1&t/2\\t/2&1\end{pmatrix}.\]
Both matrices are strictly positive definite and direct multiplication yields \(A_t^\top W_AA_t=W_A\) and \(B_t^\top W_BB_t=W_B\). Thus each fixed-order orbit lies in a bounded ellipse, uniformly in the number of sweeps.

**2. The balanced exact growth law.** Direct multiplication gives
\[\frac12(A_t^\top A_t+B_t^\top B_t)=\left(1+\frac{t^4}{2}\right)I_2.\]
Conditioning on \(z_n\) and using independence of the next orientation gives an exact conditional norm identity. Iterating conditional expectations proves the displayed formula for every \(n\ge0\).

**3. Exact second-moment operator for all biases.** Let \(C_n=\mathbb E[z_nz_n^\top]\), and define \(\Phi_p(C)=pA_tCA_t^\top+(1-p)B_tCB_t^\top\). With \(C=\begin{psmallmatrix}u&v\\v&w\end{psmallmatrix}\), its coordinate matrix on \((u,v,w)\) is
\[
L_p=\begin{pmatrix}
p+(1-p)(t^2-1)^2 & 2t\bigl((1-p)t^2-1\bigr)&t^2\\
t+(p-1)t^3&1-2t^2&pt^3-t\\
t^2&2t(1-pt^2)&1-p+p(t^2-1)^2
\end{pmatrix}.
\]
A symbolic determinant expansion gives the exact **sign certificate**
\[\boxed{\det(I_3-L_p)=-8p(1-p)t^6.}\]
The characteristic polynomial \(P(\lambda)=\det(\lambda I_3-L_p)\) is monic of degree three. When \(0<p<1\), \(P(1)<0\), while \(P(\lambda)>0\) for all sufficiently large positive \(\lambda\). Hence it has a real root greater than one, and the spectral radius \(r\) of the positive covariance operator \(\Phi_p\) satisfies \(r>1\).

**4. Why every nonzero deterministic initialization grows.** Consider the adjoint positive operator on real symmetric matrices, \(\Psi_p(W)=pA_t^\top WA_t+(1-p)B_t^\top WB_t\). It has the same spectral radius \(r>1\). In finite dimensions, a positive linear map on the positive-semidefinite cone possesses a nonzero positive-semidefinite eigenmatrix \(W\) for its spectral radius. For completeness, a direct argument uses the positive resolvents \(R_s=\sum_{j\ge0}s^{-j-1}\Psi_p^j(I_2)\) for \(s>r\). If \(R_s\) remained bounded as \(s\downarrow r\), its limit would satisfy \(\Psi_p(R)=rR-I_2\); since \(R\) is positive definite, this would imply \(\Psi_p(R)\preceq(r-\delta)R\) for some \(\delta>0\), contradicting the definition of spectral radius by the induced order-unit norm. Thus \(R_s/\operatorname{tr}R_s\) has a subsequential limit \(W\succeq0\) of trace one with \(\Psi_p(W)=rW\).

This \(W\) is in fact positive definite. Were it rank one, the positive-semidefinite summands in \(\Psi_p(W)=rW\) would force the range line of \(W\) to be invariant under \(A_t^\top\). But \(A_t^\top\) has no nonzero real eigenvector when \(0<t<2\). Thus \(W\succ0\). Write \(m=\lambda_{\min}(W)>0\), \(M=\lambda_{\max}(W)\). The conditional eigenmatrix relation implies
\[\mathbb E[z_n^\top Wz_n]=r^n z_0^\top Wz_0.\]
Since \(mI_2\preceq W\preceq MI_2\), it follows that
\[\mathbb E\|z_n\|_2^2\ge\frac{m}{M}r^n\|z_0\|_2^2.\]
This completes the proof.

## Verification

The standalone `verify.py` (Python 3, SymPy) checks symbolically the two update matrices, the two preserved quadratic forms, the balanced conditional-energy identity, the three-dimensional covariance transfer polynomial, and the exact sign certificate. Independent rational-arithmetic tests enumerate all random trajectories up to six sweeps for several rational step sizes and initial conditions. Run `python verify.py` in the directory containing this file. The analytic proof, not finite enumeration, establishes the infinite-horizon statements.

At the simple rational choice \(t=1\), both fixed-order maps are elliptic and preserve different positive quadratic forms, while for the fair mixture
\[\mathbb E\|z_n\|_2^2=\left(\frac32\right)^n\|z_0\|_2^2.\]

## Relationship to prior work

Zhang and Yu (2019/2020) analyze fixed-order Gauss--Seidel and simultaneous gradient algorithms for bilinear games; their unregularized alternating gradient method has bounded cyclic behavior. Zhang, Wang, Lessard and Grosse (2021) likewise emphasize bounded alternating dynamics in the purely bilinear example, and study convergence under additional curvature. Sebbouh, Cuturi and Peyré (2021) introduce a randomized method which randomly executes *one* coordinate/player update per iteration, in a nonconvex--strongly-concave setting. This is not independent random selection of the order of two completed updates. Nan, Das Gupta, Iyengar and Kroer (2025/2026) study fixed-order alternating bilinear play and ergodic guarantees, not i.i.d. orientation switching or the exact quadratic-moment growth displayed here.

The general principle that random products of individually bounded matrices can exhibit positive Lyapunov growth is classical. The contribution asserted here is the specifically motivated, exact all-bias moment-instability theorem for these two genuine minimax update orders, together with the explicit one-step conditional energy law and the strict contrast with both conserved deterministic ellipses. No claim is made that matrix-product instability is new as a general phenomenon.

## Limitations

The theorem does not assert almost-sure growth, any nonasymptotic high-probability bound, or analogous behavior for decreasing step sizes. It does not cover nonlinear or strongly convex--concave games, nonidentically distributed/correlated orientations, minibatch noise, or methods that update only one player per iteration. The mean-square rate at unequal probabilities is given implicitly by a finite-dimensional positive operator and is not given here in a closed elementary radical expression. An undiscovered specialist treatment of randomly switching symplectic Euler variants may cover some of these conclusions.

## References

- G. Zhang and Y. Yu, *Convergence of Gradient Methods on Bilinear Zero-Sum Games*, arXiv:1908.05699v1 (first public 2019-08-15); ICLR 2020. https://arxiv.org/abs/1908.05699
- G. Zhang, Y. Wang, L. Lessard and R. Grosse, *Near-optimal Local Convergence of Alternating Gradient Descent-Ascent for Minimax Optimization*, arXiv:2102.09468 (2021). https://arxiv.org/abs/2102.09468
- O. Sebbouh, M. Cuturi and G. Peyré, *Randomized Stochastic Gradient Descent Ascent*, arXiv:2111.13162 (2021). https://arxiv.org/abs/2111.13162
- T. Nan, S. Das Gupta, G. Iyengar and C. Kroer, *On the \(O(1/T)\) Convergence of Alternating Gradient Descent--Ascent in Bilinear Games*, arXiv:2510.03855 (2025); ICLR 2026. https://arxiv.org/abs/2510.03855
