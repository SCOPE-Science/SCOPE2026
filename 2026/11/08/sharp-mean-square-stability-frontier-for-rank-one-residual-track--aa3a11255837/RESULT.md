# Sharp mean-square stability frontier for rank-one residual-tracking Kaczmarz

## Finding

For the unaccelerated uniform-singleton residual-tracking Kaczmarz (VRRK-AS), the sharp mean-square stability threshold on \(m\) identical scalar rows is

\[
\boxed{\alpha_*(m)=\frac{m-2+\sqrt{(m-2)^2+\frac{8m(m-1)}{2m-1}}}{2m(m-1)}}\qquad(m\ge2).
\]

The full stochastic error state is geometrically mean-square stable for **every** initialization precisely when \(0<\alpha<\alpha_*(m)\). At the threshold, some starts do not decay in mean square; for every greater step some starts have exponentially growing mean-square error. For the residual-tracker initialization specified in the motivating algorithm, the same **if-and-only-if** convergence frontier holds whenever the least-squares solution is nonzero. The result gives a sharp rate-calibration limit for a fully coherent, potentially inconsistent rank-one system; it does not imply a universal upper bound for other matrices.

## Assumptions and scope

Fix an integer \(m\ge2\), the matrix \(A=\mathbf1_{m\times1}\), and arbitrary real \(b_1,\ldots,b_m\). The unique least-squares minimizer is \(x_*:=\bar b=m^{-1}\sum_{i=1}^m b_i\); the optimal residual components are \(r_i^*=x_*-b_i\). At each iteration an index \(I_k\) is drawn independently and uniformly from \(\{1,\ldots,m\}\). The unaccelerated, with-replacement, non-stopping residual-tracking update, in this specialization, is

\[
\begin{aligned}
x_{k+1}&=x_k-\alpha\left[m\bigl((x_k-b_{I_k})-\bar r_{I_k,k}\bigr)+\sum_{j=1}^m\bar r_{j,k}\right],\\
\bar r_{I_k,k+1}&=x_k-b_{I_k},\qquad
\bar r_{j,k+1}=\bar r_{j,k}\quad(j\ne I_k).
\end{aligned}
\]

All updates on the right use the pre-update iterate and residual table. This is the exact uniform singleton specialization of the source's Algorithm 1 and of the SAGA/JacSketch estimator, not ordinary randomized Kaczmarz. The original implementation initializes \(x_0=0\) and \(\bar r_{i,0}=-b_i\). The general full-state claim permits arbitrary finite deterministic initial values. The norm under discussion is the Euclidean norm squared of the scalar iterate error and all \(m\) residual-table errors, **not** a finite-time objective-monotonicity guarantee.

Define \(e_k=x_k-x_*\), \(s_{i,k}=\bar r_{i,k}-(x_*-b_i)\), \(t_k=m^{-1}\sum_i s_{i,k}\), and \(V_k=m^{-1}\sum_i(s_{i,k}-t_k)^2\). Write \(c=1-m\alpha\). Then, for each sampled index \(i\),

\[
e_{k+1}=c e_k+m\alpha(s_{i,k}-t_k),\qquad
s_{i,k+1}=e_k,\qquad s_{j,k+1}=s_{j,k}\ (j\ne i).
\]

For the original initialization, \(e_0=s_{1,0}=\cdots=s_{m,0}=-x_*\). If \(x_*=0\), the initialized state is already an exact fixed point for every stepsize; this exception is excluded when asserting a sharp threshold for that *particular* start.

## Proof

**Exact four-moment closure.** Set \(u_k=(\mathbb E e_k^2,\mathbb E[e_k t_k],\mathbb E t_k^2,\mathbb E V_k)^\top\). Conditional on the current state, uniform sampling gives

