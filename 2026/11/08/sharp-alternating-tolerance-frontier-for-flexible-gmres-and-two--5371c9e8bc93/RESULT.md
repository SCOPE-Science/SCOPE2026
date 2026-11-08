# Sharp alternating-tolerance frontier for flexible GMRES and two-step restart

## Finding

For exact-arithmetic right-preconditioned flexible GMRES (FGMRES), suppose the inner residual at outer iteration \(j\) obeys \(\|v_j-Az_j\|_2\le\mu_j\), where \(\|v_j\|_2=1\) and \(\mu_{2k-1}=a\), \(\mu_{2k}=b\) for fixed \(0<a,b<1\). Define \(D_{-1}=D_0=1\) and
\[
D_j=D_{j-1}-\mu_j^2D_{j-2}\quad(j\ge1).
\]

The following is a sharp universal classification across nonsingular linear systems, admissible variable preconditioners, and dimensions \(N\) large enough for the stated iteration index.

**Unrestarted frontier.** Strict decrease at every nonterminal step is guaranteed for all admissible runs, independently of their dimension, **if and only if** \(a+b\le1\). Throughout this region \(D_j>0\) for every finite \(j\), and for \(1\le m<N\),
\[
\boxed{\frac{\|r_m\|_2}{\|r_0\|_2}\le
\frac{a^{\lceil m/2\rceil}b^{\lfloor m/2\rfloor}}{\sqrt{D_{m-1}}}.}
\]
For each fixed finite \(m\), equality is attainable using \(A=I_N\) and invertible variable matrix preconditioners, with \(N\ge m+1\). Conversely, if \(a+b>1\), there is a finite-dimensional nonsingular system and admissible invertible variable preconditioners that cause unrestarted Arnoldi breakdown with nonzero residual after finitely many iterations. The converse is a worst-case existence statement, not a claim that all runs break down.

**Periodic exact profile.** Put \(E_k=D_{2k}\), \(E_0=1\), and \(E_1=1-a^2-b^2\). Then
\[
E_k=(1-a^2-b^2)E_{k-1}-a^2b^2E_{k-2},\qquad
D_{2k-1}=E_k+b^2E_{k-1},
\]
so the even-step sharp bound is
\[
B_{2k}=\frac{(ab)^k}{\sqrt{E_k+b^2E_{k-1}}}.
\]
When \(a+b<1\), let
\[
\lambda_\pm=\frac{1-a^2-b^2\pm\sqrt{(1-(a+b)^2)(1-(a-b)^2)}}2.
\]
Then \(E_k=(\lambda_+^{k+1}-\lambda_-^{k+1})/(\lambda_+-\lambda_-)\), and the limiting ratio of consecutive two-step worst-case bounds is \(ab/\sqrt{\lambda_+}<1\). On the exact boundary \(a+b=1\),
\[
B_{2k}=(ab)^{k/2}\sqrt{\frac{a}{k+a}},\qquad
B_{2k+1}=\frac{a(ab)^{k/2}}{\sqrt{k+1}}\quad(k\ge0).
\]
Thus the entire closed triangular region admits decaying dimension-independent bounds at any fixed iteration index.

**Restart contrast.** Restarting FGMRES every two outer iterations (resetting the alternating phase at each restart) admits the exact sharp worst-case contraction bound per completed cycle
\[
\boxed{\Phi(a,b)=
\begin{cases}
\dfrac{ab}{\sqrt{1-a^2}},&a^2+b^2<1,\\
a,&a^2+b^2\ge1.
\end{cases}}
\]
A cycle can break down at its second stage at the threshold, but if it terminates with the best residual available from that cycle, the displayed contraction remains valid; in all cases \(\Phi(a,b)<1\). In the nonempty *restart-rescue wedge* \(a+b>1\) and \(a^2+b^2<1\), unrestarted FGMRES has no universal nonstagnation guarantee, whereas each two-step restarted cycle guarantees a strict two-stage improvement, uniformly over nonsingular systems and admissible variable preconditioners. For example, \((a,b)=(4/5,2/5)\) has \(\Phi=8/15\), while a worst-case unrestarted run can break down at its third step with nonzero residual.

## Assumptions and scope

Let \(A\in\mathbb R^{N\times N}\) be nonsingular, \(r_0=b_0-Ax_0\ne0\), and let FGMRES use full Euclidean orthogonalization and a separately chosen invertible real-linear map \(M_j^{-1}\) at step \(j\). Here \(b_0\) denotes the right-hand side (distinct from tolerance \(b\)). Set \(z_j=M_j^{-1}v_j\), \(w_j=Az_j\), \(\|v_j\|_2=1\), and \(r_m=b_0-Ax_m\) the minimal-residual FGMRES residual. The only quality requirement is \(\|v_j-w_j\|_2\le\mu_j\), not that the inner map arises from a particular Krylov algorithm. If an Arnoldi step produces no new direction, retain the best residual in the available subspace. No statement concerns rounding errors, nonnormality restrictions, cost of obtaining the preconditioners, or individual fixed-in-advance preconditioning sequences. The sharpness witnesses choose matrices depending on the iteration history, as allowed in the universal worst-case question.

