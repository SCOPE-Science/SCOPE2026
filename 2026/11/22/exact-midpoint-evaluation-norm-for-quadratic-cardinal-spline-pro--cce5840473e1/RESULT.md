# Exact midpoint evaluation norm for quadratic cardinal spline projection

## Finding
Let \(B\) be the nonnegative quadratic cardinal B-spline supported on \([0,3]\), normalized so \(\sum_{j\in\mathbb Z}B(t-j)=1\). Let \(P\) be the real \(L^2(\mathbb R)\) orthogonal projector onto the closed spline space spanned by integer translates of \(B\), extended to bounded inputs by its absolutely convergent reproducing kernel. The point-evaluation functional \(E(f)=(Pf)(1/2)\) has the exact norm \(\|E\|_{L^\infty\to\mathbb R}=\Lambda\), where the following fully explicit radical-root series converges geometrically:

Set \(u_1=-13+\sqrt{105}\), \(u_2=-13-\sqrt{105}\), \(r_i=(u_i+\sqrt{u_i^2-4})/2\) (both strictly between \(-1\) and \(0\)), and
\[
 g_j=\frac{60}{\sqrt{105}}\left(\frac{r_1^{|j|}}{r_1-r_1^{-1}}-\frac{r_2^{|j|}}{r_2-r_2^{-1}}\right),\qquad
 a_j=\frac{(-1)^j}{8}(g_{j-1}+6g_j+g_{j+1})\quad(j\ge0),\qquad a_{-1}=a_1.
\]
For \(m\ge0\), define on the indicated half-intervals
\[
 L_m(s)=a_m(3/4-s^2)-\frac{a_{m-1}}2(1/2-s)^2-\frac{a_{m+1}}2(1/2+s)^2\quad(0\le s\le1/2),
\]
\[
 R_m(s)=\frac{a_m}2(3/2-s)^2-a_{m+1}(3/4-(1-s)^2)+\frac{a_{m+2}}2(s-1/2)^2\quad(1/2\le s\le1).
\]
Each \(R_m\) has exactly one root \(\sigma_m\in(1/2,1)\); each \(L_m\) is strictly positive, and \(R_m\) is positive before this root and negative afterward. Then
\[
 \boxed{\displaystyle\Lambda=2\sum_{m=0}^{\infty}\left[\int_0^{1/2} L_m(s)\,ds+2\int_{1/2}^{\sigma_m}R_m(s)\,ds-\int_{1/2}^{1}R_m(s)\,ds\right].}
\]
All summands are integrals of explicitly given quadratic polynomials between algebraically specified roots. In particular,
\[
 \boxed{1.75676378<\Lambda<1.75676379.}
\]
For input data restricted to \(0\le f\le1\), the largest possible downward excursion of \((Pf)(1/2)\) below zero equals exactly \((\Lambda-1)/2\), with the corresponding positive excursion above one also equal to this quantity.

## Assumptions and scope
Here \(B(x)=x^2/2\) on \([0,1]\), \(B(x)=(-2x^2+6x-3)/2\) on \([1,2]\), \(B(x)=(3-x)^2/2\) on \([2,3]\), and zero elsewhere. All spaces and functions are real. The result concerns the **fixed physical midpoint** \(x=1/2\) in the unit cell, not the global \(L^\infty\)-norm of \(P\). The norming data are measurable essentially bounded inputs; continuous data approximate the sharp ratio. The series defines the number exactly, independently of decimal arithmetic.

## Proof
**1. Infinite Gram inverse.** For \(B_j(t)=B(t-j)\), direct integration of the three polynomial pieces gives \(\langle B_0,B_0\rangle=11/20\), \(\langle B_0,B_1\rangle=13/60\), \(\langle B_0,B_2\rangle=1/120\), and all further entries zero. Thus the Gram convolution symbol is \((66+26(z+z^{-1})+(z^2+z^{-2}))/120\). With \(u=z+z^{-1}\) this becomes \((u^2+26u+64)/120\), and factoring it at \(u_1,u_2\), followed by the geometric two-sided Green function, gives exactly the sequence \(g_j\) in the finding. Its exponential decay makes the inverse convolution bounded on \(\ell^2\) and \(\ell^\infty\), and justifies all kernel sums by absolute convergence.

