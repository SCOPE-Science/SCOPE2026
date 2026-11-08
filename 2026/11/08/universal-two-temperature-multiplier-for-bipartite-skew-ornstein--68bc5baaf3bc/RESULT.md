# Universal two-temperature multiplier for bipartite skew Ornstein–Uhlenbeck networks

## Finding
Let \(p,q\ge 1\), \(A=A^{\mathsf T}\succ0\) on \(\mathbb R^p\), \(C=C^{\mathsf T}\succ0\) on \(\mathbb R^q\), and \(B\in\mathbb R^{p\times q}\). For the stationary diffusion
\[
 dX_t=M X_t\,dt+\sqrt{2D}\,dW_t,\qquad
 M=\begin{pmatrix}-A&-B\\ B^{\mathsf T}&-C\end{pmatrix},\quad
 D=\operatorname{diag}(T_+ I_p,T_- I_q),\quad T_+,T_->0,
\]
write \(\Phi(T_+,T_-)\) for the stationary, all-coordinates-even entropy-production rate. Then
\[
 \boxed{\Phi(T_+,T_-)=\frac{(T_++T_-)^2}{4T_+T_-}\Phi(1,1).}
\]
This holds at arbitrary finite dimension and coupling strength, including noncommuting symmetric relaxation matrices. If \(B\ne0\), then \(\Phi(1,1)>0\), and unequal group temperatures strictly increase dissipation. For any parameterized family of such drifts (independent of temperature), all minimizing or maximizing drift-parameter choices are **identical** at every positive temperature ratio, provided the admissible parameter set is the same. This last assertion concerns argmin/argmax sets where they exist; it does not assert the existence or uniqueness of an optimizer.

## Assumptions and scope
The noise amplitudes are uniform within each of two coordinate groups, with independent isotropic Wiener components. Within each group the deterministic linear relaxation is symmetric positive definite, while inter-group deterministic coupling is skew-adjoint: the upper-right block is \(-B\), and the lower-left is \(B^{\mathsf T}\). All coordinates have even time-reversal parity, and the stated rate is the standard stationary Fokker–Planck current quadratic form. Friction, temperature calibration and time-reversal convention are held fixed as specified. The result does not cover arbitrary nonreciprocal cross-block coupling, intra-group rotational drift, unequal temperatures within a group, odd-parity velocity coordinates, or non-Gaussian forcing.

The symmetric part \((M+M^{\mathsf T})/2=-\operatorname{diag}(A,C)\) is negative definite, so \(M\) is Hurwitz. The unique stationary covariance \(S\succ0\) solves \(MS+SM^{\mathsf T}=-2D\). The irreversible-current matrix \(Q=MS+D\) is antisymmetric, and
\[
 \Phi=\operatorname{tr}\bigl(S^{-1}Q^{\mathsf T}D^{-1}Q\bigr)\ge0.
\]

## Proof
Set \(J=\operatorname{diag}(I_p,-I_q)\). Direct block transposition gives \(M^{\mathsf T}J=JM\). Let \(S_0\) denote the covariance for diffusion \(I\) and \(Q_0=MS_0+I\). Define
\[
 \alpha=\frac{T_++T_-}{2},\quad \beta=\frac{T_+-T_-}{2},\quad
 \delta=\alpha^2-\beta^2=T_+T_->0,
 \qquad R=-M^{-1}J.
\]
Since \(M^{\mathsf T}J=JM\), matrix \(R\) is symmetric and satisfies \(MR=RM^{\mathsf T}=-J\). Uniqueness in the Lyapunov equation therefore implies the **exact covariance and current decompositions**
\[
 S=\alpha S_0+\beta R,\qquad Q=MS+D=\alpha Q_0.
\]
(The displayed covariance is positive definite by the stationary Lyapunov integral; the individual summand \(R\) need not be positive.)

For any positive definite diffusion matrix, expansion of the current quadratic form together with \(MS+SM^{\mathsf T}=-2D\) yields
\[
 \Phi=\operatorname{tr}(M^{\mathsf T}D^{-1}MS)+\operatorname{tr}M.
\tag{1}
\]
Indeed, the expansion has two cross terms \(2\operatorname{tr}M\) and a final term \(\operatorname{tr}(S^{-1}D)=-\operatorname{tr}M\).

