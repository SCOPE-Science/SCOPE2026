# Sharp two-phase Markov–Bernstein constant for damped conjugate modes

## Finding

Fix real \(a,b>0\). Let \(X_{a,b}\) be the two-dimensional real function space
\[
X_{a,b}=\{e^{-at}(A\cos(bt)+B\sin(bt)):A,B\in\mathbb R,\ t\ge0\},
\]
equipped with the supremum norm on the nonnegative half-line. The *sharp first-derivative constant* is
\[
\mathcal M(a,b)=\sup_{0\ne f\in X_{a,b}}\frac{\|f'\|_{L^\infty(0,\infty)}}{\|f\|_{L^\infty(0,\infty)}}.
\]
Write \(r=a/b\), \(R=\sqrt{1+r^2}\), \(\phi=\arctan r\), and
\[
u_1(r)=\frac\pi2+\arctan r.
\]
Let \(u_c(r)\) be the unique root in \((\arctan(1/r),\pi)\) of
\[
e^{ru_c}(r\sin u_c-\cos u_c)=1.
\]
Then the sharp constant, including its attainment, is
\[
\boxed{\mathcal M(a,b)=b(1+r^2)e^{r u_*(r)}\sin u_*(r),\qquad u_*(r)=\min\{u_1(r),u_c(r)\}.}
\]
There is a unique transition ratio \(r_*>0\), defined by
\[
\frac{2r_*}{\sqrt{1+r_*^2}}\exp\!\left(r_*\left(\frac\pi2+\arctan r_*\right)\right)=1,
\qquad r_*=0.29908438015271477\ldots.
\]
For \(0<r\le r_*\), the sharp constant simplifies to
\[
\mathcal M(a,b)=b\sqrt{1+r^2}\,e^{r(\pi/2+\arctan r)},
\]
and the normalized real extremizer has just one active positive-time absolute-value contact, apart from the transition. For \(r>r_*\), it instead has two active contacts, at time zero and at \(u_c/b\), with opposite values. In both regimes the real extremizer is unique up to real scaling and sign. The same sharp constant applies to the full complex span of the two conjugate exponentials.

The dimensionless constant \(\mathcal M(br,b)/b\) is continuously differentiable but not twice differentiable at \(r_*\). Its second derivative has an explicit strictly negative jump, specified below. Also,
\[
\lim_{r\downarrow0}\frac{\mathcal M(br,b)}b=1,
\qquad
\lim_{r\to\infty}\frac{\mathcal M(br,b)}{br}
=\frac{q}{q-1}=4.59112147666862\ldots,
\]
where \(q=1+W(e^{-1})\) is the unique root in \((1,2)\) of \((q-1)e^q=1\). Here \(W\) is the principal Lambert function.

## Assumptions and scope

All statements about sharpness and extremizers refer to the first derivative and the supremum norm on \([0,\infty)\), without a weight in that norm. The parameters satisfy \(a>0\), \(b>0\); the zero-frequency and zero-damping cases occur only as limiting regimes. Complex functions mean arbitrary complex linear combinations of \(e^{(-a+ib)t}\) and \(e^{(-a-ib)t}\). No assertion is made about higher derivatives, sums with additional exponentials, finite observation windows, or systems with two different decay rates.

## Proof

**1. Reduce to initial velocity and unit frequency.** Put \(s=bt\). Since differentiation in \(t\) multiplies the derivative norm by \(b\), it is enough to calculate the dimensionless constant for \(b=1\), \(a=r\). The space is invariant under right translations \((T_hf)(t)=f(t+h)\), which contract the supremum norm. Differentiation commutes with these translations, so
\[
\sup_{f\ne0}\frac{\|f'\|_\infty}{\|f\|_\infty}
=\sup_{f\ne0}\frac{|f'(0)|}{\|f\|_\infty}.
\]
The equality follows by applying the initial-velocity bound to each \(T_hf\), then using \(h=0\) for the opposite inequality.

For any complex combination, translate to a point attaining its derivative supremum, rotate its complex phase to make the derivative real and nonnegative, and take the real part. This produces a real damped sinusoid with the same initial derivative and no greater supremum norm. Therefore the real and complex sharp constants coincide.

**2. Exact one-variable reduction.** Any nonzero real member can, up to an overall nonzero scalar, be expressed as
\[
f(t)=e^{-rt}\cos(t-\theta).
\]
Let \(\phi=\arctan r\). Choose \(u\in[0,\pi)\) with \(\theta\equiv u+\phi\pmod\pi\). All positive-time stationary points have times \(u+k\pi\), and their absolute values decrease by \(e^{-r\pi}\) each period. Thus the supremum is the larger of the endpoint value and the first stationary absolute value:
\[
\|f\|_\infty
=\frac1R\max\{|\cos u-r\sin u|,e^{-ru}\}.
\]
Meanwhile \(|f'(0)|=R\sin u\). Hence the dimensionless sharp constant equals
\[
C(r)=\max_{0\le u\le\pi}
\frac{R^2\sin u}{\max\{|\cos u-r\sin u|,e^{-ru}\}}.
\tag{1}
\]
The equality also includes phases with a stationary point at the endpoint; the endpoints \(u=0,\pi\) contribute zero to (1).

**3. One switching point and one maximizer.** Define
\[
g_r(u)=e^{ru}(\cos u-r\sin u).
\]
For \(0<u<\pi\),
\[
g_r'(u)=-R^2e^{ru}\sin u<0,
\quad g_r(0)=1,\quad g_r(\pi)=-e^{r\pi}<-1.
\]
Consequently there is one and only one \(u_c\) with \(g_r(u_c)=-1\); it lies after the zero of \(\cos u-r\sin u\), namely in \((\arctan(1/r),\pi)\). The denominator in (1) is \(e^{-ru}\) for \(u\le u_c\), and \(r\sin u-\cos u\) for \(u\ge u_c\). Thus its ratio is respectively
\[
F_r(u)=R^2e^{ru}\sin u
\quad\text{and}\quad
H_r(u)=\frac{R^2}{r-\cot u}.
\]
The function \(F_r\) increases strictly up to the unique point \(u_1=\pi/2+\phi\), then decreases strictly. The function \(H_r\) decreases strictly throughout \([u_c,\pi)\). Therefore the unique maximizing phase is \(u_*=\min\{u_1,u_c\}\), proving the sharp formula.

**4. Transition and explicit extremizers.** Since \(\sin u_1=1/R\), \(\cos u_1=-r/R\), one has
\[
g_r(u_1)=-\frac{2r}{R}e^{ru_1}.
\]
The function \(h(r)=2r e^{r u_1(r)}/R\) increases strictly from zero to infinity: its logarithmic derivative is \(1/r+u_1(r)>0\). Hence the unique \(r_*\) with \(h(r_*)=1\) separates \(u_c>u_1\) from \(u_c<u_1\), with equality at the threshold.

For each \(r>0\) define, in the dimensionless time variable,
\[
f_r(t)=R e^{r u_*}e^{-rt}\cos(t-u_*-\phi).
\]
Its endpoint value has magnitude at most one, its first stationary value at \(t=u_*\) equals one, and every later stationary value has smaller absolute magnitude. Thus \(\|f_r\|_\infty=1\) and
\[
f'_r(0)=R^2e^{r u_*}\sin u_*=C(r).
\]
For \(r<r_*\), the endpoint value is strictly greater than \(-1\), so only the first stationary point is active. For \(r\ge r_*\), \(f_r(0)=-1\) and \(f_r(u_*)=1\). Uniqueness of the maximizing phase in (1) proves uniqueness of normalized real extremizers up to sign.

**5. Differentiability at the contact transition.** Set \(W(r,u)=R^2e^{ru}\sin u\). The two analytic branches are \(W(r,u_1(r))\) below the threshold and \(W(r,u_c(r))\) above it. They agree at \(r_*\), where \(W_u(r_*,u_1)=0\); their first derivatives therefore agree. Implicit differentiation of \(e^{ru_c}(r\sin u_c-\cos u_c)=1\) gives
\[
u_c'(r)=-\frac{u_c+e^{r u_c}\sin u_c}{W(r,u_c)}.
\]
At \(r_*\), put \(R_*=\sqrt{1+r_*^2}\), \(u_*=u_1(r_*)\), and \(W_*=W(r_*,u_*)\). Then
\[
u_1'(r_*)=R_*^{-2},\qquad
u_c'(r_*)=-R_*^{-2}-u_*/W_*,\qquad
W_{uu}(r_*,u_*)=-R_*^2W_*.
\]
Differentiating the two composites twice and using \(W_u(r,u_1(r))=0\) yields the strictly negative jump
\[
\boxed{C''(r_*+)-C''(r_*-)
=-R_*^2W_*\left(\frac{2}{R_*^2}+\frac{u_*}{W_*}\right)^2<0.}
\]
This establishes \(C\in C^1\) but \(C\notin C^2\) at the unique phase transition.

**6. Endpoint asymptotics.** As \(r\downarrow0\), the low-damping branch gives
\[
C(r)=1+\frac\pi2r+O(r^2).
\]
For sufficiently large \(r\), \(u_*=u_c\). Set \(x_r=ru_c\); its defining equation is
\[
e^{x_r}\left(r\sin(x_r/r)-\cos(x_r/r)\right)=1.
\]
The monotonicity already established places \(x_r\) between \(1\) and \(2\) for all sufficiently large \(r\). Uniform convergence on that interval identifies its unique limit \(q\in(1,2)\), characterized by \(e^q(q-1)=1\). Consequently
\[
\lim_{r\to\infty}\frac{C(r)}r
=\lim_{r\to\infty}\frac{(1+r^2)e^{x_r}\sin(x_r/r)}r
=q e^q=\frac{q}{q-1}.
\]
All asymptotic statements follow. This completes the proof.

## Verification

The standalone, standard-library-only `check.py` computes \(r_*\), the unique stationary-contact root, and the claimed sharp constant using bracketing. It compares the formula against 58 independent phase grids with 1,001 phases each, probes explicitly normalized extremizers at 2,001 times for each parameter, and checks a separate coefficient-angle formulation. It also checks the large-damping limit and numerically probes the second-derivative jump. These are supplementary finite checks; the proof above establishes the continuum and all-parameter statements.

Reproduction: `python3 check.py` from the directory containing this document and the script. No source download or specialized software is required for the checker.

## Relationship to prior work

Protasov, *Generalized Markov–Bernstein inequalities and stability of dynamical systems* (first arXiv submission 25 September 2022), defines general exponential-polynomial sharp constants and reduces them to finite-dimensional constrained uniform approximation; his results for exact sharp constants focus on real exponent systems. The present claim evaluates the minimal nonreal conjugate pair exactly, including its active-contact transition, explicit uniqueness, and differentiability loss; it does **not** prove Protasov's general comparison conjecture.

Kamalov and Protasov, *Chebyshev approximation by non-Chebyshev systems* (first arXiv submission 24 March 2024), give a general constrained approximation algorithm and numerical Markov–Bernstein examples. In their Section 9.4, the damped harmonic example includes an additional \(e^{-t}\) mode in addition to the sine and cosine modes. The exact analytic two-dimensional phase diagram here is not their numerical three-mode example. The older Borwein–Erdélyi work on exponential sums supplies a different family of real-exponent Markov–Bernstein bounds.

## Limitations

This theorem concerns one conjugate pair sharing one decay rate and the first-derivative uniform norm. It does not establish a comparison theorem for arbitrary complex spectra or multiple modes. The explicit numerical value of \(r_*\) is a computed approximation, not a claim of an elementary closed form; the root equation is the exact definition. Prior-publication priority remains subject to discovery of older specialist work on maximum initial velocities of damped oscillators. No independent mathematical validation has been performed.

## References

1. V. Yu. Protasov, *Generalized Markov–Bernstein inequalities and stability of dynamical systems*, arXiv:2209.12250 (first public version 25 September 2022), https://arxiv.org/abs/2209.12250.
2. V. Yu. Protasov and R. Kamalov, *Chebyshev approximation by non-Chebyshev systems*, arXiv:2403.16330 (first public version 24 March 2024), https://arxiv.org/abs/2403.16330.
3. P. Borwein and T. Erdélyi, *A sharp Bernstein-type inequality for exponential sums*, Journal für die reine und angewandte Mathematik 476 (1996), 127–141, https://doi.org/10.1515/CRLL.1996.476.127.