## Proof

**1. Residual recursion.** Write \(R_j=\|r_j\|_2/\|r_{j-1}\|_2\) when both residuals are nonzero, and \(\delta_j=\|v_j-w_j\|_2\). The flexible minimal/orthogonal-residual identity together with the preconditioner-residual bound gives, whenever the preceding steps have strict reduction,
\[
R_j\le\frac{\delta_j}{\sqrt{1-R_{j-1}^2}}.
\]
For completeness, let \(W_j=\operatorname{span}(w_1,\ldots,w_j)\) and \(r_{j-1}=\|r_{j-1}\|u\) with \(u\perp W_{j-1}\). The orthogonal-residual element of \(v_j+W_{j-1}\) is collinear with \(u\), of norm \(1/\sqrt{1-R_{j-1}^2}\), by the standard GMRES/FFOM projection geometry. Replacing \(v_j\) by the available vector \(w_j\) then bounds the next minimal residual by \(\delta_j\) times that orthogonal-residual norm. This is exactly the established flexible Brown identity and the a posteriori inequality of Güttel–Nyman, Proposition 3.1–3.2; neither identity is asserted as new here.

Define \(\gamma_0=0\) and \(\gamma_j=\mu_j/\sqrt{1-\gamma_{j-1}^2}\) while all \(\gamma_j<1\). Induction with the preceding inequality gives \(R_j\le\gamma_j\). From the determinant recurrence,
\[
\gamma_j^2=\mu_j^2\frac{D_{j-2}}{D_{j-1}},\qquad
1-\gamma_j^2=\frac{D_j}{D_{j-1}}.
\]
Multiplication telescopes: \(\prod_{j=1}^m\gamma_j=(\prod_{j=1}^m\mu_j)/\sqrt{D_{m-1}}\), proving the proposed bound wherever all relevant continuants are positive.

**2. Exact triangle.** Consider the real symmetric tridiagonal matrix \(K_q\) of size \(q\) with zero diagonal and successive off-diagonal entries \(a,b,a,b,\ldots\). The determinant \(\det(I_q-K_q)\) equals \(D_{q-1}\). Every row sum of \(K_q\) is at most \(a+b\), and for finite \(q\ge2\), at least one boundary row sum is strictly smaller; hence Perron–Frobenius strictness yields \(\lambda_{\max}(K_q)<a+b\). The bipartite sign symmetry ensures its other eigenvalues have no larger absolute value. Therefore \(I_q-K_q\) is positive definite for all finite \(q\) if \(a+b\le1\); every \(D_j>0\), and \(\gamma_j<1\) follows. Conversely, if \(a+b>1\), the all-ones Rayleigh quotient of \(K_q\) tends to \(a+b>1\), so some sufficiently large \(K_q\) has an eigenvalue exceeding one. Its \(I_q-K_q\) is not positive definite. By Sylvester's criterion, a first leading determinant \(D_j\) is nonpositive, while all earlier ones are positive. This gives the exact universal safety frontier.

**3. Finite sharpness and failure construction.** We give the construction explicitly, rather than treating a numerical match as a proof. Choose \(A=I_N\), initial unit vector \(v_1=e_1\), and dimension \(N\ge m+1\). Inductively, with \(W_{j-1}=\operatorname{span}(w_1,\ldots,w_{j-1})\), decompose \(v_j=p_j+u_j\) with \(p_j=P_{W_{j-1}}v_j\) and \(u_j\perp W_{j-1}\). For the previously constructed equality trajectory, \(q_j=\|u_j\|=\sqrt{1-\gamma_{j-1}^2}\). If \(\mu_j<q_j\), choose any new unit vector \(e_{j+1}\perp\operatorname{span}(v_1,\ldots,v_j)\) and set
\[
w_j=p_j+\left(1-\frac{\mu_j^2}{q_j^2}\right)u_j
+\frac{\mu_j\sqrt{q_j^2-\mu_j^2}}{q_j}e_{j+1}.
\]
Direct expansion verifies \(\|v_j-w_j\|=\mu_j\) and \((v_j-w_j)\perp W_j\). The Arnoldi new direction is \(e_{j+1}\). Since \(W_{j-1}\subset\operatorname{span}(v_1,\ldots,v_j)\) and the latter is \(W_{j-1}+\operatorname{span}(v_j)\), the preceding minimal residual is a scalar multiple of \(u_j\), and the next minimal residual is the same scalar multiple of \(v_j-w_j\). Their norm ratio is therefore exactly \(R_j=\mu_j/q_j=\gamma_j\). The map \(M_j^{-1}=I+(w_j-v_j)v_j^{\mathsf T}\) sends \(v_j\) to \(w_j\) and has determinant \(v_j^{\mathsf T}w_j=1-\mu_j^2>0\), so it is an admissible invertible preconditioner. Induction attains equality at every prescribed step.

