# A sharp planar negative-set inequality in the fourth Hermite Fourier band

## Finding

Use the unitary Fourier convention
\[
\widehat f(\xi)=\int_{\mathbb R^2}f(x)e^{-2\pi i x\cdot\xi}\,dx.
\]
Let \(\mathcal E_4\) be the real vector space of all functions \(f(x)=e^{-\pi|x|^2}P(x)\), with \(P\) a real polynomial of total degree at most four, for which \(\widehat f=f\) and \(f(0)=0\). For every nonzero \(f\in\mathcal E_4\), its nonpositive set \(M(f)=\{x\in\mathbb R^2:f(x)\le0\}\) satisfies
\[
\boxed{|M(f)|\ge 2.}
\]
Equality occurs exactly for positive scalar multiples of
\[
 f_*(x)=e^{-\pi|x|^2}\,(\pi|x|^2)(\pi|x|^2-2).
\]
In particular, allowing *all* nonradial fourth-Hermite modes never improves on the radial disk. More strongly, the excess negative area has an exact nonnegative angular Fisher-information decomposition described below.

## Assumptions and scope

Lebesgue measure and the standard Euclidean norm are used on \(\mathbb R^2\). The functions are real-valued, nonzero, Gaussian times a polynomial of *total* degree at most four, self-Fourier with eigenvalue \(+1\), and vanish at zero. The conclusion also covers functions whose nonpositive set has infinite area (using the extended-real inequality); no hypothesis of eventual pointwise nonnegativity is needed.

Write \(x=r(\cos\theta,\sin\theta)\), \(s=\pi r^2\), \(\phi=2\theta\), and \(\langle h\rangle=(2\pi)^{-1}\int_0^{2\pi}h(\phi)\,d\phi\). For a finite-area \(M(f)\), there is a *unique* positive scalar normalization for which
\[
 f(r,\theta)=e^{-s}s[-A(\phi)+sB(\phi)],
\]
where
\[
 U(\phi)=a\cos\phi+c\sin\phi,\qquad V(\phi)=b\cos2\phi+d\sin2\phi,
\]
\[
 B(\phi)=2-2U(\phi)+V(\phi)>0,\qquad A(\phi)=4-3U(\phi).
\]
The exact area identity is
\[
\boxed{|M(f)|=2+\frac12\left\langle\big(\partial_\phi\log B\big)^2\right\rangle+
\left\langle\frac{(-A)_+}{B}\right\rangle,}
\]
where \(q_+=\max(q,0)\). These terms are independently nonnegative. This is the stronger form of the finding.

## Proof

**1. Complete Fourier-eigenfunction normal form.** In two dimensions the real Fourier eigenfunctions of the form Gaussian times a polynomial of total degree at most four with eigenvalue \(+1\) are the Hermite orders zero and four. Vanishing at the origin determines the order-zero coefficient. A basis of the remaining five-dimensional real space is given, in polar coordinates, by
\[
 e^{-s}(-4s+2s^2),\quad e^{-s}s(3-2s)\cos\phi,\quad e^{-s}s(3-2s)\sin\phi,
\]
\[
 e^{-s}s^2\cos2\phi,\quad e^{-s}s^2\sin2\phi.
\]
Each expression has Fourier eigenvalue \(+1\). This follows directly by differentiating the self-Fourier Gaussian (and is checked symbolically by the included checker); equivalently they are the radial Laguerre and angular Hermite modes of total order four. Thus every nonzero admissible function has
\[
 f=e^{-s}s[-4q+3U+s(2q-2U+V)],
\]
with real \(q,a,c,b,d\), where \(U,V\) are as above. The parameters all vanish only for the zero function.

**2. Finiteness forces a positive angular leading coefficient.** Put \(B_q=2q-2U+V\). If \(B_q\) is negative on a nonempty open arc, then \(f\) is negative for all sufficiently large \(r\) in an open cone, so \(|M(f)|=\infty\). If \(B_q\equiv0\), Fourier orthogonality forces \(q=a=c=b=d=0\), excluded. Otherwise, finite area requires \(B_q\ge0\) pointwise. Its angular mean is \(2q\), so \(q>0\); multiplying by \(q^{-1}\) gives the normal form with mean \(B=2\).

