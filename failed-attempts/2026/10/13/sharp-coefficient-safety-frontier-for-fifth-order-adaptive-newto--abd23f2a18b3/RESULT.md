# Sharp coefficient safety frontier for fifth-order adaptive Newton–Schulz polar iteration

## Finding

Let \(\alpha_\star\) be the unique real root larger than \(3/8\) of
\[
128\alpha^3+496\alpha^2-1026\alpha+27=0,
\qquad \alpha_\star=1.472229260972032\ldots.
\]
For any integer dimensions \(m\ge n\ge1\), any real full-column-rank matrix \(A\in\mathbb R^{m\times n}\) normalized by \(\|A\|_2\le1\), and **every sequence** of coefficients \(\alpha_k\in[3/8,u]\), with \(3/8\le u<\alpha_\star\), the iteration
\[
X_0=A,\quad R_k=I_n-X_k^{\mathsf T}X_k,\quad
X_{k+1}=X_k\bigl(I_n+\tfrac12R_k+\alpha_kR_k^2\bigr)
\]
converges in spectral norm to the polar factor \(Q=A(A^{\mathsf T}A)^{-1/2}\). The coefficients may depend arbitrarily on past iterates or randomized sketches. There exists a finite \(K\) and a constant \(C_u<\infty\), independent of dimensions and the coefficient sequence, for which
\[
\|R_{k+1}\|_2\le C_u\|R_k\|_2^2\qquad(k\ge K).
\]
In particular, the constrained coefficient range \([3/8,29/20]\) proposed for degree-two residual fitting (fifth-degree matrix iteration) in PRISM is strictly within the universally convergent range.

The endpoint is sharp for **unrestricted choices of coefficients in that interval**. At \(u=\alpha_\star\) there is a scalar \(x_0\in(0,1)\) and a constant coefficient sequence \(\alpha_k=u\) for which the iteration reaches a fixed point different from one. For every \(u>\alpha_\star\) there is a scalar \(x_0\in(0,1)\) and the constant sequence \(\alpha_k=u\) for which the iterates diverge to \(+\infty\). This sharpness does not assert failure of any particular adaptive fitting rule.

## Assumptions and scope

All matrices and coefficient sequences are real. Matrix multiplication and coefficient selection are interpreted in exact arithmetic. Full column rank ensures all initial singular values are positive. The normalization \(\|A\|_2\le1\) places the initial squared singular-value residuals in \([0,1)\). The bound on coefficients is deterministic and pathwise; no distributional properties of sketches are needed. No assertion of dimension-independent iteration count for arbitrarily small initial singular values is made.

Write \(g_\alpha(t)=1+t/2+\alpha t^2\), \(P_\alpha(t)=(1-t)g_\alpha(t)^2\), and \(h_\alpha(t)=1-P_\alpha(t)\). The residual \(t=1-x^2\) of a positive singular value obeys \(t^+=h_\alpha(t)\). Let
\[
t_*(\alpha)=\frac{8\alpha-3}{10\alpha},\qquad
M(\alpha)=\frac{(2\alpha+3)^3(16\alpha-1)^2}{25000\alpha^3},
\qquad \alpha\ge3/8.
\]

## Proof

