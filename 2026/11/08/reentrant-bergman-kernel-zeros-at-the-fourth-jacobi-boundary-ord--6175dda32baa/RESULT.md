# Reentrant Bergman-kernel zeros at the fourth Jacobi boundary order

## Finding

Consider normalized planar area measure on the open unit disk and the radial weight
\[\omega_a(z)=|z|^{2a}(1-|z|^2)^4,\qquad a>-1.\]
Write \(t=a+1>0\), \(s=z\overline w\), and define the exact threshold
\[\tau=\frac{\sqrt{15+2\sqrt{19}}-3}{2}=0.935046092329740\ldots.\]
The reproducing kernel of the holomorphic weighted Bergman space has the following complete scalar-zero classification, with zeros counted with multiplicity in \(|s|<1\):

1. For \(0<t<\tau\), there is exactly one zero. It is simple and lies in \((-1,0)\).
2. For \(\tau\le t\le2\), the kernel is zero-free on the bidisk. At \(t=\tau\), one simple numerator zero lies at \(s=-1\), and at \(t=2\), two simple numerator zeros lie at \(s=e^{\pm i\pi/3}\), all outside the open scalar disk.
3. For \(t>2\), there are exactly two scalar zeros. They are a simple nonreal conjugate pair in \(|s|<1\).

Thus zero-freeness is reentrant: a negative-real scalar zero exits at \(t=\tau\), a zero-free interval persists through \(t=2\), and a nonreal conjugate pair enters after \(t=2\). For every \(s\) in the open scalar disk, points \(z,w\) in the open unit disk can be selected with \(z\overline w=s\), so the scalar count is exactly the relevant weighted Lu Qi-Keng classification.

## Assumptions and scope

The weight is precisely \(|z|^{2a}(1-|z|^2)^4\), not \((1-|z|)^4\). The real parameter \(a>-1\) may be negative, zero, or positive. Area is normalized by \(1/\pi\). Zeros of the rational scalar kernel \(K_t(s)\) are counted for \(|s|<1\), with the boundary excluded. The theorem concerns only boundary order four; it does not assert an all-order classification.

## Proof

**1. Exact monomial norms and kernel numerator.** In normalized area measure the squared norm of \(z^n\) equals
\[\int_0^1 u^{n+t-1}(1-u)^4\,du=B(n+t,5)=\frac{24}{(n+t)(n+t+1)(n+t+2)(n+t+3)(n+t+4)}.\]
Orthogonality of monomials therefore gives
\[K_t(s)=\frac1{24}\sum_{n=0}^{\infty}(n+t)(n+t+1)(n+t+2)(n+t+3)(n+t+4)s^n
=\frac{Q_t(s)}{24(1-s)^6}.\]
The degree-at-most-five numerator is explicitly
\[\begin{aligned}
Q_t(s)={}&t(t+1)(t+2)(t+3)(t+4)\\
&-5(t-1)(t+1)(t+2)(t+3)(t+4)s\\
&+10t(t-1)(t+2)(t+3)(t+4)s^2\\
&-10t(t-1)(t+1)(t+3)(t+4)s^3\\
&+5t(t-1)(t+1)(t+2)(t+4)s^4\\
&-t(t-1)(t+1)(t+2)(t+3)s^5.
\end{aligned}\]
It follows either by repeated use of \(s\,d/ds\) on \((1-s)^{-1}\), or by coefficient comparison. Since \(1-s\ne0\) in the scalar disk, the kernel zeros are exactly the zeros of \(Q_t\) there.

**2. Cayley transform.** Put \(s=(w-1)/(w+1)\). Then \(|s|<1\) is equivalent to \(\operatorname{Re}w>0\). Set \(T_t(w)=(w+1)^5Q_t((w-1)/(w+1))\). Exact expansion gives
\[\begin{aligned}
T_t(w)={}&120w^5+120(2t+3)w^4+240(t^2+3t+1)w^3\\
&+80(2t+3)(t^2+3t-1)w^2\\
&+40(2t^4+12t^3+16t^2-6t-9)w\\
&+8(2t+3)(2t^4+12t^3+12t^2-18t-5).
\end{aligned}\]
The Cayley map accounts for a degree drop when \(t=1\): then \(Q_1=120\), while \(T_1=120(w+1)^5\), whose artificial roots at \(w=-1\) are outside the relevant right half-plane.