It remains to exclude angular zeros. If the nonnegative nonconstant trigonometric polynomial \(B\) vanishes at \(\phi_0\), then, for some integer \(m\in\{1,2\}\) and \(C>0\),
\[
 B(\phi_0+t)=Ct^{2m}+O(t^{2m+1}).
\]
The crucial identity
\[
\boxed{A=2B+\tfrac12 B''}
\]
shows that \(A(\phi_0+t)/B(\phi_0+t)=m(2m-1)t^{-2}+O(|t|^{-1})\), which is positive and nonintegrable. On each ray with \(A,B>0\), \(f<0\) precisely for \(0<s<A/B\). Polar integration near \(\phi_0\) consequently gives \(|M(f)|=\infty\). Hence finite negative area implies \(B>0\) everywhere.

**3. Exact area and positive decomposition.** When \(B>0\), the negative radial interval at angle \(\phi\) is \(0<s<(A(\phi)/B(\phi))_+\). Since \(dx=ds\,d\theta/(2\pi)\), and every \(2\pi\)-periodic function of \(\phi=2\theta\) has the same mean under \(\theta\) and \(\phi\),
\[
 |M(f)|=\left\langle \frac{A_+}{B}\right\rangle
 =\left\langle\frac A B\right\rangle+\left\langle\frac{(-A)_+}{B}\right\rangle.
\]
Using the identity from Step 2 and integrating by parts over a full period,
\[
 \left\langle\frac A B\right\rangle
 =2+\frac12\left\langle\frac{B''}{B}\right\rangle
 =2+\frac12\left\langle\left(\frac{B'}B\right)^2\right\rangle.
\]
This proves the exact formula, the bound, and its equality characterization: equality forces \(B'\equiv0\), whence \(U=V=0\); the normalized polynomial is then \(-4s+2s^2\). Conversely this polynomial is negative exactly on the open disk \(\pi r^2<2\), which has area \(2\). Positive scalar multiples have the same set; negative multiples have an infinite-area nonpositive set. □

**4. A local rigidity coefficient.** For \(\varepsilon^2=a^2+b^2+c^2+d^2\to0\), one has \(A>0\), \(B>0\), and expansion of the exact identity gives
\[
 |M(f)|=2+\frac14(a^2+b^2+c^2+d^2)+O(\varepsilon^3).
\]
This quantifies the strict cost of every independent first nonradial Hermite perturbation.

## Verification

`CHECK.py` is a standalone symbolic and numerical consistency checker requiring Python, SymPy, and NumPy. It applies the Fourier Gaussian differentiation rule to all five basis polynomials and proves symbolically that each is self-Fourier; it also proves symbolically \(A=2B+B''/2\), checks the area/decomposition identity on six sample coefficient tuples, and checks three singular boundary scales. The checker is finite supplementary evidence; the all-function result and the singular-zero argument are analytical.

Run `python CHECK.py`. Expected summary: `CHECK_OK symbolic_Fourier_eigenbases=5 angular_exact_identities=6 singular_boundary_tests=3`.

## Relationship to prior work

Roni Edwin, *Fourier inequalities and sign uncertainty II*, arXiv:2611.08224v1 (first public November 5, 2026), introduces the **definite-set uncertainty principle** asking how small the nonpositive set of an unrestricted Fourier eigenfunction with \(f(0)=0\) can be. Its general bound concerns arbitrary admissible functions, not this sharp, fully nonradial finite-Hermite-band classification.

Gonçalves, Oliveira e Silva, and Steinerberger, arXiv:1602.03366, investigate the *last sign-change radius* and properties of unrestricted extremizers, a distinct objective. Giraud and Peschanski, arXiv:math-ph/0504015, use Hermite/Laguerre polynomial algebra to study pointwise positivity conditions, including radial two-dimensional examples; no corresponding sharp nonpositive-*area* classification or angular Fisher identity appears in the inspected Sections II–IV. The Hermite eigenbasis itself is classical, not claimed new.

## Limitations

The bound is sharp **within the specified degree-four Gaussian–Hermite Fourier eigenspace in dimension two**; it does not assert a sharp bound for arbitrary Fourier eigenfunctions, for other degrees or dimensions, or for the last-sign radius. Literature equivalence beyond the inspected sources remains possible. Independent auditing has not been performed. The included numerical quadratures neither prove the infinite-dimensional claim nor certify publication priority.

## References

1. Roni Edwin, *Fourier inequalities and sign uncertainty II*, arXiv:2611.08224v1, first submitted 2026-11-05, https://arxiv.org/html/2611.08224v1.
2. Felipe Gonçalves, Diogo Oliveira e Silva, Stefan Steinerberger, *Hermite polynomials, linear flows on the torus, and an uncertainty principle for roots*, arXiv:1602.03366, https://arxiv.org/abs/1602.03366.
3. B. G. Giraud and R. Peschanski, *On positive functions with positive Fourier transforms*, arXiv:math-ph/0504015, https://arxiv.org/abs/math-ph/0504015.