\[
\mathbb E_i(e')^2=c^2e^2+m^2\alpha^2V,
\qquad
\mathbb E_i(e't')=\frac{c}{m}e^2+\frac{c(m-1)}m et-\alpha V.
\]

Using \(t'=t+(e-s_i)/m\) and expanding the updated table variance yields the **exact**, not upper-bounding, recurrence \(u_{k+1}=M_m(\alpha)u_k\) with

\[
M_m(\alpha)=\begin{pmatrix}
c^2&0&0&m^2\alpha^2\\
c/m&c(m-1)/m&0&-\alpha\\
1/m^2&2(m-1)/m^2&(m-1)^2/m^2&1/m^2\\
(m-1)/m^2&-2(m-1)/m^2&(m-1)/m^2&(m^2-m-1)/m^2
\end{pmatrix}.
\]

Straight symbolic elimination gives

\[
\det(I-M_m(\alpha))=-\frac{2\alpha}{m^2}P_m(\alpha),\quad
P_m(\alpha)=m(m-1)(2m-1)\alpha^2-(m-2)(2m-1)\alpha-2.
\]

The polynomial has one positive root, exactly \(\alpha_*(m)\). It satisfies \(m^{-1}<\alpha_*(m)<2m^{-1}\), since \(P_m(m^{-1})=-m^{-1}<0\) and \(P_m(2m^{-1})=4m-4>0\).

**Why the moment spectral radius controls *all* initial conditions.** Let \(Y=(e,s_1,\ldots,s_m)^\top\). Each sample acts by a real matrix \(B_i\), so the covariance map \(\mathcal T(C)=m^{-1}\sum_iB_iCB_i^\top\) preserves the cone of positive-semidefinite matrices. Its adjoint is also positivity preserving. The finite-dimensional Perron–Frobenius theorem for a proper invariant cone gives a nonzero positive-semidefinite eigenmatrix at the nonnegative real spectral radius \(\rho(\mathcal T)\). Permuting table coordinates commutes with \(\mathcal T\); averaging this positive eigenmatrix over all such permutations leaves a nonzero positive eigenmatrix. The four permutation-invariant symmetric quadratic observables are spanned by \(e^2,et,t^2,V\); their exact dual action is the transpose of \(M_m(\alpha)\). The symmetric covariance subspace is their dual, and hence \(\rho(\mathcal T)\) is an eigenvalue of \(M_m(\alpha)\). Conversely that four-dimensional invariant dual subspace has no eigenvalues larger in modulus than \(\mathcal T\). Thus

\[
\rho(\mathcal T)=\rho(M_m(\alpha)).
\]

At \(\alpha=0\) the characteristic polynomial is

\[
\det(zI-M_m(0))=
\frac{(z-1)(mz-m+1)^2(mz-m+2)}{m^3}.
\]

The simple eigenvalue at one has analytic perturbation derivative \(\left.\frac{dz}{d\alpha}\right|_{0}=-2m\). All other eigenvalues at zero stepsize have modulus less than one for \(m\ge2\), so \(\rho(\mathcal T)<1\) for all sufficiently small positive \(\alpha\). If the spectral radius were to reach or cross one at any smaller positive step than \(\alpha_*(m)\), the cone Perron eigenvalue would be real and equal to one at the first crossing. That would force \(\det(I-M_m(\alpha))=0\), contradicted by its only positive zero. Therefore \(\rho<1\) throughout \(0<\alpha<\alpha_*(m)\), and \(\rho=1\) at the boundary by continuity. Above it \(P_m(\alpha)>0\), hence \(\det(I-M_m(\alpha))<0\); the monic quartic \(\det(zI-M_m(\alpha))\) must then have a real root \(z>1\). Consequently \(\rho>1\), excluding reentrant stability.

The full second moment converges geometrically to zero for every initial \(Y_0\) exactly if \(\rho(\mathcal T)<1\). At and beyond the frontier, a nonzero positive-semidefinite Perron eigenmatrix of the adjoint provides an initial state with nonvanishing, respectively exponentially increasing, second moment (the span of rank-one positive matrices is the whole symmetric matrix space).

**The source's actual initialization is not exceptional when \(x_*\ne0\).** Normalize the initial state to \(Y_0=(1,\mathbf1_m)\), since scaling by \(-x_*\) does not affect stability. The first update gives \(Y_1=(c,\mathbf1_m)\); at the second update, selecting any index \(i\) gives \(Y_{2,i}=(c^2,\mathbf1_m+(c-1){\bf e}_i)\), where the standard coordinate vector \({\bf e}_i\) refers only to the residual table. Because \(c-1=-m\alpha\ne0\), these \(m+2\) reachable vectors span \(\mathbb R^{m+1}\): differences of the second-step vectors span the tracker zero-sum subspace, the first-step difference supplies the primal coordinate, and the initial state supplies the common tracker direction.

For \(\alpha\ge\alpha_*(m)\), choose a nonzero positive-semidefinite eigenmatrix \(Q\) of the adjoint covariance map satisfying \(\mathcal T^*(Q)=\rho Q\), with \(\rho\ge1\). If \(Y_0^\top QY_0\) vanished, positivity would force every reachable vector through two steps into \(\ker Q\), contradicting their span. Hence \(Y_0^\top QY_0>0\) and

\[
\mathbb E\|Y_k\|_2^2\ge
\frac{Y_0^\top QY_0}{\|Q\|_{\rm op}}\,\rho^k.
\]

This gives persistent positive second moment at the threshold, exponential growth beyond it, for every original initialization with \(x_*\ne0\). Further, a table coordinate updated with probability \(1/m\) each step satisfies

\[
\mathbb E s_{i,k}^2=(1-1/m)^k s_{i,0}^2+
\frac1m\sum_{j=0}^{k-1}(1-1/m)^{k-1-j}\mathbb E e_j^2.
\]

If the primal mean-square error tended to zero, this geometric convolution would force every table second moment to zero as well, contradicting the lower bound. Thus the *primal* mean-square convergence criterion for the prescribed nonzero-solution initialization is also necessary and sufficient.

**Comparison scale.** The source's Remark 3.3 specifies \(\alpha_{\rm suff}=1/[m(m+4)]\) on this matrix, whereas

\[
\alpha_*(m)=m^{-1}+\frac{1}{2m^3}+\frac{1}{4m^4}+O(m^{-5}),
\quad
\frac{\alpha_*(m)}{\alpha_{\rm suff}}=m+4+O(m^{-1}).
\]

This compares its stated conservative sufficient choice to the exact stability boundary, not the fastest expected convergence step or an optimal complexity guarantee.

## Verification

The standalone `verify.py` derives the determinant and characteristic polynomial symbolically with SymPy, checks the moment closure by exact rational substitution for nonexchangeable starting tables, enumerates small finite sample-word trees, and evaluates spectra numerically on both sides of the threshold. It reports 354 checks. These finite tests check algebra and examples only; they do not establish infinite-horizon convergence or priority. The cone spectral-radius argument and reachable-state spanning proof supply those analytic parts.

## Relationship to prior work

Xie, Qi, and Han [1], Algorithm 1, Theorem 3.2, Remark 3.3 and Proposition 3.4, define the residual tracker, establish sufficient stochastic convergence, and prove the JacSketch correspondence. Defazio, Bach and Lacoste-Julien [2] introduce SAGA and sufficient convergence rates. Gower, Richtárik and Bach [3] prove general JacSketch guarantees; Gazagnadou, Gower and Salmon [4] refine minibatch SAGA stepsizes. None of the inspected relevant portions supplies the present exact necessary-and-sufficient coherent-row cutoff or the nondecay statement for the specified initialization. General second-moment operator techniques are classical; the mathematical contribution assessed here is the exact four-moment reduction, positive-root frontier and boundary classification for this particular algorithm and input family.

## Limitations

The result assumes a single scalar unknown, exactly equal unit rows, independent uniform singleton sampling, constant positive stepsize and the unaccelerated update. It neither settles arbitrary matrices, nonuniform sketches, mini-batches or momentum, nor estimates wall-clock performance. All claims concern mean-square expectations in exact arithmetic, not almost-sure divergence. Independent historical-priority confirmation and independent mathematical audit have not been performed. Equivalent older specialized SAGA calculations may exist despite the available searches.

## References

[1] J. Xie, H.-D. Qi, D. Han, *Efficient variance reduction for randomized Kaczmarz methods via residual-tracking control variates*, arXiv:2610.39537, first posted 2026-10-29, https://arxiv.org/abs/2610.39537.

[2] A. Defazio, F. Bach, S. Lacoste-Julien, *SAGA: A Fast Incremental Gradient Method With Support for Non-Strongly Convex Composite Objectives*, arXiv:1407.0202, https://arxiv.org/abs/1407.0202.

[3] R. M. Gower, P. Richtárik, F. Bach, *Stochastic quasi-gradient methods: variance reduction via Jacobian sketching*, Mathematical Programming, DOI:10.1007/s10107-020-01506-0, https://doi.org/10.1007/s10107-020-01506-0.

[4] A. Gazagnadou, R. M. Gower, J. Salmon, *Optimal Mini-Batch and Step Sizes for SAGA*, arXiv:1902.00071, https://arxiv.org/abs/1902.00071.

[5] G. Mulayoff, T. Michaeli, *Exact Mean Square Linear Stability Analysis for SGD*, arXiv:2306.07850, https://arxiv.org/abs/2306.07850.
