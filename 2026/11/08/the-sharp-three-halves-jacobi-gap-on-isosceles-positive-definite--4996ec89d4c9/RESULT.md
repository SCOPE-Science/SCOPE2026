# The sharp three-halves Jacobi gap on isosceles positive-definite correlation matrices

## Finding

For every \(0<a<1\) and \(0<b<\sqrt{(1+a)/2}\), set
\[
C_{a,b}=\begin{pmatrix}1&a&b\\a&1&b\\b&b&1\end{pmatrix},\qquad
\kappa_*(C)=\inf_{D\succ0\,\mathrm{diagonal}}\frac{\lambda_{\max}(DCD)}{\lambda_{\min}(DCD)}.
\]
The standard Jacobi scaling leaves this unit-diagonal matrix unchanged. Its sharp multiplicative cost relative to unrestricted optimal positive diagonal congruence scaling satisfies
\[
\boxed{1\le\frac{\kappa_2(C_{a,b})}{\kappa_*(C_{a,b})}<\frac32.}
\]
The upper constant is the **unattained exact supremum** over this natural two-parameter family. Specifically, with \(a=1-t^2\) and \(b=\sqrt{1-t}\), the ratio tends to \(3/2\) as \(t\downarrow0\). This is a quantitative worst-case comparison, not a claim to have first solved pointwise optimal diagonal scaling in dimension three.

## Assumptions and scope

All matrices are real symmetric, \(3\times3\), positive definite with unit diagonal and two equal positive off-diagonal correlations. The domain \(0<a<1\), \(0<b<\sqrt{(1+a)/2}\) is exactly the indicated positive-definiteness domain, since the eigenvalue in the antisymmetric first-two-coordinate mode is \(1-a\), while the symmetric block has determinant \(1+a-2b^2\). All scalings \(D\) are positive diagonal, and all condition numbers are spectral \(2\)-norm condition numbers. The same proof applies to the sign-congruent class obtained by changing vertex signs, but this is not used to enlarge the stated domain.

## Proof

**Step 1: Reduce the global three-variable diagonal-scaling optimum to one variable.** For an arbitrary positive diagonal \(D\), let \(m=\lambda_{\min}(DCD)\), \(M=\lambda_{\max}(DCD)\), and \(H=mD^{-2}\). Then \(H\preceq C\preceq(M/m)H\). Swap the first two coordinates and average these two diagonal \(H\) matrices. Because \(C\) is invariant under the swap, the average is feasible with the same ratio. Rescaling by the reciprocal diagonal square root shows that some global optimal scaling has the form \(D_x=\operatorname{diag}(\sqrt{x},\sqrt{x},1)\), with \(x>0\). This reduction is valid for any competing diagonal matrix, so it proves global rather than merely symmetry-restricted optimality.

Write \(u=b^2\). The eigenvalues of \(D_x C D_x\) are
\[
\lambda_0(x)=(1-a)x,\qquad
\lambda_\pm(x)=\frac{(1+a)x+1\pm\sqrt{((1+a)x-1)^2+8ux}}2.
\]
Always \(\lambda_+(x)>\lambda_0(x)\). The two-block condition \(\lambda_+(x)/\lambda_-(x)\) decreases up to \(x_{\rm bal}=1/(1+a)\) and increases thereafter: indeed its spectral-contrast square is
\[
1-\frac{4(1+a-2u)x}{((1+a)x+1)^2},
\]
which is minimized by maximizing the displayed positive fraction. Also \(\lambda_+(x)/x\) is strictly decreasing, since after dividing the symmetric block by \(x\) its top eigenvalue is a strictly decreasing function of \(1/\sqrt{x}\) for \(b>0\). The crossing \(\lambda_-(x)=\lambda_0(x)\), if positive, occurs at \(x_{\rm cross}=(a-u)/(a(1-a))\). Consequently the optimal squared scale is
\[
x_*=\max\left\{\frac1{1+a},\frac{a-u}{a(1-a)}\right\}.
\]
The exact optimal condition number, needed only as an established intermediate calculation, is
\[
\kappa_* =\begin{cases}
\displaystyle\frac{a(1+a-2u)}{(a-u)(1-a)},&0<u\le\displaystyle\frac{2a^2}{1+a},\\[4pt]
\displaystyle\frac{1+\rho}{1-\rho},\quad \rho=\sqrt{\frac2{1+a}}\,b,&\displaystyle\frac{2a^2}{1+a}\le u<\frac{1+a}{2}.
\end{cases}
\]
The formulas agree at the joining boundary. They can be checked from the eigenvalues just displayed. The use of a pointwise optimality formula is not itself the claimed contribution; a general exact three-dimensional scaling solution predates this result.

**Step 2: Reduce the approximation ratio to three regions.** Put \(s=\sqrt{a^2+8u}\). At the Jacobi scaling \(x=1\), the largest eigenvalue is \((2+a+s)/2\), and the smallest is \(\min\{1-a,(2+a-s)/2\}\). The changeover is at \(u=a^2\). Since \(a^2<2a^2/(1+a)<a\), the parameter domain splits into
\[
\mathrm{I}:0<u\le a^2,\quad
\mathrm{II}:a^2\le u\le\frac{2a^2}{1+a},\quad
\mathrm{III}:\frac{2a^2}{1+a}\le u<\frac{1+a}{2}.
\]
In region I, the strict upper bound \(\kappa_2(C)/\kappa_*<3/2\) is equivalent to positivity of
\[
F_1=3a(1+a-2u)-(2+a+s)(a-u).
\]
Since \(s\le3a\) and \(a-u>0\),
\[
F_1\ge(1-a)(a+2u)>0.
\]

