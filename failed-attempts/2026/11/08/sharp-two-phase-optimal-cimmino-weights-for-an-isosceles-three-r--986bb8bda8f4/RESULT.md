# Sharp two-phase optimal Cimmino weights for an isosceles three-row Gram matrix

## Finding

For a nonsingular three-equation system with normalized row normals having the symmetric overlap pattern \(\langle u_1,u_2\rangle=\langle u_1,u_3\rangle=c>0\) and \(\langle u_2,u_3\rangle=d>0\), the global minimum one-step Euclidean error contraction of positively weighted Cimmino reflection is given exactly by a two-branch formula. Its optimal weights change analytic form when \(c^2=2d^2/(1+d)\). This solves the full three-weight optimization for this family, not only optimization of a common scalar multiplier.

Let \(s=1+d\) and \(z=1-d\). Define
\[
q_* = \begin{cases}
\dfrac{d(1-d)}{d-c^2}, & c^2<\dfrac{2d^2}{1+d},\\[4pt]
1+d, & c^2\ge\dfrac{2d^2}{1+d},
\end{cases}
\]
and
\[
b_* = \begin{cases}
\dfrac{2}{q_*+1+d}, & c^2<\dfrac{2d^2}{1+d},\\[4pt]
\dfrac{1}{1+d}, & c^2\ge\dfrac{2d^2}{1+d}.
\end{cases}
\]
Then \(w_*=(q_*b_*,b_*,b_*)\) is globally optimal among **all** positive weight triples, and
\[
\inf_{w_1,w_2,w_3>0}\left\|I-\sum_{i=1}^3w_i u_i u_i^{\mathsf T}\right\|_2
=\begin{cases}
\dfrac{q_*+3d-1}{q_*+1+d}, & c^2<\dfrac{2d^2}{1+d},\\[4pt]
c\sqrt{\dfrac{2}{1+d}}, & c^2\ge\dfrac{2d^2}{1+d}.
\end{cases}
\]
The symmetric optimal triple is unique; other nonsymmetric optima are not excluded by this statement.

## Assumptions and scope

The vectors \(u_i\in\mathbb R^3\) have Euclidean norm one and Gram matrix
\[
G=\begin{pmatrix}1&c&c\\c&1&d\\c&d&1\end{pmatrix},
\quad 0<d<1,\quad 0<c<\sqrt{(1+d)/2}.
\]
The assumptions give \(\det G=(1-d)(1+d-2c^2)>0\); hence the vectors are linearly independent. For a consistent real nonsingular system, the weighted error iteration is \(e^{(k+1)}=M(w)e^{(k)}\), \(M(w)=I-\sum_iw_i u_i u_i^{\mathsf T}\). We minimize its sharp induced Euclidean operator norm over all \(w_i>0\), without requiring a prescribed sum of weights. All assertions concern real matrices and exact arithmetic.

## Proof

**1. Symmetry reduces the global search.** Interchanging the second and third vector preserves \(G\). Since these vectors form a basis, this permutation extends to an orthogonal map \(Q\) on \(\mathbb R^3\) with \(Qu_1=u_1\), \(Qu_2=u_3\), and \(Qu_3=u_2\). Consequently the objectives for \((w_1,w_2,w_3)\) and \((w_1,w_3,w_2)\) agree. The map \(w\mapsto\|I-\sum_iw_i u_i u_i^{\mathsf T}\|_2\) is convex, so averaging these two triples does not increase the objective. Thus the global infimum equals the infimum over \((w_1,w_2,w_3)=(qb,b,b)\) with \(q,b>0\).

**2. Three explicit eigenvalues.** Nonzero eigenvalues of \(\sum_iw_i u_i u_i^{\mathsf T}\) equal those of \(\operatorname{diag}(\sqrt w)G\operatorname{diag}(\sqrt w)\). In the antisymmetric vector \((0,1,-1)\) and its symmetric orthogonal complement, the scaled eigenvalues are
\[
bz,\qquad b\lambda_-(q),\qquad b\lambda_+(q),
\quad
\lambda_\pm(q)=\frac{q+s\pm\sqrt{(q-s)^2+8qc^2}}2.
\]
Because \(c^2<s/2\), each \(\lambda_-(q)\) is positive, \(\lambda_+(q)>s>z\), and \(\lambda_-(q)\) increases strictly with \(q>0\). To verify strict increase, differentiate: with \(\Delta=\sqrt{(q-s)^2+8qc^2}\),
\[
2\lambda_-'(q)=1-\frac{q-s+4c^2}{\Delta}>0,
\]
since \(\Delta^2-(q-s+4c^2)^2=8c^2(s-2c^2)>0\).

**3. Optimizing the common scale.** Set \(L(q)=\min\{z,\lambda_-(q)\}\) and \(H(q)=\lambda_+(q)\). For each fixed ratio \(q\), the unique optimal scale is \(b(q)=2/(H(q)+L(q))\), giving the minimal norm \((H(q)-L(q))/(H(q)+L(q))\). It therefore suffices to minimize the ratio \(H(q)/L(q)\).