**1. Exact maximum and critical coefficient.** Differentiation yields
\[
P_\alpha'(t)=-\frac{t}{4}(10\alpha t-8\alpha+3)
  (2\alpha t^2+t+2).
\]
The final factor is strictly positive for \(t\ge0\), so on \([0,1]\), \(P_\alpha\) increases until \(t=t_*(\alpha)\) and decreases afterward (with the maximum at \(t=0\) when \(\alpha=3/8\)). Substitution gives \(\max_{0\le t\le1}P_\alpha(t)=M(\alpha)\). Direct factorization gives
\[
M(\alpha)-\Bigl(1+\frac1{2\alpha}\Bigr)
=\frac{(4\alpha+1)^2}{25000\alpha^3}
  \bigl(128\alpha^3+496\alpha^2-1026\alpha+27\bigr).
\]
For \(\alpha\ge3/8\), the function \(M(\alpha)\) is strictly increasing: each \(P_\alpha(t)\) is nondecreasing in \(\alpha\), and its positive maximizing argument for \(\alpha>3/8\) makes the increase strict. The comparison function \(1+1/(2\alpha)\) is decreasing. Hence there is exactly one crossing above \(3/8\), since \(M(3/8)=1<1+4/3\) and \(M(\alpha)\) is unbounded. In particular, the cubic is negative at \(\alpha=29/20\), where it equals \(-6909/250\), and positive at \(\alpha=3/2\), where it equals \(36\). Thus \(29/20<\alpha_\star<3/2\).

**2. A common invariant interval for all coefficients.** Fix \(u<\alpha_\star\), \(u\ge3/8\), and put \(b=-1/(2u)\). We show that every map \(h_\alpha\) with \(3/8\le\alpha\le u\) preserves \((b,1)\). If \(0<t<1\), then \(g_\alpha(t)>1\) so \(h_\alpha(t)<t\). Moreover, \(P_\alpha(t)\le P_u(t)\le M(u)<1+1/(2u)\) gives \(h_\alpha(t)>b\). If \(b<t<0\), then \(t<0\) and \(1/2+\alpha t\ge1/2+ut>0\), so \(g_\alpha(t)=1+t(1/2+\alpha t)<1\). On the other hand, Taylor's theorem applied to \((1-t)^{-1/2}\) at zero, whose third derivative is positive, yields for \(t<0\)
\[
(1-t)^{-1/2}\le1+\frac t2+\frac{3t^2}{8}\le g_\alpha(t).
\]
Thus \(1\le(1-t)g_\alpha(t)^2<1-t\), or \(t<h_\alpha(t)\le0\). In particular, no iterate ever escapes \((b,1)\).

**3. Convergence under arbitrary switching.** A positive residual strictly decreases for as long as it remains positive; if it ever crosses zero, it thereafter remains nonpositive and increases. Since \(g_\alpha(t)>1\) at every fixed \(t>0\), uniformly in \(\alpha\in[3/8,u]\), a positive residual cannot converge to a positive limit. For \(b<t<0\), the strict inequality \(g_\alpha(t)<1\) holds uniformly in the same compact coefficient interval, so a negative residual cannot converge to a negative limit either. Therefore each scalar residual tends to zero. An SVD of \(A\) gives \(X_k=U\operatorname{diag}(x_{1,k},\ldots,x_{n,k})V^{\mathsf T}\), with \(x_{i,k}>0\) and each residual following the same scalar rule. Hence \(X_k\to UV^{\mathsf T}=Q\).

For \(t\) near zero, an exact polynomial expansion gives
\[
h_\alpha(t)=\Bigl(\frac34-2\alpha\Bigr)t^2
 +(\alpha+\tfrac14)t^3 +(\alpha-\alpha^2)t^4+\alpha^2t^5.
\]
All coefficients are uniformly bounded over \(\alpha\in[3/8,u]\). Thus there is a \(C_u<\infty\) such that \(|h_\alpha(t)|\le C_u|t|^2\) whenever \(|t|\le1/2\). Each singular residual tends to zero, so this bound applies to the spectral norm from some index onward and proves the stated uniform local quadratic estimate.

