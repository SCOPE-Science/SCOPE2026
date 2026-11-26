# Sharp affine Bernstein positivity threshold on the two-sphere and a dimensional obstruction

## Finding

For every integer \(n\ge1\), let \(\mathcal B_n\) be ordinary degree-\(n\) Bernstein approximation in the **dot-product coordinate** \(t\in[-1,1]\):
\[
(\mathcal B_n f)(t)=\sum_{j=0}^{n}\binom nj
 \left(\frac{1+t}{2}\right)^j\left(\frac{1-t}{2}\right)^{n-j}
 f\left(-1+\frac{2j}{n}\right).
\]
A continuous \(f:[-1,1]\to\mathbb R\) is *spherically positive definite on* \(\mathbb S^d\) if the matrix \(\bigl(f(x_i\cdot x_j)\bigr)_{i,j=1}^M\) is positive semidefinite for every positive integer \(M\) and every collection of points \(x_i\in\mathbb S^d\).

**Sharp two-sphere classification:** \(\mathcal B_n\) preserves this positive-definite cone on \(\mathbb S^2\) for **every** continuous positive-definite input exactly when
\[
\boxed{1\le n\le3.}
\]
For each \(n\ge4\), the degree-\(n+2\) Legendre zonal kernel \(P_{n+2}(x\cdot y)\) is a positive-definite input whose Bernstein image is not positive definite. Precisely, in its Legendre expansion the coefficient of \(P_n\) is
\[
\boxed{\frac{(2n+1)(3-n)n!}{6n^{n+1}}<0.}
\]

**All-dimensional obstruction:** For every integer sphere dimension \(d\ge2\), put \(\lambda=(d-1)/2\) and \(R_m^{(d)}(t)=C_m^{\lambda}(t)/C_m^{\lambda}(1)\). The coefficient of \(R_n^{(d)}\) in \(\mathcal B_n R_{n+2}^{(d)}\) is exactly
\[
\boxed{
 \frac{n!}{n^n}\,
 \frac{(n+1)(n+2)(n+\lambda)(d+1-n)}
 {3n(n+d-1)(n+d)}.
}
\]
Consequently **no** ordinary affine Bernstein operator of degree \(n\ge d+2\) preserves the spherical positive-definite cone on \(\mathbb S^d\). This necessary degree restriction is not claimed sufficient when \(d\ge3\).

## Assumptions and scope

The sphere is the Euclidean unit sphere \(\mathbb S^d\subset\mathbb R^{d+1}\), with \(d\ge2\). The integer approximation degree is \(n\ge1\); degree zero is not part of the stated family. The Gegenbauer polynomials have the standard normalization \(C_m^{\lambda}(1)=(2\lambda)_m/m!\), and \(P_m=C_m^{1/2}\). The notation \([q]_{R_n^{(d)}}\) denotes the coefficient of \(R_n^{(d)}\) in the unique finite Gegenbauer expansion of a polynomial \(q\), with no hidden dimension or volume factor. Positive definiteness refers to positive semidefinite Gram matrices of **all** finite sizes, not merely pointwise nonnegativity of \(f\). The operator here uses dot-product nodes, unlike the geodesic-distance Bernstein operator studied for the circle.

## Proof

**1. Schoenberg reduction.** The classical Schoenberg characterization identifies continuous zonal positive-definite functions on \(\mathbb S^d\) with the uniformly convergent expansions \(f=\sum_{m\ge0}a_mR_m^{(d)}\), where \(a_m\ge0\) and \(\sum_m a_m<\infty\). Each \(R_m^{(d)}(x\cdot y)\) is positive definite by the spherical-harmonic addition theorem. Because \(\mathcal B_n\) is a convex combination of finitely many samples and is linear, positivity of all its Gegenbauer-basis images suffices for cone preservation. Conversely, a single negative Gegenbauer coefficient in the image of a basis kernel disproves preservation.

