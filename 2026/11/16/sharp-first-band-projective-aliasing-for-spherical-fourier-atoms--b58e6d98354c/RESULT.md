# Sharp first-band projective aliasing for spherical Fourier atoms

## Finding

Fix a wavenumber \(\kappa>0\) and the normalized area measure \(d\sigma\) on \(S^2\). For each source location \(x\in\mathbb R^3\), set \(\phi_x(\omega)=e^{i\kappa\omega\cdot x}\). Let \(P_1\) denote orthogonal projection onto the four-dimensional complex space of spherical harmonics of degrees zero and one, namely \(\operatorname{span}_{\mathbb C}\{1,\omega_1,\omega_2,\omega_3\}\). Only the *complex projective line* \([P_1\phi_x]\) is observed: an unknown nonzero complex source amplitude is not assumed known.

**Theorem (sharp first-band alias boundary and complete fibers).** Define the spherical Bessel functions, with their continuous values at zero,
\[
 j_0(z)=\frac{\sin z}{z},\qquad
 j_1(z)=\frac{\sin z-z\cos z}{z^2}.
\]
For \(r=|x|>0\), \(u=x/r\), \(z=\kappa r\), the exact low-band atom is
\[
 P_1\phi_x(\omega)=j_0(z)+3i j_1(z)\,u\cdot\omega,
 \qquad P_1\phi_0=1.
\]
It never vanishes identically. On the set where \(j_0(z)\ne0\), the projective line is represented uniquely by the real *ratio coordinate*
\[
 Y(x)=h(\kappa|x|)\frac{x}{|x|},\qquad
 h(z)=\frac{j_1(z)}{j_0(z)}=\frac1z-\cot z,\qquad Y(0)=0,
\]
through \([P_1\phi_x]=[1+3iY(x)\cdot\omega]\). On \(0<z<\pi\), \(h\) is strictly increasing from zero to \(+\infty\), hence for each \(R>0\),
\[
 x\longmapsto[P_1\phi_x]\quad\text{is injective on }\overline B_R(0)
 \quad\Longleftrightarrow\quad \kappa R<\pi.
\]
This includes the closed-ball boundary: at \(\kappa R=\pi\), the two distinct points \(x=\pm(\pi/\kappa)u\) have the same line for every unit \(u\).

The *global* projective fibers have the following exhaustive description. Every spherical shell \(|x|=n\pi/\kappa\), \(n\ge1\), has zero degree-zero coefficient; all atoms on such shells share a line exactly when their directions belong to the same unoriented axis \(\{u,-u\}\). There is no projective equivalence between these zero-mean atoms and atoms with nonzero mean. Elsewhere the fibers are the level sets of \(Y\). In the interval \(0<z<\pi\), each nonzero ratio vector has one preimage. In **each complete later interval** \(n\pi<z<(n+1)\pi\), \(n\ge1\), a prescribed nonzero ratio vector \(y\) has exactly **two** preimages: one with \(h(z)=-|y|\) and direction \(-y/|y|\), the other with \(h(z)=|y|\) and direction \(y/|y|\). The zero ratio vector has precisely the origin and all points on the positive spherical shells where \(j_1(z)=0\); there is exactly one such shell within each later complete interval. For a bounded source ball, retain only those members whose radii do not exceed its radius.

**Sharp inverse geometry in the alias-free ball.** If \(\kappa R<\pi\), then for all \(x,x'\in\overline B_R(0)\),
\[
 \boxed{\quad |x-x'|\le\frac3\kappa|Y(x)-Y(x')|.\quad}
\]
The constant \(3/\kappa\) is sharp for every \(R>0\), by taking distinct points tending to the origin. This is stability in the ratio coordinate, **not** a claim of a radius-uniform noise bound for unnormalized raw harmonic data at the zero-mean boundary.

