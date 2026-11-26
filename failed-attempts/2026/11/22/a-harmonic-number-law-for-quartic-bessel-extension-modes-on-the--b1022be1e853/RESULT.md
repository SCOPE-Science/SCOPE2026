# A harmonic-number law for quartic Bessel extension modes on the three-sphere

## Finding

For every integer \(n\ge1\), let \(J_n\) denote the ordinary Bessel function of the first kind and put

\[
Q_n=\int_0^\infty J_n(r)^4\,\frac{dr}{r},\qquad S_n=\sum_{j=0}^{n-1}\frac1{2j+1}.
\]

Then the **exact all-order identity** is

\[
\boxed{Q_n=\frac{S_n}{\pi^2n^2}=\frac{H_{2n}-H_n/2}{\pi^2n^2}\quad(n=1,2,\ldots),}
\]

where \(H_N=\sum_{j=1}^N j^{-1}\). In particular \(\pi^2Q_n\) is a positive rational number for every positive integer order. The full sequence is strictly decreasing; its high-order expansion is

\[
Q_n=\frac{\frac12\log n+\log2+\frac12\gamma}{\pi^2 n^2}
+\frac1{48\pi^2 n^4}+O(n^{-6}),\qquad n\to\infty.
\]

For the degree-\(k\) spherical harmonic Fourier-extension mode on \(\mathbb S^3\subset\mathbb R^4\), the quartic radial moment is exactly \(I_{1,k}(4)=Q_{k+1}\) for every \(k\ge0\). Thus the previously established sharp global quadratic stability coefficient of the radial--angular \(L^4_{\mathrm{rad}}L^2_{\mathrm{ang}}\) Fourier extension inequality, under unnormalized surface measure and the Fourier convention below, has the explicit value

\[
\boxed{\Gamma_{4,4}=16\pi^3\left(1-\frac1{\sqrt3}\right).}
\]

The substantive new part is the closed-form description of **all** nonconstant modes and their precise logarithmic angular tail; the zeroth-mode value \(Q_1=1/\pi^2\) and the general sharp-stability principle were already known.

## Assumptions and scope

Here \(n\) ranges over positive integers, \(k\) over nonnegative integers, and \(\gamma\) is Euler's constant. The positive-order condition is essential for the Weber--Schafheitlin identity; no statement is made for order zero, where the integral near the origin diverges. At infinity, \(J_n(r)=O_n(r^{-1/2})\), so the defining quartic integral is absolutely convergent. Near zero, \(J_n(r)=O_n(r^n)\), again giving integrability.

The spherical specialization uses \(d=4\), \(\nu=d/2-1=1\), exponent \(q=4\), and the unnormalized surface measure \(\sigma\) on \(\mathbb S^3\). Define

\[
\widehat{f\sigma}(x)=\int_{\mathbb S^3}e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega),
\quad
\|F\|_{L^4_{\rm rad}L^2_{\rm ang}}
=\left(\int_0^\infty\!\left(\int_{\mathbb S^3}|F(r\theta)|^2d\sigma(\theta)\right)^2r^3dr\right)^{1/4}.
\]

The sharp stability coefficient formula itself is quoted from Xu (2026), not reproved here; the evaluation of its Bessel modal inputs is proved below.

## Proof

**Step 1: reduce four Bessel factors to a two-variable power kernel.** For integer \(n\ge1\), the classical Bessel product identity (DLMF 10.9.26) gives

\[
J_n(r)^2=\frac2\pi\int_0^{\pi/2}J_{2n}(2r\cos\theta)\,d\theta.
\]

The equal-positive-order Weber--Schafheitlin integral (DLMF 10.22.56--57) specializes, for \(a,b>0\), to

\[
\int_0^\infty J_{2n}(ar)J_{2n}(br)\,\frac{dr}{r}
=\frac1{4n}\left(\frac{\min(a,b)}{\max(a,b)}\right)^{2n}.
\]

For each \(a,b>0\), the integrand is absolutely integrable by Cauchy--Schwarz and \(\int_0^\infty J_{2n}(ar)^2\,dr/r=1/(4n)\); the bound \(1/(4n)\) is uniform. Hence Fubini applies after integrating over both angular variables (the zero-scale endpoints have measure zero). Combining the two identities yields

\[
Q_n=\frac1{\pi^2n} A_n,
\qquad
A_n=\int_0^{\pi/2}\!\int_0^{\pi/2}
\left(\frac{\min(\cos\theta,\cos\phi)}{\max(\cos\theta,\cos\phi)}\right)^{2n}d\theta\,d\phi.
\]

**Step 2: evaluate the double integral exactly.** By symmetry, restrict to \(\theta\le\phi\). Substituting \(u=\tan\theta\), \(v=\tan\phi\) gives

\[
A_n=2\int_0^\infty\frac{dv}{(1+v^2)^{n+1}}
\int_0^v(1+u^2)^{n-1}du.
\]

Expand the polynomial, integrate the inner monomials, and use the beta integral:

\[
\begin{aligned}
A_n&=2\sum_{j=0}^{n-1}\frac{\binom{n-1}j}{2j+1}
\int_0^\infty\frac{v^{2j+1}}{(1+v^2)^{n+1}}dv\\
&=\sum_{j=0}^{n-1}\frac{\binom{n-1}j B(j+1,n-j)}{2j+1}
=\frac1n\sum_{j=0}^{n-1}\frac1{2j+1}.
\end{aligned}
\]

