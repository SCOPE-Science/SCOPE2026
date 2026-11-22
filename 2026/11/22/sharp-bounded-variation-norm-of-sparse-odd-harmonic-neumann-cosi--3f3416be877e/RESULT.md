# Sharp bounded-variation norm of sparse odd-harmonic Neumann cosine projections

## Finding
For every integer \(m\ge1\), let \(P_m\) be the real \(L^2(0,1)\)-orthogonal projection onto
\[
E_m=\operatorname{span}\{1,\cos(m\pi x),\cos(3m\pi x)\}.
\]
Its sharp norm in the distributional Jordan-variation seminorm is **independent of frequency**:
\[
\boxed{\sup_{0<\operatorname{Var}(f)<\infty}
\frac{\operatorname{Var}(P_mf)}{\operatorname{Var}(f)}
=\frac{16\sqrt2-8}{3\pi}=1.552017146595508\ldots.}
\]
All one-jump functions with their jump at \(s=(2j+1)/(2m)\), for \(j=0,\ldots,m-1\), attain equality. These are exactly the one-jump locations attaining the norm. This is the entire frequency-uniform classification of the sharp coefficient, not merely an asymptotic bound.

## Assumptions and scope
Inputs are real functions in \(BV(0,1)\), interpreted as equivalence classes modulo Lebesgue-null sets; the seminorm is the total mass \(\operatorname{Var}(f)=|Df|((0,1))\) of the distributional derivative measure. The input can have jumps or singular-continuous derivative. Constants are annihilated by the seminorm and reproduced by the projection. There are no endpoint point-value penalties. The projector is continuous, unweighted Lebesgue-\(L^2\) projection onto the three-dimensional sparse cosine space specified above, not a Chebyshev polynomial projection onto every degree through \(3m\), not discrete cosine collocation, and not a periodic complex Fourier projection.

Explicitly,
\[
(P_m f)(x)=\int_0^1f(y)\,dy+2\sum_{k\in\{m,3m\}}
\left(\int_0^1 f(y)\cos(k\pi y)\,dy\right)\cos(k\pi x).
\]
The orthogonality and normalization follow from \(\int_0^1\cos(k\pi x)\cos(l\pi x)dx=\delta_{kl}/2\) for positive integers \(k,l\), and orthogonality to constants.

## Proof
**1. Reduction to a single jump.** For \(s\in(0,1)\), put \(h_s(x)=\mathbf1_{[s,1]}(x)\). Direct integration and differentiation give
\[
(P_mh_s)'(x)=2\sin(m\pi s)\sin(m\pi x)
+2\sin(3m\pi s)\sin(3m\pi x).
\]
Every real \(BV(0,1)\) input has the almost-everywhere representation \(f(x)=c+\int_{(0,1)}h_s(x)\,d(Df)(s)\). By Fubini, the projection's linearity, and the triangle inequality in \(L^1(0,1)\),
\[
\operatorname{Var}(P_m f)\le
\left(\sup_{0<s<1}\operatorname{Var}(P_mh_s)\right)|Df|((0,1)).
\]
Conversely each jump has unit variation. Hence the sharp operator seminorm equals the supremum of the single-jump responses. This covers all input derivative measures, not just finite step functions.

**2. Independence of \(m\).** Each absolute-value derivative in Step 1 is \(1/m\)-periodic in \(x\), because the sine terms change sign simultaneously after \(x\mapsto x+1/m\). Its integral over \((0,1)\) equals the integral of the corresponding \(m=1\) expression over one rescaled unit interval, with the phase \(m\pi s\) taken modulo \(\pi\). As \(s\) runs through \((0,1)\), every phase modulo \(\pi\) occurs. It is therefore enough to find the exact maximum when \(m=1\).

**3. An elementary one-parameter absolute integral.** Use \(\sin(3z)=\sin z\,(4\cos^2z-1)\). Write \(u=\cos^2(\pi s)\in[0,1]\). The substitution \(v=\cos(\pi x)\) yields
\[
\operatorname{Var}(P_1h_s)=\frac2\pi\sqrt{1-u}\,I(4u-1),\qquad
I(b):=\int_{-1}^{1}|1+b(4v^2-1)|\,dv.
\]
The integral \(I(b)\) is convex as a function of \(b\). Direct integration gives
\[
I(-1)=\frac{8\sqrt2-4}{3},\qquad I(-1/3)=\frac{16}{9},
\]
\[
I(b)=2(1+b/3)\quad\text{for }-1/3\le b\le1,
\]
and, for \(b\ge1\),
\[
I(b)=2(1+b/3)+\frac43(b-1)\sqrt{1-b^{-1}}
\le\frac23+2b.
\]