**2. Universal high-degree sign identity.** Define the centered finite-difference functional
\[
D_nf=\sum_{j=0}^n(-1)^{n-j}\binom nj
 f\left(-1+\frac{2j}{n}\right).
\]
Its exponential generating identity, valid for every complex \(z\), is
\[
D_n(e^{zt})=\bigl(2\sinh(z/n)\bigr)^n.
\]
It follows by comparing Taylor coefficients that \(D_n\) annihilates all powers of degree less than \(n\), and
\[
D_n(t^n)=n!\left(\frac2n\right)^n,
\qquad
\frac{D_n(t^{n+2})}{D_n(t^n)}
 =\frac{(n+1)(n+2)}{6n}.
\]
The coefficient of \(t^n\) in \(\mathcal B_nf\) is \(D_nf/2^n\).

Write \(L_m=2^m(\lambda)_m/(2\lambda)_m>0\) for the leading coefficient of \(R_m^{(d)}\). The explicit Gegenbauer polynomial formula gives the two top nonzero terms
\[
R_{n+2}^{(d)}(t)=L_{n+2}\left[t^{n+2}
 -\frac{(n+2)(n+1)}{4(n+\lambda+1)}t^n
 +\text{terms of degree below }n\right].
\]
Moreover,
\[
\frac{L_{n+2}}{L_n}=
\frac{4(n+\lambda)(n+\lambda+1)}
 {(n+2\lambda)(n+2\lambda+1)}.
\]
Apply \(D_n\), divide by \(2^nL_n\), and simplify with \(2\lambda=d-1\). This yields exactly
\[
[\mathcal B_nR_{n+2}^{(d)}]_{R_n^{(d)}}=
\frac{n!}{n^n}\frac{(n+1)(n+2)(n+\lambda)(d+1-n)}
 {3n(n+d-1)(n+d)}.
\]
Its sign is strictly negative whenever \(n\ge d+2\), proving the all-dimensional obstruction. For \(d=2\) it simplifies to the displayed Legendre formula, ruling out every \(n\ge4\). At \(n=4\) it gives \(-9/256\), the coefficient in the already published example.

**3. Positivity of all degree-one, -two and -three images on \(\mathbb S^2\).** Let \(P_m\) be an arbitrary Legendre polynomial. Its parity is \(P_m(-t)=(-1)^mP_m(t)\), while \(|P_m(t)|\le1\) for \(-1\le t\le1\). The latter bound follows from the classical integral representation
\[
P_m(\cos\vartheta)=\frac1\pi\int_0^\pi
 (\cos\vartheta+i\sin\vartheta\cos u)^m\,du.
\]
Using only the Bernstein nodes \(\{-1,0,1\}\) and \(\{-1,-1/3,1/3,1\}\), direct expansion yields the following *complete* Legendre decompositions:

For \(n=1\), \(\mathcal B_1P_m=P_0\) when \(m\) is even and \(\mathcal B_1P_m=P_1\) when \(m\) is odd. For \(n=2\), the odd case is again \(P_1\); in the even case, with \(v=P_m(0)\),
\[
\mathcal B_2P_m=\frac{2+v}{3}P_0+\frac{1-v}{3}P_2.
\]
For \(n=3\), in the even case, with \(w=P_m(1/3)\),
\[
\mathcal B_3P_m=\frac{1+w}{2}P_0+\frac{1-w}{2}P_2;
\]
in the odd case,
\[
\mathcal B_3P_m=\frac{9+3w}{10}P_1+\frac{1-3w}{10}P_3.
\]
The absolute Legendre bound makes every displayed coefficient nonnegative except that the last odd coefficient requires \(P_m(1/3)\le1/3\) for all odd \(m\).

