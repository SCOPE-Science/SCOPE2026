# Reverse-Legendre cross-polytope marginals and the asymptotic phase of axial Fourier zeros

## Finding
Let \(B_1^d=\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\leq1\}\), for an integer \(d\geq1\), and normalize Lebesgue measure on this body to mass one. If \(S=x_1+\cdots+x_d\), its density on \((-1,1)\) is the **reverse Legendre polynomial**
\[
p_d(s)=\frac{d}{2^d}s^{d-1}P_{d-1}(1/s),\qquad -1<s<1,
\]
with the removable value at \(s=0\). Here \(P_n\) is the Legendre polynomial normalized by \(P_n(1)=1\). It vanishes outside \([-1,1]\), and its endpoint values are \(p_d(\pm1)=d/2^d\). Every polynomial zero of \(p_d\) lies outside the closed interval \([-1,1]\), and for \(d\geq3\) the density is strictly decreasing on \((0,1)\) and strictly log-concave on \((-1,1)\).

Define the normalized **diagonal axial Fourier transform**
\[
F_d(t)=\frac{d!}{2^d}\int_{B_1^d}e^{it(x_1+\cdots+x_d)}\,dx
=\int_{-1}^1p_d(s)e^{its}\,ds.
\]
Then
\[
F_d(t)={}_1F_2\!\left(d;\frac{d+1}{2},\frac{d+2}{2};-\frac{t^2}{4}\right).
\]
For \(d=1,2\), \(F_d(t)=\sin(t)/t\) (with its continuous value at zero). For \(d\geq3\), \(F_d(t)>0\) on \(0\leq t\leq\pi\). The constant \(\pi\) is optimal over all dimensions, with equality at \(d=1,2\). The statement concerns the diagonal frequency direction \(t(1,\ldots,1)\), not a global zero-free Euclidean ball in frequency space.

For each **fixed** \(d\geq3\), all sufficiently large complex zeros of the entire function \(F_d\) are real and simple. There is exactly one positive zero \(t_{d,n}\) near each \(n\pi\) for every sufficiently large integer \(n\), no other sufficiently large zeros in the right half-plane, and
\[
\boxed{\displaystyle t_{d,n}=n\pi+\frac{(d-1)(d-2)}{2n\pi}+O_d(n^{-3}).}
\]
The corresponding negative zeros are their negatives. In particular, the leading high-frequency diffraction-phase delay depends quadratically on the polytope dimension.

## Assumptions and scope
Dimension \(d\) is a positive integer. The interior density is a polynomial, extended by zero beyond \([-1,1]\); this extension has a jump at the endpoints. The Fourier convention is \(e^{itS}\) without a \(2\pi\) factor. Thus the Euclidean norm of the associated frequency vector is \(\sqrt d\,|t|\). The zero asymptotic and its implied constants hold for fixed \(d\), not uniformly as \(d\to\infty\). The location of finitely many low-frequency and possible nonreal zeros is not classified.

## Proof
**1. Moments of the diagonal projection.** The volume of \(B_1^d\) is \(2^d/d!\). Decompose it into its \(2^d\) orthant simplices, parameterizing a uniform point by independent Rademacher signs times nonnegative coordinates \(U_i\) with \(\sum U_i\leq1\). The Dirichlet simplex integral is
\[
\int_{\substack{u_i\geq0\\\sum u_i\leq1}}\prod_i u_i^{a_i}\,du
=\frac{\prod_i a_i!}{(d+\sum_i a_i)!}
\]
for nonnegative integer \(a_i\). Odd moments of \(S\) vanish. In the multinomial expansion of \(S^{2j}\), the signs eliminate all terms except those with exponents \(2k_i\), where \(\sum_i k_i=j\). Each weak composition contributes the same amount; there are \(\binom{j+d-1}{d-1}\) of them. Consequently
\[
\mathbb E S^{2j}=\frac{d!(2j)!}{(d+2j)!}\binom{j+d-1}{d-1}\quad(j\geq0).
\]
The characteristic series therefore equals the displayed \({}_1F_2\) by the duplication identity for the rising factorial \((d+1)_{2j}\).

**2. Exact inversion into a reverse Legendre polynomial.** Put \(r_n(s)=s^nP_n(1/s)\). The Legendre recurrence yields
\[
nr_n(s)=(2n-1)r_{n-1}(s)-(n-1)s^2r_{n-2}(s),\qquad n\geq2,
\]
with \(r_0=r_1=1\). Define \(I_n(j)=\int_{-1}^1s^{2j}r_n(s)\,ds\). Induction in \(n\), using this recurrence and the elementary factorial identity obtained after substituting into it, gives
\[
I_n(j)=\frac{2^{n+1}(2j)!(j+n)!}{j!(2j+n+1)!},\qquad n,j\geq0.
\]
The formula is immediate for \(n=0,1\); substitution in the recurrence verifies the induction for every \(j\). On taking \(n=d-1\) and multiplying by \(d/2^d\), these moments equal the moments in Step 1. Both measures are supported on the compact interval \([-1,1]\), and all their odd moments vanish, so equality of all polynomial moments, together with polynomial density in continuous functions, identifies the measures. This proves the claimed exact density.