In region II the same strict bound is equivalent, after multiplication by positive denominators, to
\[
F_2=3a(1+a-2u)(2+a-s)-2(a-u)(1-a)(2+a+s)>0.
\]
On substituting \(u=(s^2-a^2)/8\), direct polynomial expansion gives \(F_2=(2+a+s)H_2/4\), where
\[
H_2=(1+2a)\left(s-\frac{3a(a+2)}{1+2a}\right)^2
+\frac{a(4-a)(1-a)^2}{1+2a}>0.
\]

In region III put \(\rho=\sqrt{2/(1+a)}\,b\), so \(0<\rho<1\), \(s^2=a^2+4(1+a)\rho^2\), and \(\rho\ge\sqrt2\,a/(1+a)\). The desired strict bound is equivalent to
\[
F_3=(2+a)(1+5\rho)-s(5+\rho)>0.
\]
The difference of its two positive square terms factorizes exactly:
\[
\begin{aligned}
&(2+a)^2(1+5\rho)^2-s^2(5+\rho)^2\\
&\qquad=4(1-\rho^2)\bigl[(1+a)(1+10\rho+\rho^2)-6a^2\bigr].
\end{aligned}
\]
The bracket is strictly positive because it is at least \(1+11a-6a^2>0\) when \(0<a<1\). Hence \(F_3>0\). These three inequalities prove the uniform strict upper bound. The lower bound \(\kappa_2(C)\ge\kappa_*\) follows by choosing \(D=I\) in the infimum.

**Step 3: Prove sharpness.** For \(0<t<1/2\), let \(a=1-t^2\), \(b=\sqrt{1-t}\). These parameters lie in the positive-definite region and the first case of the optimal-scaling formula. Direct simplification yields
\[
\kappa_* =\frac{(1+t)(2-t)}{t^2}.
\]
For small \(t\), the Jacobi minimum eigenvalue is \(t^2\) and its maximum eigenvalue tends to \(3\). Therefore \(\kappa_2(C)/\kappa_*\to3/2\). Strict inequality for every admissible interior parameter establishes nonattainment. This proves the theorem.

## Verification

Run `python verify_gap.py` with SymPy and Python 3. The script verifies the exact polynomial identities in all three regions, the sharp-approach formula, and a rational matrix example. It also performs reproducible numerical stress comparisons of the optimal equal-coordinate scale against perturbed candidates. The recorded run completed **6,829 assertions**. The infinite-parameter inequality and optimality reduction rely on the analytic proof above, not on sampling. At \(a=1/2\), \(b=1/4\), optimal \(D=\operatorname{diag}(\sqrt7/2,\sqrt7/2,1)\) gives spectrum \(\{7/8,7/8,11/4\}\), hence \(\kappa_*=22/7\), while \(\kappa_2(C)=(5+\sqrt3)/2\).

## Relationship to prior work

The symmetric-diagonal scaling problem and equal-modulus eigenvector optimality tests are classical [1,2]. Crucially, Kolotilina [3] **already solves optimal diagonal scaling for all quasireal Hermitian positive-definite \(3\times3\) matrices, including the pointwise optimizer and Jacobi-optimality characterization**. Those are not claimed new here. The present result instead establishes the exact **worst-case loss factor \(3/2\)** for the specific isosceles positive-correlation family, using a global bound over its full two-dimensional parameter domain and a sharp near-singular family. The inspected material in [1–5] did not state that family-wide sharp relative bound. The general dimension-dependent bound quoted by [3] is \(\kappa_{\rm Jacobi}\le n\kappa_*\), so it does not resolve this sharp factor. Later work [4,5] treats algorithmic optimization and approximate bounds rather than this exact family-wide extremum.

## Limitations

This is a low-dimensional sharp benchmark, not a claim that \(3/2\) bounds the loss for arbitrary real positive-definite matrices, arbitrary correlation patterns, or larger dimensions. It compares spectral condition numbers, not runtime or finite-precision performance. A specialist earlier derivation of this **global sharp approximation ratio**, rather than just pointwise optimizers, cannot be entirely excluded and would supersede its originality. No independent scientific audit has been performed.

## References

1. Forsythe and Straus, *On Best Conditioned Matrices*, Proceedings of the American Mathematical Society 6 (1955), 340–345. https://www.ams.org/journals/proc/1955-006-03/S0002-9939-1955-0069596-0/
2. Golub and Varah, *On a Characterization of the Best \(\ell_2\)-Scaling of a Matrix*, SIAM J. Numerical Analysis 11 (1974), 472–479. Author-hosted preprint: https://www.cs.ubc.ca/sites/default/files/tr/1972/TR-72-08.pdf
3. Kolotilina, *Solution of the Problem of Optimal Diagonal Scaling for Quasireal Hermitian Positive-Definite \(3\times3\) Matrices*, Journal of Mathematical Sciences 132 (2006), 190–213. https://doi.org/10.1007/s10958-005-0488-1 ; author-uploaded full text: https://www.researchgate.net/publication/250796934
4. Jambulapati, Li, Musco, Sidford and Tian, *Fast and Near-Optimal Diagonal Preconditioning*, arXiv:2008.01722v1 (August 4, 2020). https://arxiv.org/abs/2008.01722
5. Qu, Gao, Hinder, Ye and Zhou, *Optimal Diagonal Preconditioning*, arXiv:2209.00809v1 (September 2, 2022). https://arxiv.org/abs/2209.00809
