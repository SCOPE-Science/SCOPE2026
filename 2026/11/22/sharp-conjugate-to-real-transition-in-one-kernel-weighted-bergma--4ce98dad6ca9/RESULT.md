# Sharp conjugate-to-real transition in one-kernel weighted Bergman approximation

## Finding
Let \(\alpha>-1\), put \(\lambda=\alpha+2>1\), and consider the analytic polynomial \(f_a(z)=1+a z-z^2\) with \(a\ge0\) in the standard weighted Bergman space \(A^2_\alpha(\mathbb D)\). Among **all** single reproducing kernels at freely chosen disk points (and all complex scalar multiples), the optimal parameter sites have the following complete classification.

For \(1<\lambda<2\), define
\[
 r_0=\sqrt{\frac{2-\lambda}{2+\lambda}},\qquad
 a_c(\lambda)=\frac{2\sqrt{4-\lambda^2}}{\lambda}.
\]
For \(0\le a<a_c(\lambda)\), there are **exactly two** optimal sites,
\[
 w_\pm=r_0\exp\!\left(\pm i\arccos\frac{a}{a_c(\lambda)}\right),
\]
with the same radius \(r_0\), independent of \(a\). At \(a=a_c(\lambda)\), these merge into the unique positive-real site \(w=r_0\). For \(a>a_c(\lambda)\), the optimum is unique, real, and positive: \(w=r(a)\), where \(r(a)\) is the unique solution in \((0,1/\sqrt{\lambda+1})\) of
\[
 a\bigl[1-(\lambda+1)r^2\bigr]=(\lambda+2)r(1-r^2).
\]
If \(\lambda\ge2\), the unique optimum is \(w=0\) at \(a=0\), and for every \(a>0\) is the unique positive-real solution of the same equation. Thus conjugate off-axis optimal sites occur **if and only if** \(-1<\alpha<0\) and \(0\le a<a_c(\alpha+2)\).

The maximal captured squared norm in the conjugate-site regime (including the merger) is exactly
\[
 M_{\lambda,a}=
 \left(1+\frac{a^2}{4}\right)
 \left(\frac{2\lambda}{\lambda+2}\right)^\lambda
 \frac{16}{(\lambda+2)^2}.
\]
In the unique positive-real regime it is
\[
 M_{\lambda,a}=(1-r(a)^2)^\lambda(1+a r(a)-r(a)^2)^2.
\]
At \(a=0\), \(\lambda\ge2\), it equals \(1\). The exact squared best-approximation error is \(1+a^2/\lambda+2/[\lambda(\lambda+1)]-M_{\lambda,a}\).

The merger has an exact square-root angular law \(\theta(a)=\arccos(a/a_c)\sim\sqrt{2(a_c-a)/a_c}\) as \(a\uparrow a_c\). The optimal radius is constant to the left, while its right derivative at the merger is
\[
 \left.\frac{dr(a)}{da}\right|_{a=a_c+}=\frac{\lambda^3}{8(\lambda+2)}>0.
\]

## Assumptions and scope
The norm is
\[
 \|f\|_{A^2_\alpha}^2=\frac{\alpha+1}{\pi}\int_{|z|<1}|f(z)|^2(1-|z|^2)^\alpha\,dA(z),
\]
where \(dA\) is planar Lebesgue area. Its kernel is \(K_\lambda(z,w)=(1-z\overline w)^{-\lambda}\). A single-kernel approximant means \(cK_\lambda(\cdot,w)\), \(c\in\mathbb C\), \(w\in\mathbb D\). The full disk is optimized without a prescribed radius, phase, or symmetry. The restriction \(a\ge0\) fixes a specific real-coefficient family; no claim is made for arbitrary complex coefficients or for two or more kernels.

## Proof
**1. Exact Hilbert-space reduction.** The reproducing property shows that for fixed \(w\), projection onto \(\operatorname{span}\{K_\lambda(\cdot,w)\}\) has squared norm
\[
 |f_a(w)|^2/K_\lambda(w,w)=P_{\lambda,a}(w):=(1-|w|^2)^\lambda|1+a w-w^2|^2.
\]
Because \(P_{\lambda,a}\) is continuous on the closed disk and zero on its boundary, a maximizer exists in the open disk. Orthogonality of monomials gives \(\|f_a\|^2=1+a^2/\lambda+2/[\lambda(\lambda+1)]\).