**2. Midpoint kernel.** The only nonzero basis values at \(x=1/2\) are \(1/8,3/4,1/8\). Consequently, with the centered spline \(b(t)=B(t+3/2)\),
\[
 (Pf)(1/2)=\int_\mathbb R K(t)f(t+1/2)\,dt,\qquad
 K(t)=\sum_{j\in\mathbb Z}(-1)^j a_{|j|}b(t-j).
\]
The kernel is even. An elementary substitution into the inverse formula yields \(a_0>0\) and, for \(j\ge1\), \(a_j=Aq^{j-1}+Cp^{j-1}\), with \(q=-r_1\), \(p=-r_2\) and positive algebraic constants \(A,C\). Explicitly, \(A=\frac{60[-(1+6r_1+r_1^2)]}{8\sqrt{105}(r_1-r_1^{-1})}\) and \(C=\frac{60(1+6r_2+r_2^2)}{8\sqrt{105}(r_2-r_2^{-1})}\). Hence every \(a_j\) is positive. The geometric-mixture ratio \(a_{j+1}/a_j\) is nondecreasing for \(j\ge1\) and lies below \(q<0.44\). Direct comparison of the displayed radicals gives \(0.31<a_1/a_0<0.44\) and \(0.40<a_2/a_1<0.44\). Thus, for every \(j\ge0\),
\[
 0.31<a_{j+1}/a_j<0.44.
\]
These coarse rational bounds suffice for all ensuing sign claims.

**3. Root isolation in every cell.** On \(t=m+s\) the function \((-1)^mK(t)\) is exactly \(L_m(s)\) for \(0\le s\le1/2\), and \(R_m(s)\) for \(1/2\le s\le1\). The left polynomial is strictly concave, with positive endpoint values \((6a_m-a_{m-1}-a_{m+1})/8\) and \((a_m-a_{m+1})/2\); the ratio bounds ensure their positivity. The right polynomial is strictly convex, starts at the same positive value and ends at \((a_m-6a_{m+1}+a_{m+2})/8<0\). A quadratic with opposite endpoint signs has exactly one zero in that interval, proving the root and sign assertions. Integrating the absolute values cell by cell and using evenness proves the displayed series.

**4. Sharp functional norm and positivity defect.** The dual norm of integration against an \(L^1\) kernel on real \(L^\infty\) is the integral of its absolute value; sign data attain it. Since \(P\mathbf1=\mathbf1\), the kernel has total integral \(1\), so the positive and negative kernel masses are \((\Lambda+1)/2\) and \((\Lambda-1)/2\). Choosing indicator functions of the positive or negative kernel sets gives the asserted exact excursions.

**5. Convergence and numerical bracket.** Let \(S_M\) be the first \(M\) terms of the boxed series and set \(q=-r_1<0.44\). Since \(a_{j+1}\le q a_j\) for \(j\ge1\), support of \(b\) and its unit integral yield the analytic tail bound
\[
 0<\Lambda-S_M\le\frac{2a_{M-1}}{1-q}\quad(M\ge2).
\]
At \(M=70\), the right-hand side is less than \(2.48\times10^{-25}\). Evaluating the integrals by quadratic antiderivatives and the smaller quadratic roots gives the stated decimal bracket; the accompanying code recomputes these values.

## Verification
Run `python3 check.py` using Python's standard library. It checks inverse-Gram convolution identities, explicit algebraic coefficient ratios, each isolated quadratic root for seventy cells, the partial sum, and the analytic tail. The proof establishes all infinite assertions independently of the finite checks. All polynomial and radical definitions are included in this file; there are no external data dependencies.

## Relationship to prior work
Spline projection uniform boundedness is classical (Shadrin and later Keryan–Passenbrunner), and uniform periodic spline stability via inverse Gram decay is known (Antonopoulos–Dougalis). These establish existence of stability bounds, not the particular midpoint norm series or its cellwise sign roots. Related exact **linear** spline constants and quadratic **tail-localization** results concern distinct claims. The statement is an exact **point evaluation** invariant and is not claimed to determine the global projector norm.

## Limitations
No claim is made about which point maximizes the full projection norm, other polynomial degrees, nonuniform grids, or a closed elementary form of \(\Lambda\). A numerically printed decimal is not an independent proof of the infinite identity. Historical exact midpoint computations beyond the inspected literature could affect priority.

## References
- K. Keryan and M. Passenbrunner, *Projection Operators onto Spaces of Chebyshev Splines*, arXiv:1807.07161 (first public version 2018-07-18), https://arxiv.org/abs/1807.07161.
- D. C. Antonopoulos and V. A. Dougalis, *On the Stability of the \(L^2\) Projection and the Quasiinterpolant in the Space of Smooth Periodic Splines*, arXiv:2106.09060 (first public version 2021-06-16), https://arxiv.org/abs/2106.09060.
