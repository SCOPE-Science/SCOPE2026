# Sharp Hardy-space stability at the extremal three-site nilpotent spectral-set constant

## Finding

Let \(J_3\in M_3(\mathbb C)\) have ones in positions \((1,2)\) and \((2,3)\) and zeros elsewhere, and put \(A=\sqrt2 J_3\). Its numerical range is the closed unit disk. For any scalar Schur function \(f\in H^\infty(\mathbb D)\) satisfying \(\|f\|_\infty\le1\), set

\[
\delta(f)=2-\|f(A)\|,\qquad d(f)=\inf_{|\omega|=1}\|f-\omega z^2\|_{H^2}.
\]

Here \(H^2\) has the standard coefficient norm \(\|\sum_{k\ge0}c_kz^k\|_{H^2}^2=\sum_{k\ge0}|c_k|^2\). The exact local stability law is

\[
\boxed{\displaystyle\lim_{\eta\downarrow0}\ \sup_{\substack{\|f\|_\infty\le1\\0<\delta(f)<\eta}}\frac{d(f)}{\sqrt{\delta(f)}}=\sqrt2.}
\]

Furthermore \(\delta(f)=0\) exactly when \(f(z)=\omega z^2\) for \(|\omega|=1\), and there is a finite universal \(C\) such that \(d(f)\le C\sqrt{\delta(f)}\) for all Schur functions. The equality classification is previously known in greater generality; the asserted contribution is the optimal quantitative Hardy-space coefficient \(\sqrt2\) for this three-site nilpotent.

## Assumptions and scope

The matrices are complex, all matrix norms are Euclidean operator norms, and \(f(A)\) is the holomorphic functional calculus at the eigenvalue zero. No boundary regularity of \(f\) is required. The numerical range assertion follows from \(w(J_3)=\cos(\pi/4)=1/\sqrt2\) and rotation invariance of the numerical range of the shift. The supremum above ranges over all functions for which the denominator is positive; the family is nonempty arbitrarily close to zero deficit.

## Proof

**1. Coefficients and global extremality.** Write \(f(z)=a+bz+cz^2+\sum_{k\ge3}c_kz^k\). As \(A^3=0\),

\[
M=f(A)=\begin{pmatrix}a&\sqrt2 b&2c\\0&a&\sqrt2 b\\0&0&a\end{pmatrix},\qquad\|M\|_F^2=3|a|^2+4|b|^2+4|c|^2.
\]

Since \(\|f\|_{H^2}^2\le\|f\|_\infty^2\le1\), writing \(T=\sum_{k\ge3}|c_k|^2\) gives

\[
\|M\|^2\le\|M\|_F^2\le4-|a|^2-4T\le4.
\]

At equality \(|a|=T=0\), \(|b|^2+|c|^2=1\), and \(f=bz+cz^2\). Its supremum on the unit circle is \(|b|+|c|\le1\), so one of \(b,c\) must vanish. The case \(c=0\) yields \(\|f(A)\|=\sqrt2\), not two; hence only \(f=\omega z^2\) is extremal.

**2. A sharp second-coefficient constraint.** Let \(r=|a|\), \(s=|b|\), \(u=|c|\). The first Schur transform, when \(r<1\), writes

\[
f(z)=\frac{a+zg(z)}{1+\overline a zg(z)},\qquad\|g\|_\infty\le1,\qquad g(0)=\frac{b}{1-r^2}.
\]

