# Sharp last-sign radius of the first three self-Fourier Hermite modes

## Finding

For the real three-dimensional eigenspace spanned by the Hermite modes of orders \(0\), \(4\), and \(8\), the sharp radius beyond which a nonzero Fourier-self-dual function with nonpositive origin value can be everywhere nonnegative is
\[
R_* = \sqrt{\frac{14-2z_*}{2\pi}}=0.60096438785483901355\ldots,
\]
where \(z_*\) is the unique real root in \((11/2,6)\) of
\[
W(z)=2z^3-23z^2+84z-105=0.
\]
Equality holds exactly for the positive multiples of
\[
f_*(x)=e^{-\pi x^2}u(u-\eta_*)(u-z_*)^2,\qquad
u=2\pi x^2,\quad \eta_*=14-2z_*.
\]
The endpoint zero at \(u=\eta_*\) is simple and the subsequent zero at \(u=z_*\) is double.

## Assumptions and scope

Use the unitary Fourier convention \(\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx\). Let \(H_n\) be the physicists' Hermite polynomial and let \(\psi_n(x)=H_n(\sqrt{2\pi}\,x)e^{-\pi x^2}\). For \(n\in\{0,4,8\}\), \(\widehat{\psi_n}=\psi_n\). Define \(\mathcal E=\operatorname{span}_{\mathbb R}\{\psi_0,\psi_4,\psi_8\}\).

For each nonzero \(f\in\mathcal E\) satisfying \(f(0)\le0\) and \(f(x)\ge0\) for all sufficiently large \(|x|\), let
\[
r(f)=\inf\{R\ge0:\ f(x)\ge0\text{ for every }|x|\ge R\}.
\]
The theorem states \(r(f)\ge R_*\), with equality precisely for \(f=c f_*\), \(c>0\). Because \(\widehat f=f\), this is a sharp finite-packet, one-dimensional \(+1\) Fourier sign-uncertainty theorem. It is not the unrestricted uncertainty constant.

## Proof

**1. Reduction to zero at the origin.** Since \(\psi_0(x)=e^{-\pi x^2}>0\) and is self-Fourier, if an admissible \(f\) has \(f(0)<0\), set \(g=f-f(0)\psi_0\). Then \(g(0)=0\), and \(g(x)>f(x)\) everywhere. The polynomial multiplying the Gaussian in \(g\) has positive leading coefficient (otherwise neither \(f\) nor \(g\) could be eventually nonnegative with \(f(0)<0\)). At \(r(f)>0\), that polynomial is positive; it remains positive on a slightly larger interval to the left of \(r(f)\) and tends to \(+\infty\) on the right. Therefore \(r(g)<r(f)\). For the sharp inequality and equality classification it suffices to treat \(f(0)=0\).

**2. One-parameter polynomial reduction.** Put \(u=2\pi x^2\). Direct expansion gives
\[
H_4(\sqrt u)-H_4(0)=16u(u-3),\qquad
H_8(\sqrt u)-H_8(0)=256u\,p(u),
\]
where
\[
p(u)=u^3-14u^2+\frac{105}{2}u-\frac{105}{2}.
\]
Hence every function in \(\mathcal E\) vanishing at zero is a positive Gaussian times \(u[A(u-3)+B p(u)]\), with real \(A,B\). Eventual nonnegativity forces \(B>0\), or \(B=0,A>0\). In the latter case the last-sign radius is \(\sqrt{3/(2\pi)}>R_*\). In the former case, scale \(B=1\), leaving the single-parameter monic cubic \(q_a(u)=p(u)+a(u-3)\).

**3. Two exact contact nodes.** Define
\[
\eta_*=14-2z_*,\qquad \alpha_*=-3z_*^2+28z_*-\frac{105}{2}.
\]
The polynomial identity, reducing its constant coefficient modulo \(W(z_*)=0\), is
\[
q_{\alpha_*}(u)=(u-\eta_*)(u-z_*)^2.
\]
The cubic discriminant of \(W\) is \(-6888\). Since \(W(11/2)=-6\) and \(W(6)=3\), it has exactly one real root, with \(11/2<z_*<6\). Consequently \(2<\eta_*<3<z_*\) and \(\alpha_*>0\). The factored cubic is negative on \((0,\eta_*)\) and nonnegative on \([\eta_*,\infty)\). Its sharp radius is exactly \(R_*\).

**4. Global sharpness and uniqueness.** For any \(a>\alpha_*\), evaluation at the first contact point gives
\[
q_a(\eta_*)=(a-\alpha_*)(\eta_*-3)<0.
\]
For any \(a<\alpha_*\), evaluation at the second contact point gives
\[
q_a(z_*)=(a-\alpha_*)(z_*-3)<0.
\]
Both contact arguments lie at or beyond the prospective boundary \(\eta_*\). Thus every \(a\ne\alpha_*\) has a negative value at some \(u\ge\eta_*\) and therefore has strictly larger last-sign radius. This proves sharpness and uniqueness for functions with zero origin value. Step 1 excludes all strict-negative-origin equality cases. Finally, positive scalar multiples of the factored Gaussian are exactly the extremizers. \(\square\)

## Verification

The accompanying `verify.py` checks the exact Hermite identities, cubic factorization modulo \(W\), both contact equations, the discriminant, root brackets, and a high-precision numerical evaluation. Running `python verify.py` with SymPy reproduces the archived `verification.log`. The two-contact sign argument in Step 4 is the infinite-family proof; sampling a numerical grid is neither used nor needed.

## Relationship to prior work

Cohn–Dong–Gonçalves (first posted 2022) formulated and studied the low-degree polynomial/Gaussian sign-uncertainty problem. Their Theorem 1.2 concerns dimension tending to infinity, and Theorem 2.1 gives a Laguerre-quadrature lower bound rather than the exact finite-dimensional, three-mode optimizer above. Gonçalves–Oliveira e Silva–Steinerberger (first posted 2016) give a four-mode example using Hermite orders \(0,4,8,12\) and numerical last-sign radius about \(0.59354\), which is better for the **larger** four-mode space but does not determine the sharp smaller packet. Their unrestricted extremizer theorem concerns infinitely many double roots; it does not imply a three-mode equality classification. Other general sign-uncertainty estimates do not supply this exact cubic constant. These are implication comparisons, not claims of an exhaustive bibliography.

## Limitations

Only real coefficients and exactly the Fourier \(+1\) packet of Hermite orders \(0,4,8\) are covered. There is no claim about complex sign-ordering, degree \(12\) or higher packets, the unrestricted Bourgain–Clozel–Kahane optimum, or independent scientific validation. Priority remains subject to discovery of equivalent unindexed optimization statements.

## References

1. H. Cohn, D. Dong, F. Gonçalves, *Sign uncertainty principles and low-degree polynomials*, arXiv:2210.01684 (first posted 2022-10-04), Theorems 1.2 and 2.1; https://arxiv.org/pdf/2210.01684.
2. F. Gonçalves, D. Oliveira e Silva, S. Steinerberger, *Hermite polynomials, linear flows on the torus, and an uncertainty principle for roots*, arXiv:1602.03366 (first posted 2016-02-10), Sections 2.1 and 4.2; https://arxiv.org/pdf/1602.03366.
3. F. Gonçalves, D. Oliveira e Silva, J. P. G. Ramos, *New sign uncertainty principles*, arXiv:2003.10771 (first posted 2020-03-24); https://arxiv.org/abs/2003.10771.
