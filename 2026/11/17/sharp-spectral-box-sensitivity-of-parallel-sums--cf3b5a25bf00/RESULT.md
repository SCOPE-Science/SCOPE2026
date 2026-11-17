# Sharp spectral-box sensitivity of parallel sums

## Finding

Let \(\mathcal H\) be a real or complex Hilbert space of dimension at least two. For each fixed \(\kappa>1\), let \(\mathcal P_\kappa\) be the bounded self-adjoint operators satisfying \(I\preceq A\preceq\kappa I\). For strictly positive operators put
\[
\Phi(A,B)=(A^{-1}+B^{-1})^{-1}=B-B(A+B)^{-1}B.
\]
The **sharp uniform one-sided operator-norm Lipschitz constant** of \(A\mapsto\Phi(A,B)\), allowing all \(A_1,A_2,B\in\mathcal P_\kappa\), is
\[
\boxed{\sup_{\substack{A_1\ne A_2\\A_1,A_2,B\in\mathcal P_\kappa}}
\frac{\|\Phi(A_1,B)-\Phi(A_2,B)\|}{\|A_1-A_2\|}
=L_\kappa
=\begin{cases}
\left(\frac{\kappa}{\kappa+1}\right)^2,&1<\kappa\le2+\sqrt5,\\[2mm]
\frac{\kappa+6+\kappa^{-1}}{16},&\kappa\ge2+\sqrt5.
\end{cases}}
\]
The bound is dimension-independent and already sharp on real symmetric \(2\times2\) matrices. It also equals the supremum of the norms of the Fréchet derivatives in the first variable. For \(\kappa>2+\sqrt5\), noncommuting extremal pairs yield a larger derivative norm than any commuting pair. The unrestricted norm-Lipschitz coefficient first exceeds \(1\) exactly when \(\kappa>5+2\sqrt6\).

## Assumptions and scope

All norms are operator norms; \(A_1,A_2,B\) are bounded, positive, self-adjoint, and have spectra in \([1,\kappa]\). The inequality is *one-sided*: \(B\) is fixed when the first argument changes. For \(\kappa=1\), the parameter set is a singleton and the difference-quotient supremum has no admissible pair, so the theorem assumes \(\kappa>1\). For dimension one the sharp constant is instead \((\kappa/(\kappa+1))^2\) for every \(\kappa>1\). Common bounds \(mI\preceq A,B\preceq MI\), \(m>0\), reduce to the stated result by scaling with \(\kappa=M/m\).

## Proof

**Step 1 (derivative and global reduction).** Set \(S=A+B\). Differentiation of \(\Phi(A,B)=B-BS^{-1}B\) in a bounded self-adjoint direction \(H\) gives
\[
D_A\Phi(A,B)[H]=BS^{-1}HS^{-1}B=C H C^*,\qquad C=BS^{-1}.
\]
Its norm as a linear map on bounded self-adjoint operators is **exactly** \(\|C\|^2\): the upper bound follows from submultiplicativity and the reverse bound from positive rank-one \(H=xx^*\), with \(x\) approaching a maximizing singular direction for \(C\). This also holds in infinite-dimensional Hilbert spaces by approximate singular vectors. Along the segment \(A(t)=A_1+t(A_2-A_1)\), the derivative integrates in operator norm, yielding a global Lipschitz bound by the supremal local coefficient. Conversely, any interior pair \((A,B)\), with \(I\prec A\prec\kappa I\) in the uniform spectral-gap sense, permits sufficiently small self-adjoint increments in a maximizing rank-one direction. Extremal boundary pairs can be approximated by \(A_\varepsilon=(1-\varepsilon)A+\varepsilon (\kappa+1)I/2\), while \(B\) remains fixed. Thus the global optimum is exactly
\[
\sup_{A,B\in\mathcal P_\kappa}\|B(A+B)^{-1}\|^2.
\]

**Step 2 (dimension-free upper bound).** Define \(c=(\kappa+1)/2\), \(r=(\kappa-1)/2\), and
\[
K=2c^2-r^2=\frac{\kappa^2+6\kappa+1}{4},\qquad c^2-r^2=\kappa.
\]
For any unit vector \(z\), let \(u=Az\), \(v=Bz\), and \(a=\|v\|\in[1,\kappa]\). The spectral bounds imply \(\|u-cz\|,\|v-cz\|\le r\). By the reverse triangle inequality and the parallelogram identity,
\[
\|u+v\|\ge\|v+cz\|-r,\qquad
\|v+cz\|^2=2a^2+2c^2-\|v-cz\|^2\ge2a^2+K.
\]
As \(2a^2+K>r^2\), this implies
\[
\frac{\|Bz\|}{\|(A+B)z\|}
\le F_\kappa(a):=\frac{a}{\sqrt{2a^2+K}-r}.
\]
The supremum over \(z\) gives \(\|B(A+B)^{-1}\|\le\max_{1\le a\le\kappa}F_\kappa(a)\).

