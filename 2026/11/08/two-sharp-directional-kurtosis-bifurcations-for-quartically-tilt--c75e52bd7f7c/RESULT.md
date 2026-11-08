# Two sharp directional-kurtosis bifurcations for quartically tilted spherical measures

## Finding
For every integer \(n\ge3\), parameter \(u>0\), and unit vector \(e\in\mathbb R^n\), give the sphere \(S^{n-1}\) the probability density proportional to \(1+u(\omega\cdot e)^4\) relative to normalized surface measure. For nonzero real linear functions \(f_a(\omega)=a\cdot\omega\), the sharp normalized \(L^4/L^2\) fourth-moment interval is completely explicit, with all directional equality cases. The minimizing geometry moves from an oblique cone to the symmetry axis at one threshold; in dimensions \(n\ge11\) the maximizing geometry independently moves from the symmetry axis to its orthogonal equator at a different threshold. An exact nonnegative quadratic identity quantifies stability at the oblique minimum.

Set \(t=(a\cdot e)^2/\|a\|_2^2\in[0,1]\), and define
\[
D(t)=(n+2)(n+4)+u(3+12t),\qquad
N(t)=3(n+4)(n+6)+u(9+72t+24t^2),
\]
\[
C=\frac{(n+4)(n(n+2)+3u)}{n+6},\qquad
K(t)=C\frac{N(t)}{D(t)^2}.
\]
Then the exact normalized fourth moment is
\[
\frac{\int|f_a|^4\,d\mu_{n,u}}{(\int|f_a|^2\,d\mu_{n,u})^2}=K(t).
\]
Define the lower threshold \(u_{\mathrm{min}}(n)=(n^2-16)/15\) for \(n\ge5\). For \(n\ge5\) and \(0<u<u_{\mathrm{min}}(n)\), put
\[
t_* = \frac{6(n+4)}{(n+2)(n+4)-15u}\quad\text{with }0<t_*<1.
\]
For these parameters, the minimum is uniquely \(K(t_*)\), achieved precisely by directions with squared axial projection \(t_*\). At \(u\ge u_{\mathrm{min}}(n)\), the minimum is \(K(1)\), attained precisely by axial directions. For \(n=3,4\), the minimum is \(K(1)\) at every \(u>0\).

For \(3\le n\le10\), the maximum is \(K(0)\), achieved precisely by directions orthogonal to \(e\). For \(n\ge11\), define
\[
u_{\mathrm{max}}(n)=\frac{n+4}{15}\left(\sqrt{9n^2+48n+384}-2n-22\right).
\]
Then \(0<u_{\mathrm{max}}(n)<u_{\mathrm{min}}(n)\), and the sharp maximum is \(K(1)\) for \(u<u_{\mathrm{max}}(n)\), \(K(0)=K(1)\) at equality, and \(K(0)\) for \(u>u_{\mathrm{max}}(n)\). At the crossing, precisely the axial and equatorial directions maximize (there is no interior maximum). Every intermediate value between the respective sharp endpoints occurs.

At any oblique-minimum parameter, with \(Q=(n+2)(n+4)-15u>0\), the exact stability identity is
\[
K(t)-K(t_*)=
\frac{24uCQ}{D(t_*)}\,\frac{(t-t_*)^2}{D(t)^2}.
\]
It is strictly positive away from the minimizing cone.

## Assumptions and scope
All measures and coefficients are **real**; \(n\in\{3,4,\dots\}\), \(u>0\), \(e\in S^{n-1}\), and \(a\in\mathbb R^n\setminus\{0\}\). The sphere is equipped with normalized uniform probability measure \(\sigma\), and
\[
d\mu_{n,u}(\omega)=\frac{1+u(\omega\cdot e)^4}{1+3u/[n(n+2)]}\,d\sigma(\omega).
\]
The weight is positive everywhere and smooth; all denominator factors above are strictly positive. Equality directions are described modulo nonzero real scalar multiples of \(a\). At the max threshold the two boundary families are disjoint; at the min threshold \(t_*=1\) is the unique axial minimum. The sharp interval degenerates only in the excluded isotropic limit \(u=0\), when every direction is equivalent.

## Proof
**1. Reduction to one parameter.** Rotational invariance around \(e\) sends \(a/\|a\|\) to \(\sqrt t\,e+\sqrt{1-t}\,v\), where \(v\perp e\) is a unit vector. For the normalized uniform sphere and nonnegative integers \(r,s\), the even-monomial rule is
\[
\mathbb E_{\sigma}[\omega_1^{2r}\omega_2^{2s}]=\frac{(2r-1)!!(2s-1)!!}{n(n+2)\cdots(n+2r+2s-2)},
\]
where \((-1)!!=1\). Odd-coordinate powers integrate to zero. In particular the normalizing constant is \(Z=1+3u/[n(n+2)]\), and direct expansion yields, for \(\|a\|=1\),
\[
\mathbb E_{\mu_{n,u}}f_a^2=\frac{D(t)}{Z\,n(n+2)(n+4)},\quad
\mathbb E_{\mu_{n,u}}f_a^4=\frac{N(t)}{Z\,n(n+2)(n+4)(n+6)}.
\]
Division yields the displayed exact formula \(K(t)\). Homogeneity removes \(\|a\|\).