At the first index where \(D_j\le0\), prior steps admit that construction and satisfy \(\mu_j\ge q_j\). Instead choose \(w_j=p_j\in W_{j-1}\). Then \(\|v_j-w_j\|=q_j\le\mu_j\), \(v_j^{\mathsf T}w_j=\|p_j\|^2>0\), and thus the same rank-one map is invertible. Since \(W_j=W_{j-1}\), the new Arnoldi direction vanishes and the minimal residual remains nonzero. This proves the required adverse example whenever \(a+b>1\).

**4. Periodic solution and two-step restart.** Eliminating alternate continuants gives the second-order \(E_k\) recurrence. Its characteristic polynomial factors with the displayed roots \(\lambda_\pm\), which yields the subcritical closed form. At \(a+b=1\), these roots coalesce to \(ab\), and the repeated-root solution is \(E_k=(k+1)(ab)^k\); substitution gives both boundary formulas.

For a two-step restart cycle, the first contraction is at most \(a\). If \(b<\sqrt{1-a^2}\), the second contraction is at most \(b/\sqrt{1-a^2}\), so the total cycle bound is \(ab/\sqrt{1-a^2}\). It is sharp by the preceding finite construction with two steps. If \(b\ge\sqrt{1-a^2}\), the second residual cannot exceed the first by minimality; equality is attainable at step two by choosing \(w_2=P_{W_1}v_2\), an admissible invertible inner map because its inner-product determinant is \(a^2>0\). This proves the other branch and sharpness. Applying the same uniform bound at each restart yields \(\|r_{2k}\|_2\le\Phi(a,b)^k\|r_0\|_2\), regardless of the starting direction of each cycle.

## Verification

Execute `python verify.py` from the package directory (Python 3 and NumPy). The script checks hundreds of exact rational continuant identities, critical repeated-root formulas, numerically constructs dimension-extended FGMRES equality witnesses and tests a supercritical breakdown case. The proof above, not finite tests, establishes the all-dimension and all-iteration assertions.

## Relationship to prior work

Güttel and Nyman (arXiv:2604.27971, first submitted 2026-04-30; v2 2026-10-20) already establish the flexible FOM/GMRES residual identity and a recursive bound with actual iteration-dependent inner residual magnitudes (Propositions 3.1–3.2), then derive and prove sharp constant-tolerance Chebyshev bounds and failure behavior. Those general identities and their fixed-tolerance specialization are **prior results**. The present claim is the exact two-periodic universal safety triangle, its closed-form sharp alternating bounds and its sharp two-step restart contrast. These are not claimed as new solely because the original recursion can be iterated: the essential extra work is a periodic tridiagonal spectral positivity equivalence, explicit sharpness witnesses with admissible invertible maps, and a distinct restart boundary. The general source recursion is a strong antecedent and should be considered in any priority assessment.

Saad's original flexible inner–outer GMRES paper (1993) and Simoncini–Szyld's flexible inner–outer analysis (2003) concern variable preconditioning and convergence. Their accessible abstracts and secondary bibliographic descriptions did not establish this exact alternating-tolerance classification; lack of full access to both older papers is a residual historical-priority risk, not affirmative evidence of absence. The separate published analysis of alternating *nonlinear GMRES* involves a different method and does not directly imply a bound for the linear FGMRES residual-minimization geometry.

## Limitations

Sharpness is over all admissible variable invertible preconditioners, which may be chosen adversarially; it is not a typical-case or fixed-inner-Krylov-solver guarantee. At a failing step, Arnoldi can break down with a nonzero residual, not necessarily diverge. The displayed formulas assume Euclidean orthogonalization and exact arithmetic. They do not compare wall-clock costs of restarting, preserve precision under roundoff, or guarantee a finite-time convergence rate independent of the dimension after the algorithm has exhausted its available Krylov subspace. Literature priority remains qualified by incomplete access to some historical full texts.

## References

1. S. Güttel and L. Nyman, *Flexible GMRES converges in two phases*, arXiv:2604.27971 (first posted 2026-04-30), especially Propositions 3.1–3.2, Theorem 3.6 and Section 4; https://arxiv.org/pdf/2604.27971.
2. Y. Saad, *A Flexible Inner-Outer Preconditioned GMRES Algorithm*, SIAM J. Sci. Comput. **14** (1993), DOI: 10.1137/0914028.
3. V. Simoncini and D. B. Szyld, *Flexible Inner-Outer Krylov Subspace Methods*, SIAM J. Numer. Anal. (2003), DOI: 10.1137/S0036142902401074.
4. M. Eiermann and O. G. Ernst, orthogonal/minimal residual projection identity, cited as Theorem 3.4 in reference 1.