The last identity follows from

\[
\binom{n-1}j B(j+1,n-j)
=\frac{(n-1)!}{j!(n-j-1)!}\frac{j!(n-j-1)!}{n!}=\frac1n.
\]

Substitution into Step 1 proves \(Q_n=S_n/(\pi^2n^2)\). Separating odd and even denominators proves \(S_n=H_{2n}-H_n/2\).

**Step 3: strict ordering and asymptotics.** Since \(S_{n+1}=S_n+1/(2n+1)\) and \(S_n\ge1\),

\[
\frac{S_{n+1}}{S_n}\le1+\frac1{2n+1}<\left(1+\frac1n\right)^2.
\]

Consequently \(Q_{n+1}<Q_n\) for every positive integer \(n\). Euler--Maclaurin summation for harmonic numbers gives

\[
S_n=\frac12\log n+\log2+\frac12\gamma
+\frac1{48n^2}-\frac7{1920n^4}+O(n^{-6}).
\]

Dividing by \(\pi^2n^2\) gives the asserted expansion and particularly \(Q_n\sim(\log n)/(2\pi^2n^2)\).

**Step 4: spherical interpretation.** The standard Fourier--Bessel formula for a spherical harmonic \(Y_k\in\mathcal H_k^4\) reads

\[
\widehat{Y_k\sigma}(r\theta)
=(2\pi)^2(-i)^k r^{-1}J_{k+1}(r)Y_k(\theta).
\]

The corresponding fourth radial moment is

\[
I_{1,k}(4)=\int_0^\infty J_{k+1}(r)^4\frac{dr}{r}=Q_{k+1}.
\]

Xu's proved stability coefficient is \(\Gamma_{d,q}=(2\pi)^d[I_{\nu,0}(q)^{2/q}-I_{\nu,1}(q)^{2/q}]\) when \(d\ge3\) and \(q\) is admissible. Here \(I_{1,0}(4)=1/\pi^2\) and \(I_{1,1}(4)=1/(3\pi^2)\), so substitution yields \(\Gamma_{4,4}=16\pi^3(1-1/\sqrt3)\), with exactly the normalization specified above. This uses the published sharp-stability theorem as a premise and does not independently reprove its equality classification.

## Verification

The exact first five coefficients \(\pi^2 Q_n\) are \(1\), \(1/3\), \(23/135\), \(11/105\), and \(563/7875\). The included standalone `check.py` uses exact rational arithmetic to verify the binomial--beta identity and the monotone ordering for the first 120 positive orders, and optionally integrates \(J_n^4/r\) numerically for six orders. It passed 374 assertions in the stated runtime; the optional numerical quadrature was truncated at radius \(400\) and is not a proof of the infinite integral. The proof uses the classical product and Weber--Schafheitlin integrals and elementary beta arithmetic, so it applies to all positive integer orders regardless of the finite checks.

## Relationship to prior work

Carneiro, Oliveira e Silva, and Sousa (first public 2017; journal 2019) introduced the spherical mixed-norm modal integrals and explicitly evaluated the **base** quartic mode in their Eq. (4.11); their statements do not supply the positive-integer all-mode harmonic-number profile or the exact high-mode tail. Xu (2026), Theorems 1.2--1.3, gives strict ordering of the complete Bessel modal sequence and the sharp stability coefficient in general dimensions, but leaves the individual moments in integral form. The formula here determines them all in dimension four at quartic exponent and evaluates Xu's coefficient; it is not claimed as a new proof of Xu's strict ordering or stability theorem. The published three-dimensional quartic-Bessel profile uses half-integer orders, hence a different radial integral and different high-order decay. The underlying Bessel product and Weber--Schafheitlin transformations are classical.

## Limitations

The theorem is confined to integer Bessel orders and the \(d=4\), \(q=4\) spherical specialization. Its stability conclusion depends on Xu's independent general theorem, not on the Bessel evaluation alone. The identity is derived from standard Bessel integral formulas, so equivalent closed forms may occur in older special-function tables even though no directly matching all-order formula was identified during the literature comparison. The finite checker cannot establish priority or replace the analytic proof. No claim is made about other dimensions, noninteger orders, or other exponents.

## References

1. E. Carneiro, D. Oliveira e Silva, M. Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365 (first posted 2017), *Advances in Mathematics* 341 (2019), 583–608, especially §§1,4.2. https://arxiv.org/abs/1710.10365
2. Z. Xu, *Sharp radial--angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648 (first posted October 14, 2026), Theorems 1.2–1.3. https://arxiv.org/abs/2610.19648
3. NIST Digital Library of Mathematical Functions, §10.9.26 (Bessel products), https://dlmf.nist.gov/10.9.E26, and §10.22.56--57 (Weber--Schafheitlin integrals), https://dlmf.nist.gov/10.22.E56
4. S. Suzuki, *Identities and inequalities for integral transforms involving squares of the Bessel functions*, arXiv:2511.00137 (2025); related square-Bessel transform framework, not the fourth-moment formula. https://arxiv.org/abs/2511.00137