Let \(X=\operatorname{tr}(M^{\mathsf T}MS_0)\) and \(Y=\operatorname{tr}(M^{\mathsf T}JMS_0)\). Multiplying \(MS_0+S_0M^{\mathsf T}=-2I\) by \(JM\), taking traces, and using \(M^{\mathsf T}J=JM\) gives \(Y=-\operatorname{tr}(JM)\). Directly from \(R=-M^{-1}J\) one also has
\[
 \operatorname{tr}(M^{\mathsf T}MR)=Y,
 \qquad\operatorname{tr}(M^{\mathsf T}JMR)=-\operatorname{tr}M.
\]
Because \(D^{-1}=(\alpha I-\beta J)/\delta\), substitution into (1) cancels both mixed \(\alpha\beta\) terms:
\[
 \begin{aligned}
 \Phi(T_+,T_-)
 &=\frac{\alpha^2 X+\beta^2\operatorname{tr}M}{\delta}
       +\operatorname{tr}M\\
 &=\frac{\alpha^2}{\delta}\bigl(X+\operatorname{tr}M\bigr)
 =\frac{\alpha^2}{T_+T_-}\Phi(1,1).
 \end{aligned}
\]
Finally, \(\Phi(1,1)=0\) implies \(Q_0=0\) by positive definiteness. Hence \(MS_0=-I\), so \(M=-S_0^{-1}\) is symmetric. This is impossible if \(B\ne0\). Conversely if \(B=0\), \(M\) and \(D\) are blockwise commuting symmetric matrices, giving \(Q=0\) and zero EPR. The multiplier equals \(1+(T_+-T_-)^2/(4T_+T_-)\), proving strictness and preservation of optimizer sets.

## Verification
The accompanying `verify.py` uses only the Python standard library and exact rational Gaussian elimination to solve the finite-dimensional Lyapunov and inverse-matrix systems separately from the stated trace proof. It checks \(S=\alpha S_0+\beta R\), \(Q=\alpha Q_0\) and the EPR multiplier for 96 nontrivial combinations covering dimensions two through five, nonzero cross couplings, and non-diagonal within-group symmetric positive definite relaxation matrices; two separate decoupled examples verify \(\Phi=0\). A further exact-rational boundary example with non-symmetric intragroup relaxation violates the factorization, confirming that the structural hypothesis cannot simply be dropped. All 99 cases passed. Finite computations corroborate but do not establish the continuum-of-parameters claim; the matrix argument above is the proof.

## Relationship to prior work
Kharbanda, Burnet and Sabass (arXiv:2610.37030, first submitted 2026-10-27), in their two-dimensional modal formula (their Eq. (13)), already imply the **\(p=q=1\) instance** when their cross-coupling coefficients coincide. The two-variable factor is explicitly **not new**. That paper studies suppression of irreversible circulation by reciprocal diffusive inter-system couplings and residual strong-coupling limits; its differently heated *subsystems* may acquire additional non-diagonal diffusion terms and strong-coupling heat flux. The statement proved here instead treats skew-adjoint coupling between coordinate classes at equal diffusion within each class, for arbitrary dimensions, arbitrary internal symmetric coupling, and all finite interaction strengths. The paper's higher-dimensional treatment does not give this dimension-independent scalar thermal-contrast law.

Godrèche and Luck (arXiv:1807.00694, Sec. 2) derive general multivariate Ornstein–Uhlenbeck current and EPR matrix expressions, which are used as standard background here. Their later temperature-inhomogeneous resistor-array examples (Sec. 5) are different: the drift is symmetric and the temperature variation itself produces irreversibility. Their general formulas admit specialization, so a broad conceptual-priority risk remains; they do not state the block-sign-adjoint thermal multiplier or its parameter-optimizer consequence in the inspected text. A previously available result for a particular three-variable **isothermal** skew OU chain determines a damping optimum. That is prior coverage of the isothermal example, not of the arbitrary-dimensional two-temperature factorization or optimizer invariance. No new isothermal optimum is claimed.

## Limitations
This is a statement about the mathematical stationary-current EPR in the specified even-variable diffusion, not a general physical heat-flow theorem for arbitrary Langevin networks or variables with odd time-reversal parity. Its multiplier relies essentially on simultaneous \(M^{\mathsf T}J=JM\) and \(D=\alpha I+\beta J\); violating either condition can break factorization. For a concrete failure outside the class, take \(M=\begin{psmallmatrix}-2&-1&-1\\1&-2&0\\1&0&-2\end{psmallmatrix}\), with the first two coordinates in the \(T_+\) group and the third in the \(T_-\) group. Its intragroup skew component violates \(M^{\mathsf T}J=JM\). Direct rational Lyapunov calculation gives \(\Phi(1,1)=2\), but \(\Phi(1,2)=307/144\ne9/4\), the latter being the factorization prediction. General OU EPR formulas precede this result, the two-dimensional specialization is explicitly covered by the motivating paper, and unlocated earlier higher-dimensional symmetry-specific formulations remain a publication-priority risk.

## References
1. V. Kharbanda, A. F. Burnet and B. Sabass, *Residual dynamics determine dissipation in strongly coupled linear Langevin systems*, arXiv:2610.37030v1 (first submitted 2026-10-27), https://arxiv.org/html/2610.37030v1 .
2. C. Godrèche and J.-M. Luck, *Characterising the nonequilibrium stationary states of Ornstein-Uhlenbeck processes*, arXiv:1807.00694v2 (first submitted 2018-07-02), https://arxiv.org/html/1807.00694v2 .