Schwarz--Pick gives \(|g'(0)|\le1-|g(0)|^2\). Comparing second coefficients yields

\[
c=(1-r^2)\bigl(g'(0)-\overline a g(0)^2\bigr),\qquad
u\le 1-r^2-\frac{s^2}{1+r}.
\tag{1}
\]

For \(r=1\), \(f\) is constant and is far from the extremal deficit; therefore all subsequent near-equality arguments use \(r<1\).

**3. Uniform localization of near extremizers.** If \(\delta(f_j)\to0\), the Frobenius inequality shows \(|a_j|\to0\), \(T_j\to0\), and \(s_j^2+u_j^2\to1\). Inequality (1) gives \(u_j\le1-s_j^2+o(1)\). For any subsequential limit \(s_j^2\to q\in[0,1]\), one has \(1\le q+(1-q)^2\), forcing \(q\in\{0,1\}\). If \(q=1\), then \(u_j\to0\), so \(M_j\) converges up to phase in norm to \(\sqrt2 J_3\), whose norm is \(\sqrt2\), contradicting \(\|M_j\|\to2\). Consequently \(r_j,s_j\to0\) and \(u_j\to1\). This works for every near-extremizing sequence, without a compactness assumption on the boundary values of \(f_j\).

**4. Second-order singular-value expansion.** Multiplying \(f\) by a unimodular scalar, arrange \(c=u>0\). With \(\rho=|a|+|b|\to0\) and \(u\to1\), the first row and first column of the Hermitian row Gram matrix \(H=MM^*\) satisfy

\[
H_{11}=4u^2+r^2+2s^2,\qquad H_{12}=2\sqrt2u\overline b+\sqrt2b\overline a,\qquad H_{13}=2u\overline a.
\]

The remaining \(2\times2\) block is \(O(\rho^2)\). The Schur-complement equation for its simple top eigenvalue therefore gives, uniformly for \(u\) bounded away from zero,

\[
\lambda_{\max}(H)=H_{11}+\frac{|H_{12}|^2+|H_{13}|^2}{4u^2}+O(\rho^3)
=4u^2+2r^2+4s^2+O(\rho^3).
\]

Taking the square root gives

\[
\|M\|=2u+\frac{r^2}{2}+s^2+o(r^2+s^2).
\tag{2}
\]

The displayed expansion is valid also when either \(a\) or \(b\) is zero; at \(a=b=0\) the error vanishes. Set \(L=1-u\). Inequality (1) implies \(L\ge r^2+s^2/(1+r)\), and thus \(r^2+s^2\le(1+o(1))L\). By (2),

\[
\delta(f)=2L-\frac{r^2}{2}-s^2+o(r^2+s^2)\ge (1-o(1))L.
\tag{3}
\]

The best phase of \(z^2\) aligns with \(c\). Parseval gives exactly

\[
d(f)^2=1+\|f\|_{H^2}^2-2u\le2(1-u)=2L.
\]

Together with (3) this proves \(\limsup_{\delta(f)\downarrow0} d(f)^2/\delta(f)\le2\). Away from a neighborhood of zero deficit, \(d(f)\le\sqrt2\), so combining with the local estimate proves the stated global square-root bound with some finite \(C\).

**5. Matching inner-function family.** For \(0<t<1\), the degree-two finite Blaschke product

\[
f_t(z)=z\,\frac{z-t}{1-tz}
\]

has \(a=0\), \(b=-t\), \(c=1-t^2\) and \(\|f_t\|_{H^2}=1\). Therefore \(d(f_t)^2=2t^2\). The two nonzero squared singular values of \(f_t(A)\) have sum \(4[t^2+(1-t^2)^2]\) and product \(4t^4\). Hence

\[
\|f_t(A)\|^2=2\left(t^2+(1-t^2)^2+(1-t^2)\sqrt{1+t^4}\right),
\]

so \(\delta(f_t)=t^2+O(t^4)\). Thus \(d(f_t)/\sqrt{\delta(f_t)}\to\sqrt2\), establishing the lower bound and sharpness of the exponent and constant.

## Verification

The Frobenius bound, Schur coefficient identity, exact row-Gram entries, and inner-family singular-value formula are reproduced above, so the universal result does not rest on numerical tests. Independently, direct complex-matrix singular-value calculations for \(t=10^{-1},10^{-2},10^{-3}\) give deficit-to-square ratios approximately \(0.995000125\), \(0.999950000\), and \(0.999999500\), respectively; these are finite consistency checks, not a proof of the limit. The asymptotic statement is quantified over every Schur function, including nonpolynomial functions with infinitely many coefficients.

## Relationship to prior work

Åhag, Czyż and Virtanen proved the complete Crouzeix inequality for matrices of dimension three, and their detailed equality analysis already covers the qualitative polynomial equality cases and yields operator-level stability. Looi subsequently gave a short independent proof of the inequality. The equality characterization in this note is provided as needed background, not as an original contribution. The new claim is the **sharp asymptotic Hardy-space distance coefficient** at the three-site disk-normalized nilpotent. Existing results on two-dimensional nilpotents and matrix-value stability do not directly estimate the whole analytic symbol in \(H^2\) for this matrix.

## Limitations

The result treats scalar Schur functions and precisely this normalized three-site Jordan block; it does not establish matrix-valued symbol stability, sharp global (rather than local) constants, or analogous constants for arbitrary matrices. The asymptotic constant is proved, but the best all-deficit constant \(C\) is not determined. Quantitative symbol-distance statements under equivalent older formulations remain a possible publication-priority risk. Independent audit has not been performed.

## References

1. P. Åhag, R. Czyż, J. Virtanen, *The Complete Crouzeix Conjecture in Dimension Three and the Clouâtre–Ostermann–Ransford conjecture*, arXiv:2608.27346 (first public version 27 August 2026), especially Sections 10, 11 and 12.
2. S. Looi, *A short proof of the complete Crouzeix inequality in dimension three*, arXiv:2611.01416v1 (1 November 2026), four-page preprint.
3. S. Jin, *Rigidity at the Extremal Crouzeix Constant*, Preprints.org 202609.0079 (15 September 2026, version 2), especially its domain-rigidity discussion.