**4. Two competing spectral constraints.** On the region \(\lambda_-(q)\le z\), the ratio is \(\lambda_+(q)/\lambda_-(q)\). Its unique minimum over the positive half-line occurs at \(q=s\): indeed
\[
\left(\frac{\lambda_+(q)-\lambda_-(q)}{\lambda_+(q)+\lambda_-(q)}\right)^2
=1-\frac{4q(s-2c^2)}{(q+s)^2},
\]
and \(q/(q+s)^2\) uniquely maximizes at \(q=s\). On the region \(\lambda_-(q)\ge z\), the ratio is \(\lambda_+(q)/z\), strictly increasing in \(q\). An equality \(\lambda_-(q)=z\) can occur only if \(c^2<d\), and then it occurs uniquely at
\[
q_{\mathrm{cross}}=\frac{d(1-d)}{d-c^2}.
\]
The crossing lies below \(s\) precisely when \(c^2<2d^2/s\), because \(\lambda_-(s)=s-\sqrt{2s}\,c\). In that case the ratio falls until \(q_{\mathrm{cross}}\), then rises. Otherwise it falls until \(q=s\), then rises (any subsequent crossing cannot lower it). Thus \(q_*\) is exactly the piecewise value stated above, with no other symmetric optimal ratio.

**5. Scale, sharp rate and equality witness.** If the crossing is active, \(L=z\) and \(H=q_*+2d\), so \(b_*=2/(q_*+s)\) and the rate is \((q_*+3d-1)/(q_*+s)\). Otherwise, at \(q_*=s\), the endpoints are \(H=s+\sqrt{2s}\,c\) and \(L=s-\sqrt{2s}\,c\), giving \(b_*=1/s\) and rate \(c\sqrt{2/s}\). The formulas agree at equality \(c^2=2d^2/s\). These values are attained by the stated positive weights, and the first step establishes global optimality, not just symmetric optimality. The operator \(M(w)\) is symmetric, so its norm is attained by an extremal eigenvector and gives the exact worst-case one-step factor. All factors are strictly less than one under the assumptions.

**6. Rational example.** For \((d,c)=(1/2,1/4)\), the optimal triple is \((16/29,28/29,28/29)\). The eigenvalues of \(\sum_iw_i u_i u_i^{\mathsf T}\) are \(14/29,14/29,44/29\), and therefore the optimal factor is \(15/29\). For unit weights, the factor is \((1+\sqrt3)/4>15/29\).

## Verification

The standalone `cimmino_verify.py` evaluates symmetric \(3\times3\) eigenvalues by a Jacobi rotation algorithm using only the Python standard library. It checks the predicted optimal weights against direct spectral norms across 320 parameter pairs, compares with 24,000 additional arbitrary positive weight triples, verifies five transition points, and checks an exact rational witness. The checker reported 24,005 randomized and boundary comparisons passed. The mathematical proof above, not the sampling, establishes the universal statement. To reproduce, run `python3 cimmino_verify.py` with Python 3.9 or later.

## Relationship to prior work

Sharma, *Sharp Convergence Rates and Optimal Weights for Cimmino's Reflection Algorithm* (2026), gives the error matrix, proves globally optimal unit weights for two equations, and gives the common-scale optimum for arbitrary dimension (Theorems 1–5). The present claim solves the **additional weight-ratio optimization** for a natural three-row symmetry family and finds an active-spectral-mode transition absent from that source.

Qu, Gao, Hinder, Ye and Zhou, *Optimal Diagonal Preconditioning* (2022), develop general convex and semidefinite optimization tools for diagonal spectral conditioning. This general framework encompasses the optimization task algorithmically but does not state the closed-form three-row solution or its two spectral regimes. Classical optimal-scaling literature, including Shapiro (1985) and Kolotilina (2002), presents a residual historical-priority risk: full text of all plausible older special cases was not accessible for a definitive exclusion.

## Limitations

The exact formula assumes real unit row normals, \(0<d<1\), \(0<c<\sqrt{(1+d)/2}\), equal correlations from the first row to the other two, positive weights with unconstrained sum, and an exact linear iteration. No claim is made about nonsymmetric three-row Gram patterns, signed correlations beyond the stated domain, floating-point behavior, costs of weight computation for large systems, or uniqueness outside the symmetric weight class. The older scaling literature has not been exhaustively excluded from historical priority.

## References

1. H. Sharma, *Sharp Convergence Rates and Optimal Weights for Cimmino's Reflection Algorithm*, arXiv:2605.24692, first public 2026-05-23, https://arxiv.org/abs/2605.24692.
2. Z. Qu, W. Gao, O. Hinder, Y. Ye and Z. Zhou, *Optimal Diagonal Preconditioning*, arXiv:2209.00809, https://arxiv.org/abs/2209.00809.
3. J. Demmel, *Nearly Optimal Block-Jacobi Preconditioning*, SIAM J. Matrix Anal. Appl. 44 (2023), https://doi.org/10.1137/22M1504901.
4. A. Shapiro, *Optimal Block Diagonal \(l_2\)-Scaling of Matrices*, SIAM J. Numer. Anal. 22 (1985), https://doi.org/10.1137/0722005.
5. L. Yu. Kolotilina, *Optimally conditioned block matrices*, Linear Algebra Appl. 340 (2002), https://doi.org/10.1016/S0024-3795(01)00412-8.