**4. Endpoint and supercritical obstruction.** Fix a constant \(\alpha\ge\alpha_\star\) and set
\[
t_0=t_*(\alpha)\in(0,1),\qquad x_0=\sqrt{1-t_0}\in(0,1).
\]
At \(\alpha=\alpha_\star\), \(x_1^2=P_\alpha(t_0)=1+1/(2\alpha)\); hence \(t_1=-1/(2\alpha)\) and \(g_\alpha(t_1)=1\). This yields the non-unit fixed point \(x_1=\sqrt{1+1/(2\alpha)}>1\). For \(\alpha>\alpha_\star\), the strict maximum inequality gives \(x_1>\sqrt{1+1/(2\alpha)}\). Whenever \(x>\sqrt{1+1/(2\alpha)}\), its residual \(t=1-x^2\) satisfies \(t<-1/(2\alpha)\), so \(g_\alpha(t)=1+t(1/2+\alpha t)>1\); the next iterate strictly increases and remains above that threshold. If the increasing positive sequence had a finite limit, continuity would give a fixed point greater than the threshold, impossible because \(g_\alpha(t)>1\) there. Hence it diverges to infinity. These scalar examples complete sharpness for arbitrary admissible coefficient schedules. \(\square\)

## Verification

Run `python verify.py` using Python's standard library. The checker tests the maximum and cubic factorization, the derivative and residual polynomial identities using exact rational arithmetic over 2,014 parameter/evaluation cases; refines the threshold using high-precision decimal arithmetic; exercises 372 scalar trajectories under fixed and switching coefficients inside the recommended interval; and checks a supercritical escape witness. The observed terminal line is

`VERIFY_OK exact_rational_identities=2014 stable_trajectories=372 root=1.472229260972032 scalar_divergence_witness=1`

Finite computations are checks, not a substitute for the universal invariant-interval and scalar convergence arguments above.

## Relationship to prior work

Yang, Wang, Balabanov, Erichson and Mahoney introduce the adaptive residual-polynomial family \(g_2(t;\alpha)=1+t/2+\alpha t^2\) in PRISM. They recommend \([3/8,29/20]\) empirically for the fifth-degree update and prove their analogous sketched quadratic-rate theorem for degree one, not this degree-two global coefficient frontier (arXiv:2601.22137v1, Sections 4 and A.1 and Appendix B). The present result supplies a pathwise convergence guarantee for every coefficient selection within this range, and a sharp upper boundary for that **uniform** guarantee.

Amsel et al., *The Polar Express*, study worst-case optimal compositions of general odd polynomials on prescribed singular-value intervals (arXiv:2505.16932v5). Grishina, Smirnov and Rakhuba, *Accelerating Newton–Schulz Iteration for Orthogonalization via Chebyshev-type Polynomials*, study Chebyshev/Remez polynomial optimization and approximate orthogonalization (arXiv:2506.10935v2). Those are different coefficient-design and approximation objectives; neither inspected work supplies the present invariant-interval cubic boundary for adaptive switching in the fixed PRISM fifth-degree family. Previously published results may use an equivalent scalar-dynamics formulation; no exhaustive uniqueness claim is made.

## Limitations

The proof assumes exact arithmetic and positive initial singular values. At the critical endpoint, a special constant choice of the coefficient fails; this does **not** show that a specific optimization-based adaptive selector will make that choice. The result gives convergence and eventual quadratic order, not a uniform iteration-complexity bound independent of condition number, a sharp finite-time constant, or stability under rounding errors. The chosen cubic threshold is sharp only for the stated universal class of coefficient sequences. Independent scholarly audit has not been performed.

## References

1. Shenghao Yang, Zhichao Wang, Oleg Balabanov, N. Benjamin Erichson, and Michael W. Mahoney, “PRISM: Distribution-free Adaptive Computation of Matrix Functions for Accelerating Neural Network Training,” arXiv:2601.22137v1 (first posted 2026-01-29), https://arxiv.org/abs/2601.22137.
2. Noah Amsel et al., “The Polar Express: Optimal Matrix Sign Methods and Their Application to the Muon Algorithm,” arXiv:2505.16932v5, https://arxiv.org/abs/2505.16932.
3. Ekaterina Grishina, Matvey Smirnov, and Maxim Rakhuba, “Accelerating Newton–Schulz Iteration for Orthogonalization via Chebyshev-type Polynomials,” arXiv:2506.10935v2, https://arxiv.org/abs/2506.10935.