**Step 3 (exact scalar maximization).** Write \(g(a)=\sqrt{2a^2+K}\). Direct differentiation shows that \(F_\kappa'(a)\) has the sign of \(K-rg(a)\). Its possible interior maximum occurs at
\[
a_*^2=\frac{\kappa K}{r^2}.
\]
The condition \(a_*\le\kappa\) is equivalent to \(\kappa^2-4\kappa-1\ge0\), hence to \(\kappa\ge2+\sqrt5\). When \(\kappa\le2+\sqrt5\), the maximum is at \(a=\kappa\), with \(F_\kappa(\kappa)=\kappa/(\kappa+1)\). When \(\kappa\ge2+\sqrt5\), the maximum is at \(a=a_*\) and its value simplifies to
\[
F_\kappa(a_*)=\tfrac14\sqrt{\kappa+6+\kappa^{-1}}.
\]
These squared expressions give \(L_\kappa\). They agree at the transition.

**Step 4 (sharp two-dimensional witness).** For each \(\kappa>1\) choose \(a=\min\{\kappa,a_*\}\), \(e=(1,0)^{\mathsf T}\), and
\[
v=\begin{pmatrix}(a^2+\kappa)/(2c)\\ \sqrt{a^2-[(a^2+\kappa)/(2c)]^2}\end{pmatrix},\qquad
u=ce-r\frac{v+ce}{\|v+ce\|}.
\]
Then \(\|v\|=a\) and \(\|v-ce\|=\|u-ce\|=r\). For any real unit vector \(w=(w_1,w_2)^{\mathsf T}\), put
\[
R(w)=\begin{pmatrix}w_1&w_2\\ w_2&-w_1\end{pmatrix}.
\]
It satisfies \(R(w)^2=I\) and \(R(w)e=w\). Define
\[
A= cI+rR((u-ce)/r),\qquad B=cI+rR((v-ce)/r).
\]
Both are real symmetric with eigenvalues exactly \(1,\kappa\), and \(Ae=u\), \(Be=v\). In particular
\[
\|B(A+B)^{-1}\|\ge\frac{\|Be\|}{\|(A+B)e\|}
=\frac{a}{\|v+ce\|-r}=F_\kappa(a),
\]
which saturates the upper bound. For \(a<\kappa\) (equivalently \(\kappa>2+\sqrt5\)), the displayed witness has nonzero off-diagonal entries and its two operators do not commute. For \(a=\kappa\), the witness is commuting. Approximate \(A\) by an interior positive operator and apply Step 1 to obtain actual finite-difference quotients arbitrarily close to \(L_\kappa\).

**Step 5 (scalar/commuting comparison and expansion threshold).** When \(A,B\) commute, the spectral theorem gives
\[
\|B(A+B)^{-1}\|\le\frac{\kappa}{\kappa+1}
\]
and this is attained by \(A=I\), \(B=\kappa I\). Thus noncommutation improves the extremum precisely above the first threshold. In the second regime, \(L_\kappa>1\) is equivalent to \(\kappa^2-10\kappa+1>0\), or \(\kappa>5+2\sqrt6\), since \(\kappa>1\).

## Verification

All extremal matrices are explicitly described by Step 4 and attain the *derivative* envelope. The global Lipschitz constant is the supremum of finite differences, approached by nearby interior matrices; no claim of its attainment by two distinct arguments is required. The supplementary independent-arithmetic diagnostic script `CHECK.py` reproduces the extremal singular values, samples matrices within the box, and checks finite differences with numerical tolerances. Its finite random trials do not prove the infinite-dimensional theorem; Steps 1–5 provide that proof.

## Relationship to prior work

Alwadani, *On Parallel Sums of Set-Valued Operators: Monotonicity, Paramonotonicity, and Decomposition Invariance* (arXiv:2611.05523, publicly submitted 2026-11-03), investigates monotonicity, paramonotonicity, decomposition invariance, and normal-cone parallel sums. Its inspected Results section does not supply the spectral-box sensitivity envelope here.

Luo, Song, and Xu, *Perturbation estimation for the parallel sum of Hermitian positive semi-definite matrices* (arXiv:1806.07033, 2018), particularly Corollaries 3.2–3.3 and the Anderson–Duffin estimate they cite, establish the pointwise one-sided perturbation coefficient involving \(\|(A+B)^{-1}B\|^2\). That coefficient and its underlying differentiation are **prior knowledge**, not claimed as new. The asserted contribution is the optimal, explicitly evaluated *uniform spectral-box* envelope with its two sharp parameter thresholds, including noncommuting two-dimensional maximizers. The accessible Section 3 does not state or imply the evaluated envelope without a separate optimization.

Naik and Johnson, *Norm Inequalities for Complementable Operators and Parallel Sums* (arXiv:2607.10166, 2026), Section 4, treats block-operator norm bounds and Douglas solutions under structural hypotheses, rather than maximizing a positive operator's one-sided parallel-sum perturbation coefficient under common spectral restrictions. Older general parallel-sum norm literature could contain an equivalent bound under different terminology; publication priority is not independently certified.

## Limitations

The formula applies to strictly positive bounded self-adjoint operators on Hilbert spaces, uniform common spectral intervals, and perturbation of only one argument with the other held fixed. It does not quantify simultaneous perturbations, non-self-adjoint operators, semidefinite singular endpoints, or unequal separate spectral intervals. The dimension-one result differs after the phase boundary. Numerical diagnostics are supplementary and no independent review has been performed.

## References

1. S. T. Alwadani, *On Parallel Sums of Set-Valued Operators: Monotonicity, Paramonotonicity, and Decomposition Invariance*, arXiv:2611.05523v1 (2026), https://arxiv.org/abs/2611.05523 .
2. W. Luo, C. Song, Q. Xu, *Perturbation estimation for the parallel sum of Hermitian positive semi-definite matrices*, arXiv:1806.07033v1 (2018), especially Corollaries 3.2–3.3, https://arxiv.org/abs/1806.07033 .
3. S. M. Naik, P. S. Johnson, *Norm Inequalities for Complementable Operators and Parallel Sums*, arXiv:2607.10166v1 (2026), especially Section 4, https://arxiv.org/abs/2607.10166 .
4. W. N. Anderson Jr., R. J. Duffin, *Series and parallel addition of matrices*, J. Math. Anal. Appl. **26** (1969), 576–594 (pointwise perturbation antecedents, as cited by Luo–Song–Xu).