**Exact multipoint rank and two-atom Gram identity.** For any finite family \(x_1,\ldots,x_s\) in an alias-free closed ball, set \(y_j=Y(x_j)\), \(z_j=\kappa|x_j|\). Then
\[
 \dim_{\mathbb C}\operatorname{span}\{P_1\phi_{x_1},\ldots,P_1\phi_{x_s}\}
 =1+\dim_{\mathbb R}\operatorname{aff}\{y_1,\ldots,y_s\}.
\]
In particular two distinct atoms are independent; up to four generic atoms are independent. With \(G_{jk}=\langle P_1\phi_{x_j},P_1\phi_{x_k}\rangle_{L^2(S^2,d\sigma)}\), their two-by-two Gram determinant is
\[
 \boxed{\quad\det G=3j_0(z_1)^2j_0(z_2)^2
 \bigl(|y_1-y_2|^2+3|y_1\times y_2|^2\bigr).\quad}
\]

## Assumptions and scope

The sphere is the unit sphere in \(\mathbb R^3\). The Fourier sign convention is \(e^{+i\kappa\omega\cdot x}\); changing sign reflects the ratio vectors but does not alter the identifiability threshold. The inner product and orthogonal projection use probability-normalized area measure. Wavenumber \(\kappa\) is positive and known, whereas the common complex amplitude multiplying an individual atom may be unknown. Locations are real Euclidean points. The alias-free theorem concerns **closed balls centered at the origin** and the **degree-zero plus degree-one** harmonic band; it does not assert recovery of a general multiatom mixture merely from its span or an arbitrary four-mode mixture with unknown model order. The global fiber classification has no radial cutoff.

## Proof

