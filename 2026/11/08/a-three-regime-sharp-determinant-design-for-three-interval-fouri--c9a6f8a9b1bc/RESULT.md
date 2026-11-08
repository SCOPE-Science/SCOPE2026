# A three-regime sharp determinant design for three-interval Fourier Riesz bases

## Finding

For every real \(0<\delta<1\) put
\[
E_\delta=[0,1)\cup[1+\delta,2+\delta)\cup[2+2\delta,3+2\delta).
\]
For \(0<\tau<1\), the three-coset family \(\mathcal E_\tau=\{e^{2\pi i(n+r\tau)x}:n\in\mathbb Z,\ r=0,1,2\}\) has a \(3\times3\) Fourier fiber matrix \(V_{\delta,\tau}(x)\) as defined below. The **worst-fiber Gram determinant** is
\[
D_\delta(\tau)=\operatorname*{ess\,inf}_{0\le x<1}\det\big(V_{\delta,\tau}(x)^*V_{\delta,\tau}(x)\big).
\]
The sharp maximin determinant and its complete set of maximizing frequency shifts, modulo \(1\), are:
\[
\begin{array}{c|c|c}
\text{interval separation}&\max_{0<\tau<1}D_\delta(\tau)&\text{all maximizers}\;\tau\\\hline
0<\delta<\tfrac12&16&\tfrac14,\ \tfrac34\\
\delta=\tfrac12&\dfrac{9748+1360\sqrt{10}}{729}&\tau_0,\ 1-\tau_0\\
\tfrac12<\delta<1&\dfrac{25+5\sqrt5}{2}&\tfrac15,\ \tfrac45
\end{array}
\]
where
\[
\tau_0=\pi^{-1}\arcsin\sqrt{\frac{8-\sqrt{10}}{12}}\quad (\tau_0\approx0.21897346).
\]
Each maximizing family is a Riesz basis of \(L^2(E_\delta)\). Since every fiber Gram matrix is positive semidefinite with trace \(9\), its smallest eigenvalue is at least \(4\det(V^*V)/81\). Thus these determinants also provide explicit uniform (though generally nonsharp) reconstruction lower bounds \(4\max_\tau D_\delta(\tau)/81\). The objective is the **smallest fiber Gram determinant**, not the smallest fiber eigenvalue or the global Riesz condition number. No optimality for either of those other criteria is claimed.

## Assumptions and scope

Use Lebesgue measure without interval-length renormalization and complex exponentials \(e_\lambda(t)=e^{2\pi i\lambda t}\). Set \(K_\delta(x)=\{k\in\mathbb Z:x+k\in E_\delta\}\) for \(0\le x<1\); for almost every \(x\) this contains exactly three integers. Ordering them increasingly as \(k_0,k_1,k_2\), define \(V_{\delta,\tau}(x)\in\mathbb C^{3\times3}\) by \(V_{jr}=e^{2\pi i r\tau k_j}\) for \(j,r=0,1,2\). Changing row order does not change its Gram determinant. Singular shifts are allowed in the definition and have zero worst-fiber determinant. The parameter restrictions \(0<\delta<1\) and \(0<\tau<1\) are essential; the integer-spacing endpoints are excluded.

## Proof

**Fiberization.** The map \(f\mapsto(f(x+k))_{k\in K_\delta(x)}\) identifies \(L^2(E_\delta)\) unitarily with \(L^2([0,1);\mathbb C^3)\). Applying the integer Fourier series in \(x\) separately to each coset shows that analysis by \(\mathcal E_\tau\), up to coordinatewise unitary phase factors, acts fiberwise by \(V_{\delta,\tau}(x)^*\). Hence \(\mathcal E_\tau\) is a Riesz basis exactly when every positive-measure fiber matrix is invertible. Its frame-operator determinant in each fiber equals \(|\det V|^2\), which is the stated objective.

**The three possible Vandermonde types.** In the following table each triplet lists \(K_\delta(x)\) on consecutive positive-length subintervals of \([0,1)\):
\[
\begin{array}{c|c|c}
0<\delta<\tfrac12 &[0,\delta),[\delta,2\delta),[2\delta,1)&(0,2,3),(0,1,3),(0,1,2)\\
\delta=\tfrac12 &[0,\tfrac12),[\tfrac12,1)&(0,2,3),(0,1,3)\\
\tfrac12<\delta<1 &[0,2\delta-1),[2\delta-1,\delta),[\delta,1)&(0,2,4),(0,2,3),(0,1,3)
\end{array}
\]
The determinants for \((0,2,3)\) and \((0,1,3)\) coincide by reflection of the integer nodes. Let \(A(\tau), B(\tau), C(\tau)\) denote the determinants for triplets \((0,1,2),(0,1,3),(0,2,4)\). The Vandermonde product gives exactly
\[
\begin{split}
A(\tau)&=64\sin^4(\pi\tau)\sin^2(2\pi\tau),\\
B(\tau)&=64\sin^2(\pi\tau)\sin^2(2\pi\tau)\sin^2(3\pi\tau),\\
C(\tau)&=64\sin^4(2\pi\tau)\sin^2(4\pi\tau)=A(2\tau).
\end{split}
\]
Thus \(D_\delta=\min(A,B)\) in the left regime, \(D_\delta=B\) at the midpoint, and \(D_\delta=\min(B,C)\) in the right regime. All three functions satisfy \(F(1-\tau)=F(\tau)\), so it suffices to optimize \(0<\tau\le1/2\).

