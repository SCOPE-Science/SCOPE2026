# Sharp unrestricted five-tap Fourier smoothing at every difference order

## Finding
For every real \(\kappa>0\), define the Fourier smoothing cost of a real symmetric kernel \(u\), supported on \(\{-2,-1,0,1,2\}\) and normalized by \(\sum_j u(j)=1\), by
\[
\mathcal C_\kappa(u)=\max_{\theta\in[-\pi,\pi]}|e^{i\theta}-1|^\kappa\,|\widehat u(\theta)|,
\qquad \widehat u(\theta)=\sum_{j=-2}^{2}u(j)e^{ij\theta}.
\]
For positive integer \(\kappa\), this is exactly the operator norm on \(\ell^2(\mathbb Z)\) of \(f\mapsto\nabla^\kappa(u*f)\), where \(\nabla f(j)=f(j+1)-f(j)\).

Set \(r=\kappa/2\). There is exactly one \(h>(r+2)/r\) satisfying
\[
 h^{r+1}(rh-r-2)=(r+2)h-r. \tag{1}
\]
Put
\[
 A=\frac{r(1+h)}{(r+1)h},\quad B=\frac{r}{(r+2)h},\quad
 C=\frac{(r+2)h-r}{(r+1)(r+2)h}. \tag{2}
\]
There is exactly one \(z>h\) satisfying
\[
 z^r(1-Az+Bz^2)=C. \tag{3}
\]
**The exact sharp value and unique minimizer** are
\[
 \boxed{\min_u \mathcal C_\kappa(u)=2^\kappa\frac{C}{z^r}},\qquad
 \boxed{\widehat u_\kappa(\theta)=1-a y+b y^2,\quad
 y=\sin^2(\theta/2),\quad a=Az,\quad b=Bz^2}. \tag{4}
\]
Equivalently, the five spatial coefficients are uniquely
\[
 \boxed{u_\kappa(0)=1-\frac a2+\frac{3b}{8},\quad
 u_\kappa(\pm1)=\frac{a-b}{4},\quad
 u_\kappa(\pm2)=\frac b{16}.} \tag{5}
\]
The weighted Fourier multiplier has exactly three alternating sharp contacts at \(y=1/z,h/z,1\), of signs \(+,-,+\). In particular, the unique unrestricted optimizer has a sign-changing Fourier symbol and cannot be Fourier nonnegative.

For the previously unresolved unrestricted fifth difference at five taps, \(\kappa=5\) gives \(h=2.024060668721\ldots\), \(z=2.412564506748\ldots\), and
\[
 \boxed{\min_u\mathcal C_5(u)=0.733730437749\ldots},\qquad
 (u(0),u(1),u(2))=(0.311767395540\ldots,\,0.244267730955\ldots,\,0.099848571275\ldots).
\]

## Assumptions and scope
The class consists of **all real symmetric normalized** kernels with support contained in the indicated five sites; no nonnegativity constraint is imposed on coefficients or Fourier multipliers. The parameter \(\kappa\) may be any positive real, with the classical forward differences recovered at positive integers. The Fourier transform and \(\ell^2\) norm use counting measure on \(\mathbb Z\), and angular frequency belongs to the circle of period \(2\pi\). There are no requirements on input signals beyond membership in \(\ell^2(\mathbb Z)\). The root prescriptions in (1)–(3) are part of the exact result, not numerical approximations.

## Proof
**1. Fourier reduction.** Put \(y=(1-\cos\theta)/2=\sin^2(\theta/2)\). The real even trigonometric polynomials of degree at most two, normalized to one at zero frequency, are precisely
\[
 q(y)=1-ay+by^2,\qquad a,b\in\mathbb R.
\]
By the Fourier multiplier norm identity, \(|e^{i\theta}-1|=2\sqrt y\), so the original optimization is exactly
\[
 2^\kappa\inf_{a,b\in\mathbb R}\max_{0\le y\le1} y^r|1-ay+by^2|. \tag{6}
\]
This is a two-parameter (not one-parameter) weighted minimax problem.

