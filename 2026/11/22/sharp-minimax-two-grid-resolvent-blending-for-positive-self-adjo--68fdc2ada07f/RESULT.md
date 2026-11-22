# Sharp minimax two-grid resolvent blending for positive self-adjoint semigroups

## Finding

Let \(A\geq 0\) be a self-adjoint operator on a complex Hilbert space, let \(\lambda>0\), and let \(h>0\). Set
\[
Q_h=h(I-e^{-h(\lambda+A)})^{-1},\qquad P_h=Q_h-\frac h2I,\qquad
R_h(w)=wP_{h/2}+(1-w)P_h,\quad w\in\mathbb C.
\]
Thus the two levels use the same sampled semigroup at integer multiples of \(h/2\), and the coefficients sum to one. Define
\[
L(z)=\coth z-\frac1z,\quad
J(z)=\frac{\cosh^2z}{z^2}-\coth^2z\quad (z>0).
\]
There is a unique pair \((z_*,a_*)\in(0,\infty)\times(1/3,1)\) satisfying
\[
J(z_*)=a_*,
\qquad a_*\tanh z_*-L(z_*)=1-a_*.
\]
Put \(w_*=1+a_*\) and \(C_*=(1-a_*)/4\). Then, for every \(A,\lambda,h\) as above,
\[
\boxed{\|R_h(w_*)-(\lambda+A)^{-1}\|\leq C_*h.}
\]
Numerically,
\[
z_*=1.10450454618952885\ldots,\qquad
w_*=1.74430841041328044\ldots,\qquad
C_*=0.0639228973966798902\ldots .
\]
This is the *best possible universal coefficient*, even when complex blending weights are allowed: on \(L^2([0,\infty),dx)\), take \(A\) to be multiplication by \(x\). For each \(0<h\le 4z_*/\lambda\),
\[
\boxed{\min_{w\in\mathbb C}
 \|R_h(w)-(\lambda+A)^{-1}\|=C_*h,}
\]
and \(w_*\) is its unique minimizer. The negative extremal spectral scale is \(x_*=4z_*/h-\lambda\), while the opposite extremal value is approached as \(x\to\infty\).

For comparison, the classical second-order Richardson/Romberg weight \(w=4/3\) has norm error exactly \(h/6\) on this model. Optimizing the full spectrum reduces this sharp constant by a factor \((1/6)/C_*=2.607307\ldots\), without changing the first-order rate.

## Assumptions and scope

The semigroup is \(S_t=e^{-tA}\) with \(A\ge0\) self-adjoint; \(\lambda>0\) is real and \(h>0\). Both resolvents and sampling operators are bounded by continuous functional calculus. The theorem concerns uniform absolute operator norm on a positive self-adjoint class and the exact two-level affine span of the *trapezoid-corrected* sampled resolvents, not arbitrary quadrature, general complex-spectrum semigroups, or error rates for smooth vectors. A signed coarse-level weight is permitted, as in Richardson extrapolation.

The sharpness model has continuous spectrum \([0,\infty)\). If the condition \(h\lambda\le 4z_*\) fails, the same universal upper bound holds but no claim is made that its particular model's best weight remains \(w_*\).

## Proof

**1. Scalar reduction and the half-angle identity.** For a spectral value \(x\ge0\), write
\[
z=\frac{h(\lambda+x)}4>0.
\]
The symbol of the trapezoid-corrected resolvent at mesh \(h\) is
\[
P_h(x)=\frac h2\coth(2z),\qquad P_{h/2}(x)=\frac h4\coth z,
\]
and the exact resolvent has symbol \(h/(4z)\). The elementary identity
\[
2\coth(2z)=\coth z+\tanh z
\]
therefore gives, with \(a=w-1\),
\[
\frac{R_h(w)(x)-(\lambda+x)^{-1}}h
=\frac14\big(L(z)-a\tanh z\big).
\tag{1}
\]
Consequently it suffices to minimize
\[
\Phi(a)=\sup_{z>0}|L(z)-a\tanh z|.
\tag{2}
\]
For arbitrary positive self-adjoint \(A\), its spectrum samples a subset of \(z>0\), so a bound for (2) proves the universal operator inequality.