**4. Global and strict maximization.** If \(0\le u\le1/6\), then \(-1\le4u-1\le-1/3\). Convexity and the two endpoint values give \(I(4u-1)\le I(-1)\). Multiplication by \(\sqrt{1-u}<1\) makes this strict when \(u>0\).

If \(1/6\le u\le1/2\), the nonnegative-integrand formula gives
\[
\sqrt{1-u}\,I(4u-1)=\frac43\sqrt{1-u}(1+2u)
\le\frac{4\sqrt2}{3}<I(-1).
\]
The middle bound follows by differentiating the explicit expression: it increases up to \(u=1/2\).

If \(1/2\le u\le1\), then \(4u-1\ge1\), and the last bound in Step 3 yields
\[
\sqrt{1-u}\,I(4u-1)
\le\sqrt{1-u}\,(8u-4/3)
\le\frac{20\sqrt{10}}{27}<I(-1).
\]
The middle upper bound is maximized at \(u=13/18\). The final inequality is fully exact: \(\sqrt2>7/5\) gives \(I(-1)>12/5\), while \(\sqrt{10}<16/5\) gives \(20\sqrt{10}/27<64/27<12/5\). These square-root comparisons follow by squaring positive rational numbers.

Thus the unique maximizing value of \(u\) is \(u=0\). Returning to Step 3 gives the norm \(2I(-1)/\pi=(16\sqrt2-8)/(3\pi)\). For general \(m\), the equality phases are exactly \(\cos(m\pi s)=0\), namely \(s=(2j+1)/(2m)\) with \(0\le j<m\). Each corresponding single jump has norm one, completing attainment and the one-jump classification.

## Verification
Run `python3 CHECK.py` using the Python standard library. The script checks the closed absolute-integral identities, the exact rational inequalities underlying Step 4, the full one-parameter profile at 10,001 sample locations, every predicted equality location for six distinct frequencies, 600 additional jump profiles, and 450 random finite-jump superpositions. The finite computations are corroboration; the proof above establishes the infinite-dimensional result for every integer frequency.

## Relationship to prior work
The classical Chebyshev and cosine expansions provide the basis; the exact input norm here is an operator seminorm under variation, rather than a Sobolev approximation rate or sup-norm interpolation error. Benoit–Joldes–Mezzarobba (2014) treat validated uniform approximation of smooth D-finite functions by Chebyshev expansions. Orel–Perne (2014) study Chebyshev–Fourier spectral schemes and boundary-value collocation; Wang–Sloan (2015) study filtered spherical polynomial approximation. Their inspected results do not give the sharp variation norm for this sparse odd pair.

The published *Sharp total-variation norm of cubic Chebyshev spectral projection, with displaced extremizers* computes a larger coefficient \(1.565342822371915\ldots\) for the **full** degree-three Chebyshev projection, with displaced worst jumps. That operator retains its second harmonic, which is absent here: neither projector's exact norm determines the other's. The published *Exact joint sine-harmonic variation body and rigid minimizers* treats harmonics in a \(1:2\) ratio on a circle, not this Neumann \(1:3\) pair. Quadratic Jacobi-weighted polynomial projectors and discrete cyclic Fourier projectors likewise differ in spectral support or input/output seminorm. Those comparisons are material, not claims of logical independence.

## Limitations
The result concerns real one-dimensional distributional variation and sparse projections onto exactly the constant, \(m\)-th, and \(3m\)-th cosine modes. It does not extend automatically to other harmonic ratios, mixed coefficients, weighted variation, complex data, or endpoint-point-value Jordan variation. Only **one-jump** attaining locations are classified; no complete classification of arbitrary multijump extremizers is asserted. The literature comparison does not rule out unindexed older equivalent results; independent validation has not been performed.

## References
1. A. Benoit, M. Joldes and M. Mezzarobba, *Rigorous uniform approximation of D-finite functions using Chebyshev expansions*, arXiv:1407.2802v1, 2014-07-10, https://arxiv.org/html/1407.2802v1.
2. B. Orel and A. Perne, *Chebyshev-Fourier Spectral Methods for Nonperiodic Boundary Value Problems*, Journal of Applied Mathematics 2014, article 572694, published 2014-06-01, https://doi.org/10.1155/2014/572694.
3. H. Wang and I. Sloan, *On filtered polynomial approximation on the sphere*, arXiv:1509.03792, first posted 2015-09-13, https://arxiv.org/abs/1509.03792.
4. *Sharp total-variation norm of cubic Chebyshev spectral projection, with displaced extremizers*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-total-variation-norm-of-cubic-chebyshev-spectral-projectio--d84ecd4d8834.
5. *Exact joint sine-harmonic variation body and rigid minimizers*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-joint-sine-harmonic-variation-body-and-rigid-minimizers--73978a935283.