**4. Exact odd-degree pointwise bound.** At odd degrees \(m=1,3,5,7\), direct Legendre recurrence gives, respectively,
\[
P_m(1/3)\in\left\{\frac13,-\frac{11}{27},\frac13,-\frac{121}{729}\right\}.
\]
For every odd \(m\ge9\), applying the integral representation at \(\cos\vartheta=1/3\) and using that the modulus of its integrand is at most one gives
\[
\begin{aligned}
|P_m(1/3)|
&\le\frac1\pi\int_0^\pi
 \left(1-\frac89\sin^2u\right)^{m/2}\,du\\
&\le\frac1\pi\int_0^\pi
 \left(1-\frac89\sin^2u\right)^4\,du
=\frac{1921}{6561}<\frac13.
\end{aligned}
\]
The last integral is exact by expanding the fourth power and using \(\pi^{-1}\int_0^\pi\sin^{2k}u\,du=\binom{2k}{k}/4^k\). Hence all degree-one, -two and -three Legendre images have nonnegative coefficients. The Schoenberg reduction in step 1 extends this conclusion from basis polynomials to *every* continuous zonal positive-definite function on \(\mathbb S^2\). Combining with step 2 proves the sharp two-sphere classification. \(\square\)

## Verification

Running `python3 verify.py` with Python 3 and SymPy checks exact Legendre expansions for the first three Bernstein degrees against fifty basis inputs each, exact normalized Gegenbauer top-coefficient formulas for integer dimensions \(2\) through \(7\) and degrees \(1\) through \(9\), and the rational Legendre/integral identities used in the odd-degree bound. The executed checker returned `VERIFY_OK 514 exact Gegenbauer/Legendre cone, coefficient, and boundary checks`. These are supplementary finite symbolic tests; the universal results for all input degrees, all Bernstein degrees and all sphere dimensions are proved in the preceding analytic argument.

## Relationship to prior work

Otten, Nguyen and Watts (2026, arXiv:2608.04836, Section 4) explicitly show that the **degree-four** affine Bernstein operator fails to preserve the positive-definite cone on \(\mathbb S^2\), using \(P_6\), with negative \(P_4\) coefficient \(-9/256\). That example and the distinction between interval-dot-product and circle-geodesic Bernstein operators are credited. Their circle theorem establishes preservation at every degree on \(\mathbb S^1\), for a different operator. The results established here instead prove (i) preservation for every positive degree up through three on \(\mathbb S^2\), (ii) an all-order negative-coefficient formula covering *every* degree four or higher there, and (iii) an obstruction for all dimensions \(d\ge2\) whenever \(n\ge d+2\).

Schoenberg's positive-definite characterization, standard Legendre/Gegenbauer formulas and the integral representation are classical inputs, not new assertions. General Jacobi–Bernstein basis conversion formulas (Rababah, 2004) provide related algebraic machinery; the proof here gives the decisive signed coefficient and cone classification explicitly. The later 2026 work of Castillo and Sadigova on Legendre lower envelopes concerns pointwise Legendre comparisons, not the Bernstein operator's spherical positive-definiteness classification.

## Limitations

The all-dimensional assertion for \(d\ge3\) is a **necessary obstruction only**: it does not assert that Bernstein degrees \(n\le d+1\) preserve positivity there. The sharp iff classification is proved specifically for \(\mathbb S^2\). The result concerns **zonal** kernels and standard affine Bernstein sampling of the dot-product variable; it does not address arbitrary nonzonal kernels, other interpolation operators or positive-definiteness preservation under geodesic-distance Bernstein sampling. The comparison with unindexed older approximation and orthogonal-polynomial literature cannot establish historical priority conclusively.

## References

1. Matthew Otten, Nam Nguyen and Thomas W. Watts, *Preservation of Positive-Definiteness by Bernstein Operators on the Circle*, arXiv:2608.04836 (first posted 2026-08-05), especially Section 4.
2. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Mathematical Journal **9** (1942), 96–108.
3. Abedallah Rababah, *Jacobi–Bernstein Basis Transformation*, Computational Methods in Applied Mathematics (2004); classical Jacobi/Bernstein conversion methods.
4. K. Castillo and S. Sadigova, *The lower envelope of ultraspherical polynomials*, arXiv:2609.15473 (2026); related Legendre bounds.