**Two elementary polynomials.** Put \(y=\sin^2(\pi\tau)\). Then
\[
A=256y^3(1-y),\qquad B=256y^3(1-y)(3-4y)^2,
\]
with derivatives, as functions of \(y\),
\[
\frac{dA}{dy}=256y^2(3-4y),\qquad
\frac{dB}{dy}=-256y^2(4y-3)(24y^2-32y+9).
\]
The two nontrivial roots of the quadratic in the second derivative formula are \(y_\pm=(8\pm\sqrt{10})/12\), with \(0<y_-<3/4<y_+<1\).

**Left regime.** When \(0<\tau\le1/4\), \(y\le1/2\), so \(A(\tau)\le A(1/4)=16\), with equality only at \(1/4\). When \(1/4\le\tau\le1/2\), \(y\ge1/2\). On \(1/2\le y\le3/4\), the derivative of \(B\) is negative, giving \(B\le B(1/4)=16\). For \(3/4\le y\le1\), let \(u=1-y\); then
\[
B/256=(1-u)^3u(1-4u)^2\le u(1-4u)^2\le1/27<1/16,
\]
because \(0\le u\le1/4\). Equality \(D_\delta=16\) therefore occurs only at \(\tau=1/4\) in \((0,1/2]\). At that point both fiber types have determinant \(16\).

**Midpoint regime.** Maximizing \(B\) is the same as maximizing \(y^3(1-y)(3-4y)^2\) on \([0,1]\). By the derivative factorization above its only positive local maxima are \(y_-\) and \(y_+\); their values are respectively \((9748+1360\sqrt{10})/729\) and \((9748-1360\sqrt{10})/729\) after multiplication by \(256\). The former is strictly larger. Hence the unique maximizing \(\tau\) in \((0,1/2)\) is \(\tau_0\).

**Right regime.** Put \(R=(25+5\sqrt5)/2\). For \(0<\tau\le1/5\) one has \(y\le\sin^2(\pi/5)<y_-\), hence \(B\) is strictly increasing and \(B(\tau)\le B(1/5)=R\). On \(1/5\le\tau\le1/4\), put \(z=\sin^2(2\pi\tau)\), which increases from \((5+\sqrt5)/8>3/4\) to \(1\). Since \(C(\tau)=256z^3(1-z)\), it is strictly decreasing and \(C(\tau)\le C(1/5)=R\). Finally, on \([1/4,1/2]\), the preceding left-regime bound gives \(B(\tau)\le16<R\). Thus \(D_\delta\le R\), with equality only at \(1/5\) in \((0,1/2]\). The exact identities \(B(1/5)=C(1/5)=R\) follow from the elementary fifth-root trigonometric values.

Reflection \(\tau\mapsto1-\tau\) supplies the remaining and only remaining optimizers. All displayed optimal determinants are strictly positive, proving the Riesz-basis assertion.

## Verification

The supplied `CHECK.py` evaluates the Vandermonde determinant directly against the trigonometric formulas at independent test parameters and checks the symbolic derivative factorizations, radical constants, fiber partitions, and candidate optimizers. The proof above, especially its global monotonicity and polynomial inequalities, is the infinite-parameter certificate; finite sampled checks do not prove uniqueness or coverage of the continuum. The matrix uses *unnormalized* exponential columns, so an orthogonal three-point fiber has Gram determinant \(27\).

## Relationship to prior work

The three-interval spectral/tiling classification of Shi (2026) concerns the existence of orthogonal spectra, not optimizing a three-arithmetic-coset Riesz-basis volume objective. Agora–Antezana–Carbajal (2026) and Frederick–Okoudjou (2019) establish multi-tile fiber/determinant criteria and dual reconstruction. Frederick–Yacoubou Djima (2023) computes explicit examples and bounds, mainly for two co-measurable intervals and higher-dimensional multi-rectangles. Those general frameworks justify the fiber model but do not give the three sharp maximin constants or the separation transition derived here. In particular, the Vandermonde determinant identity itself is classical and not claimed as novel.

## Limitations

Only the fixed geometry with three equal-length components centered at the arithmetic starts \(0,1+\delta,2+2\delta\) is optimized, and only equally spaced three frequency cosets \(0,\tau,2\tau\) are allowed. The determinant criterion measures joint local volume and is not the optimal lower Riesz bound or condition number. There is no claim of globally optimal frequency patterns among all exponential Riesz bases, nor of independence from \(\delta\) at \(\delta=0\) or \(\delta=1\).

## References

1. R. Shi, *Fuglede's conjecture holds for three intervals*, arXiv:2607.24005v1, first posted 2026-07-27, https://arxiv.org/abs/2607.24005.
2. E. Agora, J. Antezana, D. Carbajal, *Variations on two Cabrelli's works*, arXiv:2601.05422v1, first posted 2026-01-08, https://arxiv.org/html/2601.05422v1.
3. C. Frederick, K. Okoudjou, *Finding duality for Riesz bases of exponentials on multi-tiles*, arXiv:1910.09257, 2019, https://arxiv.org/abs/1910.09257.
4. C. Frederick, K. Yacoubou Djima, *Examples of Riesz Bases of Exponentials for Multi-tiling Domains and Their Duals*, La Matematica 3 (2024), DOI:10.1007/s44007-023-00078-7; online 2023-11-20.