**1. Exact harmonic projection.** Rotational invariance yields
\[
 \int_{S^2}\!e^{iz\omega\cdot u}\,d\sigma(\omega)=\tfrac12\int_{-1}^1e^{izt}\,dt=j_0(z).
\]
Differentiating in \(z\) and using \(j_0'(z)=-j_1(z)\) yields
\[
 \int_{S^2}\!\omega\,e^{iz\omega\cdot u}\,d\sigma(\omega)=ij_1(z)u.
\]
Because \(\int\omega_i\omega_j\,d\sigma=\delta_{ij}/3\), the projection formula follows. For \(z>0\), the zeros of \(j_0\) are precisely \(n\pi\) with \(n\ge1\), and \(j_1(n\pi)=-(-1)^n/(n\pi)\ne0\). Therefore \(P_1\phi_x\ne0\) for every \(x\), and the vanishing-mean stratum has the stated unoriented-axis projective lines.

**2. Ratio fibers and exact first singular radius.** When \(j_0(z)\ne0\), divide the projection by its uniquely determined nonzero constant coefficient. Its three linear coefficients form \(3iY(x)\), so equality of projective lines is equivalent to equality of the *real* vectors \(Y\). The function \(h(z)=1/z-\cot z\) has
\[
 h'(z)=\csc^2z-\frac1{z^2}>0
\]
for every \(z>0\) away from multiples of \(\pi\), since \(|\sin z|<z\). On \((0,\pi)\) it increases from \(0\) to \(+\infty\), and \(Y\) is injective in the corresponding ball. On every interval \((n\pi,(n+1)\pi)\), \(n\ge1\), it increases from \(-\infty\) to \(+\infty\). For each \(y\ne0\), the equations \(h(z)=\pm|y|\) have one solution apiece in that interval and determine antiparallel directions. For \(y=0\), the equation \(j_1(z)=0\) has one solution per such interval and leaves direction unrestricted. At \(z=\pi\), the zero-mean lines identify antipodes. Hence precisely \(\kappa R<\pi\) gives injectivity on the closed ball.

**3. Quantitative inverse inequality.** The sine-product partial fraction identity, valid for \(0\le z<\pi\) with the removable value at zero, is
\[
 h(z)=2z\sum_{n=1}^{\infty}\frac1{n^2\pi^2-z^2}.
\]
Termwise differentiation is justified on compact subsets of \((-\pi,\pi)\). Euler's reciprocal-square sum gives
\[
 \frac{h(z)}z=2\sum_{n\ge1}\frac1{n^2\pi^2-z^2}\ge\frac13,
 \qquad
 h'(z)=2\sum_{n\ge1}\frac{n^2\pi^2+z^2}{(n^2\pi^2-z^2)^2}\ge\frac13.
\]
The radial map \(Y(x)\) has radial Jacobian eigenvalue \(\kappa h'(\kappa|x|)\) and two tangential eigenvalues \(h(\kappa|x|)/|x|\), all at least \(\kappa/3\). The same holds at the origin by continuity. Integrating its symmetric Jacobian on the line segment between arbitrary points of the convex ball gives
\[
 (Y(x)-Y(x'))\cdot(x-x')\ge\frac\kappa3|x-x'|^2.
\]
Cauchy–Schwarz proves the bound. The expansion \(h(z)=z/3+O(z^3)\) shows its sharpness as two points approach zero.

**4. Exact finite-synthesis rank.** Since \(j_0(z_j)\ne0\), column scaling takes each atom to \(1+3i y_j\cdot\omega\). Its four coefficients differ from the real column vector \((1,y_j)\) by fixed invertible row scalings, so complex column rank equals rank over \(\mathbb R\) of the real matrix with columns \((1,y_j)\), namely one plus the real affine dimension. The Gram identity follows by computing
\[
 G_{jk}=j_0(z_j)j_0(z_k)(1+3y_j\cdot y_k)
\]
and expanding its determinant using \(|a|^2|b|^2-(a\cdot b)^2=|a\times b|^2\). This also proves all asserted independence statements.

## Verification

A standalone Python checker `CHECK.py` uses only the standard library. It independently evaluates the spherical zeroth and first plane-wave moments by one-dimensional angular quadrature, checks the exact Gram determinant against four-coordinate complex inner products, samples the first-band lower Jacobian bound and inverse-distance inequality, and tests the paired aliases across several higher radial bands. Its expected successful report is `CHECK_OK ... total=914`. These finite tests are corroboration, **not** substitutes for the analytic proofs of the infinite claims. To reproduce: `python3 CHECK.py`.

## Relationship to prior work

Fannjiang, *Spherical ESPRIT by Paired Small Circles and Infinitesimal Rotations* (first public preprint 2026-09-26), studies point-cloud recovery from **full spherical Fourier signal subspaces** using paired circles and infinitesimal rotation generators, and establishes generic guarded finite-cutoff criteria. Those results concern different data and do not state the exact projective fibers of the four-dimensional unguarded degree-zero-plus-one truncation, its sharp \(\kappa R=\pi\) boundary, its global higher-shell aliases, or the sharp ratio-coordinate inverse constant. The usual spherical-Bessel identities are classical (Abramowitz–Stegun; MathWorld); none of their elementary formulas alone supplies the claimed global geometric/fiber classification. published-finding corpus searches for first-band aliases, the \(j_1/j_0\) ratio, spherical ESPRIT and the sharp radial threshold returned results on whole-sphere identifiability, concentric two-frequency recovery, and spherical projection norms, without a statement implying this exact theorem. This assessment is limited to sources actually inspected and is not a proof of global novelty.

## Limitations

The theorem applies to \(\mathbb R^3\), known positive \(\kappa\), centered source balls and only the first two harmonic degrees. The sharp inverse estimate measures differences between **ratio coordinates**, which require division by a nonzero constant coefficient; as \(\kappa R\uparrow\pi\), conversion from noisy raw coefficients becomes ill-conditioned. When \(\kappa R\ge\pi\), the projective inverse is not injective. General source mixtures, distorted spheres, and unknown wavenumber are not covered. A potentially equivalent theorem in older acoustic monopole/dipole localization literature cannot be excluded without specialist review.

## References

1. A. Fannjiang, *Spherical ESPRIT by Paired Small Circles and Infinitesimal Rotations*, arXiv:2609.33024, first public 2026-09-26. https://arxiv.org/abs/2609.33024
2. E. W. Weisstein, *Spherical Bessel Function of the First Kind*, MathWorld, identities for \(j_0\) and \(j_1\). https://mathworld.wolfram.com/SphericalBesselFunctionoftheFirstKind.html
3. M. Abramowitz and I. A. Stegun (eds.), *Handbook of Mathematical Functions*, §10.1, 1964 (classical spherical Bessel formulas).