**2. A strict single-turning-point lemma.** The function
\[
J(z)=\frac{L'(z)}{\operatorname{sech}^2z}
=\frac{\cosh^2 z}{z^2}-\coth^2z
\]
is strictly increasing from \(1/3\) to \(+\infty\). To prove the non-obvious monotonicity, put \(\xi=z^2\) and rewrite
\[
J(z)=\frac{(\cosh4z-1)/4-z^2(1+\cosh2z)}
 {z^2(\cosh2z-1)}
=\frac{\sum_{n\ge2}b_n r_n\xi^n}
 {\sum_{n\ge2}b_n\xi^n},
\]
where
\[
b_n=\frac{2^{2n-2}}{(2n-2)!}>0,\qquad
r_n=\frac{4^n}{(2n)(2n-1)}-1.
\]
The sequence \(r_n\) increases strictly for \(n\ge2\), since
\[
\frac{4^{n+1}/[(2n+2)(2n+1)]}
 {4^n/[(2n)(2n-1)]}
=\frac{4(2n)(2n-1)}{(2n+2)(2n+1)}>1.
\]
Differentiating the quotient of the two everywhere-convergent positive-coefficient series shows that its derivative with respect to \(\xi\) has numerator
\[
\sum_{m>n\ge2}(m-n)b_mb_n(r_m-r_n)\xi^{m+n-1}>0.
\]
At zero the limit is \(r_2=1/3\); at infinity the original hyperbolic expression tends to infinity. This proves the lemma.

**3. Minimax equioscillation and uniqueness.** For real \(a\), put
\[
g_a(z)=L(z)-a\tanh z.
\]
Since \(g_a'(z)=\operatorname{sech}^2z\,(J(z)-a)\), for \(a\in(1/3,1)\) the function decreases from zero to one strictly negative minimum at the unique \(z(a)>0\) with \(J(z(a))=a\), and then increases to \(1-a>0\). Define
\[
M(a)=a\tanh z(a)-L(z(a))>0.
\]
It is continuous and strictly increasing in \(a\): for \(a_2>a_1\), testing the supremum defining \(M(a_2)\) at \(z(a_1)\) shows
\[
M(a_2)\ge M(a_1)+(a_2-a_1)\tanh z(a_1)>M(a_1).
\]
Thus \(\Phi(a)=\max\{M(a),1-a\}\) in this interval. At \(a=1/3\) the negative minimum vanishes and \(1-a=2/3\), whereas at \(a=1\) the negative minimum is positive and \(1-a=0\). There is exactly one crossing \(a_*\in(1/3,1)\), characterized by
\[
M(a_*)=1-a_*.
\tag{3}
\]
At that crossing \(\Phi(a_*)=1-a_*\), and the two extremal signs are at the unique finite \(z_*=z(a_*)\) and at the limiting point \(z=\infty\).

No coefficient outside this interval does better. For \(a\le1/3\), \(g_a\) is nonnegative and increasing, so \(\Phi(a)=1-a\ge2/3>1-a_*\). For \(a\ge1\), the identity
\[
\tanh z-L(z)
=\frac1z-\frac{1}{\sinh z\cosh z}>0
\]
implies \(g_a(z)<0\); hence its negative supremum is strictly larger than the value at \(a=1\), itself larger than \(1-a_*\). For complex \(a\), taking real parts in (2) proves \(\Phi(a)\ge\Phi(\operatorname{Re}a)\). When \(\operatorname{Re}a=a_*\) but \(\operatorname{Im}a\ne0\), the limit at infinity has modulus
\[
|1-a|>|1-a_*|,
\]
so the complex optimum too is unique. This completes the scalar minimax theorem and the universal operator bound.

**4. Sharpness in one fixed spectral model.** For \(A=M_x\) on \(L^2([0,\infty),dx)\), the multiplier norm is the supremum of (1) over
\[
z\in[h\lambda/4,\infty).
\]
If \(h\lambda/4\le z_*\), this set includes the finite negative contact at \(z_*\), while its unbounded upper end retains the positive contact \(z=\infty\). The error for \(a_*\) thus has norm exactly \(C_*h\). Any real coefficient \(a<a_*\) has a strictly larger positive limiting error; any \(a>a_*\) has a strictly larger negative error at \(z_*\). Complex coefficients are no better by the real-part argument, and a nonzero imaginary part at \(a_*\) worsens the limiting error. Hence the stated minimum is exact and its coefficient unique.

**5. Numerical constants and comparison.** Eliminating \(a_*\) from (3) yields the single-root equation
\[
J(z)\bigl(1+\tanh z\bigr)-1-L(z)=0.
\]
The preceding uniqueness proof shows that this equation has exactly one positive root. Direct substitution gives opposite signs at \(z=1.10450\) and \(z=1.10451\), yielding the displayed decimal values. At the ordinary Romberg coefficient \(w=4/3\), namely \(a=1/3\), step 3 gives \(\Phi(1/3)=2/3\), so its error on the unbounded continuous-spectrum model is exactly \(h/6\).

## Verification

The coefficient-series proof in step 2 verifies the critical global monotonicity analytically, rather than inferring it from plots. Equation (1) can be checked directly from the geometric-series representation of the sampled resolvent. The standalone `check_numeric.py` verifies root bracketing, the scalar half-angle identity, and finite-grid error inequalities as diagnostic tests; no finite grid is used to establish the infinite-domain optimality. The original self-contained proof establishes all quantifiers and both sharp contacts.

## Relationship to prior work

Castillo, *Sampled resolvents of \(C_0\)-semigroups: aliasing and sharp rates on the Crandall–Pazy scale*, arXiv:2611.15563v1 (first submitted 11 November 2026), gives the sampled-resolvent identity, its trapezoid correction, the classical Romberg weights in Corollary 5.2, and a Langevin-function sharpness example in Proposition 5.10(a). Those facts are inputs, not claimed as new. Its stated bounds and weights do not determine the optimal two-grid coefficient for the *operator-norm* error on the full positive spectral half-line. Classical Chebyshev equioscillation is the guiding general principle; the exact spectral reduction, single-turning-point lemma, optimal transcendental constant, and sharp operator model are the asserted contribution.

Berrut and Trummer's 2022 article on extrapolation quadrature from equispaced samples with jumps concerns different integrand classes and Euler–Maclaurin rules, not the explicit positive self-adjoint resolvent minimax problem. Broad rational-approximation and optimal-quadrature theory may contain implicit stronger coverage; no absolute novelty assertion is implied by unsuccessful searches.

## Limitations

The scheme uses signed levels and may amplify independent sampling noise. Only the infinite-time sampled-resolvent operators are treated; truncation at finite observation time adds error. The sharpness model and uniform bound concern nonnegative self-adjoint generators and real \(\lambda>0\), not all sectorial or nonnormal operators. The optimum's exactness for the continuous-spectrum model is asserted only when \(h\lambda\le4z_*\); the universal upper bound holds without that condition. No rate beyond first order is claimed. External independent mathematical review has not been performed; prior-art coverage is necessarily provisional.

## References

1. N. Castillo, *Sampled resolvents of \(C_0\)-semigroups: aliasing and sharp rates on the Crandall–Pazy scale*, arXiv:2611.15563v1, https://arxiv.org/abs/2611.15563 (first posted 2026-11-11).
2. J.-P. Berrut and M. R. Trummer, *Extrapolation quadrature from equispaced samples of functions with jumps*, Numerical Algorithms 92 (2023), 65–88, first published 2022-12-19, https://doi.org/10.1007/s11075-022-01462-0.
3. N. Dahal, *A Matrix-Based Perspective on Multi-Level Richardson Extrapolation*, https://www.siam.org/media/ixnd5ck3/s185720r.pdf (reviewed only for the distinct smooth-expansion error model in Section 4).