**3. Shape and zero-free interval.** Write the positive roots of \(P_{d-1}\) as \(\zeta_1,\ldots,\zeta_m\), with \(m=\lfloor(d-1)/2\rfloor\); all lie strictly between zero and one. Factoring \(P_{d-1}\) proves
\[
p_d(s)=p_d(0)\prod_{j=1}^m(1-\zeta_j^2s^2),\quad
p_d(0)=\frac{d}{2^d}\frac{\binom{2d-2}{d-1}}{2^{d-1}}.
\]
This proves strict positivity, decreasingness and strict log-concavity for \(d\geq3\), as well as the location of the *polynomial-density* zeros. Since \(p_d\) is even, integration by parts gives for \(t>0\)
\[
F_d(t)=\frac{2p_d(1)\sin t}{t}
-\frac2t\int_0^1 p'_d(s)\sin(ts)\,ds.
\]
For \(0<t\leq\pi\) the first term is nonnegative and the second is strictly positive when \(d\geq3\); at \(t=0\), \(F_d(0)=1\). The flat cases \(d=1,2\) give \(\sin t/t\).

**4. Large complex zeros.** The density is an even polynomial on its support. Repeated integration by parts (a finite exact expansion) gives, uniformly for complex \(z\) with \(|z|\geq1\),
\[
\frac{zF_d(z)}{2p_d(1)}=
\sin z-\frac{c_d\cos z}{z}+O_d\!\left(\frac{e^{|\operatorname{Im}z|}}{|z|^2}\right),\qquad
c_d=-\frac{p'_d(1)}{p_d(1)}.
\]
Legendre's endpoint derivative \(P'_{d-1}(1)=d(d-1)/2\) gives \(c_d=(d-1)(d-2)/2\). For \(|\operatorname{Im}z|\geq1\), \(|\sin z|\geq\sinh|\operatorname{Im}z|\), so the perturbation is negligible at large \(|z|\). For \(|\operatorname{Im}z|<1\), \(|\sin z|\) is bounded below away from fixed small disks about \(n\pi\). On each such disk, for all sufficiently large \(|n|\), Rouché's theorem gives exactly one zero counted with multiplicity. Reality of the Fourier transform on the real line and conjugation symmetry force this unique zero to be real and hence simple. These disks account for every zero outside a compact set.

Retaining the next two integration-by-parts terms gives near \(n\pi\) the sharper equation \(\sin z-c_d\cos z/z+O_d(\sin z/z^2)+O_d(\cos z/z^3)=0\). The root first satisfies \(z-n\pi=O_d(n^{-1})\), and substitution then gives \(z-n\pi=c_d/(n\pi)+O_d(n^{-3})\). This completes the claimed expansion.

## Verification
The standalone `check.py` verifies 208 exact polynomial moment identities for dimensions \(1\) through \(16\), twelve independent hypergeometric-vs-integral comparisons for dimensions \(3,5,8\), and fifteen large-real-zero phase checks for dimensions \(3,4,5,8,11\). Its output is provided as `check_output.txt`; the Python dependencies are listed in `requirements.txt`. The tests do not prove infinitely many zero locations: the induction, polynomial factorization, and complex Rouché argument above provide that proof.

## Relationship to prior work
Benguria–Levitin–Parnovski (2008 preprint, later 2009 journal article) introduce Fourier null varieties and the directional projection-section formula for centrally symmetric convex bodies. Their generic framework does not give the reverse-Legendre diagonal marginal of the regular cross-polytope or this dimension-dependent high-frequency zero phase. Gómez-Serrano–Levitin–Platt–Polterovich (2026) study global nearest Fourier zeros and convex-body isoperimetry, including rotationally symmetric bipyramids, rather than the present all-dimensional \(\ell_1\)-ball diagonal projection. Classical Legendre recurrences and elementary endpoint Fourier asymptotics are inputs, not independent novelty claims.

## Limitations
This is a directional statement, not a solution of the full multivariate Fourier null-variety problem or its nearest-zero radius. No count of the finite exceptional zeros is asserted. The reverse-Legendre formula is expressed using elementary classical ingredients, and historical equivalent presentations in spline/projection literature are a publication-priority risk. The real-zero asymptotic is fixed-dimension, not uniform in growing dimension.

## References
- R. Benguria, M. Levitin and L. Parnovski, *Fourier transform, null variety, and Laplacian's eigenvalues*, arXiv:0801.1617, first submitted 10 January 2008; Journal of Functional Analysis 257 (2009), 2088–2123. https://arxiv.org/abs/0801.1617
- J. Gómez-Serrano, M. Levitin, D. Platt and I. Polterovich, *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, arXiv:2609.10517, 9 September 2026. https://arxiv.org/abs/2609.10517
- NIST Digital Library of Mathematical Functions, Chapter 14 (Legendre polynomials) and Chapter 16 (generalized hypergeometric functions), https://dlmf.nist.gov/.