**2. Complete angular optimization.** Write \(w=r e^{i\theta}\), \(x=\cos\theta\), and \(t=r^2\). For \(0<r<1\), direct expansion gives
\[
 |1+a w-w^2|^2=(1+t)^2+a^2t+2ar(1-t)x-4t x^2.
\]
The right side is strictly concave in \(x\in[-1,1]\), and its unconstrained vertex is \(x_0=a(1-t)/(4r)\ge0\). Hence the angular maximizer has \(x=\min\{1,x_0\}\), and in the interior-vertex region its value factorizes **exactly** as
\[
 |1+a w-w^2|_{\max\theta}^2=(1+a^2/4)(1+r^2)^2.
\]
The vertex is feasible exactly when \(a\le4r/(1-r^2)\). This implies the global envelope inequality
\[
 P_{\lambda,a}(w)\le(1+a^2/4)G_\lambda(r^2),\qquad G_\lambda(t)=(1-t)^\lambda(1+t)^2,
\]
with equality precisely when the unconstrained angular vertex is attained. The logarithmic derivative is
\[
 \frac{G'_\lambda(t)}{G_\lambda(t)}=
 \frac{(2-\lambda)-(2+\lambda)t}{1-t^2}.
\]
Consequently, for \(1<\lambda<2\), \(G_\lambda\) has a unique maximum at \(t_0=(2-\lambda)/(2+\lambda)\), while for \(\lambda\ge2\) it decreases strictly on \((0,1)\). If \(1<\lambda<2\) and \(a\le4r_0/(1-r_0^2)=a_c\), the envelope maximum is attained at \(r=r_0\) with the precisely stated phases. These are the only maxima, since both radial and angular equalities are strict elsewhere. For \(a=0\), \(\lambda\ge2\), the only maximizer is the origin.

**3. Uniqueness in the real-site regime.** For \(a>0\), the angular maximizer lies on the positive real axis for \(0\le r\le r_b\), where \(r_b\) is uniquely determined by \(a=4r_b/(1-r_b^2)\). For \(r\ge r_b\), the angular envelope equals \((1+a^2/4)G_\lambda(r^2)\). In the claimed real-site cases, either \(\lambda\ge2\) or \(\lambda<2\) and \(r_b>r_0\); hence this envelope is strictly decreasing from \(r_b\) onward. Its derivative at \(r_b\) is negative and agrees with the real-site branch derivative.

On \([0,r_b]\), maximizing squared energy is equivalent to maximizing the positive function \((1-r^2)^{\lambda/2}(1+a r-r^2)\). Its derivative has the same sign as
\[
 a\bigl[1-(\lambda+1)r^2\bigr]-(\lambda+2)r(1-r^2).
\]
There is a unique zero: on \((0,1/\sqrt{\lambda+1})\) the stationarity equation is \(a=h_\lambda(r)\), with
\[
 h_\lambda(r)=\frac{(\lambda+2)r(1-r^2)}{1-(\lambda+1)r^2},\qquad
 h'_\lambda(r)=\frac{(\lambda+2)[1+(\lambda-2)r^2+(\lambda+1)r^4]}{[1-(\lambda+1)r^2]^2}>0.
\]
The derivative polynomial is positive for every \(\lambda>1\): its coefficients are nonnegative when \(\lambda\ge2\), while for \(1<\lambda<2\) its discriminant is negative and its leading coefficient positive. The function \(h_\lambda\) increases from zero to infinity. Beyond \(1/\sqrt{\lambda+1}\), the derivative of the real-site objective is strictly negative. As the derivative at \(r_b\) is negative, the unique root lies below \(r_b\), and it is the unique global maximizer. At the merger \(r_b=r_0\), the same root is \(r_0\); all angular maxima coalesce.

**4. Critical responses.** From \(a_c=4r_0/(1-r_0^2)\), the angular law is exactly \(\cos\theta=a/a_c\), giving its square-root asymptotic. The optimal radius is fixed at \(r_0\) below the merger. By implicit differentiation of \(h_\lambda(r(a))=a\),
\[
 r'_+(a_c)=1/h'_\lambda(r_0)=\frac{\lambda^3}{8(\lambda+2)}.
\]
The energy formula is obtained by inserting \(r_0\) into the factorized angular maximum. This finishes all equality and boundary cases.

## Verification
The self-contained `checker.py` evaluates the exact global candidate, performs independent bounded numerical optimization of the full angular envelope, checks thousands of radii over a grid of weights and polynomial coefficients, and tests the critical square-root and one-sided derivative laws. Running `python checker.py` with Python 3, NumPy and SciPy produces a PASS report with 21,896 finite assertions. These diagnostics check algebraic normalization and boundary behavior but are **not** an exhaustive or infinite proof; global uniqueness follows from the analytic monotonicity arguments above.

## Relationship to prior work
Qu, Qian and Deng (arXiv:2006.03290, originally posted 5 June 2020) prove general existence of best kernel approximations. Qu, Qian, Li and Zhu (2021 online, 2022 journal) give the standard weighted Bergman projection formula and the one-kernel objective \((1-|w|^2)^{\lambda/2}|f(w)|\), but their §5 concerns existence, not the explicit global parameter phase diagram for this polynomial. Qian (arXiv:2201.07228) further addresses general existence. The present calculation uses their established formulation, and claims as additional content only the all-weight global optimizer classification, conjugate-to-real critical curve, stationary-branch uniqueness, and precise critical responses. A published two-kernel quadratic Bergman result concerns **two** point kernels approximating \(z^2\), and a Bergman quadratic fourth-moment result optimizes a different integral functional; neither implies this one-kernel weighted point-evaluation theorem. No claim is made that these searches establish absolute historical priority.

## Limitations
This is an exact theorem for a specific three-term real quadratic family, not a complete algorithm for arbitrary weighted Bergman target functions. It does not classify the two-kernel problem or the behavior for complex \(a\). Numerical diagnostics do not replace the proof. Historical priority has not been independently certified.

## References
1. W. Qu, T. Qian, G.-T. Deng, *A sufficient condition for n-Best Kernel Approximation in Reproducing Kernel Hilbert Spaces*, arXiv:2006.03290 (first posted 5 June 2020), https://arxiv.org/abs/2006.03290.
2. W. Qu, T. Qian, H. Li, K. Zhu, *Best kernel approximation in Bergman spaces*, Applied Mathematics and Computation 416 (2022), 126749, available online 10 November 2021, DOI:10.1016/j.amc.2021.126749; lawful full text https://fie.must.edu.mo/id-14973/file/view/id-11806.pdf.
3. T. Qian, *n-Best Kernel Approximation in Reproducing Kernel Hilbert Spaces*, arXiv:2201.07228 (18 January 2022), https://arxiv.org/abs/2201.07228.