**3. Exact Routh array.** Denote by \(a_5,\ldots,a_0\) the coefficients of \(T_t\) in descending order. The first Routh column for this degree-five polynomial is
\[\begin{aligned}
&120,\\
&120(2t+3),\\
&160(t+1)(t+2),\\
&8(2t+1)(2t+3)(2t+5),\\
&\frac{-64t(t-2)(t+1)(t+2)(t+3)(t+5)}{(2t+1)(2t+5)},\\
&8(2t+3)p(t),
\end{aligned}\]
where \(p(t)=2t^4+12t^3+12t^2-18t-5\). All entries before the fifth are strictly positive for \(t>0\). The fifth entry is positive for \(0<t<2\), zero at \(t=2\), and negative for \(t>2\).

Writing \(u=t(t+3)\), one has \(p(t)=2u^2-6u-5\). Since \(u\) increases strictly from zero to infinity on \(t>0\), \(p\) has the unique positive zero \(t=\tau\), is negative below it and positive above it. Away from \(\tau\) and \(2\), the Routh count of roots in \(\operatorname{Re}w>0\) is therefore respectively \(1,0,2\) on \((0,\tau)\), \((\tau,2)\), and \((2,\infty)\). As no first-column entry vanishes away from the two thresholds, this count is valid without imaginary-axis exceptional roots.

**4. Boundary points and root types.** At \(t=\tau\), \(T_t(0)=0\), corresponding to \(s=-1\). The coefficient of \(w\) is strictly positive there, so the boundary root is simple. The remaining transformed roots lie strictly in the left half-plane. Indeed, after dividing \(T_{\tau}(w)\) by \(w\), the quartic Routh first column is \(a_5,a_4,b_1,c_1,a_1\), all strictly positive at \(t=\tau\). Equivalently its Hurwitz determinants are \(a_4>0\), \(a_4b_1>0\), \(a_4b_1c_1>0\), and \(a_4b_1c_1a_1>0\).

At \(t=2\), exact factorization gives
\[T_2(w)=120(w+3)(w^2+3)(w^2+4w+7),\]
and equivalently
\[Q_2(s)=-120(s-2)(s^2-3s+3)(s^2-s+1).\]
Exactly two simple roots lie on \(|s|=1\), namely \(e^{\pm i\pi/3}\), while all other roots lie outside the closed scalar disk. At \(0<t<\tau\), the sole right-half-plane root must be real (nonreal roots occur in pairs); it is simple, and its scalar image is negative because \(K_t(s)>0\) for \(0\le s<1\). For \(t>2\), every coefficient of \(T_t(w)\) is positive, so it has no positive real zero. Its two right-half-plane zeros therefore form a nonreal conjugate pair and are simple. The classification follows.

## Verification

A standalone script, `jacobi_reentrance_check.py`, symbolically checks the numerator, Cayley transformation, Routh entries, threshold equation, and factorizations; it also checks eight representative parameter values numerically. To reproduce, run `python jacobi_reentrance_check.py` with SymPy and NumPy installed. The output is `JACOBI_REENTRANCE_CHECK_PASS exact_identities=9 numerical_root_cases=8`. These tests corroborate algebra and sample roots; the Routh sign argument, not numerical tests, proves the all-parameter root counts.

## Relationship to prior work

Perälä's work on vanishing radial Bergman kernels proves general finite-zero phenomena and constructs radial weights with prescribed finite numbers of zeros. It does not determine the fourth-Jacobi-order phase diagram or the two threshold mechanisms. Miña-Díaz establishes kernel representations for weights built from powers of finite Blaschke products; these do not include the independent factor \((1-|z|^2)^4\). Beberok develops Jacobi and Routh-Hurwitz methods for Bergman kernels of intersections of complex ellipsoids, but its statements concern different several-variable domains and do not assert this continuous origin-exponent transition. Previously established classifications at Jacobi boundary orders one and two involve a single negative-real entry/exit and do not imply the present nonreal reentry.

## Limitations

The result gives zeros only in the scalar disk, equivalently existence of kernel zeros in the disk bidomain. It does not give a full classification for other integer or noninteger boundary orders, nor quantitative conditioning or zero trajectories away from the transition values. Identifying an unknown broader generalized Eulerian-polynomial or Schur-stability result that implies the exact two thresholds remains a historical-priority risk. No independent mathematical audit is represented here.

## References

1. Erwin Miña-Díaz, *A representation for the reproducing kernel of a weighted Bergman space*, arXiv:2212.08118 (first posted 2022-12-15), https://arxiv.org/abs/2212.08118.
2. Antti Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976 (first posted 2017-03-17), https://arxiv.org/abs/1703.05976.
3. Tomasz Beberok, *The Bergman kernel: Explicit formulas, deflation, Lu Qi-Keng problem and Jacobi polynomials*, Czechoslovak Mathematical Journal 67 (2017), 537–549, https://doi.org/10.21136/CMJ.2017.0073-16.