**2. First root and critical heights.** On \(h>(r+2)/r\), the left side of
\[
 h^{r+1}=\frac{(r+2)h-r}{rh-(r+2)}
\]
is strictly increasing from a finite positive value to infinity, while the right side strictly decreases from infinity to \((r+2)/r\). Its derivative has numerator \(r^2-(r+2)^2=-4(r+1)<0\). Thus (1) has exactly one root \(h\) in that interval. The constants in (2) obey \(A,B,C>0\), and
\[
 Q(h):=1-Ah+Bh^2=\frac{(r+2)-rh}{(r+1)(r+2)}<0,
\quad Q'(h)=\frac{r(rh-r-2)}{(r+1)(r+2)h}>0.
\]
Since \(Q'(z)=-A+2Bz\) strictly increases, \(Q\) strictly increases on \([h,\infty)\). Hence \(Q\) has exactly one zero beyond \(h\), after which \(z^rQ(z)\) strictly increases from zero to infinity. It follows that (3) has exactly one root \(z>h\), and that root satisfies \(Q(z)>0\).

**3. Exact alternation.** Define \(q_*(y)=1-Azy+Bz^2y^2\). Direct differentiation gives
\[
 \frac{d}{dy}\{y^r q_*(y)\}=
 \frac{r}{h}y^{r-1}(zy-1)(zy-h),\qquad y>0. \tag{7}
\]
Since \(z>h>1\), the critical points \(t=1/z\) and \(v=h/z\) lie strictly between zero and one. Evaluation yields
\[
 q_*(t)=C>0,\quad
 q_*(v)=\frac{r+2-rh}{(r+1)(r+2)}<0,\quad
 q_*(1)=Q(z)=\frac{C}{z^r}>0.
\]
Equation (1) makes \(v^r q_*(v)=-C/z^r\), while equation (3) gives \(q_*(1)=C/z^r\). The derivative sign pattern in (7) is positive, negative, positive across the intervals separated by \(t,v\). Combined with \(y^rq_*(y)\to0\) at the origin, this proves
\[
 \max_{0\le y\le1}y^r|q_*(y)|=\frac{C}{z^r},
\]
with all three indicated contacts and no larger hidden interior values.

**4. Global sharpness and uniqueness.** Let \(q(y)=1-\widetilde a y+\widetilde b y^2\) be any competitor whose weighted supremum does not exceed \(C/z^r\). At the three sharp contacts, one must have
\[
 q(t)-q_*(t)\le0,\qquad q(v)-q_*(v)\ge0,\qquad q(1)-q_*(1)\le0.
\]
But \(d(y)=(q(y)-q_*(y))/y\) is affine on \((0,1]\), and \(t<v<1\). Consequently \(d(v)\) is a strictly positive convex combination of \(d(t)\) and \(d(1)\). The three inequalities force \(d(t)=d(v)=d(1)=0\); hence \(q=q_*\). No competitor can have smaller supremum, and equality uniquely determines \(q_*\). Fourier cosine expansion gives exactly (5), proving the theorem. Because the middle sharp contact is strictly negative and the others positive, \(q_*\) is not nonnegative on the Fourier circle.

## Verification
Execute `python3 CHECK.py` (standard library only). It solves (1)–(3) by bracketing, reconstructs the exact three-contact pattern and Fourier coefficients for eleven representative positive orders, samples 2,001 points at each order, and independently tests six coefficient perturbations per order against all analytic stationary points. The fifth-order value and coefficient values above reproduce the checker output. The proof for all real \(\kappa>0\) is Steps 1–4, not the finite computational sample.

For an additional low-order normalization check, \(\kappa=1\) yields exactly the uniform five-point kernel \(u(j)=1/5\) and the known sharp constant \(2/5\). For \(\kappa=5\), numerical linear programming on a fine mesh also independently returns the same three active frequencies. Neither check substitutes for the analytic global argument.

## Relationship to prior work
Gaitán, Garzón and Madrid (arXiv:2604.25074v1; first posted April 28, 2026) solve unrestricted general-radius difference orders one, two and three, and Fourier-nonnegative orders four and six. Their Table 2 explicitly leaves the unrestricted fourth and sixth orders, and remaining orders, open at general radius. Their weighted alternation and Fejér–Riesz squaring methods are prior tools; those methods do not by themselves give the unrestricted radius-two formula (1)–(5) for every order.

The published *All-order sharp three-point smoothest averages* gives the unrestricted one-parameter radius-one answer, not the two-parameter radius-two answer. The published *Sharp high-difference binomial limits for fixed-radius discrete Fourier smoothers* gives the asymptotic sharp norm at each fixed radius (including a radius-two limiting constant), explicitly without exact finite-order optimizers. This result instead gives **all finite orders and a unique optimal five-site kernel**, and is compatible with those limits. The existing general fourth/sixth-order Fourier-positive results do not cover an optimizer whose Fourier symbol changes sign.

## Limitations
There is no claim for support radius greater than two, for nonsymmetric/complex filters, or for frequency-dependent weights other than the stated power multiplier. The extremal parameters are specified as unique roots of scalar equations, not radicals. An equivalent special weighted-Chebyshev formula under older approximation-theory terminology may exist beyond inspected literature; independent external priority validation has not been conducted.

## References
1. J. Gaitán, C. Garzón and J. Madrid, *The smoothest average and some extremal problems for polynomials*, arXiv:2604.25074v1 (April 28, 2026), https://arxiv.org/abs/2604.25074.
2. *All-order sharp three-point smoothest averages* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-all-order-sharp-three-point-smoothest-averages--97ecaa4cd5e9.
3. *Sharp high-difference binomial limits for fixed-radius discrete Fourier smoothers* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-high-difference-binomial-limits-for-fixed-radius-discrete--ec4a8b1168c3.
4. N. Kravitz and S. Steinerberger, *The smoothest average: Dirichlet, Fejér and Chebyshev*, Bull. London Math. Soc. 53 (2021), 1801–1815, https://doi.org/10.1112/blms.12543.
5. S. Richardson, *A Sharp Fourier Inequality and the Epanechnikov Kernel*, arXiv:2310.09713 (2023), https://arxiv.org/abs/2310.09713.