**2. Global stationary-point structure.** Differentiate the rational function before dividing by its positive factors. The cancellation identity is
\[
N'(t)D(t)-2N(t)D'(t)
=48u\left(\big((n+2)(n+4)-15u\big)t-6(n+4)\right).
\]
Thus the derivative has at most one zero; if present in \((0,1)\), it changes sign from negative to positive and is the strict global minimum. The conditions \(0<t_*<1\) are equivalent to \(n\ge5\) and \(0<u<(n^2-16)/15\). Otherwise \(K\) decreases strictly on \([0,1)\), giving the axial minimum. In all cases the maximum is attained at an endpoint and there is no interior maximizer.

**3. Sharp maximum and crossing dimension.** Let
\[
B=-(n-10)(n+2)(n+4)^2+(12n^2+180n+528)u+45u^2.
\]
The exact endpoint identity is
\[
N(1)D(0)^2-N(0)D(1)^2=-24u B.
\]
For \(3\le n\le10\), \(B>0\), so \(K(1)<K(0)\). For \(n\ge11\), \(B(0)<0\), \(B\) increases strictly with \(u>0\), and its unique positive root is the claimed \(u_{\mathrm{max}}(n)\). This determines the max direction on either side and both equality directions at the root. Direct simplification and squaring positive quantities give \(0<u_{\mathrm{max}}(n)<(n^2-16)/15\) for every integer \(n\ge11\), so the two threshold phenomena are separated.

**4. Exact oblique stability and sharp interval.** For \(t_*\in(0,1)\), substituting the stationary equation \(Q t_*=6(n+4)\) into the rational difference gives
\[
\frac{N(t)}{D(t)^2}-\frac{N(t_*)}{D(t_*)^2}
=\frac{24uQ(t-t_*)^2}{D(t_*)D(t)^2}.
\]
Multiplying by \(C\) proves the exact positive stability formula, including the complete equality condition. Every \(t\in[0,1]\) is realized by a nonzero \(a\), and \(K\) is continuous, so the image is the entire closed interval between sharp minimum and maximum.

## Verification
The standalone script `check_quartic_zonal.py` checks the derivative polynomial identity, endpoint comparison, and interior stability as exact symbolic identities. It independently reconstructs spherical moments from the double-factorial integration rule and tests 352 exact rational examples in dimensions 3 through 24, plus 20,412 exact values against the global classification. These finite diagnostics support, but do not replace, the unrestricted analytical proof above. Run with `python check_quartic_zonal.py` using Python 3 and SymPy.

## Relationship to prior work
Dai and Xu (2007) develop analysis and harmonic expansions for weighted sphere measures with finite-reflection-group-invariant weights. Their maximal/multiplier theorems are not sharp fourth-moment optimization of linear functions under the present **positive polynomial zonal weight**. Gräf and Hielscher (2014 repository / 2015 publication) develop computational global optimization for polynomials on spheres; that general machinery does not state the explicit two-threshold norm classification. Bagnato, Faliva and Zoia (2016) use orthogonal-polynomial modification of spherical (radial) distributions to engineer kurtosis; their visible discussion centers on changing the radial variable, whereas the present measure is supported on a fixed sphere and changes directional mass. The latter paper's complete text was not obtained, so unindexed-equivalence risk remains.

The present weight is motivated as the first nonconstant even monomial order beyond the quadratic tilt. Under the analogous positive quadratic tilt \(1+u(\omega\cdot e)^2\), the normalized fourth-moment function is
\[
K^{(2)}(t)=\frac{3(n+2)(n+u)}{n+4}\frac{n+4+u+4ut}{(n+2+u+2ut)^2}.
\]
For its positive denominator \(D_2(t)=n+2+u+2ut\), the derivative numerator has the exact sign identity \(N_2'(t)D_2(t)-2N_2(t)D_2'(t)=-8u(1+ut)<0\). Thus no oblique minimizer or endpoint-maximizer exchange occurs. The quartic family therefore displays two specific geometrical behaviors absent from the immediately lower-degree family. This is a sharp **family-level** distinction, not a claim about all possible zonal weights.

## Limitations
The classification concerns degree-one real linear functions, one-parameter positive quartic axial weights, and fourth moments. It does not address arbitrary zonal weights, nonlinear functions, complex coefficients, or other moment exponents. The full text of one nearby 2016 kurtosis source was inaccessible; published equivalence in unindexed directional-statistics literature is not logically excluded by the completed comparisons. No independent mathematical audit has been performed.

## References
1. Feng Dai and Yuan Xu, *Maximal Function and Multiplier Theorem for Weighted Space on the Unit Sphere*, arXiv:math/0703928, first public March 30, 2007. https://arxiv.org/abs/math/0703928 .
2. Luca Bagnato, Mario Faliva and Maria Grazia Zoia, *The Role of Orthogonal Polynomials in Tailoring Spherical Distributions to Kurtosis Requirements*, Symmetry 8(8), 77 (2016). https://doi.org/10.3390/sym8080077 .
3. Manuel Gräf and Ralf Hielscher, *Fast global optimization on the torus, the sphere and the rotation group*, Optimization Online repository (2014) and published version (2015). https://optimization-online.org/wp-content/uploads/2014/02/4228.pdf .
